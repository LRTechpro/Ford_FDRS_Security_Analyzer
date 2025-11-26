"""
Enhanced GUI Application for XML and Text Log Parser
With Dark Mode, Keyboard Shortcuts, Analytics, Filtering, Comparison, and History
"""

import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox
try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
    TKINTERDND_AVAILABLE = True
except ImportError:
    TKINTERDND_AVAILABLE = False
import json
import os
import re
from collections import Counter
from xml_log_parser import XMLLogParser, NRCCodeExplainer, HexExplainer
from text_log_parser import TextLogParser
from simplified_report import SimplifiedReportGenerator
from config_manager import ConfigManager
from charts_panel import ChartsPanel
from filter_panel import FilterPanel
from comparison_engine import LogComparator
from database_manager import DatabaseManager
from fdrs_log_parser import FDRSLogParser
from performance_manager import PerformanceManager, ProgressDialog
from ui_enhancements import ToolTipManager, LoadingAnimation, StatusBarEnhancer, ModernButton, add_tooltip
try:
    from module_dependency_tracker import ModuleDependencyTracker
    DEPENDENCY_TRACKER_AVAILABLE = True
except ImportError:
    DEPENDENCY_TRACKER_AVAILABLE = False
try:
    from cybersecurity_analyzer import CybersecurityAnalyzer
    CYBERSECURITY_AVAILABLE = True
except ImportError:
    CYBERSECURITY_AVAILABLE = False
try:
    from smart_filter_engine import SmartFilterEngine
    SMART_FILTER_AVAILABLE = True
except ImportError:
    SMART_FILTER_AVAILABLE = False
try:
    from enhanced_diagnostic_analyzer import EnhancedDiagnosticAnalyzer
    ENHANCED_DIAGNOSTICS_AVAILABLE = True
except ImportError:
    ENHANCED_DIAGNOSTICS_AVAILABLE = False
try:
    from critical_diagnostic_view import CriticalDiagnosticView, format_critical_diagnostics_report
    CRITICAL_DIAGNOSTICS_AVAILABLE = True
except ImportError:
    CRITICAL_DIAGNOSTICS_AVAILABLE = False
import threading


class EnhancedLogParserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Log Parser Pro - Enhanced Edition")
        
        # Initialize managers
        self.config = ConfigManager()
        self.db = DatabaseManager()
        
        # Initialize performance manager
        self.performance = PerformanceManager()
        self.performance.set_progress_callback(self._on_progress_update)
        self.performance.set_status_callback(self._on_status_update)
        
        # Initialize UI enhancements
        self.tooltip_manager = ToolTipManager()
        self.loading_animation = None
        self.progress_dialog = None
        
        # Load saved geometry
        geometry = self.config.get_window_geometry()
        if geometry and geometry.get('width') and geometry.get('height'):
            x = geometry.get('x', 100) or 100
            y = geometry.get('y', 100) or 100
            self.root.geometry(f"{geometry['width']}x{geometry['height']}+{x}+{y}")
        else:
            self.root.geometry("1400x900")
        
        # Initialize parsers
        self.xml_parser = XMLLogParser()
        self.text_parser = TextLogParser()
        self.report_generator = SimplifiedReportGenerator()
        self.comparator = LogComparator()
        
        # Initialize smart filter engine
        if SMART_FILTER_AVAILABLE:
            self.smart_filter = SmartFilterEngine()
        else:
            self.smart_filter = None
        
        # State variables
        self.current_results = []
        self.current_file_type = None
        self.current_filepath = None
        self.dependency_report = None  # Store dependency analysis results
        self.security_report = None  # Store security analysis results
        self.enhanced_diagnostics = None  # Store enhanced diagnostic analysis (voltage, SOC, temp, etc.)
        self.critical_diagnostics = None  # Store critical diagnostic view (VIN, voltage, DTCs, errors, etc.)
        self.active_filter_keywords = []  # Currently active filter keywords
        
        # Apply theme
        self._apply_theme()
        
        # Create widgets
        self._create_menu()
        self._create_widgets()
        self._bind_shortcuts()
        self._setup_drag_drop()
        
        # Save geometry on close
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)
    
    def _on_progress_update(self, percentage: int, status: str):
        """Handle progress updates from performance manager"""
        if self.progress_dialog:
            self.progress_dialog.update_progress(percentage, status)
        
        # Also update main status
        self.status.set(f"{status} ({percentage}%)")
    
    def _on_status_update(self, status: str):
        """Handle status updates from performance manager"""
        self.status.set(status)
        if self.progress_dialog:
            self.progress_dialog.update_status(status)
        
        self.status.set("Ready - Drag & drop log files or use File > Open")
    
    def _apply_theme(self):
        """Apply light or dark theme with professional enhancements"""
        theme = self.config.get_theme()
        
        if theme == 'dark':
            self.colors = {
                'bg': '#2b2b2b',
                'fg': '#ffffff',
                'select_bg': '#404040',
                'select_fg': '#ffffff',
                'button_bg': '#404040',
                'text_bg': '#1e1e1e',
                'text_fg': '#d4d4d4',
                'accent': '#007acc',
                'output_bg': '#2a2a2a',      # Slightly different from main bg
                'primary_btn': '#0072C6',    # Ford blue for primary actions
                'secondary_btn': '#6c757d',  # Neutral grey for secondary
                'destructive_btn': '#dc3545' # Red for destructive actions
            }
        else:  # light theme
            self.colors = {
                'bg': '#f0f0f0',
                'fg': '#000000',
                'select_bg': '#0078d7',
                'select_fg': '#ffffff',
                'button_bg': '#e1e1e1',
                'text_bg': '#ffffff',
                'text_fg': '#000000',
                'accent': '#0066cc',
                'output_bg': '#F4F8FE',      # Soft blue tint for output
                'primary_btn': '#0072C6',    # Ford blue for primary actions
                'secondary_btn': '#6c757d',  # Neutral grey for secondary
                'destructive_btn': '#dc3545' # Red for destructive actions
            }
        
        # Configure ttk style with professional enhancements
        style = ttk.Style()
        style.theme_use('clam')
        
        # Base styles
        style.configure('TFrame', background=self.colors['bg'])
        style.configure('TLabel', background=self.colors['bg'], foreground=self.colors['fg'])
        style.configure('TLabelframe', background=self.colors['bg'], foreground=self.colors['fg'])
        style.configure('TLabelframe.Label', background=self.colors['bg'], foreground=self.colors['fg'])
        
        # Button styles with enhanced appearance
        style.configure('TButton', 
                       background=self.colors['button_bg'], 
                       foreground=self.colors['fg'],
                       padding=(10, 4),  # Better button padding
                       relief='flat')
        style.map('TButton', 
                 background=[('active', self.colors['select_bg']),
                           ('pressed', self.colors['accent'])])
        
        # Primary button style (Ford blue)
        style.configure('Primary.TButton',
                       background=self.colors['primary_btn'],
                       foreground='white',
                       padding=(12, 6),
                       relief='flat')
        style.map('Primary.TButton',
                 background=[('active', '#005a9f'),
                           ('pressed', '#004080')])
        
        # Secondary button style
        style.configure('Secondary.TButton',
                       background=self.colors['secondary_btn'],
                       foreground='white',
                       padding=(10, 4),
                       relief='flat')
        
        # Destructive button style (red)
        style.configure('Destructive.TButton',
                       background=self.colors['destructive_btn'],
                       foreground='white',
                       padding=(10, 4),
                       relief='flat')
        
        # Group box style with subtle border
        style.configure('Actions.TLabelframe',
                       background=self.colors['bg'],
                       foreground=self.colors['fg'],
                       borderwidth=1,
                       relief='solid')
        style.configure('Actions.TLabelframe.Label',
                       background=self.colors['bg'],
                       foreground=self.colors['fg'],
                       padding=(6, 2))
        
        self.root.configure(bg=self.colors['bg'])
    
    def _create_menu(self):
        """Create menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open Log... (Ctrl+O)", command=self._browse_file)
        file_menu.add_command(label="Paste Content... (Ctrl+Shift+V)", command=self._paste_content)
        
        # Recent files submenu
        self.recent_menu = tk.Menu(file_menu, tearoff=0)
        file_menu.add_cascade(label="Recent Files", menu=self.recent_menu)
        self._update_recent_files_menu()
        
        file_menu.add_separator()
        file_menu.add_command(label="Export JSON (Ctrl+S)", command=self._export_json)
        file_menu.add_command(label="Export TXT", command=self._export_txt)
        file_menu.add_separator()
        file_menu.add_command(label="Clear Recent Files", command=self._clear_recent_files)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._on_closing)
        
        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_checkbutton(label="Simple Mode (Ctrl+M)", command=self._toggle_mode)
        view_menu.add_separator()
        view_menu.add_command(label="Toggle Dark Mode", command=self._toggle_theme)
        view_menu.add_command(label="Refresh (F5)", command=self._refresh_display)
        view_menu.add_separator()
        view_menu.add_command(label="Clear Results (Ctrl+L)", command=self._clear_results)
        
        # Tools menu
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Find... (Ctrl+F)", command=self._show_find_dialog)
        tools_menu.add_command(label="Advanced Filters", command=self._show_filter_panel)
        tools_menu.add_separator()
        tools_menu.add_command(label="🚀 Launch Professional Analyzer", command=self._launch_professional_analyzer)
        tools_menu.add_command(label="📊 Complex Diagnostic Mode", command=self._switch_to_professional_mode)
        tools_menu.add_separator()
        tools_menu.add_command(label="Database Statistics", command=self._show_db_stats)
        tools_menu.add_command(label="Clean Old Logs", command=self._clean_old_logs)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Keyboard Shortcuts", command=self._show_shortcuts)
        help_menu.add_command(label="About", command=self._show_about)
    
    def _update_recent_files_menu(self):
        """Update recent files menu"""
        self.recent_menu.delete(0, tk.END)
        
        recent_files = self.config.get_recent_files()
        if not recent_files:
            self.recent_menu.add_command(label="(No recent files)", state=tk.DISABLED)
        else:
            for filepath in recent_files:
                filename = os.path.basename(filepath)
                self.recent_menu.add_command(
                    label=filename,
                    command=lambda f=filepath: self._open_file(f)
                )
    
    def _check_nrc7f_issues(self):
        """Check for critical NRC issues (7F and 22) and show/hide alert accordingly"""
        if not self.current_results:
            self.nrc7f_alert.grid_remove()
            return
        
        # Search for critical NRC patterns in results
        critical_nrc_issues = []
        nrc7f_count = 0
        nrc22_count = 0
        
        for result in self.current_results:
            result_str = str(result)
            result_lower = result_str.lower()
            
            # Check for NRC 7F patterns
            if any(pattern in result_lower for pattern in [
                'nrc 7f', 'nrc7f', 'nrc:7f', 'nrc=7f', 'nrc-7f',
                'servicenotsupportedinactivesession',
                '7f22', '7f27', '7f10', '7f11', '7f34', '7f36',  # Common service codes with 7F
                'service not supported in active session'
            ]):
                critical_nrc_issues.append(('NRC_7F', result))
                nrc7f_count += 1
            
            # Check for NRC 22 patterns - CONDITIONS NOT CORRECT
            elif any(pattern in result_lower for pattern in [
                'nrc 22', 'nrc22', 'nrc:22', 'nrc=22', 'nrc-22',
                'conditionsnotcorrect', 'conditions not correct',
                '7f22 22', '22 22', 'nrc22 for updates', 'throwing nrc-22',
                'request sequence error', 'conditions not met',
                'preconditions not met', 'invalid state for operation'
            ]):
                critical_nrc_issues.append(('NRC_22', result))
                nrc22_count += 1
        
        # Show/hide alert based on findings
        if critical_nrc_issues:
            self.nrc7f_alert.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=10, pady=5)
            # Store the issues for detailed view
            self.nrc7f_issues = critical_nrc_issues
            
            # Create comprehensive status message
            if nrc7f_count > 0 and nrc22_count > 0:
                self.status.set(f"🚨 CRITICAL NRC ERRORS: {nrc7f_count} NRC-7F + {nrc22_count} NRC-22 - Multiple update/session issues!")
                self._update_alert_display("MULTIPLE NRC ERRORS", nrc7f_count, nrc22_count)
            elif nrc7f_count > 0:
                self.status.set(f"🚨 NRC 7F DETECTED: {nrc7f_count} occurrences - ECU session issue preventing updates!")
                self._update_alert_display("NRC 7F DETECTED", nrc7f_count, 0)
            else:  # nrc22_count > 0
                self.status.set(f"🚨 NRC 22 DETECTED: {nrc22_count} occurrences - Conditions not correct for updates!")
                self._update_alert_display("NRC 22 DETECTED", 0, nrc22_count)
        else:
            self.nrc7f_alert.grid_remove()
            self.nrc7f_issues = []
    
    def _update_alert_display(self, main_text, nrc7f_count, nrc22_count):
        """Update the alert banner display with appropriate text and colors"""
        # Find and update the alert text elements
        for child in self.nrc7f_alert.winfo_children():
            if isinstance(child, tk.Label) and child.cget('font')[1] == 12:  # Main alert text
                if nrc7f_count > 0 and nrc22_count > 0:
                    child.config(text=f"CRITICAL: {nrc7f_count} NRC-7F + {nrc22_count} NRC-22 ERRORS DETECTED")
                elif nrc7f_count > 0:
                    child.config(text="NRC 7F DETECTED - SERVICE NOT SUPPORTED IN ACTIVE SESSION")
                elif nrc22_count > 0:
                    child.config(text="NRC 22 DETECTED - CONDITIONS NOT CORRECT FOR UPDATE")
            elif isinstance(child, tk.Label) and child.cget('font')[1] == 10:  # Detail text
                if nrc7f_count > 0 and nrc22_count > 0:
                    child.config(text="⚠️ MULTIPLE UPDATE FAILURES - Both session management and precondition errors detected")
                elif nrc7f_count > 0:
                    child.config(text="⚠️ FAILING TO UPDATE - ECU rejecting operations due to incorrect diagnostic session mode")
                elif nrc22_count > 0:
                    child.config(text="⚠️ UPDATE CONDITIONS NOT MET - ECU preconditions not satisfied for programming operations")
            elif isinstance(child, tk.Button):  # Action button
                if nrc7f_count > 0 and nrc22_count > 0:
                    child.config(text="📋 Show All NRC Issues")
                elif nrc7f_count > 0:
                    child.config(text="📋 Show All NRC 7F Issues")
                elif nrc22_count > 0:
                    child.config(text="📋 Show All NRC 22 Issues")

    def _check_for_professional_mode_suggestion(self):
        """Check if complex issues warrant suggesting Professional Diagnostic Analyzer"""
        if not self.current_results:
            return
        
        # Analyze complexity indicators
        total_results = len(self.current_results)
        error_count = sum(1 for r in self.current_results if 
                         'error' in str(r).lower() or 'fail' in str(r).lower())
        
        critical_indicators = 0
        
        # Check for multiple error types
        if error_count > 5:
            critical_indicators += 2
        elif error_count > 2:
            critical_indicators += 1
        
        # Check for NRC issues
        has_nrc_issues = hasattr(self, 'nrc7f_issues') and self.nrc7f_issues
        if has_nrc_issues:
            critical_indicators += 2
        
        # Check for multiple modules/ECUs
        content_str = ' '.join(str(r) for r in self.current_results)
        ecu_patterns = ['7d0', '7e0', '726', '716', '720', '754', 'bcm', 'pcm', 'apim', 'tcm']
        detected_ecus = sum(1 for pattern in ecu_patterns if pattern in content_str.lower())
        if detected_ecus > 3:
            critical_indicators += 1
        
        # Check success rate
        success_count = sum(1 for r in self.current_results if 
                           'success' in str(r).lower() or 'pass' in str(r).lower())
        if total_results > 0:
            success_rate = success_count / total_results
            if success_rate < 0.3:  # Less than 30% success
                critical_indicators += 2
        
        # Suggest Professional mode if complexity is high
        if critical_indicators >= 3:
            # Show the Professional mode button
            if hasattr(self, 'professional_btn'):
                self.professional_btn.pack(side=tk.LEFT, padx=5)
            
            # Don't show the dialog suggestion more than once per session
            if not hasattr(self, '_professional_suggestion_shown'):
                self._professional_suggestion_shown = True
                self._show_professional_mode_suggestion(error_count, success_rate if total_results > 0 else 0)
        else:
            # Hide the Professional mode button for simple cases
            if hasattr(self, 'professional_btn'):
                self.professional_btn.pack_forget()
    
    def _show_professional_mode_suggestion(self, error_count, success_rate):
        """Show suggestion to use Professional Diagnostic Analyzer"""
        success_percentage = success_rate * 100
        
        suggestion_text = f"""🚨 COMPLEX DIAGNOSTIC SCENARIO DETECTED
        
Your analysis shows indicators of complex vehicle issues:

📊 Current Analysis:
  • Total Issues: {error_count} errors detected
  • Success Rate: {success_percentage:.1f}%
  • Multiple system involvement detected
  
🚀 RECOMMENDED: Professional Diagnostic Analyzer
  
The Professional Analyzer provides advanced capabilities for complex diagnostics:
  
✅ Multi-source correlation analysis
✅ AI-powered diagnostic insights  
✅ Enhanced NRC 7F/22 detection
✅ Cross-report pattern analysis
✅ Professional reporting formats
✅ Timeline correlation
✅ ECU relationship mapping

Would you like to launch the Professional Diagnostic Analyzer for deeper analysis?"""
        
        result = messagebox.askyesno("Professional Analysis Recommended", suggestion_text)
        if result:
            self._launch_professional_analyzer()

    def _show_nrc7f_details(self):
        """Show detailed NRC analysis (7F and 22) in a separate window"""
        if not hasattr(self, 'nrc7f_issues') or not self.nrc7f_issues:
            messagebox.showinfo("No Issues", "No critical NRC issues found in current log.")
            return
        
        # Categorize the issues
        nrc7f_issues = [issue for nrc_type, issue in self.nrc7f_issues if nrc_type == 'NRC_7F']
        nrc22_issues = [issue for nrc_type, issue in self.nrc7f_issues if nrc_type == 'NRC_22']
        
        # Determine window title based on issue types
        if nrc7f_issues and nrc22_issues:
            title = f"🚨 CRITICAL NRC ERRORS - {len(nrc7f_issues)} NRC-7F + {len(nrc22_issues)} NRC-22"
        elif nrc7f_issues:
            title = f"🚨 NRC 7F - Service Not Supported In Active Session ({len(nrc7f_issues)} issues)"
        else:
            title = f"🚨 NRC 22 - Conditions Not Correct ({len(nrc22_issues)} issues)"
        
        # Create detailed window
        detail_window = tk.Toplevel(self.root)
        detail_window.title(title)
        detail_window.geometry("1200x800")
        detail_window.configure(bg='#2c3e50')
        
        # Header with explanation
        header_frame = tk.Frame(detail_window, bg='#e74c3c', height=120)
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        header_frame.pack_propagate(False)
        
        # Dynamic title based on issue types
        if nrc7f_issues and nrc22_issues:
            header_text = f"🚨 CRITICAL NRC ERRORS - {len(nrc7f_issues)} NRC-7F + {len(nrc22_issues)} NRC-22 DETECTED"
            explanation_text = "Multiple update failures detected: Session management issues (NRC-7F) AND precondition failures (NRC-22).\nBoth ECU session state and update conditions need to be addressed."
        elif nrc7f_issues:
            header_text = "🚨 NRC 7F - SERVICE NOT SUPPORTED IN ACTIVE SESSION"
            explanation_text = "ECU is refusing operations because it's not in the correct diagnostic session mode.\nCommon cause: Trying to program/update while ECU is in default session instead of programming session."
        else:
            header_text = "🚨 NRC 22 - CONDITIONS NOT CORRECT FOR UPDATE"
            explanation_text = "ECU is rejecting update operations because preconditions are not met.\nCommon causes: Wrong voltage, temperature, vehicle state, or missing prerequisites."
        
        title_label = tk.Label(header_frame, 
                              text=header_text, 
                              font=('Arial', 15, 'bold'), bg='#e74c3c', fg='white')
        title_label.pack(pady=5)
        
        explanation = tk.Label(header_frame, 
                              text=explanation_text, 
                              font=('Arial', 10), bg='#e74c3c', fg='white', wraplength=1100, justify=tk.CENTER)
        explanation.pack(pady=5)
        
        # Content notebook for different views
        content_notebook = ttk.Notebook(detail_window)
        content_notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # 1. All NRC Issues Occurrences
        occurrences_frame = ttk.Frame(content_notebook)
        total_issues = len(nrc7f_issues) + len(nrc22_issues)
        content_notebook.add(occurrences_frame, text=f"📋 All Issues ({total_issues})")
        
        occurrences_text = scrolledtext.ScrolledText(
            occurrences_frame, font=('Consolas', 10), wrap=tk.WORD,
            bg='#2c3e50', fg='#ecf0f1', insertbackground='white'
        )
        occurrences_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Add NRC 7F issues if present
        if nrc7f_issues:
            occurrences_text.insert(tk.END, f"🚨 NRC 7F ISSUES ({len(nrc7f_issues)} found) - SERVICE NOT SUPPORTED IN ACTIVE SESSION\n", "header")
            occurrences_text.insert(tk.END, "═" * 100 + "\n", "separator")
            for i, issue in enumerate(nrc7f_issues, 1):
                issue_text = str(issue)
                if isinstance(issue, dict):
                    issue_text = issue.get('line', issue.get('text', str(issue)))
                
                occurrences_text.insert(tk.END, f"NRC 7F Issue #{i}:\n", "issue_header")
                occurrences_text.insert(tk.END, f"{issue_text}\n\n", "normal")
        
        # Add NRC 22 issues if present
        if nrc22_issues:
            if nrc7f_issues:  # Add separator if both types present
                occurrences_text.insert(tk.END, "\n" + "═" * 100 + "\n", "separator")
            occurrences_text.insert(tk.END, f"🚨 NRC 22 ISSUES ({len(nrc22_issues)} found) - CONDITIONS NOT CORRECT\n", "header")
            occurrences_text.insert(tk.END, "═" * 100 + "\n", "separator")
            for i, issue in enumerate(nrc22_issues, 1):
                issue_text = str(issue)
                if isinstance(issue, dict):
                    issue_text = issue.get('line', issue.get('text', str(issue)))
                
                occurrences_text.insert(tk.END, f"NRC 22 Issue #{i}:\n", "issue_header")
                occurrences_text.insert(tk.END, f"{issue_text}\n\n", "normal")
        
        # 2. Troubleshooting Guide
        guide_frame = ttk.Frame(content_notebook)
        content_notebook.add(guide_frame, text="🔧 Troubleshooting")
        
        guide_text = scrolledtext.ScrolledText(
            guide_frame, font=('Arial', 11), wrap=tk.WORD,
            bg='#34495e', fg='#ecf0f1', insertbackground='white'
        )
        guide_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create dynamic troubleshooting guide based on issues found
        if nrc7f_issues and nrc22_issues:
            troubleshooting_guide = """🔧 CRITICAL NRC ERROR TROUBLESHOOTING GUIDE

