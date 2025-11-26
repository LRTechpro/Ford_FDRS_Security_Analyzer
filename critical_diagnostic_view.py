"""
Critical Diagnostic View - Priority Display for Vehicle Diagnostics
Shows the most important diagnostic information first:
- Vehicle VIN
- Voltage Status
- DTCs and Failed Errors
- Success Reports
- DID Responses (changing/trying to change)
- Hex/ASCII Communication with explanations
- Proximate Cause Report with Evidence
"""

import re
import json
from typing import Dict, List, Any, Tuple, Optional
from datetime import datetime


class CriticalDiagnosticView:
    """
    Extracts and displays critical diagnostic information in priority order
    """
    
    def __init__(self):
        self.vin_patterns = [
            r'VIN[:\s]*([A-HJ-NPR-Z0-9]{17})',
            r'F190[:\s]*([A-HJ-NPR-Z0-9]{17})',
            r'Vehicle.*ID[:\s]*([A-HJ-NPR-Z0-9]{17})',
            r'\b([A-HJ-NPR-Z0-9]{17})\b'
        ]
        
        self.voltage_patterns = [
            r'voltage[:\s]*(\d+\.?\d*)\s*V',
            r'battery[:\s]*(\d+\.?\d*)\s*V',
            r'DE02[:\s]*.*?([0-9A-Fa-f]{2})',  # Battery voltage DID
            r'(\d{2}\.\d+)\s*V'
        ]
        
        self.dtc_patterns = [
            r'DTC[:\s#]*([BPUC][0-9A-Fa-f]{4})',
            r'diagnostic.*code[:\s]*([BPUC][0-9A-Fa-f]{4})',
            r'trouble.*code[:\s]*([BPUC][0-9A-Fa-f]{4})',
            r'([BPUC][0-9A-Fa-f]{4})'
        ]
        
        self.did_patterns = [
            r'(DE[0-9A-Fa-f]{2})[:\s]*([0-9A-Fa-f]+)',
            r'(F1[0-9A-Fa-f]{2})[:\s]*([0-9A-Fa-f]+)',
            r'Diag service request[:\s]*([0-9A-Fa-f]+)',
            r'Diag service response[:\s]*([0-9A-Fa-f]+)'
        ]
        
        self.hex_communication_patterns = [
            r'Input DTC byte field[:\s]*([0-9A-Fa-f]{8,})',
            r'Parsed DTC byte field[:\s]*([0-9A-Fa-f]{8,})',
            r'service request[:\s]*([0-9A-Fa-f]{8,})',
            r'service response[:\s]*([0-9A-Fa-f]{8,})',
            r'(?:0x)?([0-9A-Fa-f]{12,})'
        ]
        
        # DID explanations
        self.did_explanations = {
            'F186': 'Active Diagnostic Session',
            'F187': 'ECU Manufacturing Date',
            'F188': 'ECU Serial Number',
            'F189': 'ECU Software Version',
            'F190': 'Vehicle VIN',
            'F191': 'ECU Hardware Version',
            'F192': 'ECU Software Version/Date',
            'F193': 'System Supplier ID',
            'F194': 'ECU Manufacturing Date',
            'F195': 'ECU Installation Date',
            'F196': 'ECU Installation Date/Time',
            'F197': 'System Supplier ECU Software Version',
            'F198': 'System Supplier ECU Software Version',
            'DE00': 'Vehicle Speed Sensor',
            'DE01': 'Engine Temperature',
            'DE02': 'Battery Voltage',
            'DE03': 'Engine Load',
            'DE04': 'Throttle Position',
            'DE05': 'Fuel System Status',
            'DE06': 'Engine RPM',
            'DE07': 'Diagnostic Readiness',
            'DE08': 'Oxygen Sensor Data',
            'DE09': 'Fuel Pressure',
            'DE0A': 'Intake Manifold Pressure',
            'DE0B': 'Engine Runtime',
            'DE0C': 'Distance with MIL On',
            'DE12': 'Powertrain Data'
        }
        
        # NRC code explanations
        self.nrc_codes = {
            '10': 'General Reject',
            '11': 'Service Not Supported',
            '12': 'SubFunction Not Supported',
            '13': 'Incorrect Message Length',
            '14': 'Response Too Long',
            '21': 'Busy Repeat Request',
            '22': 'Conditions Not Correct',
            '24': 'Request Sequence Error',
            '25': 'No Response From SubNet Component',
            '26': 'Failure Prevents Execution Of Requested Action',
            '31': 'Request Out Of Range',
            '33': 'Security Access Denied',
            '35': 'Invalid Key',
            '36': 'Exceed Number Of Attempts',
            '37': 'Required Time Delay Not Expired',
            '70': 'Upload Download Not Accepted',
            '71': 'Transfer Data Suspended',
            '72': 'General Programming Failure',
            '73': 'Wrong Block Sequence Counter',
            '78': 'Request Correctly Received - Response Pending',
            '7E': 'SubFunction Not Supported In Active Session',
            '7F': 'Service Not Supported In Active Session'
        }
        
    def extract_critical_diagnostics(self, results: List[Dict]) -> Dict[str, Any]:
        """
        Extract all critical diagnostic information from results
        """
        critical_data = {
            'vehicle_info': self._extract_vehicle_info(results),
            'voltage_status': self._extract_voltage_status(results),
            'dtc_analysis': self._extract_dtc_analysis(results),
            'error_analysis': self._extract_error_analysis(results),
            'success_analysis': self._extract_success_analysis(results),
            'did_responses': self._extract_did_responses(results),
            'hex_communications': self._extract_hex_communications(results),
            'proximate_cause': self._analyze_proximate_cause(results),
            'timeline': self._build_diagnostic_timeline(results)
        }
        
        # Guard: Never return a boolean, always a dict
        if isinstance(critical_data, dict):
            return critical_data
        else:
            import logging
            logging.error(f"BUG: extract_critical_diagnostics would return non-dict: {type(critical_data)} value={critical_data}")
            return {}  # Always return a dict
    
    def _extract_vehicle_info(self, results: List[Dict]) -> Dict[str, Any]:
        """Extract vehicle identification information"""
        vehicle_info = {
            'vin': None,
            'vin_source': None,
            'vin_confidence': 'unknown'
        }
        
        for i, result in enumerate(results):
            result_str = str(result).upper()
            
            # Look for VIN patterns
            for pattern in self.vin_patterns:
                match = re.search(pattern, result_str, re.IGNORECASE)
                if match:
                    potential_vin = match.group(1)
                    if self._validate_vin(potential_vin):
                        vehicle_info['vin'] = potential_vin
                        vehicle_info['vin_source'] = f"Line {i+1}"
                        vehicle_info['vin_confidence'] = 'high'
                        break
            
            if vehicle_info['vin']:
                break
        
        return vehicle_info
    
    def _validate_vin(self, vin: str) -> bool:
        """Validate VIN format"""
        if len(vin) != 17:
            return False
        
        # VIN should not contain I, O, Q
        forbidden_chars = ['I', 'O', 'Q']
        for char in forbidden_chars:
            if char in vin.upper():
                return False
        
        # Should contain mix of letters and numbers
        has_letters = any(c.isalpha() for c in vin)
        has_numbers = any(c.isdigit() for c in vin)
        
        return has_letters and has_numbers
    
    def _extract_voltage_status(self, results: List[Dict]) -> Dict[str, Any]:
        """Extract battery/system voltage information"""
        voltage_data = {
            'readings': [],
            'status': 'unknown',
            'message': 'No voltage data found',
            'average': None,
            'min_voltage': None,
            'max_voltage': None,
            'critical_events': []
        }
        
        for i, result in enumerate(results):
            result_str = str(result)
            
            # Look for voltage patterns
            for pattern in self.voltage_patterns:
                matches = re.finditer(pattern, result_str, re.IGNORECASE)
                for match in matches:
                    try:
                        if 'DE02' in pattern:
                            # Convert hex to voltage
                            hex_val = match.group(1)
                            voltage = int(hex_val, 16) / 10.0  # Common conversion
                        else:
                            voltage = float(match.group(1))
                        
                        if 8.0 <= voltage <= 16.0:  # Reasonable voltage range
                            voltage_data['readings'].append({
                                'voltage': voltage,
                                'line': i + 1,
                                'context': result_str[:100]
                            })
                            
                            # Check for critical voltage events
                            if voltage < 11.0:
                                voltage_data['critical_events'].append({
                                    'line': i + 1,
                                    'voltage': voltage,
                                    'severity': 'critical',
                                    'message': f'Critical low voltage: {voltage}V'
                                })
                            elif voltage > 14.5:
                                voltage_data['critical_events'].append({
                                    'line': i + 1,
                                    'voltage': voltage,
                                    'severity': 'warning',
                                    'message': f'High voltage detected: {voltage}V'
                                })
                    except (ValueError, IndexError):
                        continue
        
        # Analyze voltage readings
        if voltage_data['readings']:
            voltages = [r['voltage'] for r in voltage_data['readings']]
            voltage_data['average'] = sum(voltages) / len(voltages)
            voltage_data['min_voltage'] = min(voltages)
            voltage_data['max_voltage'] = max(voltages)
            
            # Determine status
            avg_voltage = voltage_data['average']
            if avg_voltage < 11.0:
                voltage_data['status'] = 'critical'
                voltage_data['message'] = f'CRITICAL: Battery voltage critically low ({avg_voltage:.1f}V)'
            elif avg_voltage < 12.0:
                voltage_data['status'] = 'warning'
                voltage_data['message'] = f'WARNING: Battery voltage low ({avg_voltage:.1f}V)'
            elif avg_voltage > 14.5:
                voltage_data['status'] = 'warning'
                voltage_data['message'] = f'WARNING: Charging system voltage high ({avg_voltage:.1f}V)'
            else:
                voltage_data['status'] = 'good'
                voltage_data['message'] = f'Battery voltage normal ({avg_voltage:.1f}V)'
        
        return voltage_data
    
    def _extract_dtc_analysis(self, results: List[Dict]) -> Dict[str, Any]:
        """Extract and analyze Diagnostic Trouble Codes"""
        dtc_data = {
            'active_dtcs': [],
            'pending_dtcs': [],
            'cleared_dtcs': [],
            'dtc_summary': {},
            'critical_codes': []
        }
        
        for i, result in enumerate(results):
            result_str = str(result)
            
            # Look for DTC patterns
            for pattern in self.dtc_patterns:
                matches = re.finditer(pattern, result_str, re.IGNORECASE)
                for match in matches:
                    dtc_code = match.group(1).upper()
                    
                    # Determine DTC status from context
                    status = 'active'
                    if 'cleared' in result_str.lower() or 'clear' in result_str.lower():
                        status = 'cleared'
                    elif 'pending' in result_str.lower():
                        status = 'pending'
                    
                    dtc_entry = {
                        'code': dtc_code,
                        'line': i + 1,
                        'status': status,
                        'context': result_str[:200],
                        'description': self._get_dtc_description(dtc_code),
                        'severity': self._assess_dtc_severity(dtc_code)
                    }
                    
                    # Add to appropriate list
                    if status == 'active':
                        dtc_data['active_dtcs'].append(dtc_entry)
                    elif status == 'pending':
                        dtc_data['pending_dtcs'].append(dtc_entry)
                    elif status == 'cleared':
                        dtc_data['cleared_dtcs'].append(dtc_entry)
                    
                    # Track critical codes
                    if dtc_entry['severity'] == 'critical':
                        dtc_data['critical_codes'].append(dtc_entry)
        
        # Create summary
        total_dtcs = len(dtc_data['active_dtcs']) + len(dtc_data['pending_dtcs'])
        dtc_data['dtc_summary'] = {
            'total_active': len(dtc_data['active_dtcs']),
            'total_pending': len(dtc_data['pending_dtcs']),
            'total_cleared': len(dtc_data['cleared_dtcs']),
            'total_critical': len(dtc_data['critical_codes']),
            'health_status': 'good' if total_dtcs == 0 else 'warning' if total_dtcs < 3 else 'critical'
        }
        
        return dtc_data
    
    def _get_dtc_description(self, dtc_code: str) -> str:
        """Get description for DTC code"""
        # Basic DTC code interpretation
        if dtc_code.startswith('P'):
            return f"Powertrain code - Engine/transmission system issue"
        elif dtc_code.startswith('B'):
            return f"Body code - Body control system issue"
        elif dtc_code.startswith('C'):
            return f"Chassis code - Suspension/brake system issue"
        elif dtc_code.startswith('U'):
            return f"Network code - Communication system issue"
        else:
            return f"Diagnostic trouble code"
    
    def _assess_dtc_severity(self, dtc_code: str) -> str:
        """Assess severity of DTC code"""
        # Critical codes that indicate serious safety issues
        critical_prefixes = ['P0300', 'P0301', 'P0302', 'P0303', 'P0304', 'P0420', 'U']
        
        for prefix in critical_prefixes:
            if dtc_code.startswith(prefix):
                return 'critical'
        
        return 'warning'
    
    def _extract_error_analysis(self, results: List[Dict]) -> Dict[str, Any]:
        """Extract and categorize all errors and failures"""
        error_data = {
            'communication_errors': [],
            'system_errors': [],
            'programming_errors': [],
            'timeout_errors': [],
            'nrc_errors': [],
            'error_summary': {}
        }
        
        for i, result in enumerate(results):
            result_str = str(result)
            result_lower = result_str.lower()
            
            # Check for various error types
            if any(keyword in result_lower for keyword in ['error', 'fail', 'exception', 'not successful']):
                error_entry = {
                    'line': i + 1,
                    'text': result_str,
                    'type': 'general',
                    'severity': 'warning'
                }
                
                # Categorize error type
                if any(keyword in result_lower for keyword in ['communication', 'comm', 'timeout', 'no response']):
                    error_entry['type'] = 'communication'
                    error_data['communication_errors'].append(error_entry)
                elif any(keyword in result_lower for keyword in ['programming', 'flash', 'update']):
                    error_entry['type'] = 'programming'
                    error_data['programming_errors'].append(error_entry)
                elif 'timeout' in result_lower:
                    error_entry['type'] = 'timeout'
                    error_data['timeout_errors'].append(error_entry)
                elif 'nrc' in result_lower:
                    error_entry['type'] = 'nrc'
                    # Extract NRC code
                    nrc_match = re.search(r'NRC[:\s=]*([0-9A-Fa-f]{2})', result_str, re.IGNORECASE)
                    if nrc_match:
                        nrc_code = nrc_match.group(1).upper()
                        error_entry['nrc_code'] = nrc_code
                        error_entry['nrc_description'] = self.nrc_codes.get(nrc_code, 'Unknown NRC')
                    error_data['nrc_errors'].append(error_entry)
                else:
                    error_data['system_errors'].append(error_entry)
        
        # Create summary
        total_errors = (len(error_data['communication_errors']) + 
                       len(error_data['system_errors']) + 
                       len(error_data['programming_errors']) + 
                       len(error_data['timeout_errors']) + 
                       len(error_data['nrc_errors']))
        
        error_data['error_summary'] = {
            'total_errors': total_errors,
            'communication_issues': len(error_data['communication_errors']),
            'system_issues': len(error_data['system_errors']),
            'programming_issues': len(error_data['programming_errors']),
            'timeout_issues': len(error_data['timeout_errors']),
            'nrc_issues': len(error_data['nrc_errors']),
            'health_status': 'good' if total_errors == 0 else 'warning' if total_errors < 5 else 'critical'
        }
        
        return error_data
    
    def _extract_success_analysis(self, results: List[Dict]) -> Dict[str, Any]:
        """Extract and categorize successful operations"""
        success_data = {
            'successful_operations': [],
            'completed_tests': [],
            'successful_communications': [],
            'success_summary': {}
        }
        
        for i, result in enumerate(results):
            result_str = str(result)
            result_lower = result_str.lower()
            
            # Check for success indicators
            if any(keyword in result_lower for keyword in ['success', 'pass', 'complete', 'ok', 'successful']):
                # Make sure it's not actually an error
                if not any(keyword in result_lower for keyword in ['error', 'fail', 'not successful']):
                    success_entry = {
                        'line': i + 1,
                        'text': result_str,
                        'type': 'general'
                    }
                    
                    # Categorize success type
                    if any(keyword in result_lower for keyword in ['test', 'check']):
                        success_entry['type'] = 'test'
                        success_data['completed_tests'].append(success_entry)
                    elif any(keyword in result_lower for keyword in ['communication', 'response', 'diag']):
                        success_entry['type'] = 'communication'
                        success_data['successful_communications'].append(success_entry)
                    else:
                        success_data['successful_operations'].append(success_entry)
        
        # Create summary
        total_successes = (len(success_data['successful_operations']) + 
                          len(success_data['completed_tests']) + 
                          len(success_data['successful_communications']))
        
        success_data['success_summary'] = {
            'total_successes': total_successes,
            'successful_operations': len(success_data['successful_operations']),
            'completed_tests': len(success_data['completed_tests']),
            'successful_communications': len(success_data['successful_communications'])
        }
        
        return success_data
    
    def _extract_did_responses(self, results: List[Dict]) -> Dict[str, Any]:
        """Extract DID (Data Identifier) requests and responses"""
        did_data = {
            'did_transactions': [],
            'changing_dids': [],
            'failed_dids': [],
            'did_summary': {}
        }
        
        current_request = None
        
        for i, result in enumerate(results):
            result_str = str(result)
            
            # Look for DID patterns
            for pattern in self.did_patterns:
                matches = re.finditer(pattern, result_str, re.IGNORECASE)
                for match in matches:
                    if 'request' in result_str.lower():
                        current_request = {
                            'line': i + 1,
                            'request_data': match.group(0),
                            'hex_data': match.group(1) if len(match.groups()) >= 1 else match.group(0)
                        }
                    elif 'response' in result_str.lower() and current_request:
                        response_data = {
                            'request_line': current_request['line'],
                            'response_line': i + 1,
                            'request_data': current_request['request_data'],
                            'response_data': match.group(0),
                            'hex_data': match.group(1) if len(match.groups()) >= 1 else match.group(0),
                            'did_code': self._extract_did_code(current_request['hex_data']),
                            'explanation': self._explain_did_transaction(current_request['hex_data'], match.group(0))
                        }
                        
                        did_data['did_transactions'].append(response_data)
                        current_request = None
            
            # Look for DID codes directly
            did_match = re.search(r'\b(DE[0-9A-Fa-f]{2}|F1[0-9A-Fa-f]{2})\b', result_str, re.IGNORECASE)
            if did_match:
                did_code = did_match.group(1).upper()
                if did_code in self.did_explanations:
                    # Check if this DID is changing/being modified
                    if any(keyword in result_str.lower() for keyword in ['write', 'set', 'update', 'config', 'change']):
                        did_data['changing_dids'].append({
                            'line': i + 1,
                            'did_code': did_code,
                            'description': self.did_explanations[did_code],
                            'context': result_str,
                            'change_type': 'write' if 'write' in result_str.lower() else 'update'
                        })
        
        # Create summary
        did_data['did_summary'] = {
            'total_transactions': len(did_data['did_transactions']),
            'changing_dids': len(did_data['changing_dids']),
            'failed_dids': len(did_data['failed_dids'])
        }
        
        return did_data
    
    def _extract_did_code(self, hex_data: str) -> str:
        """Extract DID code from hex data"""
        # Look for DID pattern in hex data
        did_match = re.search(r'(DE[0-9A-Fa-f]{2}|F1[0-9A-Fa-f]{2})', hex_data, re.IGNORECASE)
        if did_match:
            return did_match.group(1).upper()
        return 'Unknown'
    
    def _explain_did_transaction(self, request_hex: str, response_hex: str) -> str:
        """Explain what a DID transaction means"""
        did_code = self._extract_did_code(request_hex)
        if did_code in self.did_explanations:
            return f"Reading {self.did_explanations[did_code]} - {did_code}"
        return f"Data identifier transaction - {did_code}"
    
    def _extract_hex_communications(self, results: List[Dict]) -> Dict[str, Any]:
        """Extract hex/ASCII communications with explanations"""
        hex_data = {
            'communications': [],
            'hex_patterns': [],
            'ascii_discoveries': [],
            'communication_summary': {}
        }
        
        for i, result in enumerate(results):
            result_str = str(result)
            
            # Look for hex communication patterns
            for pattern in self.hex_communication_patterns:
                matches = re.finditer(pattern, result_str, re.IGNORECASE)
                for match in matches:
                    hex_value = match.group(1)
                    
                    communication_entry = {
                        'line': i + 1,
                        'hex_data': hex_value,
                        'context': result_str,
                        'explanation': self._explain_hex_communication(hex_value),
                        'ascii_interpretation': self._hex_to_ascii(hex_value),
                        'protocol_analysis': self._analyze_protocol(hex_value)
                    }
                    
                    hex_data['communications'].append(communication_entry)
                    
                    # Check for ASCII content
                    ascii_content = self._hex_to_ascii(hex_value)
                    if ascii_content and len(ascii_content) >= 3:
                        hex_data['ascii_discoveries'].append({
                            'line': i + 1,
                            'hex_data': hex_value,
                            'ascii_text': ascii_content,
                            'context': result_str[:100]
                        })
        
        # Create summary
        hex_data['communication_summary'] = {
            'total_communications': len(hex_data['communications']),
            'ascii_discoveries': len(hex_data['ascii_discoveries'])
        }
        
        return hex_data
    
    def _explain_hex_communication(self, hex_data: str) -> str:
        """Explain what hex communication data means"""
        if not hex_data:
            return "No data"
        
        clean_hex = hex_data.replace('0x', '').replace(' ', '').upper()
        explanations = []
        
        # Analyze based on length and patterns
        if len(clean_hex) >= 12:
            # Ford diagnostic pattern
            if clean_hex.startswith('0000'):
                explanations.append("🚗 Ford Vehicle Diagnostic Communication")
                
                # ECU identifier
                if len(clean_hex) >= 6:
                    ecu_id = clean_hex[4:6]
                    if ecu_id == '7D':
                        explanations.append("📱 Infotainment System (SYNC/Radio)")
                    elif ecu_id == '7E':
                        explanations.append("🏎️ Engine Control Module (PCM)")
                    elif ecu_id == '75':
                        explanations.append("🔧 Body Control Module")
                    else:
                        explanations.append(f"🔧 Vehicle Module {ecu_id}")
                
                # Service identifier
                if len(clean_hex) >= 8:
                    service_id = clean_hex[6:8]
                    if service_id == '22':
                        explanations.append("📖 Data Request Service")
                    elif service_id == '19':
                        explanations.append("🔍 DTC Request Service")
                    elif service_id == '14':
                        explanations.append("🗑️ Clear DTC Service")
                    elif service_id == '10':
                        explanations.append("🔐 Session Control Service")
                    else:
                        explanations.append(f"⚙️ Service {service_id}")
        
        # Look for specific patterns
        if 'CB' in clean_hex:
            explanations.append("📋 Configuration Block Data")
        if clean_hex.endswith('00'):
            explanations.append("✅ Success Status")
        if 'FF' in clean_hex:
            explanations.append("🔧 Broadcast/All Modules")
        
        return " | ".join(explanations) if explanations else f"Diagnostic Data: {clean_hex[:16]}..."
    
    def _hex_to_ascii(self, hex_data: str) -> str:
        """Convert hex data to ASCII if possible"""
        try:
            clean_hex = hex_data.replace('0x', '').replace(' ', '')
            if len(clean_hex) % 2 != 0:
                return ""
            
            ascii_chars = []
            for i in range(0, len(clean_hex), 2):
                byte_hex = clean_hex[i:i+2]
                byte_val = int(byte_hex, 16)
                if 32 <= byte_val <= 126:  # Printable ASCII
                    ascii_chars.append(chr(byte_val))
                else:
                    ascii_chars.append('.')
            
            ascii_text = ''.join(ascii_chars)
            # Only return if we have substantial readable content
            readable_count = sum(1 for c in ascii_text if c.isalnum())
            if readable_count >= 3:
                return ascii_text
        except (ValueError, IndexError):
            pass
        
        return ""
    
    def _analyze_protocol(self, hex_data: str) -> Dict[str, str]:
        """Analyze communication protocol"""
        analysis = {
            'protocol': 'Unknown',
            'direction': 'Unknown',
            'service_type': 'Unknown'
        }
        
        clean_hex = hex_data.replace('0x', '').replace(' ', '').upper()
        
        # Determine protocol
        if clean_hex.startswith('0000'):
            analysis['protocol'] = 'UDS (Unified Diagnostic Services)'
        elif len(clean_hex) >= 6:
            analysis['protocol'] = 'CAN Diagnostic'
        
        # Determine direction and service
        if len(clean_hex) >= 8:
            service_byte = clean_hex[6:8]
            if service_byte in ['22', '19', '14', '10']:
                analysis['direction'] = 'Request'
            elif service_byte.startswith('6') or service_byte.startswith('5'):
                analysis['direction'] = 'Response'
            
            # Service type
            service_map = {
                '22': 'Read Data By Identifier',
                '19': 'Read DTC Information',
                '14': 'Clear Diagnostic Information',
                '10': 'Diagnostic Session Control',
                '62': 'Read Data Response',
                '59': 'DTC Information Response'
            }
            analysis['service_type'] = service_map.get(service_byte, f'Service {service_byte}')
        
        return analysis
    
    def _analyze_proximate_cause(self, results: List[Dict]) -> Dict[str, Any]:
        """Analyze the most likely root cause with evidence"""
        cause_analysis = {
            'primary_cause': 'Unknown',
            'confidence': 'low',
            'evidence': [],
            'recommendations': [],
            'risk_level': 'medium'
        }
        
        # Collect evidence
        error_patterns = []
        communication_issues = 0
        voltage_issues = 0
        dtc_count = 0
        programming_issues = 0
        
        for i, result in enumerate(results):
            result_str = str(result).lower()
            
            # Count different types of issues
            if any(keyword in result_str for keyword in ['communication', 'timeout', 'no response']):
                communication_issues += 1
                error_patterns.append('communication')
            
            if any(keyword in result_str for keyword in ['voltage', 'battery']):
                voltage_issues += 1
                error_patterns.append('power')
            
            if any(keyword in result_str for keyword in ['dtc', 'trouble code']):
                dtc_count += 1
                error_patterns.append('dtc')
            
            if any(keyword in result_str for keyword in ['programming', 'flash', 'update']):
                programming_issues += 1
                error_patterns.append('programming')
        
        # Analyze patterns and determine primary cause
        if communication_issues >= 3:
            cause_analysis['primary_cause'] = 'Communication System Failure'
            cause_analysis['confidence'] = 'high'
            cause_analysis['evidence'].append(f"Multiple communication failures detected ({communication_issues} instances)")
            cause_analysis['recommendations'].extend([
                "Check CAN bus integrity and termination",
                "Verify module connections and power supply",
                "Test for electromagnetic interference"
            ])
            cause_analysis['risk_level'] = 'high'
        
        elif voltage_issues >= 2:
            cause_analysis['primary_cause'] = 'Electrical System Issue'
            cause_analysis['confidence'] = 'high'
            cause_analysis['evidence'].append(f"Power supply problems detected ({voltage_issues} instances)")
            cause_analysis['recommendations'].extend([
                "Test battery voltage and charging system",
                "Check for loose connections",
                "Verify power supply stability during diagnostics"
            ])
            cause_analysis['risk_level'] = 'high'
        
        elif programming_issues >= 2:
            cause_analysis['primary_cause'] = 'Software/Programming Issue'
            cause_analysis['confidence'] = 'medium'
            cause_analysis['evidence'].append(f"Programming-related issues detected ({programming_issues} instances)")
            cause_analysis['recommendations'].extend([
                "Verify software compatibility",
                "Check programming preconditions",
                "Ensure stable power during programming"
            ])
            cause_analysis['risk_level'] = 'medium'
        
        elif dtc_count >= 2:
            cause_analysis['primary_cause'] = 'Multiple System Faults'
            cause_analysis['confidence'] = 'medium'
            cause_analysis['evidence'].append(f"Multiple diagnostic trouble codes present ({dtc_count} codes)")
            cause_analysis['recommendations'].extend([
                "Address DTCs in order of severity",
                "Perform system-wide diagnostic scan",
                "Check for common failure modes"
            ])
            cause_analysis['risk_level'] = 'medium'
        
        else:
            cause_analysis['primary_cause'] = 'Normal Operation with Minor Issues'
            cause_analysis['confidence'] = 'low'
            cause_analysis['evidence'].append("No major patterns detected")
            cause_analysis['recommendations'].append("Continue monitoring for emerging issues")
            cause_analysis['risk_level'] = 'low'
        
        return cause_analysis
    
    def _build_diagnostic_timeline(self, results: List[Dict]) -> List[Dict]:
        """Build a chronological timeline of key diagnostic events"""
        import re
        timeline = []
        
        for i, result in enumerate(results):
            result_str = str(result)
            
            # Extract timestamp if present (HH:MM:SS format)
            timestamp_match = re.search(r'(\d{2}:\d{2}:\d{2})', result_str)
            timestamp = timestamp_match.group(1) if timestamp_match else f"Line {i + 1}"
            
            # Identify significant events with specific details
            event_type = None
            significance = 'low'
            description = result_str[:150]
            
            # Check for ApplicationState changes
            if 'ApplicationState' in result_str:
                state_match = re.search(r'ApplicationState.*?to\s+(\w+)', result_str, re.IGNORECASE)
                if state_match:
                    state = state_match.group(1)
                    event_type = 'Application State'
                    significance = 'high'
                    description = f"ApplicationState set to {state}"
                    
            # Check for NRC 31 errors with DID
            elif 'NRC 31' in result_str or 'nrc_31' in result_str.lower():
                did_match = re.search(r'(?:DID|did)\s*[:\s]*([0-9A-Fa-f]{4})', result_str)
                event_type = 'NRC 31 Error'
                significance = 'high'
                if did_match:
                    description = f"NRC 31 error (DID {did_match.group(1)})"
                else:
                    description = "NRC 31 error detected"
                    
            # Check for ValidateFlashAction
            elif 'ValidateFlashAction' in result_str:
                if 'FAIL' in result_str.upper():
                    event_type = 'Flash Validation'
                    significance = 'high'
                    description = "ValidateFlashAction → FAIL"
                elif 'PASS' in result_str.upper():
                    event_type = 'Flash Validation'
                    significance = 'high'
                    description = "ValidateFlashAction → PASS"
                    
            # Check for DTCs
            elif any(keyword in result_str for keyword in ['DTC', 'trouble code']):
                dtc_match = re.search(r'([PCBU][0-9A-F]{4})', result_str)
                event_type = 'DTC Event'
                significance = 'high'
                if dtc_match:
                    description = f"DTC detected: {dtc_match.group(1)}"
                else:
                    description = "DTC event"
                    
            # Check for software mismatches
            elif 'software' in result_str.lower() and 'mismatch' in result_str.lower():
                did_match = re.search(r'([0-9A-F]{4})', result_str)
                event_type = 'Software Mismatch'
                significance = 'high'
                if did_match:
                    description = f"Software mismatch at DID {did_match.group(1)}"
                else:
                    description = "Software version mismatch"
                    
            # Check for programming/flash events
            elif any(keyword in result_str.lower() for keyword in ['programming', 'flash', 'reprogram']):
                event_type = 'Programming Event'
                significance = 'high'
                if 'start' in result_str.lower():
                    description = "Flash programming started"
                elif 'complete' in result_str.lower() or 'finish' in result_str.lower():
                    description = "Flash programming completed"
                else:
                    description = "Flash programming event"
                    
            # Check for voltage/power events
            elif any(keyword in result_str.lower() for keyword in ['voltage', 'battery']):
                event_type = 'Power Event'
                significance = 'medium'
                volt_match = re.search(r'(\d+\.?\d*)\s*[Vv]', result_str)
                if volt_match:
                    description = f"Voltage: {volt_match.group(1)}V"
                else:
                    description = "Power/voltage event"
            
            if event_type:
                timeline.append({
                    'line': i + 1,
                    'event_type': event_type,
                    'significance': significance,
                    'description': description,
                    'timestamp': timestamp
                })
        
        return timeline


