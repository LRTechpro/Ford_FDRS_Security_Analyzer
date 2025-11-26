"""
Module Dependency Tracker
Tracks sub-modules/nodes communicated with during update/programming processes
Helps identify missing dependencies that cause module update failures
"""

from typing import Dict, List, Set, Tuple, Any
import re
from collections import defaultdict

try:
    from ecu_reference import get_ecu_info, format_ecu_info
    ECU_REFERENCE_AVAILABLE = True
except ImportError:
    ECU_REFERENCE_AVAILABLE = False


class ModuleDependencyTracker:
    """Tracks module communication patterns and dependencies"""
    
    # Known valid Ford ECU addresses (whitelist approach - only these are actual modules)
    VALID_ECU_ADDRESSES = {
        # 6xx range modules (specific addresses only)
        '6E0', '6F0', '6F1', '6F2', '6F3', '6F5', '6F6', '6F7',
        # 7xx range modules (all valid Ford module addresses)
        '702', '703', '706', '712', '713', '716', '720', '721', '723', '724', '725', '726', '727',
        '730', '731', '732', '733', '734', '736', '737', '740', '741', '744', '746', '750', '751',
        '754', '760', '761', '762', '763', '764', '765', '766', '774', '775', '776', '777', '783',
        '787', '791', '792', '795', '797', '7A1', '7A2', '7A3', '7A4', '7A7', '7B1', '7B2', '7B3',
        '7B4', '7C1', '7C4', '7C5', '7C6', '7C7', '7D0', '7E0', '7E2', '7E4', '7E6', '7E7', '7E9',
        '7F2',
    }
    
    # Known module dependencies (target module -> required dependencies)
    KNOWN_DEPENDENCIES = {
        '7E0': ['732', '726', '7E4'],  # PCM needs Gateway, BCM, BECM
        '754': ['7E0', '732', '726'],  # TCU needs PCM, Gateway, BCM
        '7D0': ['732', '726', '727'],  # APIM needs Gateway, BCM, ACM
        '726': ['732', '7E4'],         # BCM needs Gateway, BECM
        '760': ['732', '7E0'],         # ABS needs Gateway, PCM
        '737': ['732', '726'],         # RCM needs Gateway, BCM
        '733': ['726', '732'],         # HVAC needs BCM, Gateway
        '720': ['726', '732'],         # IPC needs BCM, Gateway
        '727': ['7D0', '726'],         # ACM needs APIM, BCM
    }
    
    # Programming/update related service IDs
    PROGRAMMING_SERVICES = {
        '0x10': 'Diagnostic Session Control',
        '0x11': 'ECU Reset',
        '0x27': 'Security Access',
        '0x28': 'Communication Control',
        '0x31': 'Routine Control',
        '0x34': 'Request Download',
        '0x35': 'Request Upload',
        '0x36': 'Transfer Data',
        '0x37': 'Request Transfer Exit',
        '0x38': 'Request File Transfer',
        '0x85': 'Control DTC Setting',
    }
    
    def __init__(self):
        self.communication_log = []  # List of (source, target, service, status, timestamp)
        self.module_sessions = defaultdict(list)  # module -> list of communications
        self.dependency_map = defaultdict(set)  # module -> set of modules it communicated with
        self.programming_attempts = []  # List of programming/update attempts
        self.failed_dependencies = []  # List of failed dependency communications
    
    def parse_log_for_dependencies(self, log_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Parse log results to extract module dependencies and communication patterns
        
        Args:
            log_results: Parsed log entries from text_log_parser or xml_log_parser
        
        Returns:
            Dictionary containing dependency analysis
        """
        self._reset()
        
        for entry in log_results:
            self._process_entry(entry)
        
        return self._generate_dependency_report()
    
    def _reset(self):
        """Reset all tracking data"""
        self.communication_log = []
        self.module_sessions = defaultdict(list)
        self.dependency_map = defaultdict(set)
        self.programming_attempts = []
        self.failed_dependencies = []
    
    def _is_likely_ecu_address(self, hex_value: str, text: str) -> bool:
        """
        Determine if a 3-char hex value is likely an ECU address vs. a DID
        
        STRICT filtering: Only 7xx range are valid ECU addresses
        ECU addresses start with 7 (7E0, 7D0, 732, etc.)
        Everything else (206, 222, 237, 696, etc.) is NOT an ECU module
        """
        hex_upper = hex_value.upper()
        
        # Check if mentioned as DID in context
        if re.search(r'(?:DID|did)\s*(?:0x)?' + hex_value, text, re.IGNORECASE):
            return False
        
        # Use whitelist approach: ONLY accept known valid Ford ECU addresses
        if hex_upper in self.VALID_ECU_ADDRESSES:
            return True
        
        # Everything else is NOT an ECU address (including all DIDs)
        return False
    
    def _process_entry(self, entry: Dict[str, Any]):
        """Process a single log entry to extract communication data"""
        # Get the text content
        text = entry.get('line', entry.get('text', ''))
        
        # Extract ECU addresses (3-character hex like 7E0, 732, etc.)
        all_addresses = re.findall(r'\b([0-9A-Fa-f]{3})\b', text)
        
        # Filter to only actual ECU addresses (not DIDs)
        ecu_addresses = [addr for addr in all_addresses if self._is_likely_ecu_address(addr, text)]
        
        # Extract service IDs (like 0x10, 0x27, etc.)
        service_ids = re.findall(r'(?:Service|service)\s+(?:0x)?([0-9A-Fa-f]{2})', text)
        service_ids += re.findall(r'\b(0x[0-9A-Fa-f]{2})\b', text)
        
        # Determine if this is programming-related
        is_programming = any(
            service in text.upper() for service in 
            ['PROGRAM', 'FLASH', 'UPDATE', 'DOWNLOAD', 'UPLOAD', 'TRANSFER']
        ) or any(sid in self.PROGRAMMING_SERVICES for sid in service_ids)
        
        # Determine status
        status = 'unknown'
        if 'SUCCESS' in text.upper() or 'PASS' in text.upper():
            status = 'success'
        elif 'ERROR' in text.upper() or 'FAIL' in text.upper() or 'NRC' in text.upper():
            status = 'failed'
        elif 'WARN' in text.upper():
            status = 'warning'
        elif 'TIMEOUT' in text.upper():
            status = 'timeout'
        
        # Extract timestamp
        timestamp = entry.get('log_timestamp', entry.get('timestamp', ''))
        
        # If we found ECU addresses, track the communication
        if len(ecu_addresses) >= 1:
            target_ecu = ecu_addresses[0].upper()
            
            # Track all ECUs mentioned in this line
            for ecu in ecu_addresses:
                ecu = ecu.upper()
                self.module_sessions[ecu].append({
                    'text': text,
                    'status': status,
                    'timestamp': timestamp,
                    'is_programming': is_programming,
                    'services': service_ids
                })
            
            # Track dependencies (module communicating with other modules)
            if len(ecu_addresses) > 1:
                for i, ecu in enumerate(ecu_addresses):
                    ecu = ecu.upper()
                    for other_ecu in ecu_addresses[i+1:]:
                        other_ecu = other_ecu.upper()
                        if ecu != other_ecu:
                            self.dependency_map[ecu].add(other_ecu)
                            self.dependency_map[other_ecu].add(ecu)
            
            # Track programming attempts
            if is_programming:
                self.programming_attempts.append({
                    'target': target_ecu,
                    'status': status,
                    'timestamp': timestamp,
                    'text': text,
                    'services': service_ids
                })
            
            # Track failed dependencies
            if status in ['failed', 'timeout'] and len(ecu_addresses) > 1:
                self.failed_dependencies.append({
                    'target': target_ecu,
                    'related_modules': ecu_addresses[1:],
                    'status': status,
                    'text': text,
                    'timestamp': timestamp
                })
    
    def _generate_dependency_report(self) -> Dict[str, Any]:
        """Generate comprehensive dependency analysis report"""
        report = {
            'summary': self._generate_summary(),
            'module_communications': self._analyze_module_communications(),
            'programming_attempts': self._analyze_programming_attempts(),
            'missing_dependencies': self._identify_missing_dependencies(),
            'failed_communications': self._analyze_failed_communications(),
            'dependency_graph': self._build_dependency_graph(),
            'recommendations': self._generate_recommendations()
        }
        
        return report
    
    def _generate_summary(self) -> Dict[str, Any]:
        """Generate summary statistics"""
        total_modules = len(self.module_sessions)
        failed_programming = len([p for p in self.programming_attempts if p['status'] == 'failed'])
        
        return {
            'total_modules_involved': total_modules,
            'total_programming_attempts': len(self.programming_attempts),
            'failed_programming_attempts': failed_programming,
            'failed_dependencies_count': len(self.failed_dependencies),
            'modules_with_dependencies': len(self.dependency_map)
        }
    
    def _analyze_module_communications(self) -> List[Dict[str, Any]]:
        """Analyze communication patterns for each module"""
        analysis = []
        
        for module, sessions in self.module_sessions.items():
            success_count = sum(1 for s in sessions if s['status'] == 'success')
            failed_count = sum(1 for s in sessions if s['status'] == 'failed')
            programming_count = sum(1 for s in sessions if s['is_programming'])
            
            module_info = {
                'module_id': module,
                'module_name': self._get_module_name(module),
                'total_communications': len(sessions),
                'successful': success_count,
                'failed': failed_count,
                'programming_related': programming_count,
                'communicated_with': list(self.dependency_map.get(module, set()))
            }
            
            analysis.append(module_info)
        
        # Sort by failed count (most problematic first)
        analysis.sort(key=lambda x: x['failed'], reverse=True)
        
        return analysis
    
    def _analyze_programming_attempts(self) -> List[Dict[str, Any]]:
        """Analyze programming/update attempts"""
        if not self.programming_attempts:
            return []
        
        attempts = []
        for attempt in self.programming_attempts:
            attempts.append({
                'target_module': attempt['target'],
                'module_name': self._get_module_name(attempt['target']),
                'status': attempt['status'],
                'timestamp': attempt['timestamp'],
                'services_used': list(set(attempt['services'])),
                'description': attempt['text'][:100]
            })
        
        return attempts
    
    def _identify_missing_dependencies(self) -> List[Dict[str, Any]]:
        """Identify potentially missing module dependencies"""
        missing = []
        
        for module, expected_deps in self.KNOWN_DEPENDENCIES.items():
            if module in self.module_sessions:
                # Module was involved in communications
                actual_deps = self.dependency_map.get(module, set())
                
                for expected_dep in expected_deps:
                    if expected_dep not in actual_deps:
                        # Expected dependency not found in communications
                        missing.append({
                            'target_module': module,
                            'target_name': self._get_module_name(module),
                            'missing_dependency': expected_dep,
                            'dependency_name': self._get_module_name(expected_dep),
                            'severity': 'high' if expected_dep == '732' else 'medium'  # Gateway is critical
                        })
        
        return missing
    
    def _analyze_failed_communications(self) -> List[Dict[str, Any]]:
        """Analyze failed communication attempts"""
        if not self.failed_dependencies:
            return []
        
        failures = []
        for failure in self.failed_dependencies:
            failures.append({
                'target_module': failure['target'],
                'target_name': self._get_module_name(failure['target']),
                'status': failure['status'],
                'related_modules': [
                    {
                        'id': mod,
                        'name': self._get_module_name(mod)
                    }
                    for mod in failure['related_modules']
                ],
                'description': failure['text'][:100],
                'timestamp': failure['timestamp']
            })
        
        return failures
    
    def _build_dependency_graph(self) -> Dict[str, List[str]]:
        """Build a dependency graph showing all module relationships"""
        graph = {}
        
        for module, deps in self.dependency_map.items():
            graph[module] = {
                'name': self._get_module_name(module),
                'dependencies': [
                    {
                        'id': dep,
                        'name': self._get_module_name(dep)
                    }
                    for dep in deps
                ]
            }
        
        return graph
    
    def _generate_recommendations(self) -> List[str]:
        """Generate recommendations based on dependency analysis"""
        recommendations = []
        
        # Check for Gateway issues
        if '732' in self.module_sessions:
            gsm_failed = sum(1 for s in self.module_sessions['732'] if s['status'] == 'failed')
            if gsm_failed > 0:
                recommendations.append(
                    "⚠️ Gateway Support Module (732) has failed communications. "
                    "This is a critical dependency for most modules. Resolve Gateway issues first."
                )
        
        # Check for missing dependencies during programming
        if self.programming_attempts:
            failed_prog = [p for p in self.programming_attempts if p['status'] == 'failed']
            if failed_prog:
                recommendations.append(
                    f"❌ {len(failed_prog)} programming/update attempts failed. "
                    "Check that all dependency modules are present and have correct software versions."
                )
        
        # Check for missing known dependencies
        missing_deps = self._identify_missing_dependencies()
        if missing_deps:
            high_severity = [d for d in missing_deps if d['severity'] == 'high']
            if high_severity:
                recommendations.append(
                    f"🔍 {len(high_severity)} critical module dependencies missing. "
                    "Update may fail if these modules are not properly configured."
                )
        
        # Check for timeout issues
        timeouts = [f for f in self.failed_dependencies if f['status'] == 'timeout']
        if timeouts:
            recommendations.append(
                f"⏱️ {len(timeouts)} communication timeouts detected. "
                "Check CAN bus connections and module power supply."
            )
        
        if not recommendations:
            recommendations.append("✅ No critical dependency issues detected.")
        
        return recommendations
    
    def _get_module_name(self, module_id: str) -> str:
        """Get human-readable module name"""
        if ECU_REFERENCE_AVAILABLE:
            info = get_ecu_info(module_id)
            if info:
                return format_ecu_info(module_id)
        
        # Fallback names
        fallback_names = {
            '7E0': 'PCM (Powertrain Control Module)',
            '732': 'GSM (Gateway Support Module)',
            '726': 'BCM (Body Control Module)',
            '7D0': 'APIM (Accessory Protocol Interface Module)',
            '754': 'TCU (Transmission Control Unit)',
            '760': 'ABS (Anti-lock Braking System)',
            '737': 'RCM (Restraint Control Module)',
            '7E4': 'BECM (Battery Energy Control Module)',
            '733': 'HVAC (Climate Control)',
            '720': 'IPC (Instrument Panel Cluster)',
            '727': 'ACM (Audio Control Module)',
        }
        
        return fallback_names.get(module_id.upper(), f"Module {module_id}")
    
    def format_dependency_report_text(self, report: Dict[str, Any]) -> str:
        """Format dependency report as human-readable text"""
        lines = []
        
        lines.append("="*80)
        lines.append("🔗 MODULE DEPENDENCY ANALYSIS")
        lines.append("="*80)
        lines.append("")
        
        # Summary
        summary = report['summary']
        lines.append("📊 SUMMARY")
        lines.append("-"*80)
        lines.append(f"Total Modules Involved: {summary['total_modules_involved']}")
        lines.append(f"Programming Attempts: {summary['total_programming_attempts']}")
        lines.append(f"Failed Programming: {summary['failed_programming_attempts']}")
        lines.append(f"Failed Dependencies: {summary['failed_dependencies_count']}")
        lines.append("")
        
        # Recommendations
        if report['recommendations']:
            lines.append("💡 RECOMMENDATIONS")
            lines.append("-"*80)
            for rec in report['recommendations']:
                lines.append(f"  • {rec}")
            lines.append("")
        
        # Module Communications
        if report['module_communications']:
            lines.append("📡 MODULE COMMUNICATION ANALYSIS")
            lines.append("-"*80)
            for module in report['module_communications'][:10]:  # Show top 10
                lines.append(f"\n{module['module_name']} ({module['module_id']})")
                lines.append(f"  Total Communications: {module['total_communications']}")
                lines.append(f"  ✅ Successful: {module['successful']}")
                if module['failed'] > 0:
                    lines.append(f"  ❌ Failed: {module['failed']}")
                if module['programming_related'] > 0:
                    lines.append(f"  💾 Programming Related: {module['programming_related']}")
                if module['communicated_with']:
                    lines.append(f"  🔗 Communicated With: {', '.join(module['communicated_with'])}")
            lines.append("")
        
        # Missing Dependencies
        if report['missing_dependencies']:
            lines.append("⚠️  POTENTIALLY MISSING DEPENDENCIES")
            lines.append("-"*80)
            for missing in report['missing_dependencies']:
                # Use better contrast colors instead of bright yellow
                severity_icon = "🔴" if missing['severity'] == 'high' else "�"  # Orange instead of yellow
                lines.append(f"{severity_icon} {missing['target_name']} missing dependency:")
                lines.append(f"   → {missing['dependency_name']} ({missing['missing_dependency']})")
            lines.append("")
        
        # Failed Communications
        if report['failed_communications']:
            lines.append("❌ FAILED COMMUNICATIONS")
            lines.append("-"*80)
            for failure in report['failed_communications'][:5]:  # Show first 5
                lines.append(f"\n{failure['target_name']} - {failure['status'].upper()}")
                if failure['related_modules']:
                    related = ', '.join([m['name'] for m in failure['related_modules']])
                    lines.append(f"  Related Modules: {related}")
                lines.append(f"  {failure['description']}")
            lines.append("")
        
        lines.append("="*80)
        
        return '\n'.join(lines)


# Convenience function for quick analysis
def analyze_dependencies(log_results: List[Dict[str, Any]]) -> Tuple[Dict[str, Any], str]:
    """
    Quick function to analyze dependencies from log results
    
    Args:
        log_results: Parsed log entries
    
    Returns:
        Tuple of (report dict, formatted text report)
    """
    tracker = ModuleDependencyTracker()
    report = tracker.parse_log_for_dependencies(log_results)
    formatted_text = tracker.format_dependency_report_text(report)
    
    return report, formatted_text
