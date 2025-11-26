"""
Modern UI Enhancements
Provides tooltips, improved drag & drop, loading animations, and better user feedback
"""

import tkinter as tk
from tkinter import ttk
import time
from typing import Optional, Callable, Dict, Any

class ToolTipManager:
    """Creates modern tooltips for widgets"""
    
    def __init__(self):
        self.tooltip_windows = {}
        self.delay = 500  # milliseconds
    
    def create_tooltip(self, widget, text: str, delay: int = 500):
        """Create a tooltip for a widget"""
        self.delay = delay
        
        def on_enter(event):
            self.schedule_tooltip(widget, text)
        
        def on_leave(event):
            self.hide_tooltip(widget)
        
        def on_motion(event):
            self.hide_tooltip(widget)
            self.schedule_tooltip(widget, text)
        
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)
        widget.bind("<Motion>", on_motion)
    
    def schedule_tooltip(self, widget, text: str):
        """Schedule tooltip to appear after delay"""
        def show():
            if widget.winfo_exists():
                self.show_tooltip(widget, text)
        
        # Cancel any existing scheduled tooltip
        if hasattr(widget, '_tooltip_job'):
            widget.after_cancel(widget._tooltip_job)
        
        # Schedule new tooltip
        widget._tooltip_job = widget.after(self.delay, show)
    
    def show_tooltip(self, widget, text: str):
        """Show tooltip near widget"""
        # Check if tooltip already exists
        if widget in self.tooltip_windows:
            return
        
        # Create tooltip window
        tooltip = tk.Toplevel(widget)
        tooltip.wm_overrideredirect(True)
        tooltip.wm_attributes("-topmost", True)
        
        # Style the tooltip
        frame = tk.Frame(tooltip, background="#ffffe0", relief="solid", borderwidth=1)
        frame.pack()
        
        label = tk.Label(frame, text=text, background="#ffffe0", 
                        font=("Arial", 9), justify="left", wraplength=300)
        label.pack(padx=2, pady=1)
        
        # Position tooltip
        x = widget.winfo_rootx() + 25
        y = widget.winfo_rooty() + 25
        tooltip.geometry(f"+{x}+{y}")
        
        # Store tooltip
        self.tooltip_windows[widget] = tooltip
        
        # Auto-hide after 10 seconds
        tooltip.after(10000, lambda: self.hide_tooltip(widget))
    
    def hide_tooltip(self, widget):
        """Hide tooltip for widget"""
        if widget in self.tooltip_windows:
            self.tooltip_windows[widget].destroy()
            del self.tooltip_windows[widget]
        
        # Cancel scheduled tooltip
        if hasattr(widget, '_tooltip_job'):
            widget.after_cancel(widget._tooltip_job)

class LoadingAnimation:
    """Modern loading animation widget"""
    
    def __init__(self, parent, text="Loading..."):
        self.parent = parent
        self.text = text
        self.is_running = False
        self.animation_job = None
        self.dots = 0
        
        # Create loading frame
        self.frame = tk.Frame(parent, bg='white', relief='raised', borderwidth=2)
        
        # Loading label
        self.label = tk.Label(self.frame, text=text, font=('Arial', 12), 
                             bg='white', fg='#2c3e50')
        self.label.pack(pady=20, padx=40)
        
        # Animated dots
        self.dots_label = tk.Label(self.frame, text="", font=('Arial', 16), 
                                  bg='white', fg='#3498db')
        self.dots_label.pack(pady=(0, 20))
    
    def start(self):
        """Start the loading animation"""
        self.is_running = True
        self.frame.place(relx=0.5, rely=0.5, anchor='center')
        self._animate()
    
    def stop(self):
        """Stop the loading animation"""
        self.is_running = False
        if self.animation_job:
            self.parent.after_cancel(self.animation_job)
        self.frame.place_forget()
    
    def _animate(self):
        """Animate the loading dots"""
        if not self.is_running:
            return
        
        self.dots = (self.dots + 1) % 4
        dots_text = "●" * self.dots + "○" * (3 - self.dots)
        self.dots_label.config(text=dots_text)
        
        self.animation_job = self.parent.after(500, self._animate)
    
    def update_text(self, text: str):
        """Update loading text"""
        self.text = text
        self.label.config(text=text)