def format_critical_diagnostics_report(critical_data: Dict[str, Any]) -> str:
    """
    Format the critical diagnostics data into a comprehensive report
    """
    # Safety check: ensure critical_data is a dict
    if not isinstance(critical_data, dict):
        return f"⚠️ ERROR: Invalid critical diagnostics data (type: {type(critical_data).__name__})\n"
    
    report_lines = []
    
    # Header
    report_lines.extend([
        "╔" + "═" * 98 + "╗",
        "║" + " " * 30 + "🚨 CRITICAL DIAGNOSTIC OVERVIEW" + " " * 36 + "║",
        "║" + " " * 25 + f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}" + " " * 32 + "║",
        "╚" + "═" * 98 + "╝",
        ""
    ])
    
    # 1. VEHICLE IDENTIFICATION
    vehicle_info = critical_data.get('vehicle_info', {})
    report_lines.extend([
        "🚗 VEHICLE IDENTIFICATION",
        "=" * 100,
        ""
    ])
    
    if vehicle_info.get('vin'):
        report_lines.extend([
            f"VIN: {vehicle_info['vin']} (Found at {vehicle_info.get('vin_source', 'Unknown location')})",
            f"Confidence: {vehicle_info.get('vin_confidence', 'unknown').title()}",
            ""
        ])
    else:
        report_lines.extend([
            "❌ VIN: Not detected in diagnostic data",
            "⚠️  Recommendation: Verify vehicle connection and retry VIN read",
            ""
        ])
    
    # 2. VOLTAGE STATUS
    voltage_data = critical_data.get('voltage_status', {})
    # Safety check: ensure voltage_data is a dict
    if not isinstance(voltage_data, dict):
        voltage_data = {}
    
    report_lines.extend([
        "🔋 BATTERY/VOLTAGE STATUS",
        "=" * 100,
        ""
    ])
    
    if voltage_data.get('readings'):
        status_icon = "✅" if voltage_data.get('status') == 'good' else "⚠️" if voltage_data.get('status') == 'warning' else "❌"
        report_lines.extend([
            f"{status_icon} Status: {voltage_data.get('message', 'Unknown')}",
            f"📊 Statistics:",
            f"  • Average Voltage: {voltage_data.get('average', 0):.2f}V",
            f"  • Voltage Range: {voltage_data.get('min_voltage', 0):.2f}V - {voltage_data.get('max_voltage', 0):.2f}V",
            f"  • Total Readings: {len(voltage_data.get('readings', []))}",
            ""
        ])
        
        # Critical voltage events
        if voltage_data.get('critical_events'):
            report_lines.append("🚨 Critical Voltage Events:")
            for event in voltage_data.get('critical_events', [])[:5]:  # Show first 5
                report_lines.append(f"  • Line {event['line']}: {event['message']}")
            report_lines.append("")
    else:
        report_lines.extend([
            "❌ No voltage data detected in diagnostic log",
            "⚠️  Check: Battery monitoring may not be active",
            ""
        ])
    
    # 3. DTC ANALYSIS
    dtc_data = critical_data.get('dtc_analysis', {})
    # Safety check: ensure dtc_data is a dict
    if not isinstance(dtc_data, dict):
        dtc_data = {}
    
    report_lines.extend([
        "🔧 DIAGNOSTIC TROUBLE CODES (DTCs)",
        "=" * 100,
        ""
    ])
    
    summary = dtc_data.get('dtc_summary', {})
    if summary.get('total_active', 0) > 0 or summary.get('total_pending', 0) > 0:
        health_icon = "❌" if summary.get('health_status') == 'critical' else "⚠️" if summary.get('health_status') == 'warning' else "✅"
        report_lines.extend([
            f"{health_icon} DTC Summary:",
            f"  • Active DTCs: {summary.get('total_active', 0)}",
            f"  • Pending DTCs: {summary.get('total_pending', 0)}",
            f"  • Cleared DTCs: {summary.get('total_cleared', 0)}",
            f"  • Critical Codes: {summary.get('total_critical', 0)}",
            ""
        ])
        
        # Show active DTCs
        if dtc_data.get('active_dtcs'):
            report_lines.append("🚨 Active Diagnostic Trouble Codes:")
            for dtc in dtc_data.get('active_dtcs', [])[:10]:  # Show first 10
                if isinstance(dtc, dict):
                    severity_icon = "🔥" if dtc.get('severity') == 'critical' else "⚠️"
                    report_lines.append(f"  {severity_icon} {dtc.get('code', 'Unknown')}: {dtc.get('description', 'No description')} (Line {dtc.get('line', '?')})")
            report_lines.append("")
        
        # Show critical codes
        if dtc_data.get('critical_codes'):
            report_lines.append("🔥 Critical DTCs Requiring Immediate Attention:")
            for dtc in dtc_data.get('critical_codes', []):
                if isinstance(dtc, dict):
                    report_lines.append(f"  • {dtc.get('code', 'Unknown')}: {dtc.get('description', 'No description')} (Line {dtc.get('line', '?')})")
            report_lines.append("")
    else:
        report_lines.extend([
            "✅ No active diagnostic trouble codes detected",
            "✅ Vehicle systems reporting normal operation",
            ""
        ])
    
    # 4. ERROR ANALYSIS
    error_data = critical_data.get('error_analysis', {})
    # Safety check: ensure error_data is a dict
    if not isinstance(error_data, dict):
        error_data = {}
    
    report_lines.extend([
        "❌ FAILED OPERATIONS & ERRORS",
        "=" * 100,
        ""
    ])
    
    error_summary = error_data.get('error_summary', {})
    if error_summary.get('total_errors', 0) > 0:
        health_icon = "❌" if error_summary.get('health_status') == 'critical' else "⚠️"
        report_lines.extend([
            f"{health_icon} Error Summary:",
            f"  • Total Errors: {error_summary.get('total_errors', 0)}",
            f"  • Communication Issues: {error_summary.get('communication_issues', 0)}",
            f"  • System Issues: {error_summary.get('system_issues', 0)}",
            f"  • Programming Issues: {error_summary.get('programming_issues', 0)}",
            f"  • Timeout Issues: {error_summary.get('timeout_issues', 0)}",
            f"  • NRC (Negative Response) Issues: {error_summary.get('nrc_issues', 0)}",
            ""
        ])
        
        # Show communication errors
        if error_data.get('communication_errors'):
            report_lines.append("📡 Communication Errors:")
            for error in error_data.get('communication_errors', [])[:5]:  # Show first 5
                if isinstance(error, dict):
                    error_text = str(error.get('text', ''))[:80]
                    report_lines.append(f"  • Line {error.get('line', '?')}: {error_text}...")
            report_lines.append("")
        
        # Show NRC errors
        if error_data.get('nrc_errors'):
            report_lines.append("🚫 Negative Response Code (NRC) Errors:")
            for error in error_data.get('nrc_errors', [])[:5]:  # Show first 5
                if isinstance(error, dict):
                    nrc_desc = error.get('nrc_description', 'Unknown NRC')
                    report_lines.append(f"  • Line {error.get('line', '?')}: NRC {error.get('nrc_code', '??')} - {nrc_desc}")
            report_lines.append("")
    else:
        report_lines.extend([
            "✅ No errors detected in diagnostic operations",
            "✅ All systems responding normally",
            ""
        ])
    
    # 5. SUCCESS OPERATIONS
    success_data = critical_data.get('success_analysis', {})
    report_lines.extend([
        "✅ SUCCESSFUL OPERATIONS",
        "=" * 100,
        ""
    ])
    
    success_summary = success_data.get('success_summary', {})
    if success_summary.get('total_successes', 0) > 0:
        report_lines.extend([
            f"✅ Success Summary:",
            f"  • Total Successful Operations: {success_summary.get('total_successes', 0)}",
            f"  • Completed Tests: {success_summary.get('completed_tests', 0)}",
            f"  • Successful Communications: {success_summary.get('successful_communications', 0)}",
            ""
        ])
    else:
        report_lines.extend([
            "❓ No clear success indicators found",
            ""
        ])
    
    # 6. DID RESPONSES (Data Identifiers)
    did_data = critical_data.get('did_responses', {})
    report_lines.extend([
        "📋 DATA IDENTIFIER (DID) RESPONSES",
        "=" * 100,
        ""
    ])
    
    did_summary = did_data.get('did_summary', {})
    if did_summary.get('total_transactions', 0) > 0:
        report_lines.extend([
            f"📊 DID Transaction Summary:",
            f"  • Total DID Transactions: {did_summary.get('total_transactions', 0)}",
            f"  • DIDs Being Changed: {did_summary.get('changing_dids', 0)}",
            f"  • Failed DID Operations: {did_summary.get('failed_dids', 0)}",
            ""
        ])
        
        # Show changing DIDs
        if did_data.get('changing_dids'):
            report_lines.append("🔄 DIDs Being Modified/Changed:")
            for did in did_data.get('changing_dids', [])[:10]:  # Show first 10
                if isinstance(did, dict):
                    report_lines.append(f"  • {did.get('did_code', 'Unknown')}: {did.get('description', 'No description')} ({did.get('change_type', 'unknown').title()} operation)")
            report_lines.append("")
        
        # Show some DID transactions
        if did_data.get('did_transactions'):
            report_lines.append("📡 Recent DID Transactions:")
            for did in did_data.get('did_transactions', [])[:5]:  # Show first 5
                if isinstance(did, dict):
                    report_lines.append(f"  • Line {did.get('response_line', '?')}: {did.get('explanation', 'No explanation')}")
            report_lines.append("")
    else:
        report_lines.extend([
            "❓ No DID transactions detected",
            ""
        ])
    
    # 7. HEX/ASCII COMMUNICATION
    hex_data = critical_data.get('hex_communications', {})
    report_lines.extend([
        "🔍 HEX/ASCII COMMUNICATION ANALYSIS",
        "=" * 100,
        ""
    ])
    
    hex_summary = hex_data.get('communication_summary', {})
    if hex_summary.get('total_communications', 0) > 0:
        report_lines.extend([
            f"📡 Communication Summary:",
            f"  • Total Hex Communications: {hex_summary.get('total_communications', 0)}",
            f"  • ASCII Text Discoveries: {hex_summary.get('ascii_discoveries', 0)}",
            ""
        ])
        
        # Show key communications with explanations
        if hex_data.get('communications'):
            report_lines.append("🔍 Key Communications & Explanations:")
            for comm in hex_data.get('communications', [])[:5]:  # Show first 5
                if isinstance(comm, dict):
                    hex_preview = str(comm.get('hex_data', ''))[:32]
                    if len(str(comm.get('hex_data', ''))) > 32:
                        hex_preview += '...'
                    protocol_info = comm.get('protocol_analysis', {})
                    if not isinstance(protocol_info, dict):
                        protocol_info = {}
                    report_lines.extend([
                        f"  Line {comm.get('line', '?')}:",
                        f"    Hex: {hex_preview}",
                        f"    Meaning: {comm.get('explanation', 'No explanation')}",
                        f"    Protocol: {protocol_info.get('protocol', 'Unknown')} - {protocol_info.get('service_type', 'Unknown service')}",
                        ""
                    ])
        
        # Show ASCII discoveries
        if hex_data.get('ascii_discoveries'):
            report_lines.append("📝 ASCII Text Found in Hex Data:")
            for ascii_item in hex_data.get('ascii_discoveries', [])[:5]:  # Show first 5
                if isinstance(ascii_item, dict):
                    hex_preview = str(ascii_item.get('hex_data', ''))[:24] + '...'
                    report_lines.append(f"  • Line {ascii_item.get('line', '?')}: '{ascii_item.get('ascii_text', '')}' (from hex: {hex_preview})")
            report_lines.append("")
    else:
        report_lines.extend([
            "❓ No hex communication data detected",
            ""
        ])
    
    # 8. PROXIMATE CAUSE ANALYSIS
    cause_data = critical_data.get('proximate_cause', {})
    report_lines.extend([
        "🎯 PROXIMATE CAUSE ANALYSIS WITH EVIDENCE",
        "=" * 100,
        ""
    ])
    
    confidence_icon = "🔥" if cause_data.get('confidence') == 'high' else "⚠️" if cause_data.get('confidence') == 'medium' else "❓"
    risk_icon = "🚨" if cause_data.get('risk_level') == 'high' else "⚠️" if cause_data.get('risk_level') == 'medium' else "ℹ️"
    
    report_lines.extend([
        f"{confidence_icon} Primary Root Cause: {cause_data.get('primary_cause', 'Unknown')}",
        f"🎯 Confidence Level: {cause_data.get('confidence', 'unknown').title()}",
        f"{risk_icon} Risk Level: {cause_data.get('risk_level', 'unknown').title()}",
        ""
    ])
    
    # Evidence
    if cause_data.get('evidence'):
        report_lines.append("📋 Supporting Evidence:")
        for evidence in cause_data.get('evidence', []):
            report_lines.append(f"  • {evidence}")
        report_lines.append("")
    
    # Recommendations
    if cause_data.get('recommendations'):
        report_lines.append("🔧 Recommended Actions:")
        for i, recommendation in enumerate(cause_data['recommendations'], 1):
            report_lines.append(f"  {i}. {recommendation}")
        report_lines.append("")
    
    # 9. DIAGNOSTIC TIMELINE
    timeline = critical_data.get('timeline', [])
    if timeline:
        report_lines.extend([
            "⏰ DIAGNOSTIC EVENT TIMELINE",
            "=" * 100,
            ""
        ])
        
        # Show high significance events
        high_events = [e for e in timeline if e['significance'] == 'high']
        if high_events:
            report_lines.append("🚨 Critical Events:")
            for event in high_events[:10]:  # Show first 10
                report_lines.append(f"  • {event['timestamp']}: {event['event_type']} - {event['description'][:60]}...")
            report_lines.append("")
        
        # Show medium significance events
        medium_events = [e for e in timeline if e['significance'] == 'medium']
        if medium_events:
            report_lines.append("⚠️ Important Events:")
            for event in medium_events[:5]:  # Show first 5
                report_lines.append(f"  • {event['timestamp']}: {event['event_type']} - {event['description'][:60]}...")
            report_lines.append("")
    
    # Footer
    report_lines.extend([
        "",
        "╔" + "═" * 98 + "╗",
        "║" + " " * 35 + "END OF CRITICAL DIAGNOSTIC REPORT" + " " * 30 + "║",
        "╚" + "═" * 98 + "╝"
    ])
    
    return "\n".join(report_lines)