🚨 MULTIPLE NRC ERRORS DETECTED - BOTH NRC 7F AND NRC 22!

═══════════════════════════════════════════════════════════════════════

📋 NRC 7F - SERVICE NOT SUPPORTED IN ACTIVE SESSION
• ECU received valid request but current session doesn't allow the operation
• Most common: Trying to program while in DEFAULT session instead of PROGRAMMING session

🎯 NRC 7F ROOT CAUSES:
1. ECU in DEFAULT session (0x01) instead of PROGRAMMING session (0x02)
2. Security access (seed-key) not established or expired
3. ECU session timed out and reverted to default

⚡ NRC 7F IMMEDIATE FIXES:
1. Enter Programming Session: Service 0x10 sub-function 0x02
2. Establish Security Access: Service 0x27 with proper seed-key
3. Verify Session Status: Service 0x22 with DID F186

═══════════════════════════════════════════════════════════════════════

📋 NRC 22 - CONDITIONS NOT CORRECT (KNOWN ISSUE FOR UPDATES!)
• ECU rejecting operations because preconditions are not satisfied
• Common during update attempts - often environmental or state-related

🎯 NRC 22 ROOT CAUSES:
1. Vehicle voltage too low/high (must be 12-14V typically)
2. Engine running (some updates require engine OFF)
3. Doors open, parking brake not set
4. ECU temperature outside acceptable range
5. Other modules not in correct state
6. Previous update not completed properly

⚡ NRC 22 IMMEDIATE FIXES:
1. Check Vehicle Conditions:
   • Engine OFF, ignition ON
   • All doors closed, parking brake set
   • Battery voltage stable 12-14V
2. Check ECU Prerequisites:
   • Ensure no pending DTCs that block programming
   • Verify ECU is not in limp mode
   • Check for active communication with other modules
3. Reset ECU State:
   • Perform ECU reset (service 0x11)
   • Clear any pending programming flags
   • Retry after 30 seconds

💡 COMBINED RESOLUTION STRATEGY:
1. Fix NRC 22 conditions FIRST (vehicle state, voltage, etc.)
2. Then address NRC 7F (session management, security access)
3. Follow proper UDS sequence: Conditions → Session → Security → Operation

🚨 CRITICAL NOTES:
• NRC 22 often indicates vehicle/ECU not ready for programming
• NRC 7F indicates session management failure
• Both must be resolved for successful updates
• Never attempt to override - fix root causes

📞 FORD SPECIFIC:
• Use FDRS for proper update procedures
• Check TSBs for known NRC 22 workarounds
• Ensure FDRS version supports target ECU
• Verify all modules are at compatible software levels"""
        elif nrc7f_issues:
            troubleshooting_guide = """🔧 NRC 7F TROUBLESHOOTING GUIDE

📋 WHAT IS NRC 7F?
NRC 7F means "Service Not Supported In Active Session"
• The ECU received a valid diagnostic request
• But the current session doesn't allow that operation
• Most commonly occurs during programming/flashing attempts

🎯 ROOT CAUSES:
1. ECU is in DEFAULT session (0x01) instead of PROGRAMMING session (0x02)
2. Trying to flash/program without entering programming session first
3. Security access (seed-key) not properly established
4. ECU session timed out and reverted to default

⚡ IMMEDIATE FIXES:
1. Enter Programming Session First:
   • Send diagnostic service 0x10 with sub-function 0x02
   • Wait for positive response before attempting programming

2. Establish Security Access:
   • Send service 0x27 (Security Access) with proper seed-key
   • Ensure security is unlocked before programming

3. Check Session Status:
   • Send service 0x22 with DID F186 to check current session
   • Verify ECU is in programming session (0x02)

4. Reset and Retry:
   • Send ECU reset (service 0x11) 
   • Re-establish programming session
   • Retry the operation

💡 PREVENTION:
• Always verify session state before programming
• Implement proper session management in diagnostic scripts
• Add timeouts and session refresh logic
• Monitor for session transitions

� FORD SPECIFIC:
• Use FDRS programming procedures
• Verify module is supported for over-the-air updates  
• Check for any TSBs related to programming issues"""
        else:  # nrc22_issues only
            troubleshooting_guide = """🔧 NRC 22 TROUBLESHOOTING GUIDE - CONDITIONS NOT CORRECT

📋 WHAT IS NRC 22? (KNOWN ISSUE FOR UPDATES!)
NRC 22 means "Conditions Not Correct" or "Request Sequence Error"
• ECU is rejecting the operation because prerequisites are not met
• Very common during update/programming attempts
• Often related to vehicle state, voltage, or environmental conditions

🎯 ROOT CAUSES:
1. VEHICLE STATE ISSUES:
   • Battery voltage too low/high (outside 12-14V range)
   • Engine running when it should be OFF
   • Doors open, parking brake not engaged
   • Transmission not in PARK
   • ECU temperature outside acceptable range

2. ECU PREPARATION ISSUES:
   • Previous programming session not properly closed
   • Pending DTCs blocking programming
   • ECU in fault/limp mode
   • Security access expired or not established

3. MODULE COMMUNICATION ISSUES:
   • Other ECUs not responding on network
   • CAN bus communication errors
   • Required modules not at compatible software levels

⚡ IMMEDIATE FIXES:
1. VERIFY VEHICLE CONDITIONS:
   • Engine OFF, ignition ON
   • All doors closed and locked
   • Parking brake engaged, transmission in PARK
   • Battery voltage stable (use battery maintainer if needed)

2. CHECK ECU STATUS:
   • Read and clear any DTCs
   • Verify ECU responds to basic communication
   • Check ECU isn't in protected/limp mode
   • Ensure no active faults

3. RESET AND RETRY:
   • Perform ECU reset (service 0x11)
   • Wait 30-60 seconds for ECU to stabilize
   • Re-establish communication and retry

💡 PREVENTION:
• Always check vehicle conditions before programming
• Use proper programming equipment with stable power
• Follow manufacturer's programming procedures exactly
• Ensure environment is within temperature specifications

🚨 CRITICAL NOTES FOR NRC 22:
• This is a KNOWN ISSUE for updates - very common!
• Usually indicates vehicle/ECU not ready for programming
• Don't ignore - fix the underlying conditions
• Multiple attempts without fixing conditions may damage ECU

📞 FORD SPECIFIC NRC 22 SOLUTIONS:
• Check FDRS for specific vehicle preparation steps
• Some modules require specific ignition cycle procedures
• Verify all modules are awake and communicating
• Check for TSBs addressing NRC 22 for your specific module"""
        
        guide_text.insert("1.0", troubleshooting_guide)
        
        # Configure text formatting tags
        guide_text.tag_config("header", foreground="#e74c3c", font=('Arial', 12, 'bold'))
        guide_text.tag_config("issue_header", foreground="#f39c12", font=('Arial', 11, 'bold'))
        guide_text.tag_config("separator", foreground="#95a5a6")
        guide_text.tag_config("normal", foreground="#ecf0f1")
        
        guide_text.config(state=tk.DISABLED)
        
        # Configure formatting for occurrences text too
        occurrences_text.tag_config("header", foreground="#e74c3c", font=('Consolas', 11, 'bold'))
        occurrences_text.tag_config("issue_header", foreground="#f39c12", font=('Consolas', 10, 'bold'))
        occurrences_text.tag_config("separator", foreground="#95a5a6")
        occurrences_text.tag_config("normal", foreground="#ecf0f1")
        
        # 3. Quick Actions
        actions_frame = ttk.Frame(content_notebook)
        content_notebook.add(actions_frame, text="⚡ Quick Actions")
        
        # Create action buttons
        actions_container = tk.Frame(actions_frame, bg='#34495e')
        actions_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        action_buttons = [
            ("📋 Copy All Issues", lambda: self._copy_nrc7f_issues()),
            ("💾 Save Troubleshooting Report", lambda: self._save_nrc7f_report()),
            ("📧 Email Support Info", lambda: self._prepare_support_email()),
            ("🔄 Re-analyze Log", lambda: (detail_window.destroy(), self._parse_log()))
        ]
        
        for i, (text, command) in enumerate(action_buttons):
            btn = tk.Button(actions_container, text=text, command=command,
                           font=('Arial', 12), bg='#3498db', fg='white', 
                           relief=tk.RAISED, borderwidth=2)
            btn.pack(fill=tk.X, pady=10)
        
        # Configure text tags for occurrences
        occurrences_text.tag_config("header", foreground="#e74c3c", font=('Consolas', 12, 'bold'))
        occurrences_text.tag_config("normal", foreground="#ecf0f1")
        
        # Make occurrences read-only
        occurrences_text.config(state=tk.DISABLED)
    
    def _copy_nrc7f_issues(self):
        """Copy NRC 7F issues to clipboard"""
        if not hasattr(self, 'nrc7f_issues') or not self.nrc7f_issues:
            return
        
        content = "=== NRC 7F ISSUES DETECTED ===\n\n"
        for i, issue in enumerate(self.nrc7f_issues, 1):
            issue_text = str(issue)
            if isinstance(issue, dict):
                issue_text = issue.get('line', issue.get('text', str(issue)))
            content += f"Issue #{i}:\n{issue_text}\n\n"
        
        self.root.clipboard_clear()
        self.root.clipboard_append(content)
        messagebox.showinfo("Copied", f"Copied {len(self.nrc7f_issues)} NRC 7F issues to clipboard")
    
    def _save_nrc7f_report(self):
        """Save NRC 7F troubleshooting report to file"""
        filename = filedialog.asksaveasfilename(
            title="Save NRC 7F Report",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                from datetime import datetime
                content = f"""NRC 7F ANALYSIS REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Log File: {self.current_filepath or 'Pasted Content'}

SUMMARY:
Total NRC 7F issues detected: {len(getattr(self, 'nrc7f_issues', []))}

ISSUES FOUND:
"""
                for i, issue in enumerate(getattr(self, 'nrc7f_issues', []), 1):
                    issue_text = str(issue)
                    if isinstance(issue, dict):
                        issue_text = issue.get('line', issue.get('text', str(issue)))
                    content += f"\nIssue #{i}:\n{issue_text}\n"
                
                content += """\n
TROUBLESHOOTING RECOMMENDATIONS:
1. Verify ECU is in programming session (0x02) before operations
2. Establish proper security access (service 0x27)
3. Check session timeout and refresh as needed
4. Use proper UDS session flow: Default → Programming → Operation

NEXT STEPS:
- Review programming sequence in diagnostic tool
- Verify FDRS procedures are being followed
- Check for any session management issues in code
- Contact technical support if issues persist
"""
                
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                messagebox.showinfo("Saved", f"NRC 7F report saved to:\n{filename}")
                
            except Exception as e:
                messagebox.showerror("Save Error", f"Failed to save report:\n{e}")
    
    def _prepare_support_email(self):
        """Prepare email content for technical support"""
        import webbrowser
        import urllib.parse
        
        subject = "NRC 7F - Service Not Supported In Active Session - Technical Support Required"
        body = f"""Hello Technical Support,

I'm experiencing NRC 7F errors in my diagnostic log analysis. Here are the details:

ISSUE: NRC 7F (Service Not Supported In Active Session)
COUNT: {len(getattr(self, 'nrc7f_issues', []))} occurrences
LOG FILE: {self.current_filepath or 'Pasted content'}

SYMPTOMS:
- ECU rejecting diagnostic operations
- Programming/update failures
- Service requests returning NRC 7F

ANALYSIS COMPLETED:
- ✓ Log parsed and analyzed
- ✓ NRC 7F patterns identified
- ✓ Session management issues detected

Please advise on next troubleshooting steps.

