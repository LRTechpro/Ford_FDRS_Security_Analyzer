"""
Enhanced Simple Mode Report Generator
Creates educational, beginner-friendly reports that teach hex/ASCII interpretation
Focuses on practical learning while showing diagnostic results
"""

from typing import List, Dict, Any, Tuple, Union
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


class EnhancedSimpleReportGenerator:
    """Enhanced simplified report generator with educational hex/ASCII content"""
    
    # Comprehensive Ford ECU/Module Database
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
    
    def __init__(self):
        self.primary_module = None
        self.secondary_modules = []
        self.detected_ecus = {}
        self.hex_explanations = []
        self.ascii_discoveries = []
        self.educational_tips = []
        
    def generate_educational_report(self, results: List[Dict[str, Any]], file_type: str) -> str:
        """
        Generate an educational, beginner-friendly report that teaches hex/ASCII interpretation
        
        Args:
            results: Parsed log results
            file_type: 'xml' or 'text'
            
        Returns:
            Educational report as string
        """
        if not results:
            return self._generate_no_issues_report()
        
        # Analyze data for educational content
        self._analyze_for_learning(results)
        
        report_lines = []
        
        # Header with learning focus
        report_lines.extend(self._generate_educational_header())
        
        # Part 1: Hex & ASCII Learning Section
        report_lines.extend(self._generate_hex_ascii_learning_section())
        
        # Part 2: What the Log is Telling Us
        report_lines.extend(self._generate_diagnostic_interpretation(results))
        
        # Part 3: Practical Examples from Your Log
        report_lines.extend(self._generate_practical_examples(results))
        
        # Part 4: Summary and Next Steps
        report_lines.extend(self._generate_learning_summary(results))
        
        return "\n".join(report_lines)
    
    def _generate_no_issues_report(self) -> str:
        """Generate educational content even when no issues found"""
        return """
🎓 LEARNING MODE - Log Analysis Report
=====================================

✅ Great News! No errors found in your log file!

📚 WHAT THIS MEANS:
• All diagnostic tests passed successfully
• No communication failures detected
• All modules responded properly

🔍 LEARNING OPPORTUNITY:
Even though there are no errors, this is a great opportunity to learn how to read logs!

📖 BASIC LOG READING CONCEPTS:

🔢 HEX VALUES (Hexadecimal):
• Hex uses 0-9 and A-F (16 possible values per digit)
• Example: 0x7D0 = 2000 in decimal
• Common in automotive for module addresses

📝 ASCII CONVERSION:
• ASCII converts numbers to readable text
• Example: 0x48 0x65 0x6C 0x6C 0x6F = "Hello"
• Helps find hidden text in diagnostic data

🚗 AUTOMOTIVE TERMS:
• ECU = Electronic Control Unit (car's computer modules)
• DID = Data Identifier (specific data request)
• NRC = Negative Response Code (error codes)

💡 TIP: Even successful logs contain valuable diagnostic data!
Try looking for module addresses (like 7D0, 716) and data values.
"""
    
    def _generate_educational_header(self) -> List[str]:
        """Generate educational header"""
        return [
            "🎓 LEARNING MODE - Beginner's Log Analysis",
            "=" * 80,
            "",
            "📚 WELCOME TO LOG ANALYSIS LEARNING!",
            "",
            "This report will teach you how to read and understand system logs,",
            "with special focus on HEX values and ASCII conversion.",
            "",
            "🎯 WHAT YOU'LL LEARN:",
            "• How to read hexadecimal (hex) values",
            "• How to convert hex to ASCII text",
            "• What diagnostic codes mean",
            "• How to identify important vs. routine data",
            "",
            "=" * 80,
            ""
        ]
    
    def _generate_hex_ascii_learning_section(self) -> List[str]:
        """Generate educational section about hex and ASCII"""
        lines = [
            "📖 LEARNING SECTION 1: Understanding HEX and ASCII",
            "=" * 80,
            "",
            "🔢 WHAT IS HEXADECIMAL (HEX)?",
            "",
            "Hexadecimal is a number system using 16 symbols:",
            "• Digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9",
            "• Letters: A, B, C, D, E, F (representing 10, 11, 12, 13, 14, 15)",
            "",
            "Examples:",
            "• 0x41 in hex = 65 in decimal = 'A' in ASCII",
            "• 0x48 in hex = 72 in decimal = 'H' in ASCII",
            "• 0x7D0 in hex = 2000 in decimal (common ECU address)",
            "",
            "📝 WHAT IS ASCII?",
            "",
            "ASCII converts numbers to readable characters:",
            "• Values 32-126 are printable characters",
            "• Values below 32 are control characters",
            "• Values above 126 are extended characters",
            "",
            "Common ASCII values:",
            "• 0x20 = space character",
            "• 0x30-0x39 = digits '0'-'9'",
            "• 0x41-0x5A = uppercase letters 'A'-'Z'",
            "• 0x61-0x7A = lowercase letters 'a'-'z'",
            "",
        ]
        
        # Add discovered examples from the log
        if self.hex_explanations:
            lines.extend([
                "🔍 HEX EXAMPLES FOUND IN YOUR LOG:",
                "-" * 50,
                ""
            ])
            
            for example in self.hex_explanations[:5]:  # Show top 5 examples
                lines.extend([
                    f"📍 Found: {example['hex_value']}",
                    f"   → Decimal: {example['decimal']}",
                    f"   → ASCII: '{example['ascii']}'",
                    f"   → Context: {example['context']}",
                    ""
                ])
        
        lines.extend([
            "=" * 80,
            ""
        ])
        
        return lines
    
    def _generate_diagnostic_interpretation(self, results: List[Dict[str, Any]]) -> List[str]:
        """Generate section explaining what the diagnostic data means"""
        lines = [
            "🏥 LEARNING SECTION 2: Diagnostic Data Interpretation",
            "=" * 80,
            "",
            "🚗 AUTOMOTIVE DIAGNOSTIC BASICS:",
            "",
            "🔧 ECU (Electronic Control Unit):",
            "• Think of these as the car's computers",
            "• Each ECU controls different systems (engine, brakes, etc.)",
            "• They communicate using specific addresses (like 7D0, 716)",
            "",
            "📋 DID (Data Identifier):",
            "• Specific requests for information",
            "• Example: F190 might request software version",
            "• Response contains the actual data",
            "",
            "❌ NRC (Negative Response Code):",
            "• Error codes when something goes wrong",
            "• Example: 0x31 = 'Request Out of Range'",
            "• Help diagnose communication problems",
            "",
        ]
        
        # Analyze and explain what we found
        summary = self._analyze_results_for_learning(results)
        
        lines.extend([
            "🔍 WHAT WE FOUND IN YOUR LOG:",
            "-" * 50,
            f"📊 Total diagnostic events: {summary['total_events']}",
            f"✅ Successful communications: {summary['successes']}",
            f"❌ Failed communications: {summary['failures']}",
            f"🔧 Unique ECUs detected: {len(summary['unique_ecus'])}",
            "",
        ])
        
        if summary['unique_ecus']:
            lines.extend([
                "🎯 ECU MODULES FOUND:",
                ""
            ])
            
            # Separate critical and non-critical modules
            critical_ecus = {}
            normal_ecus = {}
            
            for ecu_id, ecu_info in summary['unique_ecus'].items():
                if ecu_id in self.FORD_ECU_DATABASE and self.FORD_ECU_DATABASE[ecu_id]['critical']:
                    critical_ecus[ecu_id] = ecu_info
                else:
                    normal_ecus[ecu_id] = ecu_info
            
            # Show critical modules first
            if critical_ecus:
                lines.extend([
                    "⚠️  CRITICAL MODULES:",
                    ""
                ])
                for ecu_id, ecu_info in critical_ecus.items():
                    module_data = self.FORD_ECU_DATABASE.get(ecu_id, {})
                    lines.extend([
                        f"📍 [{module_data.get('abbr', ecu_id)}] {ecu_id}:",
                        f"   → {ecu_info.get('name', 'Unknown module')}",
                        f"   → Communications: {ecu_info.get('comm_count', 0)} events",
                        f"   → Status: {'✅ Active' if ecu_info.get('active', False) else '⚠️ Limited response'}",
                        f"   → Importance: CRITICAL SYSTEM",
                        ""
                    ])
            
            # Show normal modules
            if normal_ecus:
                lines.extend([
                    "📌 SUPPORT MODULES:",
                    ""
                ])
                for ecu_id, ecu_info in normal_ecus.items():
                    module_data = self.FORD_ECU_DATABASE.get(ecu_id, {})
                    lines.extend([
                        f"📍 [{module_data.get('abbr', ecu_id)}] {ecu_id}:",
                        f"   → {ecu_info.get('name', 'Unknown module')}",
                        f"   → Communications: {ecu_info.get('comm_count', 0)} events",
                        f"   → Status: {'✅ Active' if ecu_info.get('active', False) else '⚠️ Limited response'}",
                        ""
                    ])
            
            # Add ECU Quick Reference for detected modules
            lines.extend([
                "",
                "📚 ECU QUICK REFERENCE (Modules in Your Log):",
                "-" * 50,
                ""
            ])
            
            for ecu_id in sorted(summary['unique_ecus'].keys()):
                if ecu_id in self.FORD_ECU_DATABASE:
                    module_data = self.FORD_ECU_DATABASE[ecu_id]
                    criticality = "⚠️ CRITICAL" if module_data['critical'] else "ℹ️ Standard"
                    lines.extend([
                        f"• {ecu_id} = {module_data['abbr']} ({criticality})",
                        f"  {module_data['name']}",
                        ""
                    ])
        
        lines.extend([
            "=" * 80,
            ""
        ])
        
        return lines
    
    def _generate_practical_examples(self, results: List[Dict[str, Any]]) -> List[str]:
        """Generate practical examples from the actual log data"""
        lines = [
            "💡 LEARNING SECTION 3: Practical Examples from Your Log",
            "=" * 80,
            "",
        ]
        
        # Find the most educational examples
        examples = self._extract_educational_examples(results)
        
        if examples:
            lines.extend([
                "🔍 LET'S DECODE SOME REAL DATA:",
                "",
            ])
            
            for i, example in enumerate(examples[:3], 1):  # Show top 3 examples
                lines.extend([
                    f"📖 EXAMPLE {i}: {example['title']}",
                    "-" * 60,
                    f"Raw data: {example['raw_data']}",
                    "",
                    "🔍 Step-by-step breakdown:",
                ])
                
                for step in example['breakdown']:
                    lines.append(f"   {step}")
                
                lines.extend([
                    "",
                    f"💡 What this means: {example['explanation']}",
                    "",
                    f"🎯 Learning point: {example['learning_point']}",
                    "",
                    "─" * 60,
                    ""
                ])
        else:
            lines.extend([
                "📝 No complex data patterns found in this log.",
                "This is common in simple diagnostic sessions.",
                "",
                "🔍 THINGS TO LOOK FOR IN OTHER LOGS:",
                "• Module addresses (3 digits like 7D0, 716)",
                "• Data identifiers (4 digits like F190, F187)",
                "• Response data (multiple hex bytes)",
                "• Error codes (usually 2 digits like 31, 35)",
                ""
            ])
        
        lines.extend([
            "=" * 80,
            ""
        ])
        
        return lines
    
    def _generate_learning_summary(self, results: List[Dict[str, Any]]) -> List[str]:
        """Generate learning summary and next steps"""
        lines = [
            "🎯 LEARNING SUMMARY & NEXT STEPS",
            "=" * 80,
            "",
            "🎓 WHAT YOU'VE LEARNED:",
            "• How to read hexadecimal values and convert to ASCII",
            "• Basic automotive diagnostic concepts (ECU, DID, NRC)",
            "• How to identify important data in logs",
            "• Real examples from your actual log file",
            "",
            "💡 PRACTICAL TIPS FOR READING LOGS:",
            "",
            "🔍 Look for patterns:",
            "• 3-digit hex values (7D0, 716) = ECU addresses",
            "• 4-digit hex values (F190, F187) = Data identifiers",
            "• Sequences of hex bytes = Actual data responses",
            "• Two-digit codes after errors = NRC error codes",
            "",
            "📚 Understanding data flow:",
            "• Request: Computer asks module for information",
            "• Response: Module sends back data or error",
            "• Success: Data received and decoded",
            "• Failure: Communication problem or error code",
            "",
            "🛠️ NEXT STEPS TO IMPROVE YOUR SKILLS:",
            "",
            "1. 📖 Practice with more log files",
            "2. 🔍 Look up unfamiliar ECU addresses online",
            "3. 📝 Keep notes of common patterns you see",
            "4. 🎯 Focus on understanding one module at a time",
            "5. 💡 Use hex-to-ASCII converters to decode text data",
            "",
        ]
        
        # Add specific recommendations based on what was found
        recommendations = self._generate_specific_recommendations(results)
        if recommendations:
            lines.extend([
                "🎯 SPECIFIC RECOMMENDATIONS FOR YOUR LOG:",
                ""
            ])
            lines.extend(recommendations)
            lines.append("")
        
        lines.extend([
            "📞 NEED HELP?",
            "• Review the examples above",
            "• Try parsing different log files to see patterns",
            "• Focus on one concept at a time",
            "",
            "🌟 Remember: Every expert was once a beginner!",
            "Keep practicing and you'll become fluent in reading logs.",
            "",
            "=" * 80
        ])
        
        return lines
    
    def _analyze_for_learning(self, results: List[Dict[str, Any]]):
        """Analyze results to extract educational content about hex/ASCII"""
        self.hex_explanations = []
        self.ascii_discoveries = []
        
        for result in results:
            # Extract hex values from various fields
            self._extract_hex_examples(result)
            
            # Look for ASCII text in hex data
            self._extract_ascii_examples(result)
    
    def _extract_hex_examples(self, result: Dict[str, Any]):
        """Extract educational hex examples from a result"""
        # Look in different fields for hex values
        fields_to_check = ['text', 'line', 'attributes', 'hex_explanations']
        
        for field in fields_to_check:
            if field in result and result[field]:
                content = str(result[field])
                
                # Find hex patterns
                hex_patterns = re.findall(r'0x([0-9A-Fa-f]{1,8})', content)
                hex_patterns.extend(re.findall(r'([0-9A-Fa-f]{2,8})', content))
                
                for hex_val in hex_patterns[:3]:  # Limit examples
                    try:
                        if len(hex_val) <= 8:  # Reasonable size
                            decimal = int(hex_val, 16)
                            ascii_char = chr(decimal) if 32 <= decimal <= 126 else f"[{decimal}]"
                            
                            self.hex_explanations.append({
                                'hex_value': f"0x{hex_val.upper()}",
                                'decimal': decimal,
                                'ascii': ascii_char,
                                'context': self._get_context_description(field, result)
                            })
                    except (ValueError, OverflowError):
                        continue
    
    def _extract_ascii_examples(self, result: Dict[str, Any]):
        """Extract ASCII text discoveries from hex data"""
        # Look for sequences of hex bytes that form readable text
        fields_to_check = ['text', 'line', 'hex_explanations']
        
        for field in fields_to_check:
            if field in result and result[field]:
                content = str(result[field])
                
                # Find sequences of hex bytes
                hex_sequences = re.findall(r'(?:0x)?([0-9A-Fa-f]{2}(?:\s+[0-9A-Fa-f]{2})*)', content)
                
                for sequence in hex_sequences:
                    ascii_text = self._convert_hex_sequence_to_ascii(sequence)
                    if len(ascii_text) >= 3 and ascii_text.isprintable():
                        self.ascii_discoveries.append({
                            'hex_sequence': sequence,
                            'ascii_text': ascii_text,
                            'context': self._get_context_description(field, result)
                        })
    
    def _convert_hex_sequence_to_ascii(self, hex_sequence: str) -> str:
        """Convert a sequence of hex bytes to ASCII text"""
        try:
            # Clean and split the hex sequence
            hex_bytes = re.findall(r'[0-9A-Fa-f]{2}', hex_sequence)
            ascii_chars = []
            
            for hex_byte in hex_bytes:
                decimal = int(hex_byte, 16)
                if 32 <= decimal <= 126:  # Printable ASCII
                    ascii_chars.append(chr(decimal))
                else:
                    ascii_chars.append('.')
            
            return ''.join(ascii_chars)
        except (ValueError, TypeError):
            return ""
    
    def _get_context_description(self, field: str, result: Dict[str, Any]) -> str:
        """Get a user-friendly description of where the hex value was found"""
        context_map = {
            'text': 'XML element text',
            'line': 'Log line content',
            'attributes': 'XML attributes',
            'hex_explanations': 'Hex data field'
        }
        
        base_context = context_map.get(field, 'Unknown field')
        
        # Add more specific context if available
        if 'path' in result:
            return f"{base_context} in {result['path']}"
        elif 'line_number' in result:
            return f"{base_context} at line {result['line_number']}"
        else:
            return base_context
    
    def _analyze_results_for_learning(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze results to provide learning insights"""
        summary = {
            'total_events': len(results),
            'successes': 0,
            'failures': 0,
            'unique_ecus': {},
            'common_patterns': []
        }
        
        for result in results:
            # Count successes and failures
            if self._is_success(result):
                summary['successes'] += 1
            elif self._is_error(result):
                summary['failures'] += 1
            
            # Extract ECU information
            ecu_addresses = self._extract_ecu_addresses(result)
            for ecu_addr in ecu_addresses:
                if ecu_addr not in summary['unique_ecus']:
                    summary['unique_ecus'][ecu_addr] = {
                        'name': self._get_ecu_name(ecu_addr),
                        'comm_count': 0,
                        'active': False
                    }
                summary['unique_ecus'][ecu_addr]['comm_count'] += 1
                summary['unique_ecus'][ecu_addr]['active'] = True
        
        return summary
    
    def _extract_educational_examples(self, results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Extract the most educational examples from the log data"""
        examples = []
        
        for result in results:
            # Look for hex data that can be decoded
            example = self._create_educational_example(result)
            if example:
                examples.append(example)
        
        # Sort by educational value (prefer examples with ASCII conversion)
        examples.sort(key=lambda x: x.get('educational_score', 0), reverse=True)
        
        return examples
    
    def _create_educational_example(self, result: Dict[str, Any]) -> Union[Dict[str, Any], None]:
        """Create an educational example from a log result"""
        # Look for hex data in the result
        hex_data = self._find_hex_data(result)
        if not hex_data:
            return None
        
        # Try to create meaningful breakdown
        breakdown = self._create_hex_breakdown(hex_data)
        if not breakdown:
            return None
        
        return {
            'title': self._generate_example_title(result),
            'raw_data': hex_data,
            'breakdown': breakdown,
            'explanation': self._explain_example_meaning(result, hex_data),
            'learning_point': self._extract_learning_point(result, hex_data),
            'educational_score': self._calculate_educational_score(hex_data, breakdown)
        }
    
    def _find_hex_data(self, result: Dict[str, Any]) -> str:
        """Find the most interesting hex data in a result"""
        # Check various fields for hex data
        fields = ['text', 'line', 'hex_explanations']
        
        for field in fields:
            if field in result and result[field]:
                content = str(result[field])
                
                # Look for hex patterns
                hex_match = re.search(r'(?:0x)?([0-9A-Fa-f]{4,})', content)
                if hex_match:
                    return hex_match.group(1)
        
        return ""
    
    def _create_hex_breakdown(self, hex_data: str) -> List[str]:
        """Create a step-by-step breakdown of hex data"""
        if not hex_data or len(hex_data) < 4:
            return []
        
        breakdown = []
        
        # Break into bytes if even length
        if len(hex_data) % 2 == 0:
            bytes_list = [hex_data[i:i+2] for i in range(0, len(hex_data), 2)]
            
            breakdown.append(f"1. Split into bytes: {' '.join(bytes_list)}")
            
            # Convert each byte
            for i, byte_val in enumerate(bytes_list[:6]):  # Limit to 6 bytes
                try:
                    decimal = int(byte_val, 16)
                    ascii_char = chr(decimal) if 32 <= decimal <= 126 else f"[non-printable:{decimal}]"
                    breakdown.append(f"   Byte {i+1}: 0x{byte_val} = {decimal} decimal = '{ascii_char}'")
                except (ValueError, OverflowError):
                    continue
            
            # Try ASCII interpretation
            ascii_result = self._convert_hex_sequence_to_ascii(hex_data)
            if ascii_result and any(c.isalnum() for c in ascii_result):
                breakdown.append(f"2. ASCII interpretation: '{ascii_result}'")
        
        return breakdown
    
    def _generate_example_title(self, result: Dict[str, Any]) -> str:
        """Generate a descriptive title for an example"""
        if 'path' in result and 'Response' in str(result.get('path', '')):
            return "ECU Response Data"
        elif 'NRC' in str(result.get('text', '')):
            return "Error Code Response"
        elif any(term in str(result.get('text', '')) for term in ['F1', 'DID', 'Data']):
            return "Data Identifier Response"
        else:
            return "Diagnostic Communication"
    
    def _explain_example_meaning(self, result: Dict[str, Any], hex_data: str) -> str:
        """Explain what the example means in practical terms"""
        if 'error' in str(result.get('text', '')).lower() or 'nrc' in str(result.get('text', '')).lower():
            return "This is an error response from an ECU module, indicating a communication problem."
        elif 'success' in str(result.get('text', '')).lower() or 'pass' in str(result.get('text', '')).lower():
            return "This is a successful response containing requested diagnostic data."
        else:
            return "This represents diagnostic communication between the scan tool and vehicle modules."
    
    def _extract_learning_point(self, result: Dict[str, Any], hex_data: str) -> str:
        """Extract the key learning point from this example"""
        if len(hex_data) >= 8:
            return "Long hex sequences often contain multiple pieces of information - break them into bytes to decode."
        elif any(c.isalnum() for c in self._convert_hex_sequence_to_ascii(hex_data)):
            return "Some hex data converts to readable ASCII text - this often contains part numbers or version info."
        else:
            return "Each hex byte represents a specific value or code in the diagnostic protocol."
    
    def _calculate_educational_score(self, hex_data: str, breakdown: List[str]) -> int:
        """Calculate how educational this example is"""
        score = 0
        
        # Longer data is more educational
        score += min(len(hex_data) // 2, 10)
        
        # ASCII conversion adds value
        ascii_result = self._convert_hex_sequence_to_ascii(hex_data)
        if ascii_result and any(c.isalnum() for c in ascii_result):
            score += 15
        
        # Multiple bytes to explain
        if len(breakdown) > 3:
            score += 10
        
        return score
    
    def _generate_specific_recommendations(self, results: List[Dict[str, Any]]) -> List[str]:
        """Generate specific recommendations based on the log content"""
        recommendations = []
        
        # Check for specific patterns
        has_errors = any(self._is_error(r) for r in results)
        has_hex_data = any(self._find_hex_data(r) for r in results)
        has_ecu_addresses = any(self._extract_ecu_addresses(r) for r in results)
        
        if has_errors:
            recommendations.append("• Study the error codes (NRC) to understand communication failures")
        
        if has_hex_data:
            recommendations.append("• Practice converting hex values to ASCII to find hidden text")
        
        if has_ecu_addresses:
            recommendations.append("• Research the ECU addresses found to understand which car systems are involved")
        
        if self.ascii_discoveries:
            recommendations.append("• Look for ASCII text in hex data - it often contains useful part numbers or versions")
        
        if not recommendations:
            recommendations.append("• Try analyzing a more complex log file with diagnostic errors")
        
        return recommendations
    
    # Helper methods (simplified versions of the existing methods)
    def _is_success(self, result: Dict[str, Any]) -> bool:
        """Check if result represents success"""
        text = str(result.get('text', '') + result.get('line', '')).lower()
        return any(term in text for term in ['success', 'pass', 'ok', 'complete'])
    
    def _is_error(self, result: Dict[str, Any]) -> bool:
        """Check if result represents error"""
        text = str(result.get('text', '') + result.get('line', '')).lower()
        return any(term in text for term in ['error', 'fail', 'nrc', 'fault', 'exception'])
    
    def _extract_ecu_addresses(self, result: Dict[str, Any]) -> List[str]:
        """Extract ECU addresses from result using comprehensive database"""
        content = str(result.get('text', '') + result.get('line', ''))
        found_addresses = []
        
        # Look for all 3-digit hex patterns
        hex_patterns = re.findall(r'(?:0x)?([0-9A-Fa-f]{3})\b', content)
        
        for hex_val in hex_patterns:
            hex_upper = hex_val.upper()
            # Check if it's a known ECU address from our comprehensive database
            if hex_upper in self.FORD_ECU_DATABASE:
                found_addresses.append(hex_upper)
            # Also check ECU reference if available
            elif ECU_REFERENCE_AVAILABLE:
                try:
                    info = get_ecu_info(hex_upper)
                    if info and info.get('name') != 'Unknown':
                        found_addresses.append(hex_upper)
                except:
                    pass
        
        return list(set(found_addresses))  # Remove duplicates
    
    def _get_ecu_name(self, ecu_addr: str) -> str:
        """Get a friendly name for an ECU address using comprehensive Ford database"""
        ecu_addr_upper = ecu_addr.upper()
        
        if ecu_addr_upper in self.FORD_ECU_DATABASE:
            ecu_info = self.FORD_ECU_DATABASE[ecu_addr_upper]
            return f"{ecu_info['abbr']} - {ecu_info['name']}"
        
        # Try to find it with ECU reference if available
        if ECU_REFERENCE_AVAILABLE:
            try:
                info = get_ecu_info(ecu_addr_upper)
                if info and info.get('name') != 'Unknown':
                    return info.get('full_name', info.get('name', f"ECU {ecu_addr}"))
            except:
                pass
        
        return f"Unknown ECU {ecu_addr}"