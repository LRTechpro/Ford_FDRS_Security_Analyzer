"""
Interactive Dashboard for Real-Time Log Analysis
Provides visual metrics, progress tracking, and dynamic insights
"""

import tkinter as tk
from tkinter import ttk
from typing import Dict, List, Any, Optional
from collections import Counter


class InteractiveDashboard:
    """Dynamic dashboard with live metrics and visual insights"""
    
    def __init__(self, parent, colors: Dict[str, str]):
        self.parent = parent
        self.colors = colors
        self.data = None
        self.widgets = {}
        
        self._create_dashboard()
    
    def _create_dashboard(self):
        """Create dashboard layout"""
        # Main container with grid layout
        self.frame = ttk.Frame(self.parent)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)
        
        # Row 1: Key Metrics
        self._create_metrics_row(0)
        
        # Row 2: Health Status
        self._create_health_status(1)
        
        # Row 3: Error Distribution
        self._create_error_distribution(2)
        
        # Row 4: Module Status
        self._create_module_status(3)
        
        # Row 5: Timeline
        self._create_timeline_view(4)
    
    def _create_metrics_row(self, row: int):
        """Create key metrics cards"""
        metrics_frame = ttk.Frame(self.frame)
        metrics_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), padx=10, pady=10)
        metrics_frame.grid_columnconfigure(0, weight=1)
        metrics_frame.grid_columnconfigure(1, weight=1)
        metrics_frame.grid_columnconfigure(2, weight=1)
        metrics_frame.grid_columnconfigure(3, weight=1)
        
        # Total Items
        self.widgets['total_card'] = self._create_metric_card(
            metrics_frame, "📊 Total Items", "0", "lightblue", 0
        )
        
        # Errors
        self.widgets['error_card'] = self._create_metric_card(
            metrics_frame, "❌ Errors", "0", "#FF6B6B", 1
        )
        
        # Successes
        self.widgets['success_card'] = self._create_metric_card(
            metrics_frame, "✅ Successes", "0", "#51CF66", 2
        )
        
        # Confidence
        self.widgets['confidence_card'] = self._create_metric_card(
            metrics_frame, "🎯 Confidence", "0%", "#4DABF7", 3
        )
    
    def _create_metric_card(self, parent, title: str, value: str, color: str, col: int):
        """Create a metric card widget"""
        card = tk.Frame(parent, bg=color, relief=tk.RAISED, borderwidth=2)
        card.grid(row=0, column=col, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        title_label = tk.Label(card, text=title, bg=color, fg="white", 
                               font=('Arial', 10, 'bold'))
        title_label.pack(pady=5)
        
        value_label = tk.Label(card, text=value, bg=color, fg="white",
                               font=('Arial', 20, 'bold'))
        value_label.pack(pady=5)
        
        return {'frame': card, 'value': value_label, 'color': color}
    
    def _create_health_status(self, row: int):
        """Create health status indicator"""
        health_frame = ttk.LabelFrame(self.frame, text="🏥 System Health", padding=10)
        health_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), padx=10, pady=5)
        
        # Health bar
        self.widgets['health_canvas'] = tk.Canvas(health_frame, height=40, bg=self.colors['text_bg'])
        self.widgets['health_canvas'].pack(fill=tk.X, pady=5)
        
        # Health text
        self.widgets['health_text'] = tk.Label(health_frame, text="Waiting for analysis...",
                                                bg=self.colors['text_bg'], fg=self.colors['text_fg'],
                                                font=('Arial', 11))
        self.widgets['health_text'].pack(pady=5)
    
    def _create_error_distribution(self, row: int):
        """Create error type distribution chart"""
        dist_frame = ttk.LabelFrame(self.frame, text="📈 Error Distribution by Category", padding=10)
        dist_frame.grid(row=row, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=5)
        
        # Simple bar chart using canvas
        self.widgets['dist_canvas'] = tk.Canvas(dist_frame, height=150, bg=self.colors['text_bg'])
        self.widgets['dist_canvas'].pack(fill=tk.BOTH, expand=True)
        
        self.widgets['dist_text'] = tk.Text(dist_frame, height=6, bg=self.colors['text_bg'],
                                             fg=self.colors['text_fg'], font=('Consolas', 9))
        self.widgets['dist_text'].pack(fill=tk.BOTH, expand=True, pady=5)
    
    def _create_module_status(self, row: int):
        """Create module status grid"""
        module_frame = ttk.LabelFrame(self.frame, text="🔧 Module Status", padding=10)
        module_frame.grid(row=row, column=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=5, rowspan=1)
        
        self.widgets['module_text'] = tk.Text(module_frame, height=10, bg=self.colors['text_bg'],
                                               fg=self.colors['text_fg'], font=('Consolas', 9))
        self.widgets['module_text'].pack(fill=tk.BOTH, expand=True)
    
    def _create_timeline_view(self, row: int):
        """Create timeline visualization"""
        timeline_frame = ttk.LabelFrame(self.frame, text="⏱️ Event Timeline", padding=10)
        timeline_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), padx=10, pady=5)
        
        self.widgets['timeline_canvas'] = tk.Canvas(timeline_frame, height=80, bg=self.colors['text_bg'])
        self.widgets['timeline_canvas'].pack(fill=tk.X)
    
    def update(self, analysis_data: Dict[str, Any]):
        """Update dashboard with new data"""
        self.data = analysis_data
        
        # Update metrics
        self._update_metrics()
        
        # Update health status
        self._update_health_status()
        
        # Update error distribution
        self._update_error_distribution()
        
        # Update module status
        self._update_module_status()
        
        # Update timeline
        self._update_timeline()
    
    def _update_metrics(self):
        """Update metric cards"""
        if not self.data:
            return
        
        # Total items
        total = self.data.get('total_items', 0)
        self.widgets['total_card']['value'].config(text=str(total))
        
        # Errors
        errors = self.data.get('total_errors', 0)
        self.widgets['error_card']['value'].config(text=str(errors))
        
        # Successes
        successes = self.data.get('total_successes', 0)
        self.widgets['success_card']['value'].config(text=str(successes))
        
        # Confidence
        confidence = self.data.get('confidence', 0.0) * 100
        self.widgets['confidence_card']['value'].config(text=f"{confidence:.0f}%")
        
        # Update confidence card color based on value
        if confidence >= 80:
            color = "#51CF66"  # Green
        elif confidence >= 60:
            color = "#FFD93D"  # Yellow
        else:
            color = "#FF6B6B"  # Red
        
        self.widgets['confidence_card']['frame'].config(bg=color)
        self.widgets['confidence_card']['value'].config(bg=color)
        card_title = self.widgets['confidence_card']['frame'].winfo_children()[0]
        card_title.config(bg=color)
    
    def _update_health_status(self):
        """Update health status bar and text"""
        canvas = self.widgets['health_canvas']
        canvas.delete('all')
        
        if not self.data:
            return
        
        width = canvas.winfo_width() if canvas.winfo_width() > 1 else 800
        height = 40
        
        # Calculate health score (0-100)
        total = self.data.get('total_items', 1)
        errors = self.data.get('total_errors', 0)
        health_score = max(0, 100 - (errors / total * 100)) if total > 0 else 100
        
        # Draw health bar
        bar_width = (width - 20) * (health_score / 100)
        
        # Background
        canvas.create_rectangle(10, 10, width-10, height-10, fill='#2C2C2C', outline='')
        
        # Health bar (color based on score)
        if health_score >= 80:
            color = '#51CF66'  # Green
            status = "HEALTHY"
        elif health_score >= 60:
            color = '#FFD93D'  # Yellow
            status = "WARNING"
        elif health_score >= 40:
            color = '#FFA94D'  # Orange
            status = "DEGRADED"
        else:
            color = '#FF6B6B'  # Red
            status = "CRITICAL"
        
        canvas.create_rectangle(10, 10, 10 + bar_width, height-10, fill=color, outline='')
        
        # Text overlay
        canvas.create_text(width/2, height/2, text=f"{health_score:.0f}% - {status}",
                          font=('Arial', 12, 'bold'), fill='white')
        
        # Update health text
        error_rate = (errors / total * 100) if total > 0 else 0
        self.widgets['health_text'].config(
            text=f"Error Rate: {error_rate:.1f}% | {errors} failures out of {total} operations"
        )
    
    def _update_error_distribution(self):
        """Update error distribution visualization"""
        text = self.widgets['dist_text']
        text.delete('1.0', tk.END)
        
        if not self.data or not self.data.get('error_categories'):
            text.insert(tk.END, "No error data available")
            return
        
        # Get error categories
        categories = self.data.get('error_categories', {})
        if not categories:
            text.insert(tk.END, "No categorized errors")
            return
        
        # Sort by count
        sorted_cats = sorted(categories.items(), key=lambda x: x[1], reverse=True)
        
        # Display as text-based bar chart
        max_count = max(categories.values()) if categories else 1
        
        for category, count in sorted_cats:
            bar_length = int((count / max_count) * 40)
            bar = "█" * bar_length
            text.insert(tk.END, f"{category:20s} │ {bar} {count}\n")
    
    def _update_module_status(self):
        """Update module status display"""
        text = self.widgets['module_text']
        text.delete('1.0', tk.END)
        
        if not self.data:
            text.insert(tk.END, "No module data available")
            return
        
        modules = self.data.get('modules', {})
        if not modules:
            text.insert(tk.END, "No module information")
            return
        
        # Display module status
        for module_id, module_info in modules.items():
            status = module_info.get('status', 'unknown')
            name = module_info.get('name', module_id)
            
            if status == 'ok':
                icon = "✅"
            elif status == 'error':
                icon = "❌"
            elif status == 'warning':
                icon = "⚠️"
            else:
                icon = "❓"
            
            text.insert(tk.END, f"{icon} {name} ({module_id})\n")
    
    def _update_timeline(self):
        """Update timeline visualization"""
        canvas = self.widgets['timeline_canvas']
        canvas.delete('all')
        
        if not self.data or not self.data.get('timeline'):
            return
        
        width = canvas.winfo_width() if canvas.winfo_width() > 1 else 800
        height = 80
        
        timeline = self.data.get('timeline', [])
        if not timeline:
            return
        
        # Draw timeline
        y = height / 2
        canvas.create_line(10, y, width-10, y, fill='white', width=2)
        
        # Plot events
        time_span = len(timeline)
        if time_span == 0:
            return
        
        for i, event in enumerate(timeline):
            x = 10 + (width - 20) * (i / max(1, time_span - 1)) if time_span > 1 else width / 2
            
            event_type = event.get('type', 'unknown')
            if event_type in ['error', 'security', 'communication']:
                color = 'red'
                size = 8
            elif event_type == 'warning':
                color = 'yellow'
                size = 6
            else:
                color = 'green'
                size = 4
            
            canvas.create_oval(x-size, y-size, x+size, y+size, fill=color, outline='white')
        
        # Add labels
        canvas.create_text(10, 10, text="Start", anchor=tk.W, fill='white', font=('Arial', 9))
        canvas.create_text(width-10, 10, text="End", anchor=tk.E, fill='white', font=('Arial', 9))
    
    def get_frame(self):
        """Return the dashboard frame for embedding"""
        return self.frame
    
    def clear(self):
        """Clear all dashboard data"""
        self.data = None
        for widget_name in ['total_card', 'error_card', 'success_card', 'confidence_card']:
            if widget_name in self.widgets:
                self.widgets[widget_name]['value'].config(text="0" if 'confidence' not in widget_name else "0%")
        
        if 'health_text' in self.widgets:
            self.widgets['health_text'].config(text="Waiting for analysis...")
        
        if 'dist_text' in self.widgets:
            self.widgets['dist_text'].delete('1.0', tk.END)
        
        if 'module_text' in self.widgets:
            self.widgets['module_text'].delete('1.0', tk.END)
        
        if 'health_canvas' in self.widgets:
            self.widgets['health_canvas'].delete('all')
        
        if 'timeline_canvas' in self.widgets:
            self.widgets['timeline_canvas'].delete('all')