class DragDropEnhancer:
    """Enhanced drag and drop with visual feedback"""
    
    def __init__(self, widget):
        self.widget = widget
        self.original_bg = widget.cget('bg') if hasattr(widget, 'cget') else 'white'
        self.drop_bg = '#e8f4f8'  # Light blue
        self.hover_bg = '#d4eaf2'  # Slightly darker blue
        
    def setup_drag_drop(self, on_drop_callback: Callable):
        """Setup enhanced drag and drop"""
        try:
            # Try to use tkinterdnd2 if available
            from tkinterdnd2 import DND_FILES
            
            self.widget.drop_target_register(DND_FILES)
            self.widget.dnd_bind('<<DropEnter>>', self._on_drag_enter)
            self.widget.dnd_bind('<<DropLeave>>', self._on_drag_leave)
            self.widget.dnd_bind('<<Drop>>', lambda e: self._on_drop(e, on_drop_callback))
            
        except ImportError:
            # Fallback: Basic file selection
            self.widget.bind('<Button-1>', lambda e: self._fallback_file_select(on_drop_callback))
    
    def _on_drag_enter(self, event):
        """Visual feedback when drag enters"""
        if hasattr(self.widget, 'config'):
            self.widget.config(bg=self.hover_bg)
    
    def _on_drag_leave(self, event):
        """Reset visual feedback when drag leaves"""
        if hasattr(self.widget, 'config'):
            self.widget.config(bg=self.original_bg)
    
    def _on_drop(self, event, callback):
        """Handle file drop"""
        if hasattr(self.widget, 'config'):
            self.widget.config(bg=self.drop_bg)
        
        # Extract file path
        files = event.data.split()
        if files:
            callback(files[0])
        
        # Reset background after short delay
        self.widget.after(1000, lambda: self.widget.config(bg=self.original_bg) if hasattr(self.widget, 'config') else None)
    
    def _fallback_file_select(self, callback):
        """Fallback file selection dialog"""
        from tkinter import filedialog
        file_path = filedialog.askopenfilename(
            title="Select Log File",
            filetypes=[
                ("Log Files", "*.log *.txt *.xml"),
                ("Text Files", "*.txt"),
                ("XML Files", "*.xml"),
                ("All Files", "*.*")
            ]
        )
        if file_path:
            callback(file_path)

class StatusBarEnhancer:
    """Enhanced status bar with progress and indicators"""
    
    def __init__(self, parent):
        self.parent = parent
        
        # Create status frame
        self.frame = ttk.Frame(parent)
        
        # Status text
        self.status_var = tk.StringVar(value="Ready")
        self.status_label = ttk.Label(self.frame, textvariable=self.status_var, 
                                     relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        # Progress bar (hidden by default)
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.frame, variable=self.progress_var, 
                                           length=150, height=16)
        
        # Memory usage (if available)
        self.memory_label = ttk.Label(self.frame, text="", font=('Arial', 8), 
                                     relief=tk.SUNKEN, width=12)
        self.memory_label.pack(side=tk.RIGHT, padx=(5, 0))
        
        # File info
        self.file_info_label = ttk.Label(self.frame, text="", font=('Arial', 8), 
                                        relief=tk.SUNKEN, width=20)
        self.file_info_label.pack(side=tk.RIGHT, padx=(5, 0))
        
        # Start memory monitoring
        self._update_memory()
    
    def set_status(self, text: str, color: str = None):
        """Set status text with optional color"""
        self.status_var.set(text)
        if color and hasattr(self.status_label, 'config'):
            self.status_label.config(foreground=color)
    
    def show_progress(self, show: bool = True):
        """Show or hide progress bar"""
        if show:
            self.progress_bar.pack(side=tk.RIGHT, padx=(5, 5))
        else:
            self.progress_bar.pack_forget()
    
    def update_progress(self, percentage: float):
        """Update progress percentage"""
        self.progress_var.set(percentage)
    
    def set_file_info(self, filename: str, size_mb: float = None):
        """Set current file information"""
        if size_mb:
            info = f"{filename} ({size_mb:.1f} MB)"
        else:
            info = filename
        
        # Truncate if too long
        if len(info) > 25:
            info = "..." + info[-22:]
        
        self.file_info_label.config(text=info)
    
    def _update_memory(self):
        """Update memory usage display"""
        try:
            import psutil
            process = psutil.Process()
            memory_mb = process.memory_info().rss / 1024 / 1024
            self.memory_label.config(text=f"RAM: {memory_mb:.0f}MB")
        except (ImportError, Exception):
            self.memory_label.config(text="")
        
        # Update every 5 seconds
        self.parent.after(5000, self._update_memory)
    
    def pack(self, **kwargs):
        """Pack the status bar frame"""
        self.frame.pack(**kwargs)

