"""
Simplified Report Generator
Creates easy-to-understand summaries for beginners
Focuses on errors and successes with clear explanations
"""

from typing import List, Dict, Any
from collections import Counter
import re

try:
    from ecu_reference import get_ecu_info, explain_ecu_context, format_ecu_info, is_critical_ecu, get_did_info
    ECU_REFERENCE_AVAILABLE = True
except ImportError:
    ECU_REFERENCE_AVAILABLE = False

try:
    from module_dependency_tracker import ModuleDependencyTracker
    DEPENDENCY_TRACKER_AVAILABLE = True
except ImportError:
    DEPENDENCY_TRACKER_AVAILABLE = False


class SimplifiedReportGenerator:
    """Generates simplified, beginner-friendly reports"""
    
    # Comprehensive Ford ECU/Module Database (Official Ford Module List)
    FORD_ECU_DATABASE = {
        '7A4': {'abbr': 'AAM', 'name': 'Audio Amplifier Module', 'critical': False},
        '760': {'abbr': 'ABS', 'name': 'Anti-Lock Brake System (ABS) Control Module', 'critical': True},
        '7F2': {'abbr': 'ABSB', 'name': 'Anti-Lock Brake System (ABS) Control Module "B"', 'critical': True},
        '7C7': {'abbr': 'ACCM', 'name': 'Air Conditioning Control Module', 'critical': False},
        '6E0': {'abbr': 'ACCMB', 'name': 'Air Conditioning Control Module "B"', 'critical': False},
        '727': {'abbr': 'ACM', 'name': 'Audio Front Control Module', 'critical': False},
        '7D0': {'abbr': 'APIM', 'name': 'Accessory Protocol Interface Module', 'critical': True},
        '792': {'abbr': 'ATCM', 'name': 'All Terrain Control Module', 'critical': False},
        '703': {'abbr': 'AWD', 'name': 'All Wheel Drive', 'critical': False},
        '726': {'abbr': 'BCM', 'name': 'Body Control Module', 'critical': True},
        '6F0': {'abbr': 'BCMC (BJB)', 'name': 'Body Control Module C / Battery Junction Box', 'critical': True},
        '7E4': {'abbr': 'BECM', 'name': 'Battery Energy Control Module', 'critical': True},
        '723': {'abbr': 'BECMB', 'name': 'Battery Energy Control Module B', 'critical': True},
        '764': {'abbr': 'CCM', 'name': 'Cruise Control Module', 'critical': False},
        '7C1': {'abbr': 'CMR', 'name': 'Camera Module Rear (Driver Status Monitor Camera Module)', 'critical': False},
        '6F1': {'abbr': 'DCACA', 'name': 'Direct Current / Alternating Current Convertor Module A', 'critical': True},
        '746': {'abbr': 'DCDC', 'name': 'Direct Current / Direct Current Convertor Control Module', 'critical': True},
        '7A2': {'abbr': 'DCME', 'name': 'Door Control Module E', 'critical': False},
        '762': {'abbr': 'DCMF', 'name': 'Door Control Module F', 'critical': False},
        '7B3': {'abbr': 'DCMG', 'name': 'Door Control Module G', 'critical': False},
        '7B4': {'abbr': 'DCMH', 'name': 'Door Control Module H', 'critical': False},
        '795': {'abbr': 'DCMR', 'name': 'Differential Control Module Rear', 'critical': False},
        '740': {'abbr': 'DDM', 'name': 'Driver Door Module', 'critical': False},
        '744': {'abbr': 'DSM / RBM', 'name': 'Driver Front Seat Module / Running Board Control Module', 'critical': False},
        '783': {'abbr': 'DSP', 'name': 'Audio Digital Signal Processing Module', 'critical': False},
        '7A7': {'abbr': 'FCIM', 'name': 'Front Control Interface Module', 'critical': False},
        '7A1': {'abbr': 'GFM', 'name': 'Generic Function Module (Front Trunk Release Module(FTRM))', 'critical': False},
        '732': {'abbr': 'GSM', 'name': 'Gear Shift Module', 'critical': False},
        '716': {'abbr': 'GWM', 'name': 'Gateway Module A', 'critical': True},
        '734': {'abbr': 'HCM', 'name': 'Headlamp Control Module', 'critical': False},
        '7B2': {'abbr': 'HUD', 'name': 'Heads Up Display Module', 'critical': False},
        '733': {'abbr': 'HVAC', 'name': 'Heating, Ventilation, and Air Conditioning Module', 'critical': False},
        '720': {'abbr': 'IPC', 'name': 'Instrument Panel Cluster', 'critical': True},
        '706': {'abbr': 'IPMA', 'name': 'Image Processing Module A', 'critical': False},
        '7B1': {'abbr': 'IPMB', 'name': 'Image Processing Module B', 'critical': False},
        '6F6': {'abbr': 'LDCMA', 'name': 'Lighting Driver Control Module A', 'critical': False},
        '6F7': {'abbr': 'LDCMB', 'name': 'Lighting Driver Control Module B', 'critical': False},
        '6F5': {'abbr': 'OBCC', 'name': 'Off-Board Charger Controller', 'critical': True},
        '765': {'abbr': 'OCS', 'name': 'Occupant Classification System Module', 'critical': True},
        '750': {'abbr': 'PACM', 'name': 'Pedestrian Alert Control Module', 'critical': False},
        '736': {'abbr': 'PAM', 'name': 'Parking Assist Control Module', 'critical': False},
        '7E0': {'abbr': 'PCM', 'name': 'Powertrain Control Module', 'critical': True},
        '741': {'abbr': 'PDM', 'name': 'Passenger Door Module', 'critical': False},
        '730': {'abbr': 'PSCM', 'name': 'Power Steering Control Module', 'critical': True},
        '774': {'abbr': 'RACM', 'name': 'Rear Audio Control Module', 'critical': False},
        '766': {'abbr': 'RBM', 'name': 'Running Board Control Module', 'critical': False},
        '737': {'abbr': 'RCM', 'name': 'Restraints Control Module', 'critical': True},
        '731': {'abbr': 'RFA', 'name': 'Remote Function Actuator', 'critical': False},
        '775': {'abbr': 'RGTM', 'name': 'Rear Gate Trunk Module', 'critical': False},
        '751': {'abbr': 'RTM', 'name': 'Radio Transceiver Module', 'critical': False},
        '797': {'abbr': 'SASM', 'name': 'Steering Angle Sensor Module', 'critical': True},
        '724': {'abbr': 'SCCM', 'name': 'Steering Column Control Module', 'critical': False},
        '7A3': {'abbr': 'SCMB', 'name': 'Passenger Front Seat Module', 'critical': False},
        '702': {'abbr': 'SCMC', 'name': 'Seat Control Module C', 'critical': False},
        '763': {'abbr': 'SCMD', 'name': 'Seat Control Module D', 'critical': False},
        '776': {'abbr': 'SCME', 'name': 'Front Seat Climate Control Module', 'critical': False},
        '777': {'abbr': 'SCMF', 'name': 'Rear Seat Climate Control Module', 'critical': False},
        '712': {'abbr': 'SCMG', 'name': 'Driver Multi-Contour Seat Module', 'critical': False},
        '713': {'abbr': 'SCMH', 'name': 'Passenger Multi-Contour Seat Module', 'critical': False},
        '787': {'abbr': 'SCMJ', 'name': 'Seat Control Module J', 'critical': False},
        '7C5': {'abbr': 'SECM', 'name': 'Steering Effort Control Module', 'critical': False},
        '7E2': {'abbr': 'SOBDM', 'name': 'Secondary On-Board Diagnostic Control Module A', 'critical': False},
        '7E7': {'abbr': 'SOBDMB', 'name': 'Secondary On-Board Diagnostic Control Module B', 'critical': False},
        '7E6': {'abbr': 'SOBDMC', 'name': 'Secondary On-Board Diagnostic Control Module C', 'critical': False},
        '6F2': {'abbr': 'SODCMC', 'name': 'Side Obstacle Detection Control Module C', 'critical': False},
        '6F3': {'abbr': 'SODCMD', 'name': 'Side Obstacle Detection Control Module D', 'critical': False},
        '7C4': {'abbr': 'SODL', 'name': 'Side Obstacle Detection Control Module LH', 'critical': False},
        '7C6': {'abbr': 'SODR', 'name': 'Side Obstacle Detection Control Module RH', 'critical': False},
        '761': {'abbr': 'TCCM', 'name': 'Transfer Case Control Module', 'critical': False},
        '7E9': {'abbr': 'TCM', 'name': 'Transmission Control Module', 'critical': True},
        '754': {'abbr': 'TCU', 'name': 'Telematic Control Unit Module', 'critical': False},
        '791': {'abbr': 'TRM / TBM', 'name': 'Trailer Relay Module / Trailer Brake Control Module', 'critical': False},
        '721': {'abbr': 'VDM', 'name': 'Vehicle Dynamics Control Module', 'critical': False},
        '725': {'abbr': 'WACM', 'name': 'Wireless Accessory Charging Module', 'critical': False},
    }
    
    # Quick lookup set for valid ECU addresses
    VALID_ECU_ADDRESSES = set(FORD_ECU_DATABASE.keys())
    
    # Important DIDs that should always be reported
    IMPORTANT_DIDS = {
        '8033': 'Part Number',
        '8060': 'Diagnostic Specification Version',
        '8061': 'ECU Serial Number Component',
        '8068': 'Vehicle Manufacturer Specific Info',
        '8071': 'Software Version',
        'D027': 'Diagnostic Variant Code',
        'DE01': 'ECU Hardware Number',
        'DE02': 'ECU Hardware Version',
        'F10A': 'ECU Calibration ID',
        'F110': 'Vehicle Speed',
        'F111': 'Engine Speed (RPM)',
        'DE13': 'Diagnostic Address',
        'F124': 'System Supplier Code',
        'F129': 'ECU Software Calibration ID',
        'F12A': 'ECU Calibration Verification Number',
        'F142': 'Boot Software ID',
        'F143': 'Boot Software Finger Print',
        'F145': 'Boot Software Build Date',
        'F17F': 'ODX File Version',
        'F188': 'Vehicle Manufacturer ECU Software Number',
        'F18C': 'ECU Serial Number',
        'F1D0': 'Vehicle Configuration',
        'F1D1': 'Vehicle Configuration Status',
        'F190': 'VIN (Vehicle Identification Number)',
        'F195': 'ECU Software Version Number',
    }
    
    def __init__(self):
        self.results = []
        self.dependency_tracker = ModuleDependencyTracker() if DEPENDENCY_TRACKER_AVAILABLE else None
        self.primary_module = None  # Will be detected
        self.secondary_modules = []  # Supporting modules
        
        # Import advanced root cause analyzer
        try:
            from root_cause_analyzer import RootCauseAnalyzer
            self.root_cause_analyzer = RootCauseAnalyzer()
            self.rca_available = True
        except ImportError:
            self.root_cause_analyzer = None
            self.rca_available = False
    
    def generate_simple_report(self, results: List[Dict[str, Any]], file_type: str, fdrs_analysis: Dict[str, Any] = None, manual_primary_module: str = None) -> str:
        """
        Generate a simplified, easy-to-understand report
        
        Args:
            results: Parsed log results
            file_type: 'xml' or 'text'
            fdrs_analysis: Optional FDRS analysis data for more accurate module detection
            manual_primary_module: Optional manual override for primary module (e.g., "716" for GWM)
        
        Returns:
            Simplified report as string
        """
        if not results:
            return "✓ No errors or issues found in the log!\n\nThis is good - everything looks clean."
        
        # Apply manual override if provided
        if manual_primary_module:
            self._apply_manual_primary_module(manual_primary_module, results)
            print(f"🎯 MANUAL OVERRIDE: Primary module set to {manual_primary_module}")
        elif fdrs_analysis and fdrs_analysis.get('diagnostic_services'):
            # Use FDRS analysis for module detection if available
            self._detect_modules_from_fdrs(fdrs_analysis)
        else:
            # Fallback to standard enhanced detection
            self._detect_modules(results)
        
        report_lines = []
        
        # Header
        report_lines.append("="*80)
        report_lines.append("📊 LOG ANALYSIS REPORT - SIMPLIFIED VIEW")
        report_lines.append("="*80)
        report_lines.append("")
        
        # Module Context (PRIMARY vs SECONDARY)
        if self.primary_module:
            report_lines.append("🎯 PRIMARY MODULE")
            report_lines.append("-"*80)
            report_lines.append(f"   {self.primary_module['name']} ({self.primary_module['id']})")
            report_lines.append(f"   → {self.primary_module['description']}")
            report_lines.append("")
            
            if self.secondary_modules:
                report_lines.append("🔗 SUPPORTING MODULES (Secondary Communications)")
                report_lines.append("-"*80)
                for sec_mod in self.secondary_modules[:5]:  # Top 5
                    status_icon = "✅" if sec_mod.get('success', False) else "❌"
                    report_lines.append(f"   {status_icon} {sec_mod['name']} ({sec_mod['id']})")
                report_lines.append("")
        
        # Quick Summary
        summary = self._generate_summary(results)
        report_lines.append("📈 QUICK SUMMARY")
        report_lines.append("-"*80)
        report_lines.append(f"Total Items Found: {summary['total']}")
        report_lines.append(f"✗ Errors/Failures: {summary['errors']} {self._get_status_emoji(summary['errors'])}")
        report_lines.append(f"✓ Success/Pass: {summary['successes']} {self._get_status_emoji(summary['successes'], is_success=True)}")
        report_lines.append(f"⚠ Warnings: {summary['warnings']}")
        report_lines.append("")
        
        # Overall Status
        report_lines.append("🎯 OVERALL STATUS")
        report_lines.append("-"*80)
        status_msg = self._get_overall_status(summary)
        report_lines.append(status_msg)
        report_lines.append("")
        
        # Root Cause Analysis - Most Likely Issue & Proximate Cause
        if summary['errors'] > 0:
            root_cause = self._analyze_root_cause(results)
            report_lines.append("🔍 ROOT CAUSE ANALYSIS")
            report_lines.append("="*80)
            report_lines.append("")
            
            # Show confidence if available
            if 'confidence' in root_cause:
                confidence_pct = root_cause['confidence'] * 100
                confidence_bar = "█" * int(confidence_pct / 10) + "░" * (10 - int(confidence_pct / 10))
                report_lines.append(f"📊 Analysis Confidence: {confidence_bar} {confidence_pct:.0f}%")
                report_lines.append("")
            
            report_lines.append(f"🎯 MOST LIKELY ISSUE:")
            report_lines.append(f"   {root_cause['most_likely_issue']}")
            report_lines.append("")
            report_lines.append(f"📍 PROXIMATE CAUSE:")
            report_lines.append(f"   {root_cause['proximate_cause']}")
            report_lines.append("")
            report_lines.append(f"💡 RECOMMENDED ACTION:")
            for line in root_cause['recommended_action'].split('\n'):
                report_lines.append(f"   {line}")
            report_lines.append("")
            if root_cause.get('affected_systems'):
                report_lines.append(f"⚠️  AFFECTED SYSTEMS:")
                for system in root_cause['affected_systems']:
                    report_lines.append(f"   • {system}")
                report_lines.append("")
            report_lines.append("="*80)
            report_lines.append("")
        
        # Top Issues (Errors only)
        errors = [r for r in results if self._is_error(r)]
        if errors:
            report_lines.append("="*80)
            report_lines.append("❌ ERRORS & FAILURES (What Went Wrong)")
            report_lines.append("="*80)
            report_lines.append("")
            
            for i, error in enumerate(errors[:10], 1):  # Show max 10 errors
                report_lines.extend(self._format_error(error, i, file_type))
                report_lines.append("")
            
            if len(errors) > 10:
                report_lines.append(f"... and {len(errors) - 10} more errors (see detailed export)")
                report_lines.append("")
        
        # Successes (Brief)
        successes = [r for r in results if self._is_success(r)]
        if successes:
            report_lines.append("="*80)
            report_lines.append("✅ SUCCESSES (What Worked)")
            report_lines.append("="*80)
            report_lines.append("")
            report_lines.append(f"Total Successful Operations: {len(successes)}")
            report_lines.append("")
            
            # Show first few successes
            for i, success in enumerate(successes[:3], 1):
                report_lines.extend(self._format_success(success, i, file_type))
                report_lines.append("")
            
            if len(successes) > 3:
                report_lines.append(f"✓ ... and {len(successes) - 3} more successful operations")
                report_lines.append("")
        
        # NRC Code Summary (if any) - EMPHASIZED for visibility
        nrc_summary = self._summarize_nrc_codes(results)
        if nrc_summary:
            report_lines.append("="*80)
            report_lines.append("� NEGATIVE RESPONSE CODES (NRC) - CRITICAL DIAGNOSTIC INFO")
            report_lines.append("="*80)
            report_lines.append("")
            report_lines.append("⚠️  These codes indicate specific problems detected by the vehicle module.")
            report_lines.append("   Pay close attention to these - they explain WHY operations failed.")
            report_lines.append("")
            
            # Sort by count (most frequent first) for emphasis
            sorted_nrcs = sorted(nrc_summary.items(), key=lambda x: x[1]['count'], reverse=True)
            
            for nrc_code, info in sorted_nrcs:
                # Visual separator for each NRC
                report_lines.append("─"*80)
                report_lines.append(f"🔍 NRC Code: 0x{nrc_code} ({nrc_code})")
                report_lines.append(f"   Technical: {info['explanation']}")
                report_lines.append(f"   Occurrences: {info['count']} time(s) {'⚠️⚠️⚠️' if info['count'] > 5 else '⚠️⚠️' if info['count'] > 2 else '⚠️'}")
                report_lines.append("")
                report_lines.append("   � What This Means in Plain English:")
                # Indent the simple explanation
                simple_text = self._explain_nrc_simply(nrc_code)
                for line in simple_text.split('\n'):
                    report_lines.append(f"      {line}")
                report_lines.append("")
            report_lines.append("="*80)
            report_lines.append("")
        
        # Module Dependency Analysis (if available and relevant)
        if self.dependency_tracker and (summary['errors'] > 0 or self._has_programming_content(results)):
            dependency_report = self.dependency_tracker.parse_log_for_dependencies(results)
            if dependency_report['summary']['total_modules_involved'] > 0:
                report_lines.append("="*80)
                report_lines.append("🔗 MODULE DEPENDENCIES & COMMUNICATION")
                report_lines.append("="*80)
                report_lines.append("")
                dependency_text = self.dependency_tracker.format_dependency_report_text(dependency_report)
                # Add the dependency report (skip header since we already added it)
                dep_lines = dependency_text.split('\n')
                # Skip the first few header lines and use our own
                for line in dep_lines[4:]:
                    report_lines.append(line)
                report_lines.append("")
        
        # Action Items
        report_lines.append("="*80)
        report_lines.append("📋 RECOMMENDED ACTIONS")
        report_lines.append("="*80)
        report_lines.append("")
        actions = self._generate_action_items(results, summary)
        for action in actions:
            report_lines.append(f"• {action}")
        report_lines.append("")
        
        # Footer
        report_lines.append("="*80)
        report_lines.append("ℹ️  TIP: For full technical details, use 'Expert Mode' or export to JSON")
        report_lines.append("="*80)
        
        return "\n".join(report_lines)
    
    def _is_likely_ecu_address(self, hex_value: str) -> bool:
        """
        Determine if a 3-char hex value is likely an ECU address vs. a DID
        
        ECU addresses typically:
        - Start with 7 (e.g., 7E0, 7D0, 732, 760)
        - Are in specific ranges for OBD-II/UDS
        - Have known ECU reference info
        
        DIDs typically:
        - Are any hex value used for data requests
        - Often lower values (206, 237, etc.)
        """
        hex_upper = hex_value.upper()
        
        # Use whitelist approach: ONLY accept known valid Ford ECU addresses
        if hex_upper in self.VALID_ECU_ADDRESSES:
            return True
        
        # Check if it's in our ECU reference database as backup
        if ECU_REFERENCE_AVAILABLE:
            info = get_ecu_info(hex_upper)
            if info:
                return True
        
        # Everything else is NOT an ECU address (including all DIDs)
        return False
    
    def _detect_modules_from_fdrs(self, fdrs_analysis: Dict[str, Any]):
        """Detect modules using FDRS analysis data for more accurate results"""
        # Extract target ECU from FDRS diagnostic services
        primary_candidates = []
        
        diagnostic_services = fdrs_analysis.get('diagnostic_services', [])
        for service in diagnostic_services:
            # FDRS logs have accurate ECU address extraction
            ecu_addresses = re.findall(r'\b([0-9A-Fa-f]{3})\b', str(service))
            for ecu in ecu_addresses:
                if self._is_likely_ecu_address(ecu):
                    primary_candidates.append(ecu.upper())
        
        # Also check FDRS system info for target node
        system_info = fdrs_analysis.get('system_info', {})
        if system_info:
            # Look for node references in system info
            info_text = str(system_info)
            ecu_addresses = re.findall(r'\b([0-9A-Fa-f]{3})\b', info_text)
            for ecu in ecu_addresses:
                if self._is_likely_ecu_address(ecu):
                    primary_candidates.append(ecu.upper())
        
        if primary_candidates:
            # Use most common ECU from FDRS analysis
            primary_id = Counter(primary_candidates).most_common(1)[0][0]
            
            # Get ECU information
            if ECU_REFERENCE_AVAILABLE:
                from ecu_reference import get_ecu_info
                ecu_info = get_ecu_info(primary_id)
                if ecu_info:
                    self.primary_module = {
                        'id': primary_id,
                        'name': f"{ecu_info['acronym']} - {ecu_info['name']}",
                        'description': self._get_ecu_description(ecu_info['acronym']),
                        'is_critical': ecu_info.get('critical', False)
                    }
                else:
                    self.primary_module = {
                        'id': primary_id,
                        'name': f'Module {primary_id}',
                        'description': 'Primary target module from FDRS analysis',
                        'is_critical': False
                    }
            else:
                self.primary_module = {
                    'id': primary_id,
                    'name': f'Module {primary_id}',
                    'description': 'Primary target module from FDRS analysis',
                    'is_critical': False
                }
        else:
            # Fallback to None
            self.primary_module = None
        
        # Set secondary modules as empty for FDRS (focus on primary)
        self.secondary_modules = []

    def _get_ecu_description(self, acronym: str) -> str:
        """Get user-friendly description for ECU acronym"""
        descriptions = {
            "APIM": "Controls the infotainment system (SYNC). Critical for media, navigation, and vehicle settings.",
            "GWM": "Gateway for network communication between modules.",
            "BCM": "Controls body functions like lights, locks, wipers. Central to vehicle operation.",
            "PCM": "Controls the engine and transmission. Critical for vehicle performance.",
            "IPC": "The dashboard display showing speed, fuel, warnings, etc. Critical for driver information.",
            "TCM": "Controls transmission shifting. Critical for vehicle drivability.",
            "ABS": "Prevents wheel lockup during braking. Critical safety system.",
            "RCM": "Controls airbags and safety restraints. Critical safety system.",
        }
        return descriptions.get(acronym, f"Electronic control module for {acronym} functions.")

    def _detect_modules(self, results: List[Dict[str, Any]]):
        """Detect primary and secondary modules from log results with enhanced GWM detection"""
        module_counts = Counter()
        module_contexts = {}
        module_success = {}
        module_activities = {}  # Track types of activities per module
        
        # Count module mentions and track context
        for result in results:
            text = str(result).lower()
            original_text = str(result)  # Keep original for case-sensitive checks
            
            # Extract ECU addresses (3-char hex)
            ecu_addresses = re.findall(r'\b([0-9A-Fa-f]{3})\b', original_text)
            
            for ecu in ecu_addresses:
                # Filter out DIDs - only keep actual ECU addresses
                if not self._is_likely_ecu_address(ecu):
                    continue
                
                # Skip if context indicates it's a DID
                if re.search(r'(?:DID|did)\s*(?:0x)?' + ecu, original_text):
                    continue
                ecu_upper = ecu.upper()
                module_counts[ecu_upper] += 1
                
                # Track success status
                if ecu_upper not in module_success:
                    module_success[ecu_upper] = {'success': 0, 'fail': 0}
                
                if 'success' in text or 'pass' in text:
                    module_success[ecu_upper]['success'] += 1
                elif 'error' in text or 'fail' in text:
                    module_success[ecu_upper]['fail'] += 1
                
                # Track activity types for better primary module detection
                if ecu_upper not in module_activities:
                    module_activities[ecu_upper] = {
                        'programming': 0,
                        'security': 0,
                        'diagnostic': 0,
                        'communication': 0,
                        'dtc': 0
                    }
                
                # Analyze activity type
                if any(kw in text for kw in ['program', 'flash', 'update', 'download', 'transfer', 'upload']):
                    module_activities[ecu_upper]['programming'] += 1
                elif any(kw in text for kw in ['security', 'seed', 'key', 'access']):
                    module_activities[ecu_upper]['security'] += 1
                elif any(kw in text for kw in ['dtc', 'diagnostic trouble', 'error code']):
                    module_activities[ecu_upper]['dtc'] += 1
                elif any(kw in text for kw in ['session', 'tester present', 'communication']):
                    module_activities[ecu_upper]['communication'] += 1
                else:
                    module_activities[ecu_upper]['diagnostic'] += 1
                
                # Get module info
                if ECU_REFERENCE_AVAILABLE and ecu_upper not in module_contexts:
                    info = get_ecu_info(ecu_upper)
                    if info:
                        module_contexts[ecu_upper] = {
                            'id': ecu_upper,
                            'name': format_ecu_info(ecu_upper),
                            'description': explain_ecu_context(ecu_upper),
                            'is_critical': is_critical_ecu(ecu_upper)
                        }
        
        # Determine primary module with enhanced logic
        primary_id = None
        
        if module_counts:
            # PRIORITY 1: Look for explicit "Requested node" indicator (most reliable)
            primary_candidates = []
            for result in results:
                # Get the actual text content from the result
                if isinstance(result, dict):
                    original_text = result.get('line', result.get('text', str(result)))
                else:
                    original_text = str(result)
                
                # Look for "Requested node(0) = XXX" pattern (case insensitive)
                requested_match = re.search(r'(?:LOG>>)?\s*Requested\s+node\s*\(\d+\)\s*=\s*([0-9A-Fa-f]{3})', 
                                           original_text, re.IGNORECASE)
                if requested_match:
                    primary_candidates.append(requested_match.group(1).upper())
            
            if primary_candidates:
                # Use most common from "Requested node" lines (should be consistent)
                primary_id = Counter(primary_candidates).most_common(1)[0][0]
                print(f"✅ Primary module detected from 'Requested node': {primary_id}")
            
            # PRIORITY 2: Look for programming/update keywords to identify primary
            if not primary_id:
                programming_candidates = []
                for result in results:
                    text = str(result).lower()
                    original_text = str(result)
                    if any(kw in text for kw in ['program', 'flash', 'update', 'download', 'transfer']):
                        # Extract ECUs from programming operations
                        ecus = re.findall(r'\b([0-9A-Fa-f]{3})\b', original_text)
                        # FILTER: Only add valid ECU addresses, not DIDs
                        for ecu in ecus:
                            if self._is_likely_ecu_address(ecu):
                                programming_candidates.append(ecu.upper())
                
                if programming_candidates:
                    # Most common in programming operations
                    primary_id = Counter(programming_candidates).most_common(1)[0][0]
                    print(f"✅ Primary module detected from programming operations: {primary_id}")
            
            # PRIORITY 3: Enhanced heuristic analysis for primary module detection
            if not primary_id:
                # Score each module based on multiple factors
                module_scores = {}
                
                for ecu_id, count in module_counts.items():
                    score = 0
                    activities = module_activities.get(ecu_id, {})
                    
                    # Base score from communication frequency
                    score += count * 1
                    
                    # Bonus for programming activities (strong indicator of primary)
                    score += activities.get('programming', 0) * 10
                    
                    # Bonus for security activities (often primary module)
                    score += activities.get('security', 0) * 5
                    
                    # Bonus for DTC operations (primary modules often read DTCs)
                    score += activities.get('dtc', 0) * 3
                    
                    # Special handling for GWM (716) - Gateway modules are often primary
                    if ecu_id == '716':
                        score += 20  # Significant bonus for GWM detection
                        print(f"🔍 GWM (716) detected with enhanced scoring: base_count={count}, activities={activities}")
                    
                    # Bonus for critical ECUs
                    if ecu_id in module_contexts and module_contexts[ecu_id].get('is_critical', False):
                        score += 5
                    
                    # Penalty for modules with high failure rate
                    success_info = module_success.get(ecu_id, {'success': 0, 'fail': 0})
                    total_attempts = success_info['success'] + success_info['fail']
                    if total_attempts > 0:
                        failure_rate = success_info['fail'] / total_attempts
                        if failure_rate > 0.5:  # More than 50% failures
                            score -= 5
                    
                    module_scores[ecu_id] = score
                
                # Select highest scoring module as primary
                if module_scores:
                    primary_id = max(module_scores, key=module_scores.get)
                    print(f"✅ Primary module detected from enhanced scoring: {primary_id} (score: {module_scores[primary_id]})")
                    
                    # Debug: Show all module scores
                    print("📊 Module scoring details:")
                    for ecu_id, score in sorted(module_scores.items(), key=lambda x: x[1], reverse=True):
                        activities = module_activities.get(ecu_id, {})
                        print(f"   • {ecu_id}: {score} points (comm: {module_counts[ecu_id]}, prog: {activities.get('programming', 0)}, sec: {activities.get('security', 0)})")
            
            # PRIORITY 4: Fallback to most mentioned module
            if not primary_id:
                primary_id = module_counts.most_common(1)[0][0]
                print(f"⚠️  Primary module fallback to most mentioned: {primary_id}")
            
            # Set primary module info
            if primary_id in module_contexts:
                self.primary_module = module_contexts[primary_id]
            else:
                # Create basic info for modules not in reference
                module_name = self._get_basic_module_name(primary_id)
                self.primary_module = {
                    'id': primary_id,
                    'name': module_name,
                    'description': self._get_basic_module_description(primary_id),
                    'is_critical': primary_id in ['7D0', '716', '720', '726', '7E0']  # Common critical modules
                }
            
            print(f"🎯 FINAL PRIMARY MODULE: {self.primary_module['name']} ({primary_id})")
            
            # Secondary modules are others
            self.secondary_modules = []
            for ecu_id, count in module_counts.most_common():
                if ecu_id != primary_id:
                    module_info = module_contexts.get(ecu_id, {
                        'id': ecu_id,
                        'name': self._get_basic_module_name(ecu_id),
                        'description': self._get_basic_module_description(ecu_id)
                    })
                    # Add success status
                    success_total = module_success[ecu_id]['success']
                    fail_total = module_success[ecu_id]['fail']
                    module_info['success'] = success_total > fail_total
                    module_info['communications'] = count
                    self.secondary_modules.append(module_info)
        else:
            # No modules detected
            self.primary_module = None
            self.secondary_modules = []
            print("⚠️  No ECU modules detected in log data")
    
    def _get_basic_module_name(self, ecu_id: str) -> str:
        """Get basic module name for ECUs not in reference database"""
        # Known Ford module mappings
        basic_names = {
            '716': 'GWM - Gateway Module A',
            '7D0': 'APIM - Audio/Video Module', 
            '720': 'IPC - Instrument Panel Cluster',
            '726': 'BCM - Body Control Module',
            '7E0': 'PCM - Powertrain Control Module',
            '754': 'TCM - Transmission Control Module',
            '732': 'GSM - Gateway Support Module',
            '7E2': 'SOBDM - Side Obstacle Detection Module',
            '7E6': 'SOBDMC - Side Obstacle Detection Module C',
            '7E7': 'SOBDMB - Side Obstacle Detection Module B'
        }
        return basic_names.get(ecu_id, f'Module {ecu_id}')
    
    def _get_basic_module_description(self, ecu_id: str) -> str:
        """Get basic description for ECUs not in reference database"""
        descriptions = {
            '716': 'Gateway for network communication between modules.',
            '7D0': 'Controls the infotainment system (SYNC). Critical for media, navigation, and vehicle settings.',
            '720': 'The dashboard display showing speed, fuel, warnings, etc. Critical for driver information.',
            '726': 'Controls body functions like lights, locks, wipers. Central to vehicle operation.',
            '7E0': 'Controls the engine and transmission. Critical for vehicle performance.',
            '754': 'Controls transmission shifting. Critical for vehicle drivability.',
            '732': 'Provides gateway support functions for network communication.',
            '7E2': 'Detects obstacles on the side of the vehicle for safety.',
            '7E6': 'Side obstacle detection system component C.',
            '7E7': 'Side obstacle detection system component B.'
        }
        return descriptions.get(ecu_id, f'Electronic control module for {ecu_id} functions.')
    
    def _apply_manual_primary_module(self, module_id: str, results: List[Dict[str, Any]]):
        """Apply manual override for primary module detection"""
        module_id = module_id.upper()
        
        # Validate that the module exists in the log data
        module_found = False
        for result in results:
            text = str(result)
            if re.search(rf'\b{module_id}\b', text):
                module_found = True
                break
        
        if not module_found:
            print(f"⚠️  Warning: Module {module_id} not found in log data, but setting as primary anyway")
        
        # Set as primary module
        module_name = self._get_basic_module_name(module_id)
        self.primary_module = {
            'id': module_id,
            'name': module_name,
            'description': self._get_basic_module_description(module_id),
            'is_critical': module_id in ['7D0', '716', '720', '726', '7E0'],
            'manual_override': True
        }
        
        # Get ECU info if available
        if ECU_REFERENCE_AVAILABLE:
            try:
                info = get_ecu_info(module_id)
                if info:
                    self.primary_module.update({
                        'name': format_ecu_info(module_id),
                        'description': explain_ecu_context(module_id),
                        'is_critical': is_critical_ecu(module_id)
                    })
            except:
                pass  # Use basic info if ECU reference fails
        
        # Clear secondary modules for now (will be set later if needed)
        self.secondary_modules = []
        
        print(f"✅ Manual override applied: {self.primary_module['name']} ({module_id})")
    
    def _is_important_did(self, did: str) -> bool:
        """Check if a DID is in the important list"""
        did_upper = did.upper().replace('0X', '').replace('X', '')
        return did_upper in self.IMPORTANT_DIDS
    
    def _get_did_description(self, did: str) -> str:
        """Get description for important DID"""
        did_upper = did.upper().replace('0X', '').replace('X', '')
        return self.IMPORTANT_DIDS.get(did_upper, 'Unknown DID')
    
    def _filter_important_dids(self, text: str) -> List[Dict[str, str]]:
        """Extract only important DIDs from text"""
        # Find all DID patterns
        did_patterns = re.findall(r'(?:DID|did)\s*(?:0x)?([0-9A-Fa-f]{4})', text)
        
        important_dids = []
        for did in did_patterns:
            if self._is_important_did(did):
                important_dids.append({
                    'did': did.upper(),
                    'description': self._get_did_description(did)
                })
        
        return important_dids
    
    def _generate_summary(self, results: List[Dict[str, Any]]) -> Dict[str, int]:
        """Generate summary statistics"""
        summary = {
            'total': len(results),
            'errors': 0,
            'successes': 0,
            'warnings': 0
        }
        
        for result in results:
            if self._is_error(result):
                summary['errors'] += 1
            elif self._is_success(result):
                summary['successes'] += 1
            elif self._is_warning(result):
                summary['warnings'] += 1
        
        return summary
    
    def _is_error(self, result: Dict[str, Any]) -> bool:
        """Check if result is an error"""
        result_str = str(result).lower()
        severity = result.get('severity', '').upper()
        
        return (
            'error' in result_str or 
            'fail' in result_str or 
            severity in ['ERROR', 'CRITICAL', 'FATAL', 'FAILURE']
        )
    
    def _is_success(self, result: Dict[str, Any]) -> bool:
        """Check if result is a success - improved logic to exclude false positives"""
        result_str = str(result).lower()
        severity = result.get('severity', '').upper()
        
        # First check for error indicators - these disqualify success
        error_indicators = [
            'error', 'fail', 'exception', 'not successful', 
            'unsuccessful', 'abort', 'timeout', 'invalid',
            'denied', 'reject', 'refuse'
        ]
        
        # If any error indicators are present, it's not a success
        if any(indicator in result_str for indicator in error_indicators):
            return False
        
        # If severity indicates error/failure, not a success
        if severity in ['ERROR', 'CRITICAL', 'FATAL', 'FAILURE', 'FAIL']:
            return False
        
        # Now check for positive success indicators
        success_indicators = [
            'success', 'pass', 'complete', 'ok', 'good', 
            'valid', 'accept', 'approved'
        ]
        
        return (
            any(indicator in result_str for indicator in success_indicators) or 
            severity in ['SUCCESS', 'PASS', 'OK', 'GOOD']
        )
    
    def _is_warning(self, result: Dict[str, Any]) -> bool:
        """Check if result is a warning"""
        severity = result.get('severity', '').upper()
        return severity in ['WARNING', 'WARN']
    
    def _has_programming_content(self, results: List[Dict[str, Any]]) -> bool:
        """Check if results contain programming/update related content"""
        programming_keywords = ['program', 'flash', 'update', 'download', 'upload', 'transfer', 
                               'reprogramming', 'software', 'firmware']
        
        for result in results:
            text = str(result).lower()
            if any(keyword in text for keyword in programming_keywords):
                return True
        return False
    
    def _get_status_emoji(self, count: int, is_success: bool = False) -> str:
        """Get emoji based on count"""
        if is_success:
            if count > 10:
                return "🎉"
            elif count > 5:
                return "😊"
            elif count > 0:
                return "👍"
            else:
                return ""
        else:
            if count > 10:
                return "🔴 CRITICAL"
            elif count > 5:
                return "⚠️ HIGH"
            elif count > 0:
                return "⚡"
            else:
                return "✓"
    
    def _get_overall_status(self, summary: Dict[str, int]) -> str:
        """Generate overall status message"""
        if summary['errors'] == 0:
            return "✅ GOOD - No errors detected! Everything appears to be working correctly."
        elif summary['errors'] < 3:
            return "⚠️ MINOR ISSUES - A few errors were found. Review them below to see if action is needed."
        elif summary['errors'] < 10:
            return "⚠️ MODERATE ISSUES - Several errors detected. Investigation recommended."
        else:
            return "❌ SIGNIFICANT ISSUES - Many errors found. Immediate attention recommended."
    
    def _format_error(self, error: Dict[str, Any], index: int, file_type: str) -> List[str]:
        """Format error in simple terms with module context"""
        lines = []
        
        # Check if this is an NRC error for special emphasis
        has_nrc = error.get('nrc_explanations') is not None
        
        if has_nrc:
            lines.append(f"⚠️  NRC ERROR #{index} ⚠️")
            lines.append("="*40)
        else:
            lines.append(f"Error #{index}")
            lines.append("-"*40)
        
        # Location
        if file_type == 'xml':
            location = error.get('path', 'Unknown location')
            lines.append(f"📍 Where: {location}")
        else:
            line_num = error.get('line_number', 'Unknown')
            lines.append(f"📍 Line: {line_num}")
        
        # What happened
        if file_type == 'xml':
            text = error.get('text', error.get('tag', 'No description'))
        else:
            text = error.get('line', 'No description')
        
        lines.append(f"❌ What: {text}")
        
        # NRC Code explanation (if present) - MOVED UP for emphasis
        if has_nrc:
            lines.append("")
            lines.append("🚨 NEGATIVE RESPONSE CODE (NRC) DETECTED:")
            lines.append("-"*40)
            nrc = error['nrc_explanations'][0]
            lines.append(f"🔍 Error Code: {nrc['code']} (0x{nrc['code']})")
            lines.append(f"💡 Technical: {nrc['explanation']}")
            lines.append(f"📖 In Simple Terms:")
            simple_explanation = self._explain_nrc_simply(nrc['code'])
            # Indent the explanation for readability
            for explain_line in simple_explanation.split('\n'):
                lines.append(f"   {explain_line}")
            lines.append("-"*40)
            lines.append("")
        
        # Module Context (Primary vs Secondary)
        ecu_addresses = re.findall(r'\b([0-9A-Fa-f]{3})\b', text)
        if ecu_addresses:
            for ecu in ecu_addresses:
                ecu_upper = ecu.upper()
                if self.primary_module and ecu_upper == self.primary_module['id']:
                    lines.append(f"🎯 Module: {self.primary_module['name']} (PRIMARY TARGET)")
                else:
                    # Check if secondary
                    for sec_mod in self.secondary_modules:
                        if ecu_upper == sec_mod['id']:
                            lines.append(f"🔗 Module: {sec_mod['name']} (Supporting)")
                            break
        
        # Only show IMPORTANT DIDs
        important_dids = self._filter_important_dids(text)
        if important_dids:
            lines.append(f"📋 Important Data Identifiers:")
            for did_info in important_dids[:3]:  # Max 3 DIDs per error
                lines.append(f"   • DID {did_info['did']}: {did_info['description']}")
        
        return lines
    
    def _format_success(self, success: Dict[str, Any], index: int, file_type: str) -> List[str]:
        """Format success in simple terms"""
        lines = []
        
        if file_type == 'xml':
            text = success.get('text', success.get('tag', 'Operation succeeded'))
        else:
            text = success.get('line', 'Operation succeeded')
        
        lines.append(f"✅ {text}")
        
        return lines
    
    def _summarize_nrc_codes(self, results: List[Dict[str, Any]]) -> Dict[str, Dict]:
        """Summarize NRC codes found"""
        nrc_counts = Counter()
        nrc_explanations = {}
        
        for result in results:
            if result.get('nrc_explanations'):
                for nrc in result['nrc_explanations']:
                    code = nrc['code']
                    nrc_counts[code] += 1
                    nrc_explanations[code] = nrc['explanation']
        
        return {
            code: {
                'count': count,
                'explanation': nrc_explanations[code]
            }
            for code, count in nrc_counts.most_common()
        }
    
    def _explain_nrc_simply(self, nrc_code: str) -> str:
        """Explain NRC codes in simple terms"""
        simple_explanations = {
            '0x22': "The system isn't ready or in the right state for this action.",
            '0x35': "The security password/key was incorrect.",
            '0x31': "The requested value or setting is out of acceptable range.",
            '0x72': "Programming/flashing failed - something went wrong during update.",
            '0x73': "Data blocks were sent in wrong order during programming.",
            '0x78': "System is processing - wait for response (this is normal).",
            '0x7F': "This function isn't available in the current mode/session.",
            '0x11': "This feature is not supported by the system.",
            '0x12': "This specific option is not available.",
            '0x13': "The message format was incorrect or wrong size.",
            '0x21': "System is busy - try again in a moment.",
            '0x33': "Access denied - need proper authorization.",
            '0x36': "Too many failed attempts - locked out.",
            '0x37': "Need to wait before trying again.",
            '0x70': "Upload/download request was rejected.",
            '0x71': "Data transfer was paused.",
        }
        
        return simple_explanations.get(nrc_code, "Check documentation for details on this code.")
    
    def _generate_action_items(self, results: List[Dict[str, Any]], summary: Dict[str, int]) -> List[str]:
        """Generate recommended action items"""
        actions = []
        
        if summary['errors'] == 0:
            actions.append("✅ No action needed - log looks clean!")
            return actions
        
        # Check for specific error patterns
        nrc_codes = set()
        for result in results:
            if result.get('nrc_explanations'):
                for nrc in result['nrc_explanations']:
                    nrc_codes.add(nrc['code'])
        
        if '0x35' in nrc_codes:
            actions.append("🔐 Security issue detected - Verify authentication keys/passwords")
        
        if '0x22' in nrc_codes:
            actions.append("⚙️ System state issue - Check prerequisites before operations")
        
        if '0x72' in nrc_codes or '0x73' in nrc_codes:
            actions.append("💾 Programming failure - Review flash/update procedure")
        
        if '0x31' in nrc_codes:
            actions.append("📏 Range error - Check that values are within acceptable limits")
        
        if summary['errors'] > 10:
            actions.append("🔍 Many errors found - Consider investigating root cause")
        
        if not actions:
            actions.append("📖 Review error details above and consult documentation")
        
        actions.append("📤 Export full report (JSON/TXT) for detailed analysis")
        
        return actions
    
    def _extract_ecu_context(self, text: str) -> List[str]:
        """Extract and explain ECU node addresses and DIDs from text"""
        if not ECU_REFERENCE_AVAILABLE:
            return []
        
        lines = []
        
        # Pattern to match node addresses (3-character hex like 7D0, 760, etc.)
        node_pattern = r'\b([0-9A-Fa-f]{3})\b'
        nodes_found = re.findall(node_pattern, text)
        
        critical_nodes_found = []
        regular_nodes_found = []
        
        for node in set(nodes_found):  # Use set to avoid duplicates
            ecu_info = get_ecu_info(node)
            if ecu_info:
                if is_critical_ecu(node):
                    critical_nodes_found.append(node)
                else:
                    regular_nodes_found.append(node)
        
        # Report critical ECUs first
        if critical_nodes_found:
            for node in critical_nodes_found:
                lines.append(f"⚠️ ECU: {format_ecu_info(node)}")
                lines.append(f"   → {explain_ecu_context(node)}")
        
        # Then regular ECUs
        if regular_nodes_found:
            for node in regular_nodes_found:
                lines.append(f"🔧 ECU: {format_ecu_info(node)}")
                lines.append(f"   → {explain_ecu_context(node)}")
        
        # Pattern to match DIDs (4-character hex starting with F, like F190, F187)
        did_pattern = r'\b(F[0-9A-Fa-f]{3})\b'
        dids_found = re.findall(did_pattern, text)
        
        for did in set(dids_found):
            did_info = get_did_info(did)
            if did_info:
                lines.append(f"📋 DID {did}: {did_info}")
        
        return lines
    
    def _analyze_root_cause(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Analyze results to determine most likely issue and proximate cause
        Uses advanced RootCauseAnalyzer for multi-layer correlation
        Returns root cause analysis with actionable insights
        """
        errors = [r for r in results if self._is_error(r)]
        
        if not errors:
            return {
                'most_likely_issue': 'No errors detected',
                'proximate_cause': 'System operating normally',
                'recommended_action': 'Continue monitoring',
                'affected_systems': [],
                'confidence': 1.0,
            }
        
        # Use advanced analyzer if available
        if self.rca_available and self.root_cause_analyzer:
            try:
                analysis = self.root_cause_analyzer.analyze(results)
                pc = analysis.get('proximate_cause', {})
                
                # Extract meaningful proximate cause
                proximate_statement = ''
                if isinstance(pc, dict):
                    # Try to get a meaningful statement
                    if 'statement' in pc and isinstance(pc['statement'], str):
                        proximate_statement = pc['statement']
                    elif 'description' in pc:
                        proximate_statement = pc['description']
                    elif 'error' in pc:
                        # Extract error info more intelligently
                        error_obj = pc['error']
                        if isinstance(error_obj, dict):
                            line_text = error_obj.get('line', error_obj.get('text', ''))
                            proximate_statement = f"Error detected: {line_text[:200]}"
                        else:
                            proximate_statement = str(error_obj)[:200]
                    else:
                        proximate_statement = str(pc)[:200]
                elif isinstance(pc, str):
                    proximate_statement = pc
                else:
                    proximate_statement = "Multiple error conditions detected in log"
                
                # Convert to simplified format
                return {
                    'most_likely_issue': pc.get('category', 'DIAGNOSTIC').upper() + ' FAILURE',
                    'proximate_cause': proximate_statement,
                    'recommended_action': self._get_recommendations_from_analysis(analysis),
                    'affected_systems': pc.get('modules_affected', []),
                    'confidence': pc.get('confidence', 0.5),
                    'advanced_analysis': analysis,  # Include full analysis for detailed view
                }
            except Exception as e:
                # Fall back to legacy analysis if advanced fails
                pass
        
        # Analyze error patterns - ENHANCED for specific error types
        nrc_codes = []
        critical_ecus = []
        communication_errors = 0
        security_errors = 0
        range_errors = 0
        timeout_errors = 0
        can_errors = 0
        busy_errors = 0
        voltage_errors = 0
        soc_errors = 0
        modules_affected = set()
        
        for error in errors:
            # Get error text safely
            if isinstance(error, dict):
                error_str = error.get('line', error.get('text', str(error))).lower()
            else:
                error_str = str(error).lower()
            
            # Extract NRC codes
            if isinstance(error, dict) and error.get('nrc_explanations'):
                for nrc in error['nrc_explanations']:
                    nrc_codes.append(nrc['code'])
            
            # Also check for NRC patterns in text (7F XX YY format)
            nrc_pattern = re.search(r'7F[,\s]+([0-9A-Fa-f]{2})[,\s]+([0-9A-Fa-f]{2})', error_str.upper())
            if nrc_pattern:
                nrc_code = nrc_pattern.group(2)  # The NRC is the third byte
                if nrc_code not in nrc_codes:
                    nrc_codes.append(nrc_code)
            
            # Check for CAN bus errors
            if any(word in error_str for word in ['can error', 'bus-off', 'bus off', 'can bus', 'bus error', 
                                                   'canfd', 'can classic', 'iso15765', 'can timeout']):
                can_errors += 1
            
            # Check for busy/pending errors
            if any(word in error_str for word in ['busy', 'pending', 'response pending', '0x78', 'requestcorrectlyreceived']):
                busy_errors += 1
            
            # Check for voltage errors
            if any(word in error_str for word in ['voltage', 'vbatt', 'battery voltage', 'volt', 'power supply',
                                                   '0x93', '0x94', 'voltagetoolow', 'voltagetoohigh']):
                voltage_errors += 1
            
            # Check for state of charge errors
            if any(word in error_str for word in ['state of charge', 'soc', 'charge level', 'battery level']):
                soc_errors += 1
            
            # Check for communication/timeout errors
            if any(word in error_str for word in ['timeout', 'no response', 'communication', 'no reply', 'failed to respond']):
                communication_errors += 1
            
            # Check for security errors (0x33, 0x35, 0x36, 0x37)
            if any(word in error_str for word in ['security', 'invalid key', 'authentication', 'unauthorized',
                                                   '0x33', '0x35', '0x36', '0x37', 'securityaccessdenied',
                                                   'invalidkey', 'exceednumberofattempts']):
                security_errors += 1
            
            # Check for range errors
            if any(word in error_str for word in ['out of range', 'invalid parameter', 'range error', '0x31']):
                range_errors += 1
            
            # Check for timeout specifically
            if 'timeout' in error_str:
                timeout_errors += 1
            
            # Extract ECU context if available
            if ECU_REFERENCE_AVAILABLE:
                # Extract ECU addresses from error
                import re
                node_pattern = r'\b([0-9A-Fa-f]{3})\b'
                nodes = re.findall(node_pattern, error_str.upper())
                for node in nodes:
                    ecu_info = get_ecu_info(node)
                    if ecu_info:
                        modules_affected.add(f"{ecu_info['acronym']} ({node})")
                        if is_critical_ecu(node):
                            critical_ecus.append(ecu_info['acronym'])
        
        # Determine most likely issue based on patterns - ENHANCED
        issue_scores = {}
        
        # CAN Bus errors (highest priority for vehicle communication)
        if can_errors > 0:
            issue_scores['can_bus'] = can_errors * 4
        
        # Voltage issues (critical - can cause failures)
        if voltage_errors > 0 or '93' in nrc_codes or '94' in nrc_codes:
            issue_scores['voltage'] = (voltage_errors + nrc_codes.count('93') + nrc_codes.count('94')) * 5
        
        # State of Charge issues
        if soc_errors > 0:
            issue_scores['soc'] = soc_errors * 3
        
        # Security/Authentication issues (0x33, 0x35, 0x36, 0x37)
        if security_errors > 0 or any(code in ['33', '35', '36', '37'] for code in nrc_codes):
            sec_count = security_errors + sum(nrc_codes.count(c) for c in ['33', '35', '36', '37'])
            issue_scores['security'] = sec_count * 4
        
        # Busy/Pending (often not an actual error - lower priority)
        if busy_errors > 0 or '78' in nrc_codes:
            issue_scores['busy'] = (busy_errors + nrc_codes.count('78'))  # Lower weight
        
        # Communication/Network issues
        if communication_errors >= len(errors) * 0.3:  # 30% or more are comm errors
            issue_scores['network'] = communication_errors * 3
        
        # Configuration/Range issues (0x31)
        if range_errors > 0 or '31' in nrc_codes:
            issue_scores['configuration'] = (range_errors + nrc_codes.count('31')) * 2
        
        # Critical module failure
        if critical_ecus:
            issue_scores['critical_module'] = len(critical_ecus) * 4
        
        # Programming/Flash issues (0x72, 0x73)
        if any(code in ['72', '73'] for code in nrc_codes):
            issue_scores['programming'] = sum(nrc_codes.count(c) for c in ['72', '73']) * 4
        
        # Timeout issues
        if timeout_errors >= len(errors) * 0.3:  # 30% or more
            issue_scores['timeout'] = timeout_errors * 2
        
        # General NRC errors (if many unclassified NRCs)
        unclassified_nrcs = [c for c in nrc_codes if c not in ['78', '33', '35', '36', '37', '31', '72', '73', '93', '94']]
        if len(unclassified_nrcs) >= 3:
            issue_scores['nrc_errors'] = len(unclassified_nrcs) * 2
        
        # Determine highest scoring issue
        if not issue_scores:
            # Default to general diagnostic issue
            most_likely = 'general'
        else:
            most_likely = max(issue_scores.items(), key=lambda x: x[1])[0]
        
        # Build analysis based on most likely issue
        analysis = self._build_root_cause_analysis(
            most_likely, 
            nrc_codes, 
            critical_ecus, 
            list(modules_affected),
            len(errors)
        )
        
        return analysis
    
    def _get_recommendations_from_analysis(self, analysis: Dict) -> str:
        """Extract and format recommendations from advanced analysis"""
        if not analysis.get('recommendations'):
            return 'Review error details and consult technical documentation'
        
        rec_lines = []
        for i, rec in enumerate(analysis['recommendations'], 1):
            rec_lines.append(f"{i}. {rec['action']} (Success Rate: {rec['success_rate']*100:.0f}%)")
            for step in rec['steps']:
                rec_lines.append(f"   {step}")
        
        return '\n'.join(rec_lines)
    
    def _build_root_cause_analysis(self, issue_type: str, nrc_codes: List[str], 
                                   critical_ecus: List[str], modules: List[str],
                                   error_count: int) -> Dict[str, Any]:
        """Build detailed root cause analysis based on issue type"""
        
        analyses = {
            'can_bus': {
                'most_likely_issue': '🚌 CAN Bus Communication Error',
                'proximate_cause': 'CAN bus errors detected - modules unable to communicate properly on the vehicle network. This could be due to wiring issues, termination problems, bus-off conditions, or electromagnetic interference.',
                'recommended_action': '1️⃣ Check CAN bus wiring for shorts, opens, or damage\n   2️⃣ Verify CAN bus termination resistors (120 ohms at each end)\n   3️⃣ Test for bus-off conditions (check for modules flooding the bus)\n   4️⃣ Inspect connectors for corrosion or loose connections\n   5️⃣ Use oscilloscope to check CAN signal quality',
                'affected_systems': modules if modules else ['CAN bus network']
            },
            'voltage': {
                'most_likely_issue': '🔋 Battery Voltage Issue (CRITICAL)',
                'proximate_cause': 'Battery voltage is outside safe operating range (too low or too high). Low voltage can cause communication failures, module resets, and programming failures. High voltage can damage electronic components.',
                'recommended_action': '🚨 STOP OPERATIONS IMMEDIATELY\n   1️⃣ Check battery voltage with multimeter (should be 12.5-14.5V)\n   2️⃣ Connect battery charger/maintainer if voltage is low\n   3️⃣ Check alternator/charging system if voltage is high\n   4️⃣ Do NOT attempt programming with unstable voltage\n   5️⃣ Replace battery if it cannot hold charge',
                'affected_systems': modules if modules else ['All vehicle systems']
            },
            'soc': {
                'most_likely_issue': '⚡ State of Charge (SOC) Issue',
                'proximate_cause': 'Battery state of charge is below recommended levels for diagnostic operations. Low SOC can cause unreliable communication, module errors, and failed programming attempts.',
                'recommended_action': '1️⃣ Check battery state of charge (should be >70% for programming)\n   2️⃣ Charge battery before continuing operations\n   3️⃣ Verify battery health and capacity\n   4️⃣ Check for parasitic drain if SOC drops quickly',
                'affected_systems': modules if modules else ['Battery management system']
            },
            'busy': {
                'most_likely_issue': '⏳ Module Busy / Response Pending (NRC 0x78)',
                'proximate_cause': 'Modules are responding with "busy" or "response pending" messages. This is NORMAL during long operations like programming, flash updates, or complex calculations. The module is working and will respond when ready.',
                'recommended_action': '✅ This is usually NOT an error - just wait!\n   1️⃣ Be patient - programming can take 10-30+ minutes\n   2️⃣ Do NOT interrupt or power off during this time\n   3️⃣ Ensure stable power supply (battery charger connected)\n   4️⃣ Only take action if operation times out (>30 minutes)\n   5️⃣ If stuck, may need to retry operation from beginning',
                'affected_systems': modules if modules else ['Modules performing long operations']
            },
            'nrc_errors': {
                'most_likely_issue': '🔍 Multiple NRC (Negative Response Code) Errors',
                'proximate_cause': 'Multiple different NRC error codes detected indicating various diagnostic protocol issues. Each NRC code represents a specific rejection reason from the vehicle modules.',
                'recommended_action': '1️⃣ Review specific NRC codes in the detailed error section\n   2️⃣ Most common NRCs:\n      • 0x33 = Security access denied (wrong key)\n      • 0x35 = Invalid security key\n      • 0x22 = Conditions not correct (preconditions)\n      • 0x31 = Request out of range\n      • 0x78 = Response pending (not an error)\n   3️⃣ Address each NRC according to its specific meaning\n   4️⃣ Refer to NRC_QUICK_REFERENCE.md for detailed explanations',
                'affected_systems': modules if modules else ['Multiple diagnostic services']
            },
            'network': {
                'most_likely_issue': '🌐 Network Communication Failure',
                'proximate_cause': 'General network communication issues causing modules to lose connectivity. This typically indicates a physical network problem or a gateway/module going offline.',
                'recommended_action': '1️⃣ Check CAN bus wiring and connectors for damage\n   2️⃣ Verify all modules have proper power and ground\n   3️⃣ Check gateway module status\n   4️⃣ Scan for DTC codes that indicate bus-off conditions',
                'affected_systems': modules if modules else ['Multiple modules losing communication']
            },
            'security': {
                'most_likely_issue': '🔐 Security Access Failure',
                'proximate_cause': 'Authentication or security seed/key exchange failed. The diagnostic tool is using an incorrect security key, or the module is locked due to too many failed attempts.',
                'recommended_action': '1️⃣ Verify you have the correct security credentials for this vehicle\n   2️⃣ Check if security timer is active (may need to wait)\n   3️⃣ Clear security lockouts if possible\n   4️⃣ Use manufacturer-approved diagnostic tool with valid subscription',
                'affected_systems': modules if modules else ['Modules requiring security access']
            },
            'configuration': {
                'most_likely_issue': '⚙️ Configuration or Parameter Error',
                'proximate_cause': 'A parameter value is outside acceptable range or module configuration is incorrect. This can happen after a software update, module replacement, or when using incorrect diagnostic parameters.',
                'recommended_action': '1️⃣ Verify all parameter values are within specification\n   2️⃣ Check module configuration matches vehicle specification\n   3️⃣ Re-initialize or reconfigure affected modules\n   4️⃣ Perform module self-tests to validate configuration',
                'affected_systems': modules if modules else ['Modules with configuration errors']
            },
            'critical_module': {
                'most_likely_issue': f'⚠️ CRITICAL: {", ".join(critical_ecus) if critical_ecus else "Safety-Critical"} Module Failure',
                'proximate_cause': f'One or more SAFETY-CRITICAL modules ({", ".join(critical_ecus) if critical_ecus else "system modules"}) are experiencing failures. This affects vehicle safety systems and requires immediate attention.',
                'recommended_action': '🚨 IMMEDIATE ACTION REQUIRED:\n   1️⃣ Do not operate vehicle until issue is resolved\n   2️⃣ Check for recalled components or known issues\n   3️⃣ Verify module power supply and grounds\n   4️⃣ Consider module replacement if fault persists\n   5️⃣ Contact authorized service center',
                'affected_systems': modules if modules else [f'Critical: {", ".join(critical_ecus)}']
            },
            'programming': {
                'most_likely_issue': '💾 Module Programming/Flash Failure',
                'proximate_cause': 'Software update or module programming operation failed or was interrupted. The module may be in a partially programmed state or the flash memory is corrupt.',
                'recommended_action': '1️⃣ Check battery voltage (must be stable 12-14V during programming)\n   2️⃣ Ensure diagnostic cable is secure\n   3️⃣ Retry programming operation with known-good software\n   4️⃣ If module is bricked, may need JTAG recovery or replacement',
                'affected_systems': modules if modules else ['Modules requiring reprogramming']
            },
            'general_failure': {
                'most_likely_issue': '❌ General Module Malfunction',
                'proximate_cause': 'One or more modules are reporting general failure conditions. This can indicate hardware failure, software corruption, or environmental factors (temperature, voltage).',
                'recommended_action': '1️⃣ Check for DTC (Diagnostic Trouble Codes) for more specific information\n   2️⃣ Verify battery voltage and charging system\n   3️⃣ Check for any recent repairs or modifications\n   4️⃣ Test module in known-good vehicle if possible',
                'affected_systems': modules if modules else ['Modules reporting failures']
            },
            'timeout': {
                'most_likely_issue': '⏱️ Communication Timeout',
                'proximate_cause': 'Modules are not responding within the expected time window. This can indicate a slow/overloaded CAN bus, module entering sleep mode, or module busy with other tasks.',
                'recommended_action': '1️⃣ Check CAN bus load and traffic\n   2️⃣ Verify module wake-up procedures\n   3️⃣ Increase timeout values in diagnostic tool if possible\n   4️⃣ Check for modules stuck in boot mode or initialization',
                'affected_systems': modules if modules else ['Slow-responding modules']
            },
            'general': {
                'most_likely_issue': '🔧 Multiple Diagnostic Issues Detected',
                'proximate_cause': f'Analysis of {error_count} errors shows mixed failure patterns. The issues may be related to a common root cause or represent multiple independent problems.',
                'recommended_action': '1️⃣ Review each error individually for specific details\n   2️⃣ Look for common ECU modules across errors\n   3️⃣ Check vehicle history for recent repairs or modifications\n   4️⃣ Perform comprehensive system scan\n   5️⃣ Consider consulting technical service bulletins',
                'affected_systems': modules if modules else ['Multiple systems - see error details above']
            }
        }
        
        return analyses.get(issue_type, analyses['general'])
