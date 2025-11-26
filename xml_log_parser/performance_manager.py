"""
Performance Enhancement Module
Provides async parsing, progress tracking, and memory-efficient processing
"""

import asyncio
import threading
import time
from typing import Dict, List, Any, Callable, Optional
from pathlib import Path
import os
from concurrent.futures import ThreadPoolExecutor

class PerformanceManager:
    """Manages performance optimization for large file parsing"""
    
    def __init__(self):
        self.chunk_size = 8192  # 8KB chunks for streaming
        self.max_workers = 4    # Thread pool size
        self.progress_callback: Optional[Callable] = None
        self.status_callback: Optional[Callable] = None
        self.cancel_flag = False
        
    def set_progress_callback(self, callback: Callable[[int, str], None]):
        """Set callback for progress updates: callback(percentage, status_text)"""
        self.progress_callback = callback
        
    def set_status_callback(self, callback: Callable[[str], None]):
        """Set callback for status updates: callback(status_text)"""
        self.status_callback = callback
        
    def cancel_operation(self):
        """Cancel current operation"""
        self.cancel_flag = True
        
    def get_file_info(self, filepath: str) -> Dict[str, Any]:
        """Get file information for performance planning"""
        try:
            file_path = Path(filepath)
            file_size = file_path.stat().st_size
            
            # Estimate complexity based on file size
            if file_size < 1024 * 1024:  # < 1MB
                complexity = "Simple"
                estimated_time = "< 1 second"
            elif file_size < 10 * 1024 * 1024:  # < 10MB
                complexity = "Medium"
                estimated_time = "1-5 seconds"
            elif file_size < 100 * 1024 * 1024:  # < 100MB
                complexity = "Large"
                estimated_time = "5-30 seconds"
            else:
                complexity = "Very Large"
                estimated_time = "30+ seconds"
                
            return {
                "size_bytes": file_size,
                "size_mb": round(file_size / (1024 * 1024), 2),
                "complexity": complexity,
                "estimated_time": estimated_time,
                "use_streaming": file_size > 5 * 1024 * 1024,  # Use streaming for files > 5MB
                "use_async": file_size > 1024 * 1024  # Use async for files > 1MB
            }
        except Exception as e:
            return {"error": str(e)}
    
    def stream_file_lines(self, filepath: str):
        """Memory-efficient line-by-line file reading"""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                line_count = 0
                while True:
                    if self.cancel_flag:
                        break
                        
                    line = file.readline()
                    if not line:
                        break
                        
                    line_count += 1
                    yield line_count, line.strip()
                    
        except Exception as e:
            if self.status_callback:
                self.status_callback(f"Error reading file: {e}")
            
    def parse_file_chunked(self, filepath: str, parser_func: Callable, chunk_lines: int = 1000):
        """Parse file in chunks with progress updates"""
        self.cancel_flag = False
        results = []
        
        try:
            file_info = self.get_file_info(filepath)
            if "error" in file_info:
                return {"error": file_info["error"]}
            
            if self.status_callback:
                self.status_callback(f"Processing {file_info['complexity']} file ({file_info['size_mb']} MB)")
            
            # Count total lines first for accurate progress
            if self.status_callback:
                self.status_callback("Analyzing file structure...")
            
            total_lines = sum(1 for _ in open(filepath, 'r', encoding='utf-8', errors='ignore'))
            
            if self.status_callback:
                self.status_callback(f"Processing {total_lines:,} lines...")
            
            # Process in chunks
            chunk_data = []
            lines_processed = 0
            
            for line_num, line in self.stream_file_lines(filepath):
                if self.cancel_flag:
                    if self.status_callback:
                        self.status_callback("Operation cancelled by user")
                    return {"cancelled": True, "partial_results": results}
                
                chunk_data.append({"line_number": line_num, "content": line})
                lines_processed += 1
                
                # Process chunk when it's full
                if len(chunk_data) >= chunk_lines:
                    chunk_results = parser_func(chunk_data)
                    if chunk_results:
                        results.extend(chunk_results if isinstance(chunk_results, list) else [chunk_results])
                    chunk_data = []
                    
                    # Update progress
                    progress = int((lines_processed / total_lines) * 100)
                    if self.progress_callback:
                        self.progress_callback(progress, f"Processed {lines_processed:,} / {total_lines:,} lines")
                    
                    # Small delay to prevent UI freezing
                    time.sleep(0.001)
            
            # Process remaining data
            if chunk_data and not self.cancel_flag:
                chunk_results = parser_func(chunk_data)
                if chunk_results:
                    results.extend(chunk_results if isinstance(chunk_results, list) else [chunk_results])
                
                if self.progress_callback:
                    self.progress_callback(100, f"Completed processing {total_lines:,} lines")
            
            return {
                "results": results,
                "total_lines": total_lines,
                "items_found": len(results),
                "file_info": file_info
            }
            
        except Exception as e:
            if self.status_callback:
                self.status_callback(f"Error during processing: {e}")
            return {"error": str(e)}
    
    async def parse_file_async(self, filepath: str, parser_func: Callable):
        """Async file parsing for non-blocking UI"""
        loop = asyncio.get_event_loop()
        
        # Run the chunked parsing in a thread pool
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future = loop.run_in_executor(
                executor, 
                self.parse_file_chunked,
                filepath,
                parser_func
            )
            return await future
    
    def estimate_processing_time(self, filepath: str) -> str:
        """Estimate processing time based on file characteristics"""
        file_info = self.get_file_info(filepath)
        if "error" in file_info:
            return "Unable to estimate"
        
        return file_info.get("estimated_time", "Unknown")
    
    def get_memory_usage_mb(self) -> float:
        """Get current memory usage in MB"""
        try:
            import psutil
            process = psutil.Process(os.getpid())
            return round(process.memory_info().rss / 1024 / 1024, 2)
        except ImportError:
            return 0.0