class ModernButton:
    """Enhanced button with hover effects and icons"""
    
    def __init__(self, parent, text: str, command: Callable, icon: str = None):
        self.parent = parent
        self.command = command
        
        # Create button
        self.button = tk.Button(parent, text=f"{icon} {text}" if icon else text,
                               command=self._on_click,
                               font=('Arial', 10),
                               relief='flat',
                               borderwidth=2,
                               bg='#3498db',
                               fg='white',
                               activebackground='#2980b9',
                               activeforeground='white',
                               cursor='hand2')
        
        # Add hover effects
        self.button.bind('<Enter>', self._on_enter)
        self.button.bind('<Leave>', self._on_leave)
        
        # Track state
        self.enabled = True
    
    def _on_enter(self, event):
        """Hover enter effect"""
        if self.enabled:
            self.button.config(bg='#2980b9')
    
    def _on_leave(self, event):
        """Hover leave effect"""
        if self.enabled:
            self.button.config(bg='#3498db')
    
    def _on_click(self):
        """Handle button click with visual feedback"""
        if not self.enabled:
            return
        
        # Quick visual feedback
        original_bg = self.button.cget('bg')
        self.button.config(bg='#1f4e79')
        self.button.update()
        self.button.after(100, lambda: self.button.config(bg=original_bg))
        
        # Execute command
        self.command()
    
    def set_enabled(self, enabled: bool):
        """Enable or disable button"""
        self.enabled = enabled
        if enabled:
            self.button.config(state='normal', bg='#3498db')
        else:
            self.button.config(state='disabled', bg='#bdc3c7')
    
    def pack(self, **kwargs):
        """Pack the button"""
        self.button.pack(**kwargs)
    
    def grid(self, **kwargs):
        """Grid the button"""
        self.button.grid(**kwargs)

# Convenience functions
def add_tooltip(widget, text: str):
    """Quick function to add tooltip to any widget"""
    tooltip_manager = ToolTipManager()
    tooltip_manager.create_tooltip(widget, text)

def create_loading_overlay(parent, text="Processing..."):
    """Create a loading overlay"""
    return LoadingAnimation(parent, text)

def enhance_drag_drop(widget, callback):
    """Quick function to enhance drag and drop for a widget"""
    enhancer = DragDropEnhancer(widget)
    enhancer.setup_drag_drop(callback)

# Example usage
if __name__ == "__main__":
    # Test the UI enhancements
    root = tk.Tk()
    root.title("UI Enhancements Test")
    root.geometry("400x300")
    
    # Test tooltip
    label = tk.Label(root, text="Hover over me for tooltip")
    label.pack(pady=20)
    add_tooltip(label, "This is a modern tooltip with nice styling!")
    
    # Test modern button
    def test_command():
        print("Button clicked!")
    
    modern_btn = ModernButton(root, "Test Button", test_command, "🚀")
    modern_btn.pack(pady=10)
    
    # Test loading animation
    loading = create_loading_overlay(root, "Loading data...")
    
    def show_loading():
        loading.start()
        root.after(3000, loading.stop)  # Hide after 3 seconds
    
    tk.Button(root, text="Show Loading", command=show_loading).pack(pady=10)
    
    # Test status bar
    status_bar = StatusBarEnhancer(root)
    status_bar.set_status("Application ready")
    status_bar.set_file_info("sample.log", 2.5)
    status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    root.mainloop()