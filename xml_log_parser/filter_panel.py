"""
Filter Panel for Advanced Filtering
Provides UI for filtering logs by ECU, severity, date range, etc.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class FilterPanel:
    """Advanced filter panel dialog"""
    
    def __init__(self, parent, config_manager, callback):
        self.parent = parent
        self.config = config_manager
        self.callback = callback
        
        # Create dialog window
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Advanced Filters")
        self.dialog.geometry("600x500")
        self.dialog.transient(parent)
        
        self._create_widgets()
        
        # Load saved filters
        self._load_saved_filters()
    
    def _create_widgets(self):
        """Create filter UI components"""
        # Main container
        main_frame = ttk.Frame(self.dialog, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Preset management
        preset_frame = ttk.LabelFrame(main_frame, text="Filter Presets", padding="10")
        preset_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.preset_var = tk.StringVar()
        preset_combo = ttk.Combobox(preset_frame, textvariable=self.preset_var, width=40)
        preset_combo['values'] = self._get_preset_names()
        preset_combo.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(preset_frame, text="Load", command=self._load_preset).pack(side=tk.LEFT, padx=2)
        ttk.Button(preset_frame, text="Save", command=self._save_preset).pack(side=tk.LEFT, padx=2)
        ttk.Button(preset_frame, text="Delete", command=self._delete_preset).pack(side=tk.LEFT, padx=2)
        
        # ECU filter
        self._create_ecu_filters(main_frame)
        
        # Severity filter
        self._create_severity_filters(main_frame)
        
        # Date range filter
        self._create_date_filters(main_frame)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(button_frame, text="Apply Filters", command=self._apply_filters, width=20).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear All", command=self._clear_filters, width=20).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Close", command=self.dialog.destroy, width=20).pack(side=tk.RIGHT, padx=5)
    
    def _create_ecu_filters(self, parent):
        """Create ECU module checkboxes"""
        ecu_frame = ttk.LabelFrame(parent, text="ECU Modules", padding="10")
        ecu_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Scrollable frame for ECU list
        canvas = tk.Canvas(ecu_frame, height=150)
        scrollbar = ttk.Scrollbar(ecu_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor=tk.NW)
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # ECU checkboxes (simplified list for demo)
        self.ecu_vars = {}
        common_ecus = ['ABS', 'ABSB', 'PCM', 'TCM', 'BCM', 'APIM', 'IPC', 'RCM', 
                       'HVAC', 'PAM', 'FDIM', 'SCCM', 'ACM', 'DSM', 'GWM']
        
        for i, ecu in enumerate(common_ecus):
            var = tk.BooleanVar(value=True)
            self.ecu_vars[ecu] = var
            ttk.Checkbutton(scrollable_frame, text=ecu, variable=var).grid(
                row=i//5, column=i%5, sticky=tk.W, padx=5, pady=2
            )
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Select/Deselect all
        button_frame = ttk.Frame(ecu_frame)
        button_frame.pack(fill=tk.X, pady=5)
        ttk.Button(button_frame, text="Select All", command=lambda: self._toggle_all_ecus(True)).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Deselect All", command=lambda: self._toggle_all_ecus(False)).pack(side=tk.LEFT, padx=5)
    
    def _create_severity_filters(self, parent):
        """Create severity level checkboxes"""
        severity_frame = ttk.LabelFrame(parent, text="Severity Levels", padding="10")
        severity_frame.pack(fill=tk.X, pady=5)
        
        self.severity_vars = {}
        severities = ['CRITICAL', 'ERROR', 'WARNING', 'INFO']
        colors = ['red', 'orange', 'yellow', 'blue']
        
        for i, (severity, color) in enumerate(zip(severities, colors)):
            var = tk.BooleanVar(value=True)
            self.severity_vars[severity] = var
            cb = ttk.Checkbutton(severity_frame, text=severity, variable=var)
            cb.grid(row=0, column=i, padx=10, pady=5)
    
    def _create_date_filters(self, parent):
        """Create date range filters"""
        date_frame = ttk.LabelFrame(parent, text="Date Range", padding="10")
        date_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(date_frame, text="From:").grid(row=0, column=0, padx=5)
        self.date_from = tk.StringVar()
        ttk.Entry(date_frame, textvariable=self.date_from, width=15).grid(row=0, column=1, padx=5)
        ttk.Label(date_frame, text="(YYYY-MM-DD)").grid(row=0, column=2, padx=5)
        
        ttk.Label(date_frame, text="To:").grid(row=1, column=0, padx=5)
        self.date_to = tk.StringVar()
        ttk.Entry(date_frame, textvariable=self.date_to, width=15).grid(row=1, column=1, padx=5)
        ttk.Label(date_frame, text="(YYYY-MM-DD)").grid(row=1, column=2, padx=5)
    
    def _toggle_all_ecus(self, state):
        """Toggle all ECU checkboxes"""
        for var in self.ecu_vars.values():
            var.set(state)
    
    def _save_preset(self):
        """Save current filter configuration as preset"""
        preset_name = self.preset_var.get().strip()
        if not preset_name:
            messagebox.showwarning("No Name", "Please enter a preset name.")
            return
        
        # Collect current filter settings
        filters = {
            'ecus': {ecu: var.get() for ecu, var in self.ecu_vars.items()},
            'severities': {sev: var.get() for sev, var in self.severity_vars.items()},
            'date_from': self.date_from.get(),
            'date_to': self.date_to.get()
        }
        
        # Save to config
        presets = self.config.get('filter_presets', {})
        presets[preset_name] = filters
        self.config.set('filter_presets', presets)
        
        messagebox.showinfo("Saved", f"Filter preset '{preset_name}' saved.")
        
        # Update preset list
        self._update_preset_list()
    
    def _load_preset(self):
        """Load a saved preset"""
        preset_name = self.preset_var.get()
        if not preset_name:
            return
        
        presets = self.config.get('filter_presets', {})
        if preset_name not in presets:
            messagebox.showwarning("Not Found", f"Preset '{preset_name}' not found.")
            return
        
        filters = presets[preset_name]
        
        # Apply ECU filters
        for ecu, value in filters.get('ecus', {}).items():
            if ecu in self.ecu_vars:
                self.ecu_vars[ecu].set(value)
        
        # Apply severity filters
        for sev, value in filters.get('severities', {}).items():
            if sev in self.severity_vars:
                self.severity_vars[sev].set(value)
        
        # Apply date filters
        self.date_from.set(filters.get('date_from', ''))
        self.date_to.set(filters.get('date_to', ''))
        
        messagebox.showinfo("Loaded", f"Filter preset '{preset_name}' loaded.")
    
    def _delete_preset(self):
        """Delete a saved preset"""
        preset_name = self.preset_var.get()
        if not preset_name:
            return
        
        presets = self.config.get('filter_presets', {})
        if preset_name in presets:
            del presets[preset_name]
            self.config.set('filter_presets', presets)
            messagebox.showinfo("Deleted", f"Filter preset '{preset_name}' deleted.")
            self._update_preset_list()
    
    def _get_preset_names(self):
        """Get list of saved preset names"""
        presets = self.config.get('filter_presets', {})
        return list(presets.keys())
    
    def _update_preset_list(self):
        """Update preset combobox list"""
        # This would update the combobox values in a real implementation
        pass
    
    def _load_saved_filters(self):
        """Load previously saved filter configuration"""
        saved_filters = self.config.get_filter_config()
        
        if saved_filters:
            # Apply saved ECU selections
            selected_ecus = saved_filters.get('selected_ecus', [])
            for ecu, var in self.ecu_vars.items():
                var.set(ecu in selected_ecus or not selected_ecus)
            
            # Apply saved severity selections
            severity_levels = saved_filters.get('severity_levels', [])
            for sev, var in self.severity_vars.items():
                var.set(sev in severity_levels or not severity_levels)
    
    def _apply_filters(self):
        """Apply current filter settings"""
        # Collect selected ECUs
        selected_ecus = [ecu for ecu, var in self.ecu_vars.items() if var.get()]
        
        # Collect selected severities
        selected_severities = [sev for sev, var in self.severity_vars.items() if var.get()]
        
        # Get date range
        date_from = self.date_from.get()
        date_to = self.date_to.get()
        
        # Validate dates
        if date_from:
            try:
                datetime.strptime(date_from, '%Y-%m-%d')
            except ValueError:
                messagebox.showerror("Invalid Date", "From date must be in YYYY-MM-DD format.")
                return
        
        if date_to:
            try:
                datetime.strptime(date_to, '%Y-%m-%d')
            except ValueError:
                messagebox.showerror("Invalid Date", "To date must be in YYYY-MM-DD format.")
                return
        
        # Create filter configuration
        filters = {
            'selected_ecus': selected_ecus,
            'severity_levels': selected_severities,
            'time_range': {
                'from': date_from,
                'to': date_to
            } if date_from or date_to else None
        }
        
        # Save to config
        self.config.save_filter_config(filters)
        
        # Call callback with filters
        if self.callback:
            self.callback(filters)
        
        # Close dialog
        self.dialog.destroy()
    
    def _clear_filters(self):
        """Clear all filters (select all)"""
        self._toggle_all_ecus(True)
        for var in self.severity_vars.values():
            var.set(True)
        self.date_from.set('')
        self.date_to.set('')