class ProgressDialog:
    """Modern progress dialog with cancellation support"""
    
    def __init__(self, parent, title="Processing File"):
        import tkinter as tk
        from tkinter import ttk
        
        self.parent = parent
        self.cancelled = False
        
        # Create dialog window
        self.dialog = tk.Toplevel(parent)
        self.dialog.title(title)
        self.dialog.geometry("450x200")
        self.dialog.resizable(False, False)
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Center the dialog
        self.dialog.update_idletasks()
        x = (self.dialog.winfo_screenwidth() // 2) - (450 // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (200 // 2)
        self.dialog.geometry(f"450x200+{x}+{y}")
        
        # Create widgets
        self._create_widgets()
        
        # Handle window close
        self.dialog.protocol("WM_DELETE_WINDOW", self.cancel)
    
    def _create_widgets(self):
        import tkinter as tk
        from tkinter import ttk
        
        # Main frame
        main_frame = ttk.Frame(self.dialog, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        self.title_label = ttk.Label(main_frame, text="Processing File...", 
                                    font=('Arial', 12, 'bold'))
        self.title_label.pack(pady=(0, 10))
        
        # Status text
        self.status_label = ttk.Label(main_frame, text="Initializing...", 
                                     font=('Arial', 10))
        self.status_label.pack(pady=(0, 10))
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(main_frame, variable=self.progress_var, 
                                           maximum=100, length=400)
        self.progress_bar.pack(pady=(0, 10))
        
        # Progress percentage
        self.percent_label = ttk.Label(main_frame, text="0%", font=('Arial', 10))
        self.percent_label.pack(pady=(0, 15))
        
        # Cancel button
        self.cancel_btn = ttk.Button(main_frame, text="Cancel", command=self.cancel)
        self.cancel_btn.pack()
        
    def update_progress(self, percentage: int, status: str = ""):
        """Update progress bar and status"""
        self.progress_var.set(percentage)
        self.percent_label.config(text=f"{percentage}%")
        if status:
            self.status_label.config(text=status)
        self.dialog.update()
        
    def update_status(self, status: str):
        """Update status text"""
        self.status_label.config(text=status)
        self.dialog.update()
        
    def cancel(self):
        """Cancel the operation"""
        self.cancelled = True
        self.cancel_btn.config(text="Cancelling...", state="disabled")
        self.status_label.config(text="Cancelling operation...")
        self.dialog.update()
        
    def close(self):
        """Close the dialog"""
        self.dialog.destroy()
        
    def is_cancelled(self):
        """Check if operation was cancelled"""
        return self.cancelled

# Convenience functions for integration
def create_performance_manager():
    """Create a configured performance manager"""
    return PerformanceManager()

def show_file_analysis(filepath: str):
    """Show file analysis information"""
    manager = PerformanceManager()
    info = manager.get_file_info(filepath)
    
    if "error" in info:
        return f"Error analyzing file: {info['error']}"
    
    return f"""File Analysis:
Size: {info['size_mb']} MB ({info['size_bytes']:,} bytes)
Complexity: {info['complexity']}
Estimated Processing Time: {info['estimated_time']}
Recommended: {'Streaming mode' if info['use_streaming'] else 'Standard mode'}
"""

# Example usage
if __name__ == "__main__":
    # Test the performance manager
    manager = PerformanceManager()
    
    # Test file info
    info = manager.get_file_info("sample_log.txt")
    print("File Info:", info)
    
    print("\nPerformance enhancement module ready!")