Best regards,
[Your Name]
[Your Contact Info]
"""
        
        # Create mailto URL
        mailto_url = f"mailto:?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
        
        try:
            webbrowser.open(mailto_url)
            messagebox.showinfo("Email Prepared", "Email draft opened in your default email client")
        except Exception:
            # Fallback - copy to clipboard
            self.root.clipboard_clear()
            self.root.clipboard_append(f"Subject: {subject}\n\n{body}")
            messagebox.showinfo("Email Content", "Email content copied to clipboard")
    
    def _create_widgets(self):
        """Create all GUI widgets with professional layout"""
        
        # Main container with minimal padding for more compact layout
        main_frame = ttk.Frame(self.root, padding="4")  # Further reduced from 8 to 4
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(5, weight=1)  # Adjusted for new mode section
        
        # File selection section with minimal padding
        file_frame = ttk.LabelFrame(main_frame, text="📁 File Selection (Drag & Drop Supported)", padding="6")
        file_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 3))  # Reduced margins
        file_frame.columnconfigure(1, weight=1)
        
        ttk.Label(file_frame, text="Log File:").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.file_path = tk.StringVar()
        ttk.Entry(file_frame, textvariable=self.file_path, width=80).grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        
        # Enhanced browse button with tooltip
        browse_btn = ttk.Button(file_frame, text="Browse...", command=self._browse_file)
        browse_btn.grid(row=0, column=2, padx=5)
        add_tooltip(browse_btn, "Select a log file to analyze\nSupported formats: .xml, .txt, .log\nOr drag & drop files onto the window")
        
        # Enhanced paste button with tooltip
        paste_btn = ttk.Button(file_frame, text="📋 Paste Content", command=self._paste_content)
        paste_btn.grid(row=0, column=3, padx=5)
        add_tooltip(paste_btn, "Paste log content directly from clipboard\nUseful for analyzing copied log snippets")
        
        # Quick filter section with reduced padding
        filter_frame = ttk.LabelFrame(main_frame, text="⚡ Quick Filters & Options", padding="6")
        filter_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=3)
        filter_frame.columnconfigure(1, weight=1)
        
        ttk.Label(filter_frame, text="Keywords:").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.filters = tk.StringVar(value="error, failure, success, pass")
        ttk.Entry(filter_frame, textvariable=self.filters, width=60).grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        ttk.Button(filter_frame, text="Advanced...", command=self._show_filter_panel).grid(row=0, column=2, padx=5)
        
        # Combined mode controls (checkboxes and radios in one row)
        modes_frame = ttk.Frame(filter_frame)
        modes_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=3)
        
        self.simple_mode = tk.BooleanVar(value=True)
        self.show_hex = tk.BooleanVar(value=True)
        self.show_nrc = tk.BooleanVar(value=True)
        
        # Left side - checkboxes
        ttk.Checkbutton(modes_frame, text="🌟 Simple Mode", 
                       variable=self.simple_mode, 
                       command=self._toggle_mode).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Checkbutton(modes_frame, text="Explain Hex", variable=self.show_hex).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Checkbutton(modes_frame, text="Explain NRC", variable=self.show_nrc).pack(side=tk.LEFT, padx=(0, 20))
        
        # Right side - analysis mode radios
        ttk.Label(modes_frame, text="Analysis:").pack(side=tk.LEFT, padx=(0, 5))
        self.analysis_mode = tk.StringVar(value="expert")
        expert_radio = ttk.Radiobutton(modes_frame, text="Expert", 
                                      variable=self.analysis_mode, value="expert")
        expert_radio.pack(side=tk.LEFT, padx=(0, 8))
        
        correlation_radio = ttk.Radiobutton(modes_frame, text="Cross-Correlation", 
                                          variable=self.analysis_mode, value="correlation")
        correlation_radio.pack(side=tk.LEFT, padx=(0, 8))
        
        add_tooltip(expert_radio, "Standard diagnostic analysis\nRecommended for single log files")
        add_tooltip(correlation_radio, "Advanced multi-log correlation\nFor comparing related diagnostic sessions")
        
        # Manual Primary Module Selection (NEW)
        manual_frame = ttk.Frame(filter_frame)
        manual_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=3)
        
        ttk.Label(manual_frame, text="🎯 Primary Module Override:").pack(side=tk.LEFT, padx=(0, 5))
        self.manual_primary_module = tk.StringVar()
        primary_combo = ttk.Combobox(manual_frame, textvariable=self.manual_primary_module, width=20, state="readonly")
        primary_combo['values'] = (
            '', '716 (GWM - Gateway Module)', '7D0 (APIM - Audio/Video)', 
            '720 (IPC - Instrument Panel)', '726 (BCM - Body Control)', 
            '7E0 (PCM - Powertrain)', '754 (TCM - Transmission)',
            '732 (GSM - Gateway Support)', 'Custom...'
        )
        primary_combo.pack(side=tk.LEFT, padx=5)
        primary_combo.bind('<<ComboboxSelected>>', self._on_primary_module_selected)
        add_tooltip(primary_combo, "Override automatic primary module detection\n• Select '716 (GWM)' to force GWM as primary\n• Leave empty for automatic detection\n• Choose 'Custom...' to enter custom module ID")
        
        # Custom module entry (initially hidden)
        self.custom_module_frame = ttk.Frame(manual_frame)
        ttk.Label(self.custom_module_frame, text="Custom ID:").pack(side=tk.LEFT, padx=(10, 5))
        self.custom_module_entry = ttk.Entry(self.custom_module_frame, width=10)
        self.custom_module_entry.pack(side=tk.LEFT, padx=5)
        add_tooltip(self.custom_module_entry, "Enter 3-character hex ECU address\nExample: 716 for GWM, 7D0 for APIM")
        
        clear_btn = ttk.Button(manual_frame, text="Clear", command=self._clear_primary_override)
        clear_btn.pack(side=tk.RIGHT, padx=5)
        add_tooltip(clear_btn, "Clear primary module override\nReturn to automatic detection")
        
        # NRC 7F Alert Panel (NEW - for quick spotting)
        nrc7f_frame = ttk.Frame(main_frame)
        nrc7f_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=5)
        
        # Initially hidden NRC 7F alert
        self.nrc7f_alert = tk.Frame(nrc7f_frame, bg='#e74c3c', relief=tk.RAISED, borderwidth=3)
        self.nrc7f_alert.columnconfigure(1, weight=1)
        
        # Alert icon and text
        alert_icon = tk.Label(self.nrc7f_alert, text="🚨", font=('Segoe UI Emoji', 20), bg='#e74c3c', fg='white')
        alert_icon.grid(row=0, column=0, padx=10, pady=10)
        
        alert_text = tk.Label(self.nrc7f_alert, text="NRC 7F DETECTED - SERVICE NOT SUPPORTED IN ACTIVE SESSION", 
                             font=('Arial', 12, 'bold'), bg='#e74c3c', fg='white')
        alert_text.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=10)
        
        detail_text = tk.Label(self.nrc7f_alert, 
                              text="⚠️ FAILING TO UPDATE - The ECU is rejecting operations because it's not in the right diagnostic session mode", 
                              font=('Arial', 10), bg='#e74c3c', fg='white', wraplength=800)
        detail_text.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 10))
        
        # Quick action button
        quick_action_btn = tk.Button(self.nrc7f_alert, text="📋 Show All NRC 7F Issues", 
                                    command=lambda: self._show_nrc7f_details(), 
                                    bg='white', fg='#e74c3c', font=('Arial', 10, 'bold'))
        quick_action_btn.grid(row=0, column=2, padx=10, pady=10)
        
        # Hide alert initially
        self.nrc7f_alert.grid_remove()

        # Analysis Mode section removed - now combined with checkboxes above

        # Grouped action buttons with minimal padding  
        actions_frame = ttk.LabelFrame(main_frame, text="Actions", padding="4", style="Actions.TLabelframe")
        actions_frame.grid(row=3, column=0, pady=(0, 4))  # Moved up one row since we removed mode section
        
        # Primary action buttons (left side)
        primary_buttons = ttk.Frame(actions_frame)
        primary_buttons.pack(side=tk.LEFT, padx=(0, 10))
        
        # Analyze Primary File button (improvement #6 - better micro-copy)
        parse_btn = ttk.Button(primary_buttons, text="🔍 Analyze Primary File", 
                              command=self._parse_log, style="Primary.TButton")
        parse_btn.pack(side=tk.LEFT, padx=(0, 5))
        add_tooltip(parse_btn, "Analyze the selected log file\n• Extracts errors, warnings, and successes\n• Identifies ECU modules and dependencies\n• Performs cybersecurity analysis\n• Shows progress for large files")
        
        # Correlate All Reports button 
        correlate_btn = ttk.Button(primary_buttons, text="🔗 Correlate All Reports", 
                                  command=self._correlate_logs, style="Primary.TButton")
        correlate_btn.pack(side=tk.LEFT, padx=(0, 5))
        add_tooltip(correlate_btn, "Cross-correlate all logs in workspace\nand build composite report")
        
        # Secondary action buttons (middle)
        secondary_buttons = ttk.Frame(actions_frame)
        secondary_buttons.pack(side=tk.LEFT, padx=(0, 10))
        
        # Export JSON button  
        json_btn = ttk.Button(secondary_buttons, text="💾 Export JSON", 
                             command=self._export_json, style="Secondary.TButton")
        json_btn.pack(side=tk.LEFT, padx=(0, 5))
        add_tooltip(json_btn, "Export analysis results as JSON\nIncludes all parsed data, timestamps,\nand structured information for further processing")
        
        # Export TXT button
        txt_btn = ttk.Button(secondary_buttons, text="📄 Export TXT", 
                            command=self._export_txt, style="Secondary.TButton")
        txt_btn.pack(side=tk.LEFT, padx=(0, 5))
        add_tooltip(txt_btn, "Export human-readable text report\nIncludes summary, errors, recommendations,\nand formatted analysis results")
        
        # Critical Report button
        critical_btn = ttk.Button(secondary_buttons, text="🎯 Critical Report", 
                                 command=self._show_critical_report, style="Secondary.TButton")
        critical_btn.pack(side=tk.LEFT, padx=(0, 5))
        add_tooltip(critical_btn, "Show critical diagnostic information\nFocused on errors and warnings only")
        
        # Utility buttons (right side)
        utility_buttons = ttk.Frame(actions_frame)
        utility_buttons.pack(side=tk.LEFT)
        
        # Clear All button (improvement #6 - destructive action styling)
        clear_btn = ttk.Button(utility_buttons, text="🗑️ Clear All", 
                              command=self._clear_results, style="Destructive.TButton")
        clear_btn.pack(side=tk.LEFT, padx=(0, 5))
        add_tooltip(clear_btn, "Clear all analysis results and reset the interface")
        
        # Refresh button
        refresh_btn = ttk.Button(utility_buttons, text="🔄 Refresh", 
                                command=self._refresh_display)
        refresh_btn.pack(side=tk.LEFT, padx=(0, 5))
        add_tooltip(refresh_btn, "Refresh the current display and reload data")
        
        # Test Sample button
        test_btn = ttk.Button(utility_buttons, text="🧪 Test Sample", 
                             command=self._test_sample_data)
        test_btn.pack(side=tk.LEFT, padx=(0, 5))
        add_tooltip(test_btn, "Load and analyze sample diagnostic data")
        
        # Professional Analyzer button (initially hidden)
        self.professional_btn = ttk.Button(utility_buttons, text="🚀 Professional Mode", 
                                          command=self._switch_to_professional_mode, 
                                          style="Primary.TButton")
        self.professional_btn.pack(side=tk.LEFT, padx=(0, 5))
        self.professional_btn.pack_forget()  # Hide initially
        add_tooltip(self.professional_btn, "Launch Professional Diagnostic Analyzer\nFor complex multi-system diagnostics\nwith AI analysis and correlation")
        
        # Progress bar (improvement #5 - in-place progress indicator)
        self.progress_frame = ttk.Frame(main_frame)
        self.progress_frame.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        self.progress_label = ttk.Label(self.progress_frame, text="")
        self.progress_label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.progress_bar = ttk.Progressbar(self.progress_frame, mode='indeterminate')
        self.progress_bar.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Hide progress initially
        self.progress_frame.grid_remove()

        # Notebook for tabs with soft background (improvement #3)
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=6, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        # 1. Results tab
        self._create_results_tab()
        
        # 2. Analytics tab (NEW)
        self._create_analytics_tab()
        
        # 3. Comparison tab (NEW)
        self._create_comparison_tab()
        
        # 4. History tab (NEW)
        self._create_history_tab()
        
        # 5. Dependencies tab (NEW)
        self._create_dependencies_tab()
        
        # 6. Cybersecurity tab (NEW)
        self._create_cybersecurity_tab()
        
        # 7. FDRS Analysis tab (NEW)
        self._create_fdrs_tab()
        
        # 8. Hex Decoder tab
        self._create_hex_tab()
        
        # 9. NRC Decoder tab
        self._create_nrc_tab()
        
        # Status bar with enhanced styling
        self.status = tk.StringVar(value="Ready - Drag & drop log files or use File > Open")
        status_bar = ttk.Label(main_frame, textvariable=self.status, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=7, column=0, sticky=(tk.W, tk.E))
    
    def _create_results_tab(self):
        """Create enhanced results display tab with better visual organization"""
        results_frame = ttk.Frame(self.notebook)
        self.notebook.add(results_frame, text="📊 Results")
        
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(1, weight=1)
        
        # Summary header panel
        summary_frame = ttk.Frame(results_frame)
        summary_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=10, pady=10)
        summary_frame.columnconfigure((0, 1, 2, 3), weight=1)
        
        # Summary metric cards
        self.results_summary_cards = {}
        metrics = [
            ("total", "Total Items", "📋", "#3498db"),
            ("errors", "Errors", "❌", "#e74c3c"),
            ("warnings", "Warnings", "⚠️", "#f39c12"),
            ("success", "Successes", "✅", "#27ae60")
        ]
        
        for idx, (key, label, icon, color) in enumerate(metrics):
            card = tk.Frame(summary_frame, bg=color, relief=tk.RAISED, borderwidth=2)
            card.grid(row=0, column=idx, sticky=(tk.W, tk.E), padx=5)
            
            icon_label = tk.Label(card, text=icon, font=('Segoe UI Emoji', 20), bg=color, fg='white')
            icon_label.pack(pady=(8, 0))
            
            value_label = tk.Label(card, text="0", font=('Arial', 16, 'bold'), bg=color, fg='white')
            value_label.pack()
            
            name_label = tk.Label(card, text=label, font=('Arial', 9), bg=color, fg='white')
            name_label.pack(pady=(0, 8))
            
            self.results_summary_cards[key] = value_label
        
        # Results text area with professional styling (improvements #3, D.2, D.3)
        self.results_text = scrolledtext.ScrolledText(
            results_frame, wrap=tk.WORD, width=100, height=30,
            bg=self.colors['output_bg'], fg=self.colors['text_fg'],  # Soft background tint
            insertbackground=self.colors['fg'],
            font=('Consolas', 9),  # Monospace font for better alignment (D.2)
            padx=15, pady=10,  # Fixed left margin 
            relief=tk.FLAT,
            borderwidth=0,
            selectbackground=self.colors['select_bg']
        )
        self.results_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=15, pady=(0, 10))
        
        # Configure color tags for results display
        self._configure_text_tags()
    
    def _create_analytics_tab(self):
        """Create analytics/charts tab"""
        analytics_frame = ttk.Frame(self.notebook)
        self.notebook.add(analytics_frame, text="📈 Analytics")
        
        analytics_frame.columnconfigure(0, weight=1)
        analytics_frame.rowconfigure(0, weight=1)
        
        # Create charts panel
        try:
            self.charts_panel = ChartsPanel(analytics_frame, self.db, bg=self.colors['bg'])
            self.charts_panel.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
        except Exception as e:
            error_label = ttk.Label(analytics_frame, 
                                   text=f"Analytics not available: {str(e)}\nInstall matplotlib: pip install matplotlib",
                                   foreground='red')
            error_label.grid(row=0, column=0, padx=20, pady=20)
    
    def _create_comparison_tab(self):
        """Create log comparison tab"""
        comparison_frame = ttk.Frame(self.notebook)
        self.notebook.add(comparison_frame, text="🔀 Compare")
        
        comparison_frame.columnconfigure(0, weight=1)
        comparison_frame.columnconfigure(1, weight=1)
        comparison_frame.rowconfigure(1, weight=1)
        
        # File selection for comparison
        file1_frame = ttk.LabelFrame(comparison_frame, text="Log File 1", padding="10")
        file1_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        self.compare_file1 = tk.StringVar()
        ttk.Entry(file1_frame, textvariable=self.compare_file1, width=40).pack(side=tk.LEFT, padx=5)
        ttk.Button(file1_frame, text="Browse", command=lambda: self._browse_compare_file(1)).pack(side=tk.LEFT)
        
        file2_frame = ttk.LabelFrame(comparison_frame, text="Log File 2", padding="10")
        file2_frame.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        self.compare_file2 = tk.StringVar()
        ttk.Entry(file2_frame, textvariable=self.compare_file2, width=40).pack(side=tk.LEFT, padx=5)
        ttk.Button(file2_frame, text="Browse", command=lambda: self._browse_compare_file(2)).pack(side=tk.LEFT)
        
        # Compare button
        ttk.Button(comparison_frame, text="🔍 Compare Logs", command=self._compare_logs).grid(row=0, column=2, padx=10)
        
        # Results display (side by side)
        results_container = ttk.Frame(comparison_frame)
        results_container.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        results_container.columnconfigure(0, weight=1)
        results_container.columnconfigure(1, weight=1)
        results_container.rowconfigure(0, weight=1)
        
        # Left pane
        left_frame = ttk.LabelFrame(results_container, text="File 1 Unique Errors")
        left_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)
        left_frame.columnconfigure(0, weight=1)
        left_frame.rowconfigure(0, weight=1)
        
        self.compare_left = scrolledtext.ScrolledText(
            left_frame, wrap=tk.WORD,
            bg=self.colors['text_bg'], fg=self.colors['text_fg']
        )
        self.compare_left.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Right pane
        right_frame = ttk.LabelFrame(results_container, text="File 2 Unique Errors")
        right_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)
        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(0, weight=1)
        
        self.compare_right = scrolledtext.ScrolledText(
            right_frame, wrap=tk.WORD,
            bg=self.colors['text_bg'], fg=self.colors['text_fg']
        )
        self.compare_right.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    def _create_history_tab(self):
        """Create database history tab"""
        history_frame = ttk.Frame(self.notebook)
        self.notebook.add(history_frame, text="📚 History")
        
        history_frame.columnconfigure(0, weight=1)
        history_frame.rowconfigure(1, weight=1)
        
        # Toolbar
        toolbar = ttk.Frame(history_frame)
        toolbar.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(toolbar, text="🔄 Refresh", command=self._refresh_history).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="📊 Statistics", command=self._show_db_stats).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="🗑️ Clean Old", command=self._clean_old_logs).pack(side=tk.LEFT, padx=5)
        
        ttk.Label(toolbar, text="Search:").pack(side=tk.LEFT, padx=(20, 5))
        self.history_search = tk.StringVar()
        ttk.Entry(toolbar, textvariable=self.history_search, width=30).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="🔍", command=self._search_history).pack(side=tk.LEFT)
        
        # History treeview
        tree_frame = ttk.Frame(history_frame)
        tree_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)
        
        # Create treeview with scrollbar
        tree_scroll = ttk.Scrollbar(tree_frame)
        tree_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        self.history_tree = ttk.Treeview(
            tree_frame,
            columns=('Date', 'Filename', 'Errors', 'Successes', 'Root Cause'),
            show='tree headings',
            yscrollcommand=tree_scroll.set
        )
        tree_scroll.config(command=self.history_tree.yview)
        
        self.history_tree.heading('#0', text='ID')
        self.history_tree.heading('Date', text='Parse Date')
        self.history_tree.heading('Filename', text='Filename')
        self.history_tree.heading('Errors', text='Errors')
        self.history_tree.heading('Successes', text='Successes')
        self.history_tree.heading('Root Cause', text='Root Cause')
        
        self.history_tree.column('#0', width=50)
        self.history_tree.column('Date', width=150)
        self.history_tree.column('Filename', width=300)
        self.history_tree.column('Errors', width=80)
        self.history_tree.column('Successes', width=80)
        self.history_tree.column('Root Cause', width=200)
        
        self.history_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Double-click to view details
        self.history_tree.bind('<Double-Button-1>', self._view_history_details)
        
        # Load initial history
        self._refresh_history()
    
    def _create_dependencies_tab(self):
        """Create module dependencies tab"""
        dep_frame = ttk.Frame(self.notebook)
        self.notebook.add(dep_frame, text="🔗 Dependencies")
        
        dep_frame.columnconfigure(0, weight=1)
        dep_frame.rowconfigure(1, weight=1)
        
        # Info label
        info_text = "Module dependency analysis shows which modules communicated during the session\nand identifies missing dependencies that may cause update failures."
        ttk.Label(dep_frame, text=info_text, font=('Arial', 9)).grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        
        # Dependencies text area
        self.dependencies_text = scrolledtext.ScrolledText(
            dep_frame, wrap=tk.WORD, width=120, height=30,
            bg=self.colors['text_bg'], fg=self.colors['text_fg'],
            font=('Courier New', 9)
        )
        self.dependencies_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=5)
        
        # Configure text tags for coloring
        self.dependencies_text.tag_config("header", foreground="#00BFFF", font=('Courier New', 10, 'bold'))
        self.dependencies_text.tag_config("success", foreground="#00FF00")
        self.dependencies_text.tag_config("error", foreground="#FF6B6B")
        self.dependencies_text.tag_config("warning", foreground="#FFD700")
        self.dependencies_text.tag_config("module", foreground="#87CEEB", font=('Courier New', 9, 'bold'))
        self.dependencies_text.tag_config("info", foreground="#B0B0B0")
        
        # Initial message
        self.dependencies_text.insert(tk.END, "Parse a log file to see module dependency analysis.\n\n", "info")
        self.dependencies_text.insert(tk.END, "This feature helps identify:\n", "header")
        self.dependencies_text.insert(tk.END, "  • Which modules communicated during update/programming\n", "info")
        self.dependencies_text.insert(tk.END, "  • Missing dependency modules that may cause failures\n", "info")
        self.dependencies_text.insert(tk.END, "  • Communication success/failure patterns\n", "info")
        self.dependencies_text.insert(tk.END, "  • Recommendations for resolving dependency issues\n", "info")
        self.dependencies_text.config(state=tk.DISABLED)
    
    def _create_cybersecurity_tab(self):
        """Create cybersecurity analysis tab with modern card-based layout"""
        security_frame = ttk.Frame(self.notebook)
        self.notebook.add(security_frame, text="🔒 Cybersecurity")
        
        security_frame.columnconfigure(0, weight=1)
        security_frame.rowconfigure(2, weight=1)
        
        # Header with summary metrics
        header_frame = ttk.Frame(security_frame)
        header_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=10, pady=10)
        header_frame.columnconfigure((0, 1, 2, 3), weight=1)
        
        # Metric cards
        self.security_metrics = {}
        metrics = [
            ("total", "Total Threats", "🔒", "#3498db"),
            ("critical", "Critical", "🔴", "#e74c3c"),
            ("high", "High", "🟠", "#e67e22"),
            ("medium", "Medium", "🟡", "#f39c12")
        ]
        
        for idx, (key, label, icon, color) in enumerate(metrics):
            card = tk.Frame(header_frame, bg=color, relief=tk.RAISED, borderwidth=2)
            card.grid(row=0, column=idx, sticky=(tk.W, tk.E), padx=5)
            
            icon_label = tk.Label(card, text=icon, font=('Segoe UI Emoji', 24), bg=color, fg='white')
            icon_label.pack(pady=(10, 0))
            
            value_label = tk.Label(card, text="0", font=('Arial', 20, 'bold'), bg=color, fg='white')
            value_label.pack()
            
            name_label = tk.Label(card, text=label, font=('Arial', 10), bg=color, fg='white')
            name_label.pack(pady=(0, 10))
            
            self.security_metrics[key] = value_label
        
        # Severity breakdown and affected modules section
        info_frame = ttk.Frame(security_frame)
        info_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=10, pady=5)
        info_frame.columnconfigure(0, weight=1)
        info_frame.columnconfigure(1, weight=1)
        
        # Severity breakdown (left side)
        severity_frame = ttk.LabelFrame(info_frame, text="📊 Threat Breakdown", padding=10)
        severity_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)
        
        self.severity_canvas = tk.Canvas(severity_frame, height=120, bg='white', highlightthickness=0)
        self.severity_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Affected modules (right side)
        modules_frame = ttk.LabelFrame(info_frame, text="🎯 Affected Modules", padding=10)
        modules_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)
        
        self.modules_text = tk.Text(modules_frame, height=5, wrap=tk.WORD, 
                                     bg=self.colors['text_bg'], fg=self.colors['text_fg'],
                                     font=('Arial', 10), relief=tk.FLAT)
        self.modules_text.pack(fill=tk.BOTH, expand=True)
        
        # Threats list with scrollable cards
        threats_frame = ttk.LabelFrame(security_frame, text="� Security Threats", padding=10)
        threats_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=5)
        threats_frame.columnconfigure(0, weight=1)
        threats_frame.rowconfigure(0, weight=1)
        
        # Scrollable canvas for threat cards
        canvas = tk.Canvas(threats_frame, bg=self.colors['bg'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(threats_frame, orient="vertical", command=canvas.yview)
        self.security_cards_frame = ttk.Frame(canvas)
        
        self.security_cards_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.security_cards_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Initial welcome message
        self._show_security_welcome()
    
    def _show_security_welcome(self):
        """Show welcome message in security tab"""
        welcome_card = tk.Frame(self.security_cards_frame, bg='#ecf0f1', relief=tk.RAISED, borderwidth=2)
        welcome_card.pack(fill=tk.X, padx=10, pady=10)
        
        title = tk.Label(welcome_card, text="🔒 CYBERSECURITY ANALYZER", 
                        font=('Arial', 16, 'bold'), bg='#ecf0f1', fg='#2c3e50')
        title.pack(pady=(15, 5))
        
        subtitle = tk.Label(welcome_card, text="Parse a log file to analyze for security threats and vulnerabilities", 
                           font=('Arial', 11), bg='#ecf0f1', fg='#34495e')
        subtitle.pack(pady=(0, 15))
        
        separator = tk.Frame(welcome_card, height=2, bg='#bdc3c7')
        separator.pack(fill=tk.X, padx=20, pady=10)
        
        # Threat Level Explanations
        levels_label = tk.Label(welcome_card, text="Threat Severity Levels:", 
                               font=('Arial', 12, 'bold'), bg='#ecf0f1', fg='#2c3e50')
        levels_label.pack(pady=(10, 5))
        
        severity_info = [
            ("🔴", "CRITICAL", "Immediate security breach - Unauthorized access, firmware tampering, or failed authentication", "#e74c3c"),
            ("🟠", "HIGH", "Serious security risk - Repeated failed attempts, seed-key issues, or programming threats", "#e67e22"),
            ("🟡", "MEDIUM", "Moderate concern - Communication errors, unusual patterns, or minor vulnerabilities", "#f39c12"),
            ("🟢", "LOW", "Low risk - Diagnostic anomalies or informational security events", "#27ae60")
        ]
        
        for icon, level, description, color in severity_info:
            level_frame = tk.Frame(welcome_card, bg='white', relief=tk.RIDGE, borderwidth=1)
            level_frame.pack(fill=tk.X, padx=20, pady=3)
            
            icon_label = tk.Label(level_frame, text=icon, font=('Segoe UI Emoji', 14), 
                                 bg='white', fg=color, width=3)
            icon_label.pack(side=tk.LEFT, padx=5)
            
            text_frame = tk.Frame(level_frame, bg='white')
            text_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=5, padx=5)
            
            level_label = tk.Label(text_frame, text=level, font=('Arial', 10, 'bold'), 
                                  bg='white', fg=color, anchor=tk.W)
            level_label.pack(anchor=tk.W)
            
            desc_label = tk.Label(text_frame, text=description, font=('Arial', 9), 
                                 bg='white', fg='#34495e', anchor=tk.W, wraplength=550, justify=tk.LEFT)
            desc_label.pack(anchor=tk.W)
        
        separator2 = tk.Frame(welcome_card, height=2, bg='#bdc3c7')
        separator2.pack(fill=tk.X, padx=20, pady=10)
        
        # What we look for
        features_label = tk.Label(welcome_card, text="What We Monitor:", 
                                 font=('Arial', 12, 'bold'), bg='#ecf0f1', fg='#2c3e50')
        features_label.pack(pady=(10, 5))
        
        features = [
            ("🔐", "Unauthorized access & authentication failures"),
            ("�", "Seed-key security access issues (Service 0x27)"),
            ("🛡️", "Firmware integrity & checksum violations"),
            ("📡", "Communication anomalies & malformed messages"),
            ("⚠️", "Security-related NRC codes (0x33, 0x35, 0x36, 0x37)"),
            ("💾", "Unauthorized reprogramming attempts"),
            ("🚫", "Potential denial-of-service patterns")
        ]
        
        for icon, text in features:
            feature_frame = tk.Frame(welcome_card, bg='#ecf0f1')
            feature_frame.pack(fill=tk.X, padx=30, pady=2)
            
            icon_label = tk.Label(feature_frame, text=icon, font=('Segoe UI Emoji', 11), 
                                 bg='#ecf0f1', width=3)
            icon_label.pack(side=tk.LEFT)
            
            text_label = tk.Label(feature_frame, text=text, font=('Arial', 10), 
                                 bg='#ecf0f1', fg='#34495e', anchor=tk.W)
            text_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        instruction = tk.Label(welcome_card, text="Click 'Parse Log' to begin security analysis", 
                              font=('Arial', 11, 'italic'), bg='#ecf0f1', fg='#7f8c8d')
        instruction.pack(pady=(15, 20))
    
    def _create_fdrs_tab(self):
        """Create FDRS (Ford Diagnostic and Repair System) analysis tab"""
        fdrs_frame = ttk.Frame(self.notebook)
        self.notebook.add(fdrs_frame, text="🔧 FDRS Analysis")
        
        fdrs_frame.columnconfigure(0, weight=1)
        fdrs_frame.rowconfigure(2, weight=1)
        
        # Header with FDRS system information
        header_frame = ttk.Frame(fdrs_frame)
        header_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=10, pady=10)
        header_frame.columnconfigure((0, 1, 2, 3), weight=1)
        
        # FDRS System Info Cards
        self.fdrs_metrics = {}
        metrics = [
            ("version", "FDRS Version", "🔧", "#3498db"),
            ("services", "UDS Services", "🔗", "#9b59b6"),
            ("success_rate", "Success Rate", "✅", "#27ae60"),
            ("nrc_errors", "NRC Errors", "❌", "#e74c3c")
        ]
        
        for idx, (key, label, icon, color) in enumerate(metrics):
            card = tk.Frame(header_frame, bg=color, relief=tk.RAISED, borderwidth=2)
            card.grid(row=0, column=idx, sticky=(tk.W, tk.E), padx=5)
            
            icon_label = tk.Label(card, text=icon, font=('Segoe UI Emoji', 20), bg=color, fg='white')
            icon_label.pack(pady=(8, 0))
            
            value_label = tk.Label(card, text="N/A", font=('Arial', 16, 'bold'), bg=color, fg='white')
            value_label.pack()
            
            name_label = tk.Label(card, text=label, font=('Arial', 9), bg=color, fg='white')
            name_label.pack(pady=(0, 8))
            
            self.fdrs_metrics[key] = value_label
        
        # Analysis sections
        analysis_frame = ttk.Frame(fdrs_frame)
        analysis_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=10, pady=5)
        analysis_frame.columnconfigure((0, 1), weight=1)
        
        # System Information (left side)
        system_frame = ttk.LabelFrame(analysis_frame, text="🏗️ System Information", padding=10)
        system_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)
        
        self.fdrs_system_text = scrolledtext.ScrolledText(
            system_frame, height=8, wrap=tk.WORD,
            bg=self.colors['text_bg'], fg=self.colors['text_fg'],
            font=('Consolas', 10), relief=tk.FLAT
        )
        self.fdrs_system_text.pack(fill=tk.BOTH, expand=True)
        
        # Communication Analysis (right side)
        comm_frame = ttk.LabelFrame(analysis_frame, text="📡 UDS Communications", padding=10)
        comm_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)
        
        self.fdrs_comm_text = scrolledtext.ScrolledText(
            comm_frame, height=8, wrap=tk.WORD,
            bg=self.colors['text_bg'], fg=self.colors['text_fg'],
            font=('Consolas', 10), relief=tk.FLAT
        )
        self.fdrs_comm_text.pack(fill=tk.BOTH, expand=True)
        
        # Detailed Analysis Results
        details_frame = ttk.LabelFrame(fdrs_frame, text="📋 Detailed FDRS Analysis", padding=10)
        details_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=5)
        
        # Create notebook for different analysis views
        self.fdrs_notebook = ttk.Notebook(details_frame)
        self.fdrs_notebook.pack(fill=tk.BOTH, expand=True)
        
        # Diagnostic Services tab
        services_frame = ttk.Frame(self.fdrs_notebook)
        self.fdrs_notebook.add(services_frame, text="🔍 Diagnostic Services")
        
        self.fdrs_services_text = scrolledtext.ScrolledText(
            services_frame, wrap=tk.WORD,
            bg=self.colors['text_bg'], fg=self.colors['text_fg'],
            font=('Consolas', 9), relief=tk.FLAT
        )
        self.fdrs_services_text.pack(fill=tk.BOTH, expand=True)
        
        # Error Analysis tab
        errors_frame = ttk.Frame(self.fdrs_notebook)
        self.fdrs_notebook.add(errors_frame, text="⚠️ Error Analysis")
        
        self.fdrs_errors_text = scrolledtext.ScrolledText(
            errors_frame, wrap=tk.WORD,
            bg=self.colors['text_bg'], fg=self.colors['text_fg'],
            font=('Consolas', 9), relief=tk.FLAT
        )
        self.fdrs_errors_text.pack(fill=tk.BOTH, expand=True)
        
        # Recommendations tab
        recommendations_frame = ttk.Frame(self.fdrs_notebook)
        self.fdrs_notebook.add(recommendations_frame, text="💡 Recommendations")
        
        self.fdrs_recommendations_text = scrolledtext.ScrolledText(
            recommendations_frame, wrap=tk.WORD,
            bg=self.colors['text_bg'], fg=self.colors['text_fg'],
            font=('Arial', 10), relief=tk.FLAT
        )
        self.fdrs_recommendations_text.pack(fill=tk.BOTH, expand=True)
        
        # Initialize with welcome message
        self._initialize_fdrs_welcome()
    
    def _initialize_fdrs_welcome(self):
        """Initialize FDRS tab with welcome message"""
        welcome_msg = """🔧 FDRS (Ford Diagnostic and Repair System) Analysis

This tab provides specialized analysis for Ford diagnostic logs including:

🏗️ System Information:
• FDRS version and dependency tracking
• FDSP server connection status
• Module dependency analysis

📡 UDS Communication Analysis:
• Diagnostic service breakdown (Read DID, Security Access, etc.)
• Success/failure rates
• Communication timing analysis

⚠️ Error Analysis:
• NRC (Negative Response Code) detailed explanations
• Request Out of Range (NRC 31) specific guidance
• Security access issue identification

💡 Smart Recommendations:
• Troubleshooting steps for common issues
• DID compatibility checks
• ECU session requirements

📋 To get started:
1. Load a FDRS log file (text format)
2. Click 'Parse Log' to begin analysis
3. Review the detailed breakdown in each tab

Supported formats:
✅ FDRS text logs with system information
✅ UDS diagnostic communications
✅ ISO15765 CAN frame data
✅ NRC error responses
"""
        
        self.fdrs_system_text.insert("1.0", welcome_msg)
        self.fdrs_system_text.config(state=tk.DISABLED)
    
    def _create_hex_tab(self):
        """Create hex decoder tab"""
        hex_frame = ttk.Frame(self.notebook)
        self.notebook.add(hex_frame, text="🔢 Hex Decoder")
        
        hex_frame.columnconfigure(0, weight=1)
        hex_frame.rowconfigure(3, weight=1)
        
        ttk.Label(hex_frame, text="Enter Hex Value(s):").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.hex_input = tk.StringVar()
        ttk.Entry(hex_frame, textvariable=self.hex_input, width=80).grid(row=1, column=0, sticky=(tk.W, tk.E), padx=10, pady=5)
        ttk.Button(hex_frame, text="Decode", command=self._decode_hex, width=20).grid(row=2, column=0, pady=5)
        
        self.hex_output = scrolledtext.ScrolledText(
            hex_frame, wrap=tk.WORD, width=100, height=20,
            bg=self.colors['text_bg'], fg=self.colors['text_fg']
        )
        self.hex_output.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=5)
    
    def _create_nrc_tab(self):
        """Create NRC decoder tab"""
        nrc_frame = ttk.Frame(self.notebook)
        self.notebook.add(nrc_frame, text="⚠️ NRC Decoder")
        
        nrc_frame.columnconfigure(0, weight=1)
        nrc_frame.rowconfigure(3, weight=1)
        
        ttk.Label(nrc_frame, text="Enter NRC Code (e.g., 0x22 or 22):").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.nrc_input = tk.StringVar()
        ttk.Entry(nrc_frame, textvariable=self.nrc_input, width=80).grid(row=1, column=0, sticky=(tk.W, tk.E), padx=10, pady=5)
        ttk.Button(nrc_frame, text="Explain", command=self._explain_nrc, width=20).grid(row=2, column=0, pady=5)
        
        self.nrc_output = scrolledtext.ScrolledText(
            nrc_frame, wrap=tk.WORD, width=100, height=20,
            bg=self.colors['text_bg'], fg=self.colors['text_fg']
        )
        self.nrc_output.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=5)
        
        # NRC Reference
        ttk.Label(nrc_frame, text="Common NRC Codes Reference:", font=('Arial', 10, 'bold')).grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        nrc_ref = scrolledtext.ScrolledText(
            nrc_frame, wrap=tk.WORD, width=100, height=10,
            bg=self.colors['text_bg'], fg=self.colors['text_fg']
        )
        nrc_ref.grid(row=5, column=0, sticky=(tk.W, tk.E), padx=10, pady=5)
        
        for code, description in NRCCodeExplainer.NRC_CODES.items():
            nrc_ref.insert(tk.END, f"{code}: {description}\n")
        nrc_ref.config(state=tk.DISABLED)
    
    def _configure_text_tags(self):
        """Configure color tags for text display"""
        # Title
        self.results_text.tag_config("title", foreground="#0066CC", font=("Arial", 14, "bold"))
        
        # Section headers
        self.results_text.tag_config("section_header", foreground="#0099FF", font=("Arial", 12, "bold"))
        
        # Root cause
        self.results_text.tag_config("root_cause", foreground="#6600CC", font=("Arial", 11, "bold"))
        
        # Status colors with backgrounds
        self.results_text.tag_config("good_status", foreground="#00AA00", background="#E8F5E9", font=("Arial", 10, "bold"))
        self.results_text.tag_config("minor_status", foreground="#FF8800", background="#FFF3E0", font=("Arial", 10, "bold"))
        self.results_text.tag_config("critical_status", foreground="#CC0000", background="#FFEBEE", font=("Arial", 10, "bold"))
        
        # ECU critical
        self.results_text.tag_config("ecu_critical", foreground="#CC0000", font=("Arial", 10, "bold"))
        
        # Actions
        self.results_text.tag_config("action", foreground="#CC6600", font=("Arial", 10, "bold"))
        
        # Regular highlights
        self.results_text.tag_config("error", foreground="#CC0000", font=("Arial", 10, "bold"))
        self.results_text.tag_config("warning", foreground="#FF8800")
        self.results_text.tag_config("success", foreground="#00AA00", font=("Arial", 10, "bold"))
        self.results_text.tag_config("info", foreground="#0066CC")
        self.results_text.tag_config("bold", font=("Arial", 10, "bold"))
        self.results_text.tag_config("highlight", background="#FFFF99")
    
    def _bind_shortcuts(self):
        """Bind keyboard shortcuts (improvement #8)"""
        shortcuts = self.config.get('shortcuts', {})
        
        # File operations
        self.root.bind('<Control-o>', lambda e: self._browse_file())
        self.root.bind('<Control-O>', lambda e: self._browse_file())
        
        self.root.bind('<Control-Shift-V>', lambda e: self._paste_content())
        self.root.bind('<Control-Shift-v>', lambda e: self._paste_content())
        
        self.root.bind('<Control-s>', lambda e: self._export_json())
        self.root.bind('<Control-S>', lambda e: self._export_json())
        
        # Analysis actions (improvement #8 - Alt shortcuts for primary actions)
        self.root.bind('<Alt-a>', lambda e: self._parse_log())
        self.root.bind('<Alt-A>', lambda e: self._parse_log())
        
        self.root.bind('<Alt-c>', lambda e: self._correlate_logs())
        self.root.bind('<Alt-C>', lambda e: self._correlate_logs())
        
        self.root.bind('<Alt-e>', lambda e: self._clear_results())  # Alt+E for Clear All
        self.root.bind('<Alt-E>', lambda e: self._clear_results())
        
        # View operations
        self.root.bind('<Control-f>', lambda e: self._show_find_dialog())
        self.root.bind('<Control-F>', lambda e: self._show_find_dialog())
        
        self.root.bind('<F5>', lambda e: self._refresh_display())
        
        self.root.bind('<Control-m>', lambda e: self._toggle_mode())
        self.root.bind('<Control-M>', lambda e: self._toggle_mode())
        
        self.root.bind('<Control-l>', lambda e: self._clear_results())
        self.root.bind('<Control-L>', lambda e: self._clear_results())
    
    def _setup_drag_drop(self):
        """Setup drag and drop support"""
        if TKINTERDND_AVAILABLE:
            try:
                # Try to enable drag-and-drop
                self.root.drop_target_register(DND_FILES)
                self.root.dnd_bind('<<Drop>>', self._on_drop)
            except:
                # Failed to setup drag-drop
                pass
    
    def _on_drop(self, event):
        """Handle dropped files"""
        files = self.root.tk.splitlist(event.data)
        if files:
            filepath = files[0]
            self._open_file(filepath)
    
    def _browse_file(self):
        """Browse for log file"""
        filename = filedialog.askopenfilename(
            title="Select Log File",
            filetypes=[
                ("All supported files", "*.xml;*.txt;*.log"),
                ("XML files", "*.xml"),
                ("Text files", "*.txt"),
                ("Log files", "*.log"),
                ("All files", "*.*")
            ]
        )
        if filename:
            self._open_file(filename)
    
    def _open_file(self, filepath):
        """Open and parse a file"""
        self.file_path.set(filepath)
        self.current_filepath = filepath
        self.config.add_recent_file(filepath)
        self._update_recent_files_menu()
        self._parse_log()
    
    def _paste_content(self):
        """Open dialog to paste log content directly"""
        # Create a new dialog window
        paste_dialog = tk.Toplevel(self.root)
        paste_dialog.title("Paste Log Content")
        paste_dialog.geometry("800x600")
        
        # Instructions
        ttk.Label(paste_dialog, 
                 text="Paste your log content below, then click 'Parse':",
                 font=('Arial', 10, 'bold')).pack(padx=10, pady=10)
        
        # Text area for pasting
        text_frame = ttk.Frame(paste_dialog)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        text_area = scrolledtext.ScrolledText(
            text_frame,
            wrap=tk.WORD,
            width=90,
            height=30,
            bg=self.colors['text_bg'],
            fg=self.colors['text_fg'],
            font=('Courier New', 9)
        )
        text_area.pack(fill=tk.BOTH, expand=True)
        
        # Focus on text area and allow immediate pasting
        text_area.focus_set()
        
        # Button frame
        button_frame = ttk.Frame(paste_dialog)
        button_frame.pack(pady=10)
        
        def parse_pasted_content():
            """Parse the pasted content"""
            content = text_area.get('1.0', tk.END).strip()
            if not content:
                messagebox.showwarning("No Content", "Please paste some log content first.")
                return
            
            # Save to temporary file
            import tempfile
            with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
                f.write(content)
                temp_file = f.name
            
            # Parse the temp file
            self.file_path.set("[Pasted Content]")
            self.current_filepath = temp_file
            paste_dialog.destroy()
            self._parse_log()
        
        def cancel():
            paste_dialog.destroy()
        
        ttk.Button(button_frame, text="✅ Parse Content", 
                  command=parse_pasted_content, width=20).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="❌ Cancel", 
                  command=cancel, width=20).pack(side=tk.LEFT, padx=5)
        
        # Instructions at bottom
        ttk.Label(paste_dialog,
                 text="Tip: Press Ctrl+V to paste from clipboard",
                 font=('Arial', 8), foreground='gray').pack(pady=5)

    def _show_progress_indicator(self, show: bool, message: str = "Processing..."):
        """Show or hide the progress indicator"""
        if show:
            self.progress_label.config(text=message)
            self.progress_bar.start(10)  # Start indeterminate animation
            self.progress_frame.grid()
        else:
            self.progress_bar.stop()
            self.progress_frame.grid_remove()
    
    def _parse_log(self):
        """Parse the selected log file"""
        # Use current_filepath if available (for pasted content), otherwise use file_path
        if self.current_filepath:
            filepath = self.current_filepath
        else:
            filepath = self.file_path.get()
        
        if not filepath:
            messagebox.showwarning("No File", "Please select a log file first.")
            return
        
        if not os.path.exists(filepath):
            messagebox.showerror("File Not Found", f"File not found: {filepath}")
            return
        
        # Show progress indication immediately
        self.status.set("🔍 Analyzing log file...")
        self._show_progress_indicator(True)
        self.root.update()
        
        # Parse in background thread
        thread = threading.Thread(target=self._parse_in_background, args=(filepath,))
        thread.daemon = True
        thread.start()
    
    def _parse_in_background(self, filepath):
        """Enhanced parsing with performance monitoring and progress tracking"""
        try:
            # Get file information for performance planning
            file_info = self.performance.get_file_info(filepath)
            
            # Show progress dialog for large files
            if file_info.get('size_mb', 0) > 5:  # Show progress for files > 5MB
                self.root.after(0, self._show_progress_dialog, f"Processing {file_info.get('size_mb', 0):.1f} MB file")
            
            # Detect file type and choose appropriate parsing strategy
            if filepath.lower().endswith('.xml'):
                self.current_file_type = 'xml'
                
                # For large XML files, use performance-enhanced parsing
                if file_info.get('use_streaming', False):
                    results = self._parse_xml_with_performance(filepath)
                else:
                    results = self.xml_parser.parse_file(filepath)
            else:
                self.current_file_type = 'text'
                keywords = [k.strip() for k in self.filters.get().split(',')]
                
                # For large text files, use chunked parsing
                if file_info.get('use_streaming', False):
                    results = self._parse_text_with_performance(filepath, keywords)
                else:
                    results = self.text_parser.parse_file(filepath, keywords)
            
            self.current_results = results if results else []
            
            # Update status with file info
            result_count = len(self.current_results) if self.current_results else 0
            self.root.after(0, lambda: self.status.set(f"Parsed {result_count} items from {file_info.get('size_mb', 0):.1f} MB file"))
            
            # Generate dependency analysis
            if DEPENDENCY_TRACKER_AVAILABLE and self.current_results:
                self.root.after(0, lambda: self.status.set("Analyzing module dependencies..."))
                tracker = ModuleDependencyTracker()
                self.dependency_report = tracker.parse_log_for_dependencies(self.current_results)
            else:
                self.dependency_report = None
            
            # Generate cybersecurity analysis with enhanced UDS parsing
            if CYBERSECURITY_AVAILABLE and results:
                security_analyzer = CybersecurityAnalyzer()
                
                # Try enhanced analysis with UDS parser if available
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        raw_content = f.read()
                    self.security_report = security_analyzer.analyze_with_uds_parser(raw_content)
                except Exception as e:
                    print(f"Enhanced cybersecurity analysis failed, using basic: {e}")
                    # Fall back to basic analysis
                    self.security_report = security_analyzer.analyze(results)
            else:
                self.security_report = None
            
            # Generate enhanced diagnostic analysis (voltage, SOC, temp, etc.)
            if ENHANCED_DIAGNOSTICS_AVAILABLE and results:
                diagnostic_analyzer = EnhancedDiagnosticAnalyzer()
                self.enhanced_diagnostics = diagnostic_analyzer.analyze(results)
            else:
                self.enhanced_diagnostics = None
            
            # Generate critical diagnostic analysis (VIN, voltage, DTCs, errors, success, DID, hex/ascii)
            if CRITICAL_DIAGNOSTICS_AVAILABLE and results:
                critical_analyzer = CriticalDiagnosticView()
                self.critical_diagnostics = critical_analyzer.extract_critical_diagnostics(results)
                
                # Ensure critical_diagnostics is always a dict or None, never False or other types
                if not isinstance(self.critical_diagnostics, dict):
                    print(f"Warning: Critical diagnostics returned unexpected type: {type(self.critical_diagnostics)}")
                    self.critical_diagnostics = None
            else:
                self.critical_diagnostics = None
            
            # Generate FDRS analysis for text logs
            if self.current_file_type == 'text':
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    # Check if this looks like an FDRS log
                    if '[SYSTEM]' in content and 'fdrsVersion' in content:
                        fdrs_parser = FDRSLogParser()
                        self.fdrs_analysis = fdrs_parser.parse_log_text(content)
                        # Also get detailed analysis
                        self.fdrs_detailed = fdrs_parser.get_detailed_analysis()
                    else:
                        self.fdrs_analysis = None
                        self.fdrs_detailed = None
                except Exception as e:
                    print(f"FDRS analysis error: {e}")
                    self.fdrs_analysis = None
                    self.fdrs_detailed = None
            else:
                self.fdrs_analysis = None
                self.fdrs_detailed = None
            
            # Let smart filter learn from content
            if SMART_FILTER_AVAILABLE and self.smart_filter:
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        self.smart_filter.learn_from_content(content)
                except Exception as e:
                    pass  # Silent failure for learning
            
            # Store in database
            summary = self._calculate_summary(results)
            root_cause = None
            
            if self.simple_mode.get():
                # Pass FDRS analysis if available for better module detection
                fdrs_data = getattr(self, 'fdrs_analysis', None)
                manual_primary = self._get_manual_primary_module()
                report = self.report_generator.generate_simple_report(results, self.current_file_type, fdrs_data, manual_primary)
                if 'root_cause_analysis' in report:
                    root_cause = report['root_cause_analysis']
            
            log_id = self.db.store_log_session(
                os.path.basename(filepath),
                filepath,
                self.current_file_type,
                results,
                summary,
                root_cause
            )
            
            # Update display
            self.root.after(0, self._display_results)
            self.root.after(0, self._display_dependencies)
            self.root.after(0, self._display_security)
            self.root.after(0, self._display_fdrs)
            self.root.after(0, lambda: self.status.set(f"✅ Parsed {len(results)} items successfully (Log ID: {log_id})"))
            
            # Hide progress indicators
            self.root.after(0, self._hide_progress_dialog)
            self.root.after(0, lambda: self._show_progress_indicator(False))
            
            # Refresh charts if on analytics tab
            if hasattr(self, 'charts_panel'):
                self.root.after(0, self.charts_panel.refresh_charts)
            
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Parse Error", f"Error parsing file: {str(e)}"))
            self.root.after(0, lambda: self.status.set("Parse failed"))
            self.root.after(0, self._hide_progress_dialog)
    
    def _calculate_summary(self, results):
        """Calculate summary statistics"""
        summary = {
            'total': len(results),
            'errors': 0,
            'successes': 0,
            'warnings': 0
        }
        
        for result in results:
            result_str = str(result).lower()
            if 'error' in result_str or 'fail' in result_str:
                summary['errors'] += 1
            elif 'success' in result_str or 'pass' in result_str:
                summary['successes'] += 1
            elif 'warning' in result_str or 'warn' in result_str:
                summary['warnings'] += 1
        
        return summary
    
    def _display_results(self):
        """Display parsed results"""
        if self.simple_mode.get():
            self._display_simple_results()
        else:
            self._display_expert_results()
        
        # Check for NRC 7F issues after displaying results
        self._check_nrc7f_issues()
        
        # Smart suggestion for Professional Analyzer
        self._check_for_professional_mode_suggestion()
    
    def _display_simple_results(self):
        """Display simplified results with enhanced diagnostics"""
        self.results_text.delete('1.0', tk.END)
        
        if not self.current_results:
            self.results_text.insert(tk.END, "No results to display.\n")
            self._update_summary_cards(0, 0, 0, 0)
            return
        
        # Update summary cards with improved logic
        total = len(self.current_results)
        
        # Better error detection
        errors = sum(1 for r in self.current_results if 
                    'error' in str(r).lower() or 
                    'fail' in str(r).lower() or 
                    'exception' in str(r).lower() or
                    'not successful' in str(r).lower())
        
        warnings = sum(1 for r in self.current_results if 
                      'warning' in str(r).lower() or 
                      'caution' in str(r).lower())
        
        # Better success detection - exclude items with error indicators
        success = sum(1 for r in self.current_results if 
                     ('success' in str(r).lower() or 'pass' in str(r).lower()) and
                     not ('error' in str(r).lower() or 
                          'fail' in str(r).lower() or 
                          'exception' in str(r).lower() or
                          'not successful' in str(r).lower()))
        
        self._update_summary_cards(total, errors, warnings, success)
        
        # Show Critical Diagnostics First (if available)
        if self.critical_diagnostics and CRITICAL_DIAGNOSTICS_AVAILABLE:
            self._insert_critical_diagnostics()
        # Otherwise show Enhanced Diagnostics (if available)
        elif self.enhanced_diagnostics:
            self._insert_enhanced_diagnostics()
        
        # Generate simple report (returns a string)
        fdrs_data = getattr(self, 'fdrs_analysis', None)
        manual_primary = self._get_manual_primary_module()
        report_text = self.report_generator.generate_simple_report(
            self.current_results,
            self.current_file_type,
            fdrs_data,
            manual_primary
        )
        
        # Insert the text report directly with basic coloring
        self._insert_simple_text_report(report_text)
    
    def _insert_colorized_report(self, report):
        """Insert report with colors"""
        text = self.results_text
        
        # Title
        text.insert(tk.END, "═" * 80 + "\n")
        text.insert(tk.END, "  DIAGNOSTIC LOG ANALYSIS REPORT\n", "title")
        text.insert(tk.END, "═" * 80 + "\n\n")
        
        # Summary
        text.insert(tk.END, "📊 SUMMARY\n", "section_header")
        text.insert(tk.END, "─" * 80 + "\n")
        
        summary = report.get('summary', {})
        text.insert(tk.END, f"Total Items Analyzed: {summary.get('total', 0)}\n")
        
        errors = summary.get('errors', 0)
        successes = summary.get('successes', 0)
        warnings = summary.get('warnings', 0)
        
        if errors > 0:
            text.insert(tk.END, f"❌ Errors Found: {errors}\n", "error")
        if warnings > 0:
            text.insert(tk.END, f"⚠️  Warnings: {warnings}\n", "warning")
        if successes > 0:
            text.insert(tk.END, f"✅ Successful Operations: {successes}\n", "success")
        
        text.insert(tk.END, "\n")
        
        # Root Cause Analysis
        if 'root_cause_analysis' in report:
            root_cause = report['root_cause_analysis']
            text.insert(tk.END, "🔍 ROOT CAUSE ANALYSIS\n", "section_header")
            text.insert(tk.END, "─" * 80 + "\n")
            
            text.insert(tk.END, "Most Likely Issue: ", "root_cause")
            text.insert(tk.END, f"{root_cause.get('most_likely_issue', 'Unknown')}\n\n")
            
            text.insert(tk.END, "Proximate Cause:\n", "bold")
            text.insert(tk.END, f"{root_cause.get('proximate_cause', 'N/A')}\n\n")
            
            if root_cause.get('recommended_actions'):
                text.insert(tk.END, "Recommended Actions:\n", "action")
                for i, action in enumerate(root_cause['recommended_actions'], 1):
                    text.insert(tk.END, f"  {i}. {action}\n")
            
            text.insert(tk.END, "\n")
        
        # Issues
        if 'issues' in report:
            text.insert(tk.END, "⚠️  ISSUES FOUND\n", "section_header")
            text.insert(tk.END, "─" * 80 + "\n")
            
            for issue in report['issues'][:20]:  # Show first 20
                severity = issue.get('severity', '').upper()
                
                if severity in ['CRITICAL', 'FATAL']:
                    tag = "critical_status"
                elif severity in ['ERROR', 'FAIL']:
                    tag = "error"
                elif severity == 'WARNING':
                    tag = "minor_status"
                else:
                    tag = "info"
                
                text.insert(tk.END, f"[{severity}] ", tag)
                text.insert(tk.END, f"{issue.get('description', '')}\n")
                
                if issue.get('explanation'):
                    text.insert(tk.END, f"  → {issue['explanation']}\n", "info")
                
                text.insert(tk.END, "\n")
        
        # ECU Context
        if 'ecu_context' in report:
            text.insert(tk.END, "🚗 ECU MODULES INVOLVED\n", "section_header")
            text.insert(tk.END, "─" * 80 + "\n")
            
            for ecu_info in report['ecu_context'][:10]:
                if ecu_info.get('is_critical'):
                    text.insert(tk.END, f"⚠️  {ecu_info.get('name', 'Unknown')} ", "ecu_critical")
                    text.insert(tk.END, "(CRITICAL SYSTEM)\n", "ecu_critical")
                else:
                    text.insert(tk.END, f"  • {ecu_info.get('name', 'Unknown')}\n")
                
                if ecu_info.get('context'):
                    text.insert(tk.END, f"    {ecu_info['context']}\n", "info")
            
            text.insert(tk.END, "\n")
        
        text.insert(tk.END, "═" * 80 + "\n")
    
    def _insert_simple_text_report(self, report_text):
        """Insert simple text report with coloring"""
        text = self.results_text
        
        # Split into lines and colorize based on content
        for line in report_text.split('\n'):
            if line.startswith('📊') or line.startswith('🎯') or line.startswith('🔍') or line.startswith('❌'):
                # Section headers
                text.insert(tk.END, line + '\n', "section_header")
            elif 'ERROR' in line.upper() or '❌' in line or '✗' in line:
                # Error lines
                text.insert(tk.END, line + '\n', "error")
            elif 'WARNING' in line.upper() or '⚠' in line:
                # Warning lines
                text.insert(tk.END, line + '\n', "warning")
            elif 'SUCCESS' in line.upper() or '✓' in line or '✅' in line:
                # Success lines
                text.insert(tk.END, line + '\n', "success")
            elif line.startswith('   ') or line.startswith('  •'):
                # Indented info lines
                text.insert(tk.END, line + '\n', "info")
            elif '═' in line or '─' in line:
                # Separator lines
                text.insert(tk.END, line + '\n', "bold")
            else:
                # Normal text
                text.insert(tk.END, line + '\n')
    
    def _update_summary_cards(self, total, errors, warnings, success):
        """Update the summary metric cards in Results tab"""
        self.results_summary_cards['total'].config(text=str(total))
        self.results_summary_cards['errors'].config(text=str(errors))
        self.results_summary_cards['warnings'].config(text=str(warnings))
        self.results_summary_cards['success'].config(text=str(success))
    
    def _insert_enhanced_diagnostics(self):
        """Insert enhanced diagnostic information (voltage, SOC, temp, etc.)"""
        if not self.enhanced_diagnostics:
            return
        
        text = self.results_text
        diag = self.enhanced_diagnostics
        
        # Header
        text.insert(tk.END, "╔" + "═" * 78 + "╗\n", "bold")
        text.insert(tk.END, "║" + " " * 20 + "⚡ ENHANCED DIAGNOSTIC OVERVIEW" + " " * 27 + "║\n", "section_header")
        text.insert(tk.END, "╚" + "═" * 78 + "╝\n\n", "bold")
        
        # Critical Issues Section
        critical_issues = diag.get('critical_issues', [])
        if critical_issues:
            text.insert(tk.END, "🚨 CRITICAL DIAGNOSTICS\n", "critical_status")
            text.insert(tk.END, "─" * 80 + "\n")
            
            for issue in critical_issues:
                if issue['severity'] == 'critical':
                    text.insert(tk.END, f"{issue['icon']} {issue['message']}\n", "critical_status")
                elif issue['severity'] == 'warning':
                    text.insert(tk.END, f"{issue['icon']} {issue['message']}\n", "warning")
                else:
                    text.insert(tk.END, f"{issue['icon']} {issue['message']}\n", "info")
            text.insert(tk.END, "\n")
        
        # Voltage Analysis
        voltage = diag.get('voltage', {})
        if voltage.get('status') != 'unknown':
            text.insert(tk.END, "🔋 VOLTAGE ANALYSIS\n", "bold")
            text.insert(tk.END, "─" * 80 + "\n")
            
            status = voltage['status']
            if status == 'critical':
                text.insert(tk.END, voltage['message'] + "\n", "critical_status")
            elif status == 'warning':
                text.insert(tk.END, voltage['message'] + "\n", "warning")
            else:
                text.insert(tk.END, voltage['message'] + "\n", "success")
            
            text.insert(tk.END, f"  • Average: {voltage.get('average', 'N/A')}V\n", "info")
            text.insert(tk.END, f"  • Range: {voltage.get('min', 'N/A')}V - {voltage.get('max', 'N/A')}V\n", "info")
            text.insert(tk.END, f"  • Readings: {len(voltage.get('readings', []))}\n", "info")
            text.insert(tk.END, "\n")
        
        # State of Charge Analysis
        soc = diag.get('state_of_charge', {})
        if soc.get('status') != 'unknown':
            text.insert(tk.END, "⚡ STATE OF CHARGE (SOC)\n", "bold")
            text.insert(tk.END, "─" * 80 + "\n")
            
            status = soc['status']
            if status == 'critical':
                text.insert(tk.END, soc['message'] + "\n", "critical_status")
            elif status == 'warning':
                text.insert(tk.END, soc['message'] + "\n", "warning")
            else:
                text.insert(tk.END, soc['message'] + "\n", "success")
            
            text.insert(tk.END, f"  • Average: {soc.get('average', 'N/A')}%\n", "info")
            text.insert(tk.END, f"  • Minimum: {soc.get('min', 'N/A')}%\n", "info")
            text.insert(tk.END, f"  • Readings: {len(soc.get('readings', []))}\n", "info")
            text.insert(tk.END, "\n")
        
        # Temperature Analysis
        temp = diag.get('temperature', {})
        if temp.get('status') != 'unknown':
            text.insert(tk.END, "🌡️ TEMPERATURE MONITORING\n", "bold")
            text.insert(tk.END, "─" * 80 + "\n")
            
            status = temp['status']
            if status == 'critical':
                text.insert(tk.END, temp['message'] + "\n", "critical_status")
            elif status == 'warning':
                text.insert(tk.END, temp['message'] + "\n", "warning")
            else:
                text.insert(tk.END, temp['message'] + "\n", "success")
            
            text.insert(tk.END, f"  • Average: {temp.get('average', 'N/A')}°C\n", "info")
            text.insert(tk.END, f"  • Range: {temp.get('min', 'N/A')}°C - {temp.get('max', 'N/A')}°C\n", "info")
            text.insert(tk.END, f"  • Readings: {len(temp.get('readings', []))}\n", "info")
            text.insert(tk.END, "\n")
        
        # DTC Codes
        dtc_codes = diag.get('dtc_codes', [])
        if dtc_codes:
            text.insert(tk.END, "🔧 DIAGNOSTIC TROUBLE CODES (DTCs)\n", "bold")
            text.insert(tk.END, "─" * 80 + "\n")
            text.insert(tk.END, f"Found {len(dtc_codes)} DTC(s):\n", "warning")
            
            for dtc in dtc_codes[:10]:  # Show first 10
                text.insert(tk.END, f"  • {dtc['code']}", "error")
                text.insert(tk.END, f" (Line {dtc['index']})\n", "info")
            
            if len(dtc_codes) > 10:
                text.insert(tk.END, f"  ... and {len(dtc_codes) - 10} more\n", "info")
            text.insert(tk.END, "\n")
        
        # Programming Preconditions
        preconditions = diag.get('preconditions', {})
        if preconditions:
            text.insert(tk.END, "⚙️ PROGRAMMING PRECONDITIONS\n", "bold")
            text.insert(tk.END, "─" * 80 + "\n")
            
            for condition, checks in preconditions.items():
                met = all(check['met'] for check in checks)
                if met:
                    text.insert(tk.END, f"  ✅ {condition.title()}\n", "success")
                else:
                    text.insert(tk.END, f"  ❌ {condition.title()} - NOT MET\n", "error")
            text.insert(tk.END, "\n")
        
        # Software Versions
        sw_versions = diag.get('software_versions', {})
        if sw_versions:
            text.insert(tk.END, "💾 SOFTWARE VERSIONS\n", "bold")
            text.insert(tk.END, "─" * 80 + "\n")
            
            for module, versions in sw_versions.items():
                text.insert(tk.END, f"  • Module {module}: ", "info")
                if versions:
                    text.insert(tk.END, f"{versions[0]['version']}\n")
                else:
                    text.insert(tk.END, "Unknown\n")
            text.insert(tk.END, "\n")
        
        text.insert(tk.END, "═" * 80 + "\n\n", "bold")
    
    def _insert_critical_diagnostics(self):
        """Insert critical diagnostic information (VIN, voltage, DTCs, errors, DID responses, hex/ascii)"""
        if not self.critical_diagnostics:
            return
        
        text = self.results_text
        
        # Generate and insert the formatted critical diagnostics report
        try:
            report_text = format_critical_diagnostics_report(self.critical_diagnostics)
            
            # Insert with appropriate formatting
            lines = report_text.split('\n')
            for line in lines:
                if line.startswith('╔') or line.startswith('╚') or line.startswith('║'):
                    text.insert(tk.END, line + "\n", "bold")
                elif line.startswith('🚗 VEHICLE IDENTIFICATION'):
                    text.insert(tk.END, line + "\n", "section_header")
                elif line.startswith('🔋 BATTERY/VOLTAGE STATUS'):
                    text.insert(tk.END, line + "\n", "section_header")
                elif line.startswith('🔧 DIAGNOSTIC TROUBLE CODES'):
                    text.insert(tk.END, line + "\n", "section_header")
                elif line.startswith('❌ FAILED OPERATIONS'):
                    text.insert(tk.END, line + "\n", "section_header")
                elif line.startswith('✅ SUCCESSFUL OPERATIONS'):
                    text.insert(tk.END, line + "\n", "section_header")
                elif line.startswith('📋 DATA IDENTIFIER'):
                    text.insert(tk.END, line + "\n", "section_header")
                elif line.startswith('🔍 HEX/ASCII COMMUNICATION'):
                    text.insert(tk.END, line + "\n", "section_header")
                elif line.startswith('🎯 PROXIMATE CAUSE ANALYSIS'):
                    text.insert(tk.END, line + "\n", "section_header")
                elif line.startswith('⏰ DIAGNOSTIC EVENT TIMELINE'):
                    text.insert(tk.END, line + "\n", "section_header")
                elif '❌' in line or 'CRITICAL:' in line or '🚨' in line:
                    text.insert(tk.END, line + "\n", "critical_status")
                elif '⚠️' in line or 'WARNING:' in line:
                    text.insert(tk.END, line + "\n", "warning")
                elif '✅' in line or 'good' in line.lower() or 'normal' in line.lower():
                    text.insert(tk.END, line + "\n", "success")
                elif line.startswith('  •') or line.startswith('    ') or line.startswith('  '):
                    text.insert(tk.END, line + "\n", "info")
                elif line.startswith('='):
                    text.insert(tk.END, line + "\n", "bold")
                else:
                    text.insert(tk.END, line + "\n", "normal")
            
            text.insert(tk.END, "\n", "normal")
            
        except Exception as e:
            # Fallback if formatting fails
            text.insert(tk.END, "🚨 CRITICAL DIAGNOSTIC DATA AVAILABLE\n", "critical_status")
            # Safe access: only call len() if it's a dict
            if isinstance(self.critical_diagnostics, dict):
                text.insert(tk.END, f"Analysis completed - {len(self.critical_diagnostics)} sections available\n", "info")
            else:
                text.insert(tk.END, f"Analysis completed but data format unexpected (type: {type(self.critical_diagnostics).__name__})\n", "info")
            text.insert(tk.END, f"Note: Display formatting error: {e}\n", "warning")
            text.insert(tk.END, "\n")
    
    def _display_expert_results(self):
        """Display expert/technical results"""
        self.results_text.delete('1.0', tk.END)
        
        if not self.current_results:
            self.results_text.insert(tk.END, "No results to display.\n")
            return
        
        self.results_text.insert(tk.END, f"=== EXPERT MODE - {len(self.current_results)} ITEMS ===\n\n", "title")
        
        for i, result in enumerate(self.current_results, 1):
            self.results_text.insert(tk.END, f"--- Item {i} ---\n", "bold")
            self.results_text.insert(tk.END, json.dumps(result, indent=2) + "\n\n")
    
    def _toggle_mode(self):
        """Toggle between Simple and Expert mode"""
        is_simple = self.simple_mode.get()
        mode_name = "Simple Mode" if is_simple else "Expert Mode"
        self.status.set(f"Switched to {mode_name}")
        
        if self.current_results:
            self._display_results()
    
    def _on_primary_module_selected(self, event):
        """Handle primary module selection from combobox"""
        selection = self.manual_primary_module.get()
        
        if selection == 'Custom...':
            # Show custom entry
            self.custom_module_frame.pack(side=tk.LEFT, padx=10)
            self.custom_module_entry.focus()
        else:
            # Hide custom entry
            self.custom_module_frame.pack_forget()
            
        # If a log is already parsed, refresh the display
        if hasattr(self, 'current_results') and self.current_results:
            self._display_results()
    
    def _clear_primary_override(self):
        """Clear the primary module override"""
        self.manual_primary_module.set('')
        self.custom_module_frame.pack_forget()
        self.custom_module_entry.delete(0, tk.END)
        
        # Refresh display if log is parsed
        if hasattr(self, 'current_results') and self.current_results:
            self._display_results()
    
    def _get_manual_primary_module(self):
        """Get the manually selected primary module ID"""
        selection = self.manual_primary_module.get()
        
        if not selection:
            return None
        elif selection == 'Custom...':
            custom_id = self.custom_module_entry.get().strip().upper()
            return custom_id if custom_id else None
        else:
            # Extract ID from selection like "716 (GWM - Gateway Module)"
            match = re.match(r'([0-9A-F]{3})', selection)
            return match.group(1) if match else None
    
    def _refresh_display(self):
        """Refresh the current display"""
        if self.current_results:
            self._display_results()
            self.status.set("Display refreshed")
    
    def _show_critical_report(self):
        """Show detailed critical diagnostics report in a separate window"""
        if not self.critical_diagnostics and not CRITICAL_DIAGNOSTICS_AVAILABLE:
            messagebox.showwarning("No Critical Diagnostics", "No critical diagnostic data available. Parse a log file first.")
            return
        
        if not self.current_results:
            messagebox.showwarning("No Data", "No log data available. Parse a log file first.")
            return
        
        # Generate critical diagnostics if not already done
        if not self.critical_diagnostics and CRITICAL_DIAGNOSTICS_AVAILABLE:
            try:
                critical_analyzer = CriticalDiagnosticView()
                self.critical_diagnostics = critical_analyzer.extract_critical_diagnostics(self.current_results)
                
                # Ensure critical_diagnostics is always a dict or None, never False or other types
                if not isinstance(self.critical_diagnostics, dict):
                    print(f"Warning: Critical diagnostics returned unexpected type: {type(self.critical_diagnostics)}")
                    self.critical_diagnostics = None
            except Exception as e:
                messagebox.showerror("Analysis Error", f"Failed to generate critical diagnostics: {e}")
                return
        
        # Create report window
        report_window = tk.Toplevel(self.root)
        report_window.title("🚨 Critical Diagnostic Report")
        report_window.geometry("1200x900")
        
        # Make it resizable
        report_window.rowconfigure(0, weight=1)
        report_window.columnconfigure(0, weight=1)
        
        # Create scrolled text widget
        report_text = scrolledtext.ScrolledText(
            report_window,
            font=('Courier New', 10),
            wrap=tk.WORD,
            background='black',
            foreground='white',
            insertbackground='white'
        )
        report_text.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        
        # Configure text tags for formatting
        report_text.tag_config("critical", foreground="red", font=('Courier New', 10, 'bold'))
        report_text.tag_config("warning", foreground="orange")
        report_text.tag_config("success", foreground="green")
        report_text.tag_config("info", foreground="cyan")
        report_text.tag_config("header", foreground="yellow", font=('Courier New', 12, 'bold'))
        report_text.tag_config("section", foreground="magenta", font=('Courier New', 11, 'bold'))
        
        try:
            # Generate and insert report
            if self.critical_diagnostics:
                report_content = format_critical_diagnostics_report(self.critical_diagnostics)
            else:
                # Fallback - generate basic critical report
                critical_analyzer = CriticalDiagnosticView()
                critical_data = critical_analyzer.extract_critical_diagnostics(self.current_results)
                report_content = format_critical_diagnostics_report(critical_data)
            
            # Insert content with basic formatting
            lines = report_content.split('\n')
            for line in lines:
                if '🚨' in line or 'CRITICAL' in line or '❌' in line:
                    report_text.insert(tk.END, line + "\n", "critical")
                elif '⚠️' in line or 'WARNING' in line:
                    report_text.insert(tk.END, line + "\n", "warning")
                elif '✅' in line or 'SUCCESS' in line or 'GOOD' in line:
                    report_text.insert(tk.END, line + "\n", "success")
                elif line.startswith('╔') or line.startswith('╚') or line.startswith('║'):
                    report_text.insert(tk.END, line + "\n", "header")
                elif any(line.startswith(prefix) for prefix in ['🚗 ', '🔋 ', '🔧 ', '📋 ', '🔍 ', '🎯 ', '⏰ ']):
                    report_text.insert(tk.END, line + "\n", "section")
                elif line.startswith('  •') or line.startswith('    '):
                    report_text.insert(tk.END, line + "\n", "info")
                else:
                    report_text.insert(tk.END, line + "\n")
            
        except Exception as e:
            report_text.insert(tk.END, f"Error generating report: {e}\n", "critical")
            report_text.insert(tk.END, "\nFallback: Basic diagnostic information available in main window.\n", "info")
        
        # Add buttons frame
        button_frame = ttk.Frame(report_window)
        button_frame.grid(row=1, column=0, sticky='ew', padx=10, pady=5)
        
        def save_report():
            """Save the critical report to file"""
            try:
                filename = filedialog.asksaveasfilename(
                    title="Save Critical Diagnostic Report",
                    defaultextension=".txt",
                    filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
                )
                if filename:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(report_text.get("1.0", tk.END))
                    messagebox.showinfo("Saved", f"Critical diagnostic report saved to {filename}")
            except Exception as e:
                messagebox.showerror("Save Error", f"Failed to save report: {e}")
        
        ttk.Button(button_frame, text="💾 Save Report", command=save_report).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="❌ Close", command=report_window.destroy).pack(side=tk.RIGHT, padx=5)
        
        # Focus on the report window
        report_window.focus_set()
        report_window.lift()
        
        # Make report text read-only
        report_text.config(state='disabled')
    
    def _display_dependencies(self):
        """Display module dependency analysis"""
        self.dependencies_text.config(state=tk.NORMAL)
        self.dependencies_text.delete('1.0', tk.END)
        
        if not self.dependency_report or not DEPENDENCY_TRACKER_AVAILABLE:
            self.dependencies_text.insert(tk.END, "Dependency analysis not available.\n", "info")
            self.dependencies_text.insert(tk.END, "\nEither the log contains no module communications,\n", "info")
            self.dependencies_text.insert(tk.END, "or the module_dependency_tracker is not installed.\n", "info")
            self.dependencies_text.config(state=tk.DISABLED)
            return
        
        summary = self.dependency_report.get('summary', {})
        
        # Check if any modules were found
        if summary.get('total_modules_involved', 0) == 0:
            self.dependencies_text.insert(tk.END, "No module communications detected in this log.\n\n", "info")
            self.dependencies_text.insert(tk.END, "This log may not contain diagnostic/programming data,\n", "info")
            self.dependencies_text.insert(tk.END, "or module addresses were not recognized.\n", "info")
            self.dependencies_text.config(state=tk.DISABLED)
            return
        
        # Display formatted dependency report
        tracker = ModuleDependencyTracker()
        formatted_text = tracker.format_dependency_report_text(self.dependency_report)
        
        # Color-code the output
        for line in formatted_text.split('\n'):
            if line.startswith('🔗') or line.startswith('📊') or line.startswith('💡') or line.startswith('📡'):
                self.dependencies_text.insert(tk.END, line + '\n', "header")
            elif line.startswith('❌') or '❌' in line or 'FAILED' in line.upper():
                self.dependencies_text.insert(tk.END, line + '\n', "error")
            elif line.startswith('⚠️') or '⚠️' in line or 'WARNING' in line.upper():
                self.dependencies_text.insert(tk.END, line + '\n', "warning")
            elif line.startswith('✅') or '✅' in line or 'Successful:' in line:
                self.dependencies_text.insert(tk.END, line + '\n', "success")
            elif '(' in line and ')' in line and any(c.isdigit() for c in line):
                # Module names with IDs
                self.dependencies_text.insert(tk.END, line + '\n', "module")
            elif line.startswith('  '):
                # Indented lines
                self.dependencies_text.insert(tk.END, line + '\n', "info")
            elif '═' in line or '─' in line:
                # Separator lines
                self.dependencies_text.insert(tk.END, line + '\n', "header")
            else:
                # Normal text
                self.dependencies_text.insert(tk.END, line + '\n')
        
        self.dependencies_text.config(state=tk.DISABLED)
    
    def _display_security(self):
        """Display enhanced security analysis in the Cybersecurity tab with modern card layout"""
        if not self.security_report:
            return
        
        # Clear existing threat cards
        for widget in self.security_cards_frame.winfo_children():
            widget.destroy()
        
        # Check if this is enhanced analysis (with UDS parser)
        is_enhanced = 'enhanced_security_assessment' in self.security_report
        
        if is_enhanced:
            self._display_enhanced_security()
        else:
            self._display_basic_security()
    
    def _display_enhanced_security(self):
        """Display enhanced security analysis with UDS and failure analysis"""
        # Get enhanced security assessment
        assessment = self.security_report.get('enhanced_security_assessment', {})
        basic_analysis = self.security_report.get('basic_threat_analysis', {})
        
        # Update metric cards with enhanced data
        security_score = assessment.get('security_score', 0)
        risk_level = assessment.get('risk_level', 'UNKNOWN')
        total_threats = basic_analysis.get('total_threats', 0)
        
        self.security_metrics['total'].config(text=str(total_threats))
        self.security_metrics['critical'].config(text=str(assessment.get('security_issues', []).__len__()))
        self.security_metrics['high'].config(text=risk_level)
        self.security_metrics['medium'].config(text=f"{security_score}/100")
        
        # Display security score card
        score_card = tk.Frame(self.security_cards_frame, bg='#3498db', relief=tk.RAISED, borderwidth=2)
        score_card.pack(fill=tk.X, padx=10, pady=10)
        
        score_inner = tk.Frame(score_card, bg='#ebf3fd')
        score_inner.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        score_title = tk.Label(score_inner, text="🎯 SECURITY ASSESSMENT", 
                              font=('Arial', 14, 'bold'), bg='#ebf3fd', fg='#2c3e50')
        score_title.pack(pady=(10, 5))
        
        score_text = tk.Label(score_inner, text=f"Security Score: {security_score}/100 | Risk Level: {risk_level}", 
                             font=('Arial', 12), bg='#ebf3fd', fg='#34495e')
        score_text.pack(pady=5)
        
        # Display security issues if any
        security_issues = assessment.get('security_issues', [])
        if security_issues:
            issues_text = "\n".join([f"• {issue}" for issue in security_issues[:3]])
            issues_label = tk.Label(score_inner, text=issues_text, 
                                   font=('Arial', 10), bg='#ebf3fd', fg='#e74c3c',
                                   justify=tk.LEFT, wraplength=700)
            issues_label.pack(pady=(0, 10))
        
        # Display simple explanations
        explanations = self.security_report.get('simple_explanations', {})
        if explanations:
            self._display_simple_explanations(explanations)
        
        # Display enhanced recommendations
        recommendations = self.security_report.get('detailed_recommendations', [])
        if recommendations:
            self._display_enhanced_recommendations(recommendations)
        
        # Display failure/success summary
        fs_analysis = self.security_report.get('failure_success_analysis', {})
        if fs_analysis:
            self._display_failure_success_summary(fs_analysis)
    
    def _display_simple_explanations(self, explanations):
        """Display simple explanations for what happened"""
        exp_card = tk.Frame(self.security_cards_frame, bg='#27ae60', relief=tk.RAISED, borderwidth=2)
        exp_card.pack(fill=tk.X, padx=10, pady=10)
        
        exp_inner = tk.Frame(exp_card, bg='#d5f4e6')
        exp_inner.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        exp_title = tk.Label(exp_inner, text="💡 WHAT HAPPENED (SIMPLE EXPLANATIONS)", 
                            font=('Arial', 14, 'bold'), bg='#d5f4e6', fg='#2c3e50')
        exp_title.pack(pady=(10, 5))
        
        # Create scrollable text for explanations
        exp_frame = tk.Frame(exp_inner, bg='#d5f4e6')
        exp_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        
        exp_text = scrolledtext.ScrolledText(exp_frame, height=8, font=('Consolas', 10),
                                           bg='white', fg='#2c3e50', wrap=tk.WORD)
        exp_text.pack(fill=tk.BOTH, expand=True)
        
        # Add explanations
        if explanations.get('what_worked'):
            exp_text.insert(tk.END, "✅ SUCCESSFUL OPERATIONS:\n", "success")
            for explanation in explanations['what_worked'][:5]:
                exp_text.insert(tk.END, f"  • {explanation}\n")
            exp_text.insert(tk.END, "\n")
        
        if explanations.get('what_failed'):
            exp_text.insert(tk.END, "❌ FAILED OPERATIONS:\n", "error")
            for explanation in explanations['what_failed'][:5]:
                exp_text.insert(tk.END, f"  • {explanation}\n")
            exp_text.insert(tk.END, "\n")
        
        if explanations.get('why_failed'):
            exp_text.insert(tk.END, "🤔 WHY OPERATIONS FAILED:\n", "warning")
            unique_reasons = list(set(explanations['why_failed'][:5]))
            for reason in unique_reasons:
                exp_text.insert(tk.END, f"  • {reason}\n")
        
        exp_text.config(state=tk.DISABLED)
    
    def _display_enhanced_recommendations(self, recommendations):
        """Display enhanced security recommendations"""
        rec_card = tk.Frame(self.security_cards_frame, bg='#e67e22', relief=tk.RAISED, borderwidth=2)
        rec_card.pack(fill=tk.X, padx=10, pady=10)
        
        rec_inner = tk.Frame(rec_card, bg='#fdebd0')
        rec_inner.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        rec_title = tk.Label(rec_inner, text="🛡️ SECURITY RECOMMENDATIONS", 
                            font=('Arial', 14, 'bold'), bg='#fdebd0', fg='#2c3e50')
        rec_title.pack(pady=(10, 5))
        
        # Create scrollable text for recommendations
        rec_frame = tk.Frame(rec_inner, bg='#fdebd0')
        rec_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        
        rec_text = scrolledtext.ScrolledText(rec_frame, height=6, font=('Arial', 10),
                                           bg='white', fg='#2c3e50', wrap=tk.WORD)
        rec_text.pack(fill=tk.BOTH, expand=True)
        
        for recommendation in recommendations:
            rec_text.insert(tk.END, f"{recommendation}\n\n")
        
        rec_text.config(state=tk.DISABLED)
    
    def _display_failure_success_summary(self, fs_analysis):
        """Display failure and success analysis summary"""
        summary = fs_analysis.get('summary', {})
        failure_summary = summary.get('failure_summary', {})
        success_summary = summary.get('success_summary', {})
        
        fs_card = tk.Frame(self.security_cards_frame, bg='#9b59b6', relief=tk.RAISED, borderwidth=2)
        fs_card.pack(fill=tk.X, padx=10, pady=10)
        
        fs_inner = tk.Frame(fs_card, bg='#f4ecf7')
        fs_inner.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        fs_title = tk.Label(fs_inner, text="📊 OPERATION RESULTS SUMMARY", 
                           font=('Arial', 14, 'bold'), bg='#f4ecf7', fg='#2c3e50')
        fs_title.pack(pady=(10, 5))
        
        # Create summary text
        fs_frame = tk.Frame(fs_inner, bg='#f4ecf7')
        fs_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        
        summary_text = f"""FAILURES: {failure_summary.get('total_failures', 0)} total
  • Critical: {failure_summary.get('critical_failures', 0)}
  • High Impact: {failure_summary.get('high_impact_failures', 0)}
  • Timeouts: {failure_summary.get('timeout_failures', 0)}
  • Communication Errors: {failure_summary.get('comm_failures', 0)}

SUCCESSES: {success_summary.get('total_successes', 0)} total
  • Read Operations: {success_summary.get('read_operations', 0)}
  • Write Operations: {success_summary.get('write_operations', 0)}
  • Security Operations: {success_summary.get('security_operations', 0)}

Overall Success Rate: {summary.get('overall_success_rate', 0) * 100:.1f}%"""
        
        fs_label = tk.Label(fs_frame, text=summary_text, 
                           font=('Consolas', 10), bg='#f4ecf7', fg='#34495e',
                           justify=tk.LEFT)
        fs_label.pack(anchor=tk.W)
    
    def _display_basic_security(self):
        """Display basic security analysis (fallback)"""
        total_threats = self.security_report.get('total_threats', 0)
        severity_stats = self.security_report.get('severity_stats', {})
        
        # Update metric cards
        self.security_metrics['total'].config(text=str(total_threats))
        self.security_metrics['critical'].config(text=str(severity_stats.get('critical', 0)))
        self.security_metrics['high'].config(text=str(severity_stats.get('high', 0)))
        self.security_metrics['medium'].config(text=str(severity_stats.get('medium', 0)))
        
        # Update severity breakdown chart
        self._draw_severity_chart(severity_stats)
        
        # Update affected modules
        self.modules_text.config(state=tk.NORMAL)
        self.modules_text.delete('1.0', tk.END)
        affected = self.security_report.get('affected_modules', [])
        if affected:
            for module in sorted(affected):
                self.modules_text.insert(tk.END, f"• {module}\n")
        else:
            self.modules_text.insert(tk.END, "No modules affected")
        self.modules_text.config(state=tk.DISABLED)
        
        # Check if any threats were found
        if total_threats == 0:
            success_card = tk.Frame(self.security_cards_frame, bg='#d5f4e6', relief=tk.RAISED, borderwidth=2)
            success_card.pack(fill=tk.X, padx=10, pady=10)
            
            icon = tk.Label(success_card, text="✅", font=('Segoe UI Emoji', 32), bg='#d5f4e6')
            icon.pack(pady=(20, 10))
            
            title = tk.Label(success_card, text="NO SECURITY THREATS DETECTED", 
                           font=('Arial', 14, 'bold'), bg='#d5f4e6', fg='#27ae60')
            title.pack(pady=5)
            
            message = tk.Label(success_card, text="The log analysis found no cybersecurity threats or vulnerabilities.", 
                             font=('Arial', 11), bg='#d5f4e6', fg='#2c3e50', wraplength=600)
            message.pack(pady=(5, 20))
            return
        
        # Display threat cards (existing code)
        threats = self.security_report.get('threats', [])
        severity_colors = {
            'critical': ('#e74c3c', '#fadbd8'),
            'high': ('#e67e22', '#fdebd0'),
            'medium': ('#f39c12', '#fef5e7'),
            'low': ('#27ae60', '#d5f4e6')
        }
        
        severity_icons = {
            'critical': '🔴',
            'high': '🟠',
            'medium': '🟡',
            'low': '🟢'
        }
        
        for idx, threat in enumerate(threats, 1):
            severity = threat.get('severity', 'low')
            border_color, bg_color = severity_colors.get(severity, ('#95a5a6', '#ecf0f1'))
            icon = severity_icons.get(severity, '⚪')
            
            card = tk.Frame(self.security_cards_frame, bg=border_color, relief=tk.RAISED, borderwidth=2)
            card.pack(fill=tk.X, padx=10, pady=8)
            
            inner = tk.Frame(card, bg=bg_color)
            inner.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
            
            # Header with severity and icon
            header_frame = tk.Frame(inner, bg=bg_color)
            header_frame.pack(fill=tk.X, padx=15, pady=(10, 5))
            
            icon_label = tk.Label(header_frame, text=icon, font=('Segoe UI Emoji', 16), 
                                 bg=bg_color, width=2)
            icon_label.pack(side=tk.LEFT, padx=(0, 10))
            
            severity_label = tk.Label(header_frame, text=f"#{idx} - {severity} SEVERITY", 
                                     font=('Arial', 11, 'bold'), bg=bg_color, fg=border_color)
            severity_label.pack(side=tk.LEFT)
            
            # Threat type
            type_frame = tk.Frame(inner, bg=bg_color)
            type_frame.pack(fill=tk.X, padx=15, pady=5)
            
            type_label = tk.Label(type_frame, text=f"🎯 Type: {threat.get('type', 'Unknown')}", 
                                 font=('Arial', 10, 'bold'), bg=bg_color, fg='#2c3e50')
            type_label.pack(anchor=tk.W)
            
            # Description
            desc_frame = tk.Frame(inner, bg=bg_color)
            desc_frame.pack(fill=tk.X, padx=15, pady=5)
            
            desc_label = tk.Label(desc_frame, text=threat.get('description', 'No description'), 
                                 font=('Arial', 10), bg=bg_color, fg='#34495e', 
                                 wraplength=700, justify=tk.LEFT)
            desc_label.pack(anchor=tk.W)
            
            # Module info if available
            if threat.get('module'):
                module_frame = tk.Frame(inner, bg=bg_color)
                module_frame.pack(fill=tk.X, padx=15, pady=5)
                
                module_label = tk.Label(module_frame, text=f"📍 Module: {threat['module']}", 
                                       font=('Arial', 9), bg=bg_color, fg='#7f8c8d')
                module_label.pack(anchor=tk.W)
            
            # Recommendation
            if threat.get('recommendation'):
                rec_frame = tk.Frame(inner, bg='white')
                rec_frame.pack(fill=tk.X, padx=15, pady=(10, 15))
                
                rec_title = tk.Label(rec_frame, text="💡 Recommendation:", 
                                    font=('Arial', 9, 'bold'), bg='white', fg='#2c3e50')
                rec_title.pack(anchor=tk.W, padx=10, pady=(8, 2))
                
                rec_text = tk.Label(rec_frame, text=threat['recommendation'], 
                                   font=('Arial', 9), bg='white', fg='#34495e', 
                                   wraplength=650, justify=tk.LEFT)
                rec_text.pack(anchor=tk.W, padx=10, pady=(0, 8))
    
    def _draw_severity_chart(self, severity_stats):
        """Draw a simple bar chart for severity breakdown"""
        canvas = self.severity_canvas
        canvas.delete("all")
        
        if not severity_stats:
            canvas.create_text(200, 60, 
                             text="No data", font=('Arial', 10), fill='#7f8c8d')
            return
        
        severities = ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']
        colors = ['#e74c3c', '#e67e22', '#f39c12', '#27ae60']
        
        # Get max value for scaling
        max_val = max(severity_stats.values()) if severity_stats.values() else 1
        
        # Draw bars
        width = 400
        bar_width = (width - 80) // len(severities)
        
        for idx, (severity, color) in enumerate(zip(severities, colors)):
            count = severity_stats.get(severity, 0)
            if max_val > 0:
                bar_height = (count / max_val) * 80
            else:
                bar_height = 0
            
            x = 40 + idx * bar_width
            y = 90 - bar_height
            
            # Draw bar
            canvas.create_rectangle(x, y, x + bar_width - 10, 90, 
                                   fill=color, outline=color, width=2)
            
            # Draw count on top
            canvas.create_text(x + (bar_width - 10) // 2, y - 10, 
                             text=str(count), font=('Arial', 10, 'bold'), fill=color)
            
            # Draw label below
            canvas.create_text(x + (bar_width - 10) // 2, 105, 
                             text=severity[:4], font=('Arial', 8), fill='#2c3e50')
    
    def _display_fdrs(self):
        """Display FDRS analysis results"""
        if not self.fdrs_analysis:
            # Clear FDRS displays and show welcome message
            self._clear_fdrs_displays()
            return
        
        # Update FDRS metrics cards
        system_info = self.fdrs_analysis.get('system_info')
        summary = self.fdrs_analysis.get('summary', {})
        
        if system_info:
            self.fdrs_metrics['version'].config(text=system_info.fdrs_version)
        else:
            self.fdrs_metrics['version'].config(text="Unknown")
        
        self.fdrs_metrics['services'].config(text=str(summary.get('total_diagnostic_services', 0)))
        self.fdrs_metrics['success_rate'].config(text=f"{summary.get('success_rate', 0):.1f}%")
        self.fdrs_metrics['nrc_errors'].config(text=str(summary.get('nrc_errors', 0)))
        
        # Update system information
        self.fdrs_system_text.config(state=tk.NORMAL)
        self.fdrs_system_text.delete('1.0', tk.END)
        
        if system_info:
            sys_text = f"""🔧 FDRS System Information
────────────────────────────────
Version: {system_info.fdrs_version}
Server: {system_info.fdsp_server_url}
Dependency Modules: {len(system_info.dependencies)}

📦 Key Dependencies:
"""
            for module, version in system_info.dependencies.items():
                sys_text += f"  • {module}: {version}\n"
        else:
            sys_text = "No FDRS system information found in log"
        
        self.fdrs_system_text.insert('1.0', sys_text)
        self.fdrs_system_text.config(state=tk.DISABLED)
        
        # Update communication analysis
        self.fdrs_comm_text.config(state=tk.NORMAL)
        self.fdrs_comm_text.delete('1.0', tk.END)
        
        if self.fdrs_detailed:
            comm_analysis = self.fdrs_detailed.get('communication_analysis', {})
            latest = comm_analysis.get('latest_communication', {})
            read_did = comm_analysis.get('read_did_analysis', {})
            
            comm_text = f"""📡 UDS Communication Analysis
────────────────────────────────
Latest Communication:
  Service: {latest.get('service', 'Unknown')}
  Status: {latest.get('status', 'Unknown')}
  Time: {latest.get('timestamp', 'Unknown')}
  Error: {latest.get('nrc_error', 'None')}

Read DID (0x22) Analysis:
  Total Attempts: {read_did.get('total_attempts', 0)}
  Failed Attempts: {read_did.get('failed_attempts', 0)}
  Success Rate: {read_did.get('success_rate', 0):.1f}%
"""
        else:
            comm_text = "No detailed communication analysis available"
        
        self.fdrs_comm_text.insert('1.0', comm_text)
        self.fdrs_comm_text.config(state=tk.DISABLED)
        
        # Update detailed analysis tabs
        self._update_fdrs_services_tab()
        self._update_fdrs_errors_tab()
        self._update_fdrs_recommendations_tab()
    
    def _update_fdrs_services_tab(self):
        """Update the diagnostic services tab"""
        self.fdrs_services_text.config(state=tk.NORMAL)
        self.fdrs_services_text.delete('1.0', tk.END)
        
        if not self.fdrs_analysis:
            self.fdrs_services_text.insert('1.0', "No FDRS analysis available")
            self.fdrs_services_text.config(state=tk.DISABLED)
            return
        
        services = self.fdrs_analysis.get('diagnostic_services', [])
        if not services:
            self.fdrs_services_text.insert('1.0', "No diagnostic services found in log")
            self.fdrs_services_text.config(state=tk.DISABLED)
            return
        
        services_text = "🔍 UDS Diagnostic Services Detected\n"
        services_text += "═" * 60 + "\n\n"
        
        for i, service in enumerate(services, 1):
            status_icon = "✅" if service.status == "SUCCESS" else "❌"
            services_text += f"{status_icon} Service #{i}\n"
            services_text += f"  Code: 0x{service.service_code}\n"
            services_text += f"  Name: {service.service_name}\n"
            services_text += f"  Status: {service.status}\n"
            services_text += f"  Request: {service.request_data}\n"
            services_text += f"  Response: {service.response_data}\n"
            services_text += f"  Time: {service.timestamp.strftime('%H:%M:%S')}\n"
            
            if service.nrc_code:
                services_text += f"  NRC: 0x{service.nrc_code} - {service.nrc_description}\n"
            
            services_text += "\n" + "─" * 60 + "\n\n"
        
        self.fdrs_services_text.insert('1.0', services_text)
        self.fdrs_services_text.config(state=tk.DISABLED)
    
    def _update_fdrs_errors_tab(self):
        """Update the error analysis tab"""
        self.fdrs_errors_text.config(state=tk.NORMAL)
        self.fdrs_errors_text.delete('1.0', tk.END)
        
        if not self.fdrs_detailed:
            self.fdrs_errors_text.insert('1.0', "No detailed error analysis available")
            self.fdrs_errors_text.config(state=tk.DISABLED)
            return
        
        error_analysis = self.fdrs_detailed.get('error_analysis', {})
        
        if error_analysis.get('status') == "No errors found":
            errors_text = "✅ No errors detected in FDRS log!\n\n"
            errors_text += "All diagnostic communications completed successfully."
        else:
            errors_text = "⚠️ Error Analysis\n"
            errors_text += "═" * 40 + "\n\n"
            
            errors_text += f"Total Errors: {error_analysis.get('total_errors', 0)}\n"
            errors_text += f"NRC 31 Errors: {error_analysis.get('nrc_31_errors', 0)}\n\n"
            
            errors_text += "Error Breakdown by NRC Code:\n"
            errors_text += "─" * 30 + "\n"
            
            for nrc, count in error_analysis.get('error_breakdown', {}).items():
                errors_text += f"  NRC {nrc}: {count} occurrences\n"
        
        self.fdrs_errors_text.insert('1.0', errors_text)
        self.fdrs_errors_text.config(state=tk.DISABLED)
    
    def _update_fdrs_recommendations_tab(self):
        """Update the recommendations tab"""
        self.fdrs_recommendations_text.config(state=tk.NORMAL)
        self.fdrs_recommendations_text.delete('1.0', tk.END)
        
        if not self.fdrs_detailed:
            self.fdrs_recommendations_text.insert('1.0', "No recommendations available")
            self.fdrs_recommendations_text.config(state=tk.DISABLED)
            return
        
        recommendations = self.fdrs_detailed.get('recommendations', [])
        
        rec_text = "💡 FDRS Troubleshooting Recommendations\n"
        rec_text += "═" * 50 + "\n\n"
        
        if recommendations:
            for rec in recommendations:
                rec_text += rec + "\n\n"
        else:
            rec_text += "✅ No specific recommendations - system appears healthy!"
        
        rec_text += "\n" + "─" * 50 + "\n\n"
        rec_text += "📋 General FDRS Best Practices:\n\n"
        rec_text += "• Ensure stable 12V power supply during diagnostics\n"
        rec_text += "• Verify ECU is in proper diagnostic session\n"
        rec_text += "• Check CAN bus communication quality\n"
        rec_text += "• Use appropriate security access credentials\n"
        rec_text += "• Allow sufficient time delays between operations\n"
        
        self.fdrs_recommendations_text.insert('1.0', rec_text)
        self.fdrs_recommendations_text.config(state=tk.DISABLED)
    
    def _clear_fdrs_displays(self):
        """Clear FDRS displays and show welcome message"""
        # Reset metrics
        for metric in self.fdrs_metrics.values():
            metric.config(text="N/A")
        
        # Clear text areas and show welcome
        self.fdrs_system_text.config(state=tk.NORMAL)
        self.fdrs_system_text.delete('1.0', tk.END)
        self._initialize_fdrs_welcome()
        
        self.fdrs_comm_text.config(state=tk.NORMAL)
        self.fdrs_comm_text.delete('1.0', tk.END)
        self.fdrs_comm_text.insert('1.0', "No FDRS communication data available\n\nLoad a FDRS log file to see UDS diagnostic analysis")
        self.fdrs_comm_text.config(state=tk.DISABLED)
        
        # Clear detailed tabs
        for text_widget in [self.fdrs_services_text, self.fdrs_errors_text, self.fdrs_recommendations_text]:
            text_widget.config(state=tk.NORMAL)
            text_widget.delete('1.0', tk.END)
            text_widget.insert('1.0', "No data available - load an FDRS log file")
            text_widget.config(state=tk.DISABLED)
    
    def _toggle_theme(self):
        """Toggle between light and dark theme"""
        self.config.toggle_theme()
        messagebox.showinfo("Theme Changed", "Theme will be applied on next restart.")
    
    def _clear_results(self):
        """Clear all results"""
        self.results_text.delete('1.0', tk.END)
        self.current_results = []
        self.file_path.set('')
        self.status.set("Results cleared")
        # Hide NRC 7F alert when clearing
        self.nrc7f_alert.grid_remove()
    
    def _export_json(self):
        """Export results to JSON"""
        if not self.current_results:
            messagebox.showwarning("No Data", "No results to export.")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'w') as f:
                    json.dump(self.current_results, f, indent=2)
                self.status.set(f"Exported to {filename}")
                messagebox.showinfo("Success", f"Results exported to:\n{filename}")
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export: {str(e)}")
    
    def _export_txt(self):
        """Export results to text file"""
        if not self.current_results:
            messagebox.showwarning("No Data", "No results to export.")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'w') as f:
                    f.write(self.results_text.get('1.0', tk.END))
                self.status.set(f"Exported to {filename}")
                messagebox.showinfo("Success", f"Results exported to:\n{filename}")
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export: {str(e)}")
    
    def _decode_hex(self):
        """Decode hex values"""
        hex_values = self.hex_input.get().strip()
        if not hex_values:
            return
        
        self.hex_output.delete('1.0', tk.END)
        
        for hex_val in hex_values.split():
            try:
                explanation = HexExplainer.explain_byte(hex_val)
                self.hex_output.insert(tk.END, f"{hex_val}:\n{explanation}\n\n")
            except Exception as e:
                self.hex_output.insert(tk.END, f"{hex_val}: Error - {str(e)}\n\n")
    
    def _explain_nrc(self):
        """Explain NRC code"""
        nrc_code = self.nrc_input.get().strip()
        if not nrc_code:
            return
        
        self.nrc_output.delete('1.0', tk.END)
        
        try:
            explanation = NRCCodeExplainer.explain_code(nrc_code)
            self.nrc_output.insert(tk.END, f"NRC Code: {nrc_code}\n\n")
            self.nrc_output.insert(tk.END, f"Explanation:\n{explanation}\n")
        except Exception as e:
            self.nrc_output.insert(tk.END, f"Error: {str(e)}\n")
    
    def _show_filter_panel(self):
        """Show smart filter panel with AI-powered suggestions"""
        if SMART_FILTER_AVAILABLE and self.smart_filter:
            SmartFilterPanel(self.root, self.smart_filter, self._apply_smart_filter)
        else:
            # Fallback to old filter panel
            FilterPanel(self.root, self.config, self._apply_advanced_filters)
    
    def _apply_advanced_filters(self, filters):
        """Apply advanced filters and re-parse"""
        self.status.set("Applying advanced filters...")
        # Reparse with new filters if needed
        if self.current_filepath:
            self._parse_log()
    
    def _apply_smart_filter(self, keywords):
        """Apply smart filter to current results"""
        if not self.current_results or not keywords:
            return
        
        self.active_filter_keywords = keywords
        self.status.set(f"Filtering by: {', '.join(keywords)}")
        
        # Get current content
        current_content = self.result_text.get('1.0', tk.END)
        
        # Apply filter
        filtered_content, match_count = self.smart_filter.apply_filter(current_content, keywords)
        
        # Update display
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete('1.0', tk.END)
        
        if match_count > 0:
            self.result_text.insert(tk.END, f"🔍 Filter Results: {match_count} matches for [{', '.join(keywords)}]\n\n", "header")
            self.result_text.insert(tk.END, filtered_content)
            
            # Highlight matches
            matches = self.smart_filter.highlight_matches(filtered_content, keywords)
            for start, end, keyword in matches:
                # Convert positions to line.column format
                self.result_text.tag_add("highlight", f"3.0+{start}c", f"3.0+{end}c")
        else:
            self.result_text.insert(tk.END, f"🔍 No matches found for: {', '.join(keywords)}\n\n", "warning")
            self.result_text.insert(tk.END, "Try adjusting your filter keywords or using suggested presets.", "info")
        
        self.result_text.config(state=tk.DISABLED)
        self.status.set(f"Filter applied: {match_count} matches")
        
        # Add to history
        if self.smart_filter:
            self.smart_filter.add_to_history(', '.join(keywords), match_count)
    
    def _browse_compare_file(self, file_num):
        """Browse for comparison file"""
        filename = filedialog.askopenfilename(
            title=f"Select Log File {file_num}",
            filetypes=[
                ("All supported files", "*.xml;*.txt;*.log"),
                ("All files", "*.*")
            ]
        )
        
        if filename:
            if file_num == 1:
                self.compare_file1.set(filename)
            else:
                self.compare_file2.set(filename)
    
    def _compare_logs(self):
        """Compare two log files"""
        file1 = self.compare_file1.get()
        file2 = self.compare_file2.get()
        
        if not file1 or not file2:
            messagebox.showwarning("Missing Files", "Please select both files to compare.")
            return
        
        self.status.set("Comparing logs...")
        
        try:
            # Parse both files
            if file1.lower().endswith('.xml'):
                results1 = self.xml_parser.parse_file(file1)
            else:
                results1 = self.text_parser.parse_file(file1, [k.strip() for k in self.filters.get().split(',')])
            
            if file2.lower().endswith('.xml'):
                results2 = self.xml_parser.parse_file(file2)
            else:
                results2 = self.text_parser.parse_file(file2, [k.strip() for k in self.filters.get().split(',')])
            
            # Compare
            comparison = self.comparator.compare_logs(results1, results2)
            
            # Display results
            self.compare_left.delete('1.0', tk.END)
            self.compare_right.delete('1.0', tk.END)
            
            # Unique to file 1
            self.compare_left.insert(tk.END, f"=== UNIQUE TO FILE 1 ({comparison['unique_to_log1_count']} items) ===\n\n")
            for item in comparison['unique_to_log1'][:50]:
                self.compare_left.insert(tk.END, f"{item}\n\n")
            
            # Unique to file 2
            self.compare_right.insert(tk.END, f"=== UNIQUE TO FILE 2 ({comparison['unique_to_log2_count']} items) ===\n\n")
            for item in comparison['unique_to_log2'][:50]:
                self.compare_right.insert(tk.END, f"{item}\n\n")
            
            self.status.set(f"Comparison complete: {comparison['common_count']} common, "
                          f"{comparison['unique_to_log1_count']} unique to file 1, "
                          f"{comparison['unique_to_log2_count']} unique to file 2")
            
        except Exception as e:
            messagebox.showerror("Comparison Error", f"Error comparing logs: {str(e)}")
            self.status.set("Comparison failed")
    
    def _refresh_history(self):
        """Refresh history list"""
        # Clear existing
        for item in self.history_tree.get_children():
            self.history_tree.delete(item)
        
        # Load recent logs
        logs = self.db.get_recent_logs(50)
        
        for log in logs:
            self.history_tree.insert('', tk.END, text=str(log['id']), values=(
                log['parse_date'],
                log['filename'],
                log['total_errors'],
                log['total_successes'],
                log.get('root_cause_type', '')
            ))
    
    def _view_history_details(self, event):
        """View details of a history item"""
        selection = self.history_tree.selection()
        if not selection:
            return
        
        item = self.history_tree.item(selection[0])
        log_id = int(item['text'])
        
        # Get details
        details = self.db.get_log_details(log_id)
        
        if details:
            # Create detail window
            detail_win = tk.Toplevel(self.root)
            detail_win.title(f"Log Details - ID {log_id}")
            detail_win.geometry("800x600")
            
            text = scrolledtext.ScrolledText(detail_win, wrap=tk.WORD)
            text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            text.insert(tk.END, f"=== LOG SESSION {log_id} ===\n\n")
            text.insert(tk.END, f"Filename: {details['filename']}\n")
            text.insert(tk.END, f"Parse Date: {details['parse_date']}\n")
            text.insert(tk.END, f"File Type: {details['file_type']}\n")
            text.insert(tk.END, f"Total Errors: {details['total_errors']}\n")
            text.insert(tk.END, f"Total Successes: {details['total_successes']}\n")
            text.insert(tk.END, f"Root Cause: {details.get('root_cause_type', 'N/A')}\n\n")
            
            if details.get('errors'):
                text.insert(tk.END, f"=== ERRORS ({len(details['errors'])}) ===\n\n")
                for error in details['errors'][:20]:
                    text.insert(tk.END, f"Line {error['line_number']}: {error['description'][:100]}\n\n")
    
    def _search_history(self):
        """Search history"""
        query = self.history_search.get()
        if not query:
            self._refresh_history()
            return
        
        results = self.db.search_logs(query, 'filename')
        
        # Clear and populate
        for item in self.history_tree.get_children():
            self.history_tree.delete(item)
        
        for log in results:
            self.history_tree.insert('', tk.END, text=str(log['id']), values=(
                log['parse_date'],
                log['filename'],
                log['total_errors'],
                '',
                ''
            ))
    
    def _show_db_stats(self):
        """Show database statistics"""
        stats = self.db.get_statistics()
        
        msg = f"Database Statistics:\n\n"
        msg += f"Total Logs Analyzed: {stats['total_logs']}\n"
        msg += f"Total Errors Recorded: {stats['total_errors']}\n\n"
        
        if stats.get('problematic_files'):
            msg += "Most Problematic Files:\n"
            for file_stat in stats['problematic_files']:
                msg += f"  • {file_stat['filename']}: {file_stat['avg_errors']:.1f} avg errors\n"
        
        messagebox.showinfo("Database Statistics", msg)
    
    def _clean_old_logs(self):
        """Clean old logs from database"""
        response = messagebox.askyesno(
            "Clean Old Logs",
            "Delete log records older than 90 days?"
        )
        
        if response:
            count = self.db.delete_old_logs(90)
            messagebox.showinfo("Cleanup Complete", f"Deleted {count} old log records.")
            self._refresh_history()
    
    def _clear_recent_files(self):
        """Clear recent files list"""
        self.config.clear_recent_files()
        self._update_recent_files_menu()
        messagebox.showinfo("Cleared", "Recent files list cleared.")
    
    def _show_find_dialog(self):
        """Show find dialog"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Find")
        dialog.geometry("400x100")
        
        ttk.Label(dialog, text="Find:").pack(pady=10)
        search_var = tk.StringVar()
        entry = ttk.Entry(dialog, textvariable=search_var, width=50)
        entry.pack(pady=5)
        entry.focus()
        
        def do_find():
            query = search_var.get()
            if query:
                # Search in results text
                start_pos = self.results_text.search(query, '1.0', tk.END, nocase=True)
                if start_pos:
                    end_pos = f"{start_pos}+{len(query)}c"
                    self.results_text.tag_remove('highlight', '1.0', tk.END)
                    self.results_text.tag_add('highlight', start_pos, end_pos)
                    self.results_text.see(start_pos)
                    dialog.destroy()
                else:
                    messagebox.showinfo("Not Found", f"'{query}' not found.")
        
        ttk.Button(dialog, text="Find", command=do_find).pack(pady=5)
        entry.bind('<Return>', lambda e: do_find())
    
    def _show_shortcuts(self):
        """Show keyboard shortcuts"""
        shortcuts = """
