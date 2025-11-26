"""
Charts Panel for Analytics Visualization
Displays error trends, ECU health, and NRC frequency charts
"""

import tkinter as tk
from tkinter import ttk
try:
    import matplotlib
    matplotlib.use('TkAgg')
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False


class ChartsPanel(ttk.Frame):
    """Panel for displaying analytics charts"""
    
    def __init__(self, parent, database_manager, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.db = database_manager
        
        if not MATPLOTLIB_AVAILABLE:
            self._show_install_message()
        else:
            self._create_charts()
    
    def _show_install_message(self):
        """Show installation instructions if matplotlib not available"""
        message = tk.Label(
            self,
            text="📊 Analytics Charts Not Available\n\n"
                 "To enable analytics visualizations, install matplotlib:\n\n"
                 "pip install matplotlib\n\n"
                 "Then restart the application.",
            font=('Arial', 12),
            fg='#666666',
            justify=tk.CENTER
        )
        message.pack(expand=True)
    
    def _create_charts(self):
        """Create all chart components"""
        # Toolbar
        toolbar = ttk.Frame(self)
        toolbar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        ttk.Button(toolbar, text="🔄 Refresh Charts", command=self.refresh_charts).pack(side=tk.LEFT, padx=5)
        ttk.Label(toolbar, text="Last 30 days of data").pack(side=tk.LEFT, padx=20)
        
        # Charts container
        charts_container = ttk.Frame(self)
        charts_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create 2x2 grid for charts
        charts_container.columnconfigure(0, weight=1)
        charts_container.columnconfigure(1, weight=1)
        charts_container.rowconfigure(0, weight=1)
        charts_container.rowconfigure(1, weight=1)
        
        # 1. Error Timeline
        self.timeline_frame = self._create_error_timeline(charts_container)
        self.timeline_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        
        # 2. ECU Health Dashboard
        self.ecu_frame = self._create_ecu_health(charts_container)
        self.ecu_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        
        # 3. NRC Frequency
        self.nrc_frame = self._create_nrc_frequency(charts_container)
        self.nrc_frame.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
        
        # 4. Success Rate
        self.success_frame = self._create_success_rate(charts_container)
        self.success_frame.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)
    
    def _create_error_timeline(self, parent):
        """Create error timeline chart"""
        frame = ttk.LabelFrame(parent, text="📈 Error Timeline (30 Days)")
        
        # Create matplotlib figure
        fig = Figure(figsize=(5, 3), dpi=80)
        ax = fig.add_subplot(111)
        
        # Get data from database
        trends = self.db.get_error_trends(30)
        
        if trends['dates']:
            ax.plot(trends['dates'], trends['errors'], 'r-', label='Errors', linewidth=2)
            ax.plot(trends['dates'], trends['warnings'], 'orange', label='Warnings', linewidth=2)
            ax.set_xlabel('Date')
            ax.set_ylabel('Count')
            ax.legend()
            ax.grid(True, alpha=0.3)
            fig.autofmt_xdate()
        else:
            ax.text(0.5, 0.5, 'No data yet\nParse some logs first!', 
                   ha='center', va='center', fontsize=12, color='gray')
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis('off')
        
        fig.tight_layout()
        
        # Embed in tkinter
        canvas = FigureCanvasTkAgg(fig, frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        return frame
    
    def _create_ecu_health(self, parent):
        """Create ECU health dashboard"""
        frame = ttk.LabelFrame(parent, text="🚗 ECU Health Status")
        
        # For now, show a simple text summary
        # In a full implementation, this would be a color-coded grid
        text = tk.Text(frame, wrap=tk.WORD, height=10, bg='white')
        text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        stats = self.db.get_statistics()
        
        if stats.get('total_logs', 0) > 0:
            text.insert(tk.END, "ECU Module Health Summary:\n\n", 'bold')
            text.insert(tk.END, f"Total Diagnostics Sessions: {stats['total_logs']}\n")
            text.insert(tk.END, f"Total Errors Recorded: {stats['total_errors']}\n\n")
            
            if stats.get('problematic_files'):
                text.insert(tk.END, "Most Problematic Files:\n", 'bold')
                for file_stat in stats['problematic_files'][:5]:
                    text.insert(tk.END, f"  • {file_stat['filename']}: {file_stat['avg_errors']:.1f} avg errors\n")
        else:
            text.insert(tk.END, "No ECU data yet.\n\nParse diagnostic logs to see module health status.")
        
        text.config(state=tk.DISABLED)
        return frame
    
    def _create_nrc_frequency(self, parent):
        """Create NRC frequency chart"""
        frame = ttk.LabelFrame(parent, text="⚠️ Top NRC Codes")
        
        fig = Figure(figsize=(5, 3), dpi=80)
        ax = fig.add_subplot(111)
        
        # Get NRC data
        nrc_data = self.db.get_most_common_nrc_codes(10)
        
        if nrc_data:
            codes = [item['code'] for item in nrc_data]
            counts = [item['count'] for item in nrc_data]
            
            # Create horizontal bar chart
            ax.barh(codes, counts, color=['red', 'orange', 'yellow', 'lightblue'] * 3)
            ax.set_xlabel('Occurrences')
            ax.set_ylabel('NRC Code')
            ax.invert_yaxis()
            ax.grid(True, alpha=0.3, axis='x')
        else:
            ax.text(0.5, 0.5, 'No NRC codes yet\nParse some logs first!', 
                   ha='center', va='center', fontsize=12, color='gray')
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis('off')
        
        fig.tight_layout()
        
        canvas = FigureCanvasTkAgg(fig, frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        return frame
    
    def _create_success_rate(self, parent):
        """Create success rate gauge"""
        frame = ttk.LabelFrame(parent, text="📊 Overall Success Rate")
        
        fig = Figure(figsize=(5, 3), dpi=80)
        ax = fig.add_subplot(111)
        
        stats = self.db.get_statistics()
        
        if stats.get('total_logs', 0) > 0:
            # Calculate success rate (simplified)
            total_errors = stats.get('total_errors', 0)
            total_logs = stats.get('total_logs', 1)
            
            # Estimate success rate (100% - error percentage)
            # Assuming average of 10 operations per log
            total_operations = total_logs * 10
            success_rate = max(0, 100 - (total_errors / total_operations * 100))
            
            # Create pie chart showing success vs errors
            sizes = [success_rate, 100 - success_rate]
            colors = ['#4CAF50', '#FF5252']
            labels = [f'Success\n{success_rate:.1f}%', f'Errors\n{100-success_rate:.1f}%']
            
            ax.pie(sizes, labels=labels, colors=colors, autopct='', startangle=90)
            ax.axis('equal')
        else:
            ax.text(0.5, 0.5, 'No data yet\nParse some logs first!', 
                   ha='center', va='center', fontsize=12, color='gray')
            ax.axis('off')
        
        fig.tight_layout()
        
        canvas = FigureCanvasTkAgg(fig, frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        return frame
    
    def refresh_charts(self):
        """Refresh all charts with latest data"""
        if not MATPLOTLIB_AVAILABLE:
            return
        
        # Destroy old frames and recreate
        for frame in [self.timeline_frame, self.ecu_frame, self.nrc_frame, self.success_frame]:
            frame.destroy()
        
        # Get parent
        parent = self.timeline_frame.master
        
        # Recreate charts
        self.timeline_frame = self._create_error_timeline(parent)
        self.timeline_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        
        self.ecu_frame = self._create_ecu_health(parent)
        self.ecu_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        
        self.nrc_frame = self._create_nrc_frequency(parent)
        self.nrc_frame.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
        
        self.success_frame = self._create_success_rate(parent)
        self.success_frame.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)