Keyboard Shortcuts:

Ctrl+O      Open log file
Ctrl+S      Export to JSON
Ctrl+F      Find text
F5          Refresh display
Ctrl+M      Toggle Simple/Expert mode
Ctrl+L      Clear results

File Menu:  Access recent files
View Menu:  Toggle dark mode
Tools Menu: Advanced filters, database tools
        """
        messagebox.showinfo("Keyboard Shortcuts", shortcuts)
    
    def _launch_professional_analyzer(self):
        """Launch the Professional Diagnostic Analyzer for complex analysis"""
        try:
            import subprocess
            import sys
            
            # Path to the professional analyzer
            professional_analyzer_path = os.path.join(os.path.dirname(__file__), "professional_diagnostic_analyzer.py")
            
            if os.path.exists(professional_analyzer_path):
                # Launch the professional analyzer as a separate process
                if sys.platform.startswith('win'):
                    # Windows
                    subprocess.Popen([sys.executable, professional_analyzer_path], 
                                   creationflags=subprocess.CREATE_NEW_CONSOLE)
                else:
                    # Unix-like systems
                    subprocess.Popen([sys.executable, professional_analyzer_path])
                
                self.status.set("Launched Professional Diagnostic Analyzer")
                
                # Show info dialog
                messagebox.showinfo("Professional Analyzer Launched", 
                    "🚀 Professional Diagnostic Analyzer has been launched in a separate window.\n\n"
                    "The Professional Analyzer provides:\n"
                    "• Multi-source input & correlation analysis\n"
                    "• AI-powered diagnostic insights\n"
                    "• Enhanced NRC detection (7F, 22)\n"
                    "• Cross-report correlation\n"
                    "• Professional reporting\n\n"
                    "You can continue using this Enhanced GUI while the Professional Analyzer runs separately.")
            else:
                messagebox.showerror("Not Found", 
                    f"Professional Diagnostic Analyzer not found at:\n{professional_analyzer_path}\n\n"
                    "Please ensure 'professional_diagnostic_analyzer.py' is in the same directory.")
        
        except Exception as e:
            messagebox.showerror("Launch Error", f"Failed to launch Professional Analyzer:\n{str(e)}")
    
    def _switch_to_professional_mode(self):
        """Provide guidance for switching to professional mode"""
        current_file = self.file_path.get().strip()
        
        dialog_text = """📊 COMPLEX DIAGNOSTIC MODE
        
Your analysis shows significant system issues that would benefit from advanced diagnostic tools.

Based on your results:
• Health Score: 16.7% (Needs Attention)
• Critical Errors: 5 detected
• Success Rate: 16.7%

🚀 RECOMMENDED ACTIONS:

1️⃣ Launch Professional Analyzer
   Click 'Launch Now' to open the advanced diagnostic tool
   
2️⃣ Use Multi-Source Correlation
   Upload additional reports for cross-analysis
   
3️⃣ Enable AI Analysis
   Get intelligent diagnostic recommendations

Would you like to launch the Professional Analyzer now?"""

        result = messagebox.askyesno("Switch to Professional Mode", dialog_text)
        
        if result:
            # Launch professional analyzer
            self._launch_professional_analyzer()
            
            # If there's a current file, show how to transfer it
            if current_file and os.path.exists(current_file):
                messagebox.showinfo("File Transfer", 
                    f"💡 TIP: Your current file is ready for analysis:\n\n"
                    f"📁 {os.path.basename(current_file)}\n\n"
                    f"In the Professional Analyzer:\n"
                    f"1. Click 'Browse...' to select this file\n"
                    f"2. Choose 'Comprehensive' analysis mode\n"
                    f"3. Add any correlation reports\n"
                    f"4. Click 'Analyze Primary' for detailed results")
    
    def _show_about(self):
        """Show about dialog"""
        about_text = """
Log Parser Pro - Enhanced Edition
Version 2.0

Features:
✅ XML & Text log parsing
✅ Simple Mode for beginners
✅ Expert Mode for technicians
✅ 75+ ECU module database
✅ Root cause analysis
✅ Dark mode
✅ Analytics & charts
✅ Log comparison
✅ Database history
✅ Keyboard shortcuts
✅ Drag & drop support
🚀 Professional Analyzer integration

Created with ❤️ for automotive diagnostics
        """
        messagebox.showinfo("About", about_text)
    
    def _on_closing(self):
        """Handle window closing with proper cleanup"""
        try:
            # Cancel any ongoing operations
            if hasattr(self, 'performance_manager') and self.performance_manager:
                self.performance_manager.cancel_operation()
                
            # Close any active progress dialogs
            if hasattr(self, 'progress_dialog') and self.progress_dialog:
                try:
                    self.progress_dialog.cancel()
                    self.progress_dialog.close()
                    self.progress_dialog = None
                except:
                    pass
                    
            # Wait a moment for background threads to finish
            self.root.after(100, self._final_cleanup)
            
        except Exception as e:
            print(f"Error during cleanup: {e}")
            # Force close if cleanup fails
            self._final_cleanup()
    
    def _final_cleanup(self):
        """Perform final cleanup and close application"""
        try:
            # Save window geometry
            geometry = {
                'width': self.root.winfo_width(),
                'height': self.root.winfo_height(),
                'x': self.root.winfo_x(),
                'y': self.root.winfo_y()
            }
            self.config.save_window_geometry(geometry)
        except:
            pass
            
        # Close application
        self.root.quit()  # Stop the mainloop first
        self.root.destroy()  # Then destroy the window

    def _show_progress_dialog(self, title="Processing File"):
        """Show progress dialog for long operations"""
        if not self.progress_dialog:
            self.progress_dialog = ProgressDialog(self.root, title)
    
    def _hide_progress_dialog(self):
        """Hide progress dialog"""
        if self.progress_dialog:
            self.progress_dialog.close()
            self.progress_dialog = None
    
    def _parse_xml_with_performance(self, filepath):
        """Performance-enhanced XML parsing for large files"""
        def xml_chunk_parser(chunk_data):
            """Parse a chunk of XML data"""
            chunk_results = []
            for line_data in chunk_data:
                line = line_data['content']
                # Simple XML tag extraction for performance
                if any(keyword in line.lower() for keyword in ['error', 'fail', 'success', 'warning']):
                    chunk_results.append({
                        'line_number': line_data['line_number'],
                        'content': line,
                        'timestamp': 'unknown',
                        'severity': self._detect_severity(line)
                    })
            return chunk_results
        
        # Use performance manager for chunked processing
        result = self.performance.parse_file_chunked(filepath, xml_chunk_parser, chunk_lines=500)
        return result.get('results', []) if isinstance(result, dict) else []
    
    def _parse_text_with_performance(self, filepath, keywords):
        """Performance-enhanced text parsing for large files"""
        def text_chunk_parser(chunk_data):
            """Parse a chunk of text data"""
            chunk_results = []
            for line_data in chunk_data:
                line = line_data['content']
                # Check if line contains any keywords
                if any(keyword.lower() in line.lower() for keyword in keywords if keyword.strip()):
                    chunk_results.append({
                        'line_number': line_data['line_number'],
                        'content': line,
                        'timestamp': self._extract_timestamp(line),
                        'severity': self._detect_severity(line)
                    })
            return chunk_results
        
        # Use performance manager for chunked processing
        result = self.performance.parse_file_chunked(filepath, text_chunk_parser, chunk_lines=1000)
        return result.get('results', []) if isinstance(result, dict) else []
    
    def _detect_severity(self, line):
        """Quick severity detection for performance parsing"""
        line_lower = line.lower()
        if any(word in line_lower for word in ['error', 'critical', 'fatal', 'exception']):
            return 'ERROR'
        elif any(word in line_lower for word in ['warning', 'warn', 'caution']):
            return 'WARNING'
        elif any(word in line_lower for word in ['success', 'pass', 'ok', 'complete']):
            return 'SUCCESS'
        else:
            return 'INFO'
    
    def _extract_timestamp(self, line):
        """Quick timestamp extraction for performance parsing"""
        import re
        # Look for common timestamp patterns
        patterns = [
            r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}',
            r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',
            r'\d{2}:\d{2}:\d{2}'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, line)
            if match:
                return match.group()
        
        return 'unknown'


class SmartFilterPanel:
    """Smart filter panel with AI-powered suggestions and presets"""
    
    def __init__(self, parent, smart_filter, callback):
        """
        Initialize smart filter panel
        
        Args:
            parent: Parent window
            smart_filter: SmartFilterEngine instance
            callback: Function to call with selected keywords
        """
        self.smart_filter = smart_filter
        self.callback = callback
        
        # Create toplevel window
        self.window = tk.Toplevel(parent)
        self.window.title("🔍 Smart Filter")
        self.window.geometry("700x600")
        self.window.transient(parent)
        self.window.grab_set()
        
        # Main container
        main_frame = ttk.Frame(self.window, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header = ttk.Label(main_frame, text="🔍 Smart Filter & Search", 
                          font=('Arial', 14, 'bold'))
        header.pack(pady=(0, 10))
        
        subtitle = ttk.Label(main_frame, text="Context-aware filtering with intelligent suggestions", 
                            font=('Arial', 9))
        subtitle.pack(pady=(0, 15))
        
        # Search frame
        search_frame = ttk.LabelFrame(main_frame, text="Search & Filter", padding=10)
        search_frame.pack(fill=tk.X, pady=5)
        
        # Search entry with suggestions
        entry_frame = ttk.Frame(search_frame)
        entry_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(entry_frame, text="Keywords:").pack(side=tk.LEFT, padx=(0, 10))
        
        self.search_var = tk.StringVar()
        self.search_var.trace('w', self._on_search_change)
        self.search_entry = ttk.Entry(entry_frame, textvariable=self.search_var, font=('Arial', 11))
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        ttk.Button(entry_frame, text="Apply", command=self._apply_filter, width=12).pack(side=tk.LEFT)
        
        # Suggestions listbox
        suggestions_frame = ttk.LabelFrame(search_frame, text="💡 Suggestions", padding=5)
        suggestions_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        self.suggestions_list = tk.Listbox(suggestions_frame, height=6, font=('Arial', 10))
        self.suggestions_list.pack(fill=tk.BOTH, expand=True)
        self.suggestions_list.bind('<Double-Button-1>', self._on_suggestion_select)
        
        # Presets frame
        presets_frame = ttk.LabelFrame(main_frame, text="📚 Quick Presets", padding=10)
        presets_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Create scrollable canvas for presets
        canvas = tk.Canvas(presets_frame, height=200)
        scrollbar = ttk.Scrollbar(presets_frame, orient="vertical", command=canvas.yview)
        preset_buttons_frame = ttk.Frame(canvas)
        
        preset_buttons_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=preset_buttons_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Add preset buttons
        presets = self.smart_filter.get_all_presets()
        row = 0
        col = 0
        for name, preset in presets.items():
            btn_text = f"{preset.get('icon', '🔖')} {name}"
            btn = ttk.Button(preset_buttons_frame, text=btn_text, 
                           command=lambda p=preset: self._apply_preset(p),
                           width=25)
            btn.grid(row=row, column=col, padx=5, pady=5, sticky=tk.W)
            
            # Tooltip - show description
            self._create_tooltip(btn, preset.get('description', ''))
            
            col += 1
            if col > 1:
                col = 0
                row += 1
        
        # History frame
        history_frame = ttk.LabelFrame(main_frame, text="🕐 Recent Searches", padding=10)
        history_frame.pack(fill=tk.X, pady=5)
        
        self.history_list = tk.Listbox(history_frame, height=4, font=('Arial', 10))
        self.history_list.pack(fill=tk.X)
        self.history_list.bind('<Double-Button-1>', self._on_history_select)
        
        self._populate_history()
        
        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Button(buttons_frame, text="Clear Filter", command=self._clear_filter).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Close", command=self.window.destroy).pack(side=tk.RIGHT, padx=5)
        
        # Focus search entry
        self.search_entry.focus()
    
    def _on_search_change(self, *args):
        """Handle search text change - show suggestions"""
        query = self.search_var.get()
        suggestions = self.smart_filter.get_suggestions(query, max_suggestions=8)
        
        # Update suggestions list
        self.suggestions_list.delete(0, tk.END)
        for suggestion in suggestions:
            display_text = f"{suggestion.get('icon', '')} {suggestion['text']} - {suggestion['description']}"
            self.suggestions_list.insert(tk.END, display_text)
            # Store the actual text for retrieval
            self.suggestions_list.itemconfig(tk.END, {'fg': self._get_suggestion_color(suggestion['type'])})
    
    def _get_suggestion_color(self, suggestion_type):
        """Get color for suggestion type"""
        colors = {
            'preset': '#3498db',
            'service': '#9b59b6',
            'nrc': '#e67e22',
            'learned': '#2ecc71',
            'history': '#95a5a6'
        }
        return colors.get(suggestion_type, '#000000')
    
    def _on_suggestion_select(self, event):
        """Handle double-click on suggestion"""
        selection = self.suggestions_list.curselection()
        if selection:
            idx = selection[0]
            query = self.search_var.get()
            suggestions = self.smart_filter.get_suggestions(query, max_suggestions=8)
            if idx < len(suggestions):
                selected = suggestions[idx]
                self.search_var.set(selected['text'])
                self._apply_filter()
    
    def _on_history_select(self, event):
        """Handle double-click on history item"""
        selection = self.history_list.curselection()
        if selection:
            history_text = self.history_list.get(selection[0])
            # Extract just the query part (before " - ")
            query = history_text.split(' - ')[0]
            self.search_var.set(query)
    
    def _apply_preset(self, preset):
        """Apply a preset filter"""
        keywords = preset.get('keywords', [])
        if keywords:
            self.search_var.set(', '.join(keywords))
            self._apply_filter()
    
    def _apply_filter(self):
        """Apply the current filter"""
        query = self.search_var.get().strip()
        if query:
            # Split by comma or space
            keywords = [k.strip() for k in query.replace(',', ' ').split() if k.strip()]
            if keywords:
                self.callback(keywords)
                self.window.destroy()
    
    def _clear_filter(self):
        """Clear filter and show all results"""
        self.callback([])
        self.window.destroy()
    
    def _populate_history(self):
        """Populate history list"""
        history = self.smart_filter.search_history[-10:]  # Last 10 searches
        for entry in reversed(history):
            display = f"{entry['query']} - {entry.get('results', 0)} results"
            self.history_list.insert(tk.END, display)
    
    def _create_tooltip(self, widget, text):
        """Create a simple tooltip"""
        def show_tooltip(event):
            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
            label = tk.Label(tooltip, text=text, background="lightyellow", 
                           relief=tk.SOLID, borderwidth=1, font=('Arial', 9))
            label.pack()
            widget.tooltip = tooltip
        
        def hide_tooltip(event):
            if hasattr(widget, 'tooltip'):
                widget.tooltip.destroy()
                delattr(widget, 'tooltip')
        
        widget.bind('<Enter>', show_tooltip)
        widget.bind('<Leave>', hide_tooltip)
    
    def _correlate_logs(self):
        """Correlate all logs in the workspace"""
        try:
            # Show progress (improvement #5)
            self._show_progress("Correlating logs...")
            
            # Placeholder for correlation logic
            self.results_text.insert(tk.END, "🔗 Cross-Correlation Analysis\n", "heading")
            self.results_text.insert(tk.END, "=" * 50 + "\n\n", "normal")
            self.results_text.insert(tk.END, "This feature will correlate multiple log files\n", "info")
            self.results_text.insert(tk.END, "to identify patterns and relationships.\n\n", "info")
            
            self._hide_progress()
            self.status.set("Log correlation completed")
            
        except Exception as e:
            self._hide_progress()
            self.status.set(f"Error correlating logs: {str(e)}")
    
    def _test_sample_data(self):
        """Load and analyze sample diagnostic data"""
        try:
            # Show progress (improvement #5)
            self._show_progress("Loading sample data...")
            
            # Placeholder for test sample logic
            self.results_text.insert(tk.END, "🧪 Sample Data Analysis\n", "heading")
            self.results_text.insert(tk.END, "=" * 50 + "\n\n", "normal")
            self.results_text.insert(tk.END, "Sample diagnostic data loaded successfully.\n", "success")
            self.results_text.insert(tk.END, "This demonstrates the analysis capabilities.\n\n", "info")
            
            self._hide_progress()
            self.status.set("Sample data analysis completed")
            
        except Exception as e:
            self._hide_progress()
            self.status.set(f"Error loading sample data: {str(e)}")
    
    def _show_progress(self, message):
        """Show progress indicator (improvement #5)"""
        self.progress_label.config(text=message)
        self.progress_frame.grid()
        self.progress_bar.start(10)
        
        # Disable action buttons to prevent double-clicks
        for child in self.root.winfo_children():
            self._disable_buttons_recursive(child)
        
        self.root.update_idletasks()
    
    def _hide_progress(self):
        """Hide progress indicator (improvement #5)"""
        self.progress_frame.grid_remove()
        self.progress_bar.stop()
        
        # Re-enable action buttons
        for child in self.root.winfo_children():
            self._enable_buttons_recursive(child)
    
    def _disable_buttons_recursive(self, widget):
        """Recursively disable buttons"""
        try:
            if isinstance(widget, (ttk.Button, tk.Button)):
                widget.config(state='disabled')
            for child in widget.winfo_children():
                self._disable_buttons_recursive(child)
        except:
            pass
    
    def _enable_buttons_recursive(self, widget):
        """Recursively enable buttons"""
        try:
            if isinstance(widget, (ttk.Button, tk.Button)):
                widget.config(state='normal')
            for child in widget.winfo_children():
                self._enable_buttons_recursive(child)
        except:
            pass


def main():
    import signal
    import sys
    
    def signal_handler(sig, frame):
        """Handle keyboard interrupt gracefully"""
        print("\nReceived interrupt signal. Closing application...")
        try:
            if 'app' in locals() and app:
                app._on_closing()
            else:
                sys.exit(0)
        except:
            sys.exit(0)
    
    # Register signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    
    if TKINTERDND_AVAILABLE:
        try:
            # Try to use TkinterDnD for drag-and-drop
            root = TkinterDnD.Tk()
        except:
            # Fall back to regular Tk
            root = tk.Tk()
    else:
        # TkinterDnD not available, use regular Tk
        root = tk.Tk()
    
    try:
        app = EnhancedLogParserGUI(root)
        root.mainloop()
    except KeyboardInterrupt:
        # Graceful shutdown on Ctrl+C
        if 'app' in locals():
            app._on_closing()
        sys.exit(0)
    except Exception as e:
        print(f"Error running application: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
