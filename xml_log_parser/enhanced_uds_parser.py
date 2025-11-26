"""
Enhanced UDS (Unified Diagnostic Services) Parser
Modular ECU-specific parsing with cybersecurity analysis and detailed error reporting
"""

import re
import json
from typing import Dict, List, Any, Optional, Tuple, Union
from dataclasses import dataclass, asdict
from datetime import datetime
from abc import ABC, abstractmethod
from enum import Enum
from collections import Counter, defaultdict


class UDSServiceID(Enum):
    """UDS Service Identifiers with descriptions"""
    DIAGNOSTIC_SESSION_CONTROL = ("10", "Diagnostic Session Control")
    ECU_RESET = ("11", "ECU Reset")
    CLEAR_DIAGNOSTIC_INFO = ("14", "Clear Diagnostic Information")
    READ_DTC_INFO = ("19", "Read DTC Information")
    READ_DATA_BY_ID = ("22", "Read Data By Identifier")
    READ_MEMORY_BY_ADDRESS = ("23", "Read Memory By Address")
    SECURITY_ACCESS = ("27", "Security Access")
    COMMUNICATION_CONTROL = ("28", "Communication Control")
    WRITE_DATA_BY_ID = ("2E", "Write Data By Identifier")
    IO_CONTROL_BY_ID = ("2F", "Input Output Control By Identifier")
    ROUTINE_CONTROL = ("31", "Routine Control")
    REQUEST_DOWNLOAD = ("34", "Request Download")
    REQUEST_UPLOAD = ("35", "Request Upload")
    TRANSFER_DATA = ("36", "Transfer Data")
    REQUEST_TRANSFER_EXIT = ("37", "Request Transfer Exit")
    TESTER_PRESENT = ("3E", "Tester Present")
    CONTROL_DTC_SETTING = ("85", "Control DTC Setting")


class NRCCode(Enum):
    """Negative Response Codes with detailed explanations"""
    GENERAL_REJECT = ("10", "General Reject", "Service not supported by ECU")
    SERVICE_NOT_SUPPORTED = ("11", "Service Not Supported", "ECU doesn't implement this service")
    SUB_FUNCTION_NOT_SUPPORTED = ("12", "Sub-Function Not Supported", "Invalid sub-function parameter")
    INCORRECT_MESSAGE_LENGTH = ("13", "Incorrect Message Length", "Message format or length is wrong")
    RESPONSE_TOO_LONG = ("14", "Response Too Long", "Response exceeds buffer capacity")
    BUSY_REPEAT_REQUEST = ("21", "Busy Repeat Request", "ECU is busy, retry operation later")
    CONDITIONS_NOT_CORRECT = ("22", "Conditions Not Correct", "Prerequisites not met for operation")
    REQUEST_SEQUENCE_ERROR = ("24", "Request Sequence Error", "Wrong order of diagnostic operations")
    NO_RESPONSE_FROM_SUBNET = ("25", "No Response From Subnet", "Dependent module not responding")
    FAILURE_PREVENTS_EXECUTION = ("26", "Failure Prevents Execution", "Internal failure blocks operation")
    REQUEST_OUT_OF_RANGE = ("31", "Request Out Of Range", "Parameter/address outside valid range")
    SECURITY_ACCESS_DENIED = ("33", "Security Access Denied", "Authentication required for this operation")
    INVALID_KEY = ("35", "Invalid Key", "Wrong security key provided")
    EXCEED_NUMBER_OF_ATTEMPTS = ("36", "Exceed Number Of Attempts", "Too many failed security attempts")
    REQUIRED_TIME_DELAY = ("37", "Required Time Delay Not Expired", "Must wait before retry")
    UPLOAD_DOWNLOAD_NOT_ACCEPTED = ("70", "Upload Download Not Accepted", "Programming operation rejected")
    TRANSFER_DATA_SUSPENDED = ("71", "Transfer Data Suspended", "Data transfer halted")
    GENERAL_PROGRAMMING_FAILURE = ("72", "General Programming Failure", "Programming operation failed")
    WRONG_BLOCK_SEQUENCE = ("73", "Wrong Block Sequence Counter", "Data blocks out of sequence")
    REQUEST_CORRECTLY_RECEIVED = ("78", "Request Correctly Received - Response Pending", "Processing, please wait")


@dataclass
class UDSMessage:
    """Structured UDS message data"""
    timestamp: datetime
    ecu_address: str
    ecu_name: str
    service_id: str
    service_name: str
    sub_function: Optional[str]
    payload: str
    direction: str  # REQUEST or RESPONSE
    status: str  # SUCCESS, NRC, TIMEOUT, ERROR
    nrc_code: Optional[str] = None
    nrc_description: Optional[str] = None
    proximate_cause: Optional[str] = None
    security_implications: List[str] = None
    raw_data: str = ""

    def __post_init__(self):
        if self.security_implications is None:
            self.security_implications = []


@dataclass
class ECUDiagnosticSession:
    """Diagnostic session for a specific ECU"""
    ecu_address: str
    ecu_name: str
    session_start: datetime
    session_end: Optional[datetime]
    messages: List[UDSMessage]
    success_count: int = 0
    failure_count: int = 0
    nrc_count: int = 0
    security_issues: List[str] = None
    session_type: str = "UNKNOWN"

    def __post_init__(self):
        if self.security_issues is None:
            self.security_issues = []


class BaseECUParser(ABC):
    """Abstract base class for ECU-specific parsers"""
    
    def __init__(self, ecu_address: str, ecu_name: str):
        self.ecu_address = ecu_address.upper()
        self.ecu_name = ecu_name
        self.supported_services = set()
        self.security_services = {"27"}  # Security Access
        self.programming_services = {"34", "35", "36", "37"}  # Download/Upload services
    
    @abstractmethod
    def parse_service_specific(self, service_id: str, payload: str, direction: str) -> Dict[str, Any]:
        """Parse ECU-specific service data"""
        pass
    
    @abstractmethod
    def analyze_security_implications(self, message: UDSMessage) -> List[str]:
        """Analyze security implications of the message"""
        pass
    
    def parse_message(self, raw_data: str, timestamp: datetime) -> Optional[UDSMessage]:
        """Parse a UDS message for this ECU"""
        try:
            # Extract basic UDS structure
            message_data = self._extract_uds_structure(raw_data)
            if not message_data:
                return None
            
            # Create base message
            message = UDSMessage(
                timestamp=timestamp,
                ecu_address=self.ecu_address,
                ecu_name=self.ecu_name,
                service_id=message_data['service_id'],
                service_name=message_data['service_name'],
                sub_function=message_data.get('sub_function'),
                payload=message_data['payload'],
                direction=message_data['direction'],
                status=message_data['status'],
                nrc_code=message_data.get('nrc_code'),
                nrc_description=message_data.get('nrc_description'),
                raw_data=raw_data
            )
            
            # Add ECU-specific analysis
            specific_data = self.parse_service_specific(
                message.service_id, 
                message.payload, 
                message.direction
            )
            
            # Add security analysis
            message.security_implications = self.analyze_security_implications(message)
            
            # Determine proximate cause for failures
            if message.status in ['NRC', 'ERROR', 'TIMEOUT']:
                message.proximate_cause = self._determine_proximate_cause(message, specific_data)
            
            return message
            
        except Exception as e:
            return None
    
    def _extract_uds_structure(self, raw_data: str) -> Optional[Dict[str, Any]]:
        """Extract basic UDS message structure"""
        # Remove common prefixes and clean data
        clean_data = re.sub(r'^.*?(?:request|response)[:=\s]*', '', raw_data, flags=re.IGNORECASE)
        clean_data = re.sub(r'[^\da-fA-F]', '', clean_data)
        
        if len(clean_data) < 6:  # Minimum: ECU(3) + Service(2) + data
            return None
        
        try:
            # Parse ECU address and service ID
            ecu_addr = clean_data[4:7] if clean_data.startswith('0000') else clean_data[:3]
            service_id = clean_data[8:10] if clean_data.startswith('0000') else clean_data[3:5]
            
            # Determine direction and status
            direction = "REQUEST"
            status = "SUCCESS"
            nrc_code = None
            nrc_description = None
            
            # Check for negative response (7F)
            if service_id.upper() == "7F":
                direction = "RESPONSE"
                status = "NRC"
                if len(clean_data) >= 12:
                    original_service = clean_data[10:12]
                    nrc_code = clean_data[12:14]
                    nrc_description = self._get_nrc_description(nrc_code)
            elif int(service_id, 16) >= 0x40:  # Positive response
                direction = "RESPONSE"
                service_id = format(int(service_id, 16) - 0x40, '02X')
            
            # Get service name
            service_name = self._get_service_name(service_id)
            
            # Extract payload
            payload_start = 10 if clean_data.startswith('0000') else 5
            payload = clean_data[payload_start:] if len(clean_data) > payload_start else ""
            
            # Extract sub-function if applicable
            sub_function = None
            if payload and service_id in ["10", "11", "27", "28", "31", "85"]:
                sub_function = payload[:2]
            
            return {
                'service_id': service_id,
                'service_name': service_name,
                'sub_function': sub_function,
                'payload': payload,
                'direction': direction,
                'status': status,
                'nrc_code': nrc_code,
                'nrc_description': nrc_description
            }
            
        except (ValueError, IndexError):
            return None
    
    def _get_service_name(self, service_id: str) -> str:
        """Get service name from service ID"""
        service_map = {sid.value[0]: sid.value[1] for sid in UDSServiceID}
        return service_map.get(service_id.upper(), f"Unknown Service {service_id}")
    
    def _get_nrc_description(self, nrc_code: str) -> str:
        """Get NRC description"""
        for nrc in NRCCode:
            if nrc.value[0] == nrc_code.upper():
                return f"{nrc.value[1]} - {nrc.value[2]}"
        return f"Unknown NRC {nrc_code}"
    
    def _determine_proximate_cause(self, message: UDSMessage, specific_data: Dict[str, Any]) -> str:
        """Determine the proximate cause of failure"""
        if message.nrc_code:
            nrc_causes = {
                "10": "ECU doesn't support this diagnostic service",
                "11": "Service not implemented in this ECU variant",
                "12": "Invalid sub-function parameter or not supported",
                "13": "Message format error or incorrect length",
                "21": "ECU is busy with another operation",
                "22": "Prerequisites not met (e.g., wrong session, conditions)",
                "24": "Operations performed in wrong sequence",
                "31": "Parameter/address outside ECU's valid range",
                "33": "Security access required - need to authenticate first",
                "35": "Wrong security key - authentication failed",
                "36": "Too many failed security attempts - ECU locked",
                "37": "Must wait before retrying security access",
                "70": "Programming conditions not met",
                "72": "Programming operation failed - check power/connections",
                "73": "Data transfer error - blocks out of sequence"
            }
            return nrc_causes.get(message.nrc_code, f"ECU rejected request with NRC {message.nrc_code}")
        
        # Check for timeouts
        if "timeout" in message.raw_data.lower():
            return "ECU did not respond within expected time - check connections"
        
        # Check for communication errors
        if any(error in message.raw_data.lower() for error in ["bus off", "error frame", "lost comm"]):
            return "Communication error - check CAN bus integrity"
        
        return "Unknown failure cause"


class APIMParser(BaseECUParser):
    """APIM (Accessory Protocol Interface Module) specific parser"""
    
    def __init__(self):
        super().__init__("7D0", "APIM - Accessory Protocol Interface Module")
        self.supported_services = {"10", "11", "14", "19", "22", "27", "28", "2E", "31", "3E", "85"}
        
        # APIM-specific DIDs (Data Identifiers)
        self.apim_dids = {
            "F190": "VIN (Vehicle Identification Number)",
            "F18A": "System Supplier Identifier",  
            "F18C": "ECU Serial Number",
            "F194": "System Supplier ECU Software Number",
            "F195": "System Supplier ECU Software Version",
            "F1A0": "Vehicle Identification Data For Traceability",
            "806C": "Application Software Part Numbers",
            "D100": "Boot Software Information",
            "D101": "Application Software Information"
        }
    
    def parse_service_specific(self, service_id: str, payload: str, direction: str) -> Dict[str, Any]:
        """Parse APIM-specific service data"""
        result = {}
        
        if service_id == "22" and len(payload) >= 4:  # Read Data By Identifier
            did = payload[:4].upper()
            result['did'] = did
            result['did_name'] = self.apim_dids.get(did, f"Unknown DID {did}")
            if direction == "RESPONSE" and len(payload) > 4:
                result['data'] = payload[4:]
                result['data_interpretation'] = self._interpret_apim_data(did, payload[4:])
        
        elif service_id == "27":  # Security Access
            if len(payload) >= 2:
                sub_func = payload[:2]
                if sub_func == "01":
                    result['security_operation'] = "Request Seed"
                elif sub_func == "02":
                    result['security_operation'] = "Send Key"
                    result['security_level'] = "Level 1"
                elif sub_func == "03":
                    result['security_operation'] = "Request Seed (Level 2)"
                elif sub_func == "04": 
                    result['security_operation'] = "Send Key (Level 2)"
        
        elif service_id == "31":  # Routine Control
            if len(payload) >= 6:
                sub_func = payload[:2]
                routine_id = payload[2:6]
                result['routine_operation'] = {
                    "01": "Start Routine",
                    "02": "Stop Routine", 
                    "03": "Request Routine Results"
                }.get(sub_func, f"Unknown routine operation {sub_func}")
                result['routine_id'] = routine_id
        
        return result
    
    def analyze_security_implications(self, message: UDSMessage) -> List[str]:
        """Analyze security implications for APIM"""
        implications = []
        
        # Security Access monitoring
        if message.service_id == "27":
            if message.nrc_code == "35":
                implications.append("CRITICAL: Invalid security key - possible unauthorized access attempt")
            elif message.nrc_code == "36":
                implications.append("CRITICAL: Too many failed attempts - APIM security locked")
            elif message.status == "SUCCESS":
                implications.append("INFO: Security access granted - monitor for unauthorized operations")
        
        # Programming services
        if message.service_id in self.programming_services:
            if message.status == "SUCCESS":
                implications.append("WARNING: Programming operation active - verify authorization")
            else:
                implications.append("INFO: Programming operation blocked - security working")
        
        # Sensitive data access
        if message.service_id == "22" and hasattr(message, 'payload'):
            sensitive_dids = ["F190", "F18C", "806C"]  # VIN, Serial, Software
            if any(did in message.payload for did in sensitive_dids):
                implications.append("INFO: Sensitive data accessed - verify legitimacy")
        
        return implications
    
    def _interpret_apim_data(self, did: str, data: str) -> str:
        """Interpret APIM-specific data responses"""
        if did == "F190" and len(data) >= 34:  # VIN
            return f"VIN: {bytes.fromhex(data[:34]).decode('ascii', errors='ignore')}"
        elif did == "D100":
            return "Boot software version information"
        elif did == "806C":
            return "Application software part numbers list"
        else:
            return f"Raw data: {data}"


class GWMParser(BaseECUParser):
    """GWM (Gateway Module) specific parser"""
    
    def __init__(self):
        super().__init__("716", "GWM - Gateway Module A")
        self.supported_services = {"10", "11", "14", "19", "22", "27", "28", "3E", "85"}
        
        # GWM-specific monitoring
        self.gateway_functions = {
            "routing": "CAN message routing between networks",
            "filtering": "Message filtering and validation", 
            "security": "Network security enforcement",
            "diagnostics": "Diagnostic gateway functions"
        }
    
    def parse_service_specific(self, service_id: str, payload: str, direction: str) -> Dict[str, Any]:
        """Parse GWM-specific service data"""
        result = {}
        
        if service_id == "28":  # Communication Control
            if len(payload) >= 2:
                sub_func = payload[:2]
                control_type = {
                    "00": "Enable Rx and Tx",
                    "01": "Enable Rx, Disable Tx", 
                    "02": "Disable Rx, Enable Tx",
                    "03": "Disable Rx and Tx"
                }.get(sub_func, f"Unknown communication control {sub_func}")
                result['communication_control'] = control_type
                
                if len(payload) >= 4:
                    comm_type = payload[2:4]
                    result['communication_type'] = {
                        "01": "Normal Communication Messages",
                        "02": "Network Management Messages",
                        "03": "Normal + Network Management"
                    }.get(comm_type, f"Communication type {comm_type}")
        
        return result
    
    def analyze_security_implications(self, message: UDSMessage) -> List[str]:
        """Analyze security implications for GWM"""
        implications = []
        
        # Communication control monitoring
        if message.service_id == "28":
            if "Disable" in str(message.payload):
                implications.append("WARNING: Communication being disabled - potential DoS attack")
            elif message.status == "SUCCESS":
                implications.append("INFO: Communication control changed - monitor network traffic")
        
        # Gateway security
        if message.service_id == "27":
            if message.status == "SUCCESS":
                implications.append("CRITICAL: Gateway security access granted - high privilege level")
            elif message.nrc_code in ["35", "36"]:
                implications.append("CRITICAL: Gateway security breach attempt detected")
        
        return implications


class UDSMessageParser:
    """Main UDS message parser with ECU-specific handling"""
    
    def __init__(self):
        self.ecu_parsers = {}
        self.register_default_parsers()
        self.sessions = {}  # ECU address -> ECUDiagnosticSession
    
    def register_default_parsers(self):
        """Register default ECU parsers"""
        apim_parser = APIMParser()
        gwm_parser = GWMParser()
        
        self.ecu_parsers["7D0"] = apim_parser
        self.ecu_parsers["716"] = gwm_parser
    
    def register_parser(self, ecu_address: str, parser: BaseECUParser):
        """Register a custom ECU parser"""
        self.ecu_parsers[ecu_address.upper()] = parser
    
    def parse_uds_messages(self, log_lines: List[str]) -> Dict[str, Any]:
        """Parse UDS messages from log lines"""
        results = {
            'messages': [],
            'sessions': {},
            'summary': {
                'total_messages': 0,
                'successful_operations': 0,
                'failed_operations': 0,
                'nrc_errors': 0,
                'security_events': 0,
                'ecus_involved': set()
            },
            'security_analysis': {
                'critical_issues': [],
                'warnings': [],
                'info_events': []
            },
            'nrc_analysis': {},
            'proximate_causes': Counter()
        }
        
        for line in log_lines:
            message = self._parse_line(line)
            if message:
                results['messages'].append(message)
                self._update_session(message)
                self._update_summary(message, results)
                self._analyze_security(message, results)
        
        # Finalize sessions
        results['sessions'] = {addr: asdict(session) for addr, session in self.sessions.items()}
        
        # Convert sets to lists for JSON serialization
        results['summary']['ecus_involved'] = list(results['summary']['ecus_involved'])
        
        return results
    
    def _parse_line(self, line: str) -> Optional[UDSMessage]:
        """Parse a single log line"""
        # Extract timestamp
        timestamp = self._extract_timestamp(line)
        
        # Extract ECU address from line
        ecu_match = re.search(r'\b([0-9A-Fa-f]{3})\b', line)
        if not ecu_match:
            return None
        
        ecu_address = ecu_match.group(1).upper()
        
        # Get appropriate parser
        parser = self.ecu_parsers.get(ecu_address)
        if not parser:
            # Create generic parser for unknown ECUs
            parser = self._create_generic_parser(ecu_address)
        
        return parser.parse_message(line, timestamp)
    
    def _extract_timestamp(self, line: str) -> datetime:
        """Extract timestamp from log line"""
        # Try various timestamp formats
        patterns = [
            r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[.,]\d{3})',
            r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}[.,]\d{3})',
            r'(\d{2}:\d{2}:\d{2}[.,]\d{3})'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, line)
            if match:
                try:
                    return datetime.fromisoformat(match.group(1).replace(',', '.'))
                except:
                    pass
        
        return datetime.now()
    
    def _create_generic_parser(self, ecu_address: str) -> BaseECUParser:
        """Create a generic parser for unknown ECUs"""
        class GenericECUParser(BaseECUParser):
            def __init__(self, addr):
                super().__init__(addr, f"Unknown ECU {addr}")
            
            def parse_service_specific(self, service_id: str, payload: str, direction: str) -> Dict[str, Any]:
                return {}
            
            def analyze_security_implications(self, message: UDSMessage) -> List[str]:
                implications = []
                if message.service_id == "27":
                    implications.append("INFO: Security access attempt on unknown ECU")
                return implications
        
        parser = GenericECUParser(ecu_address)
        self.ecu_parsers[ecu_address] = parser
        return parser
    
    def _update_session(self, message: UDSMessage):
        """Update ECU diagnostic session"""
        ecu_addr = message.ecu_address
        
        if ecu_addr not in self.sessions:
            self.sessions[ecu_addr] = ECUDiagnosticSession(
                ecu_address=ecu_addr,
                ecu_name=message.ecu_name,
                session_start=message.timestamp,
                session_end=None,
                messages=[]
            )
        
        session = self.sessions[ecu_addr]
        session.messages.append(message)
        session.session_end = message.timestamp
        
        # Update counters
        if message.status == "SUCCESS":
            session.success_count += 1
        else:
            session.failure_count += 1
            
        if message.nrc_code:
            session.nrc_count += 1
        
        if message.security_implications:
            session.security_issues.extend(message.security_implications)
    
    def _update_summary(self, message: UDSMessage, results: Dict[str, Any]):
        """Update summary statistics"""
        summary = results['summary']
        summary['total_messages'] += 1
        summary['ecus_involved'].add(message.ecu_address)
        
        if message.status == "SUCCESS":
            summary['successful_operations'] += 1
        else:
            summary['failed_operations'] += 1
        
        if message.nrc_code:
            summary['nrc_errors'] += 1
            # Track NRC analysis
            nrc_key = f"{message.nrc_code} - {message.nrc_description}"
            if nrc_key not in results['nrc_analysis']:
                results['nrc_analysis'][nrc_key] = {
                    'count': 0,
                    'affected_ecus': set(),
                    'services': set()
                }
            
            results['nrc_analysis'][nrc_key]['count'] += 1
            results['nrc_analysis'][nrc_key]['affected_ecus'].add(message.ecu_address)
            results['nrc_analysis'][nrc_key]['services'].add(message.service_id)
        
        if message.security_implications:
            summary['security_events'] += 1
        
        if message.proximate_cause:
            results['proximate_causes'][message.proximate_cause] += 1
    
    def _analyze_security(self, message: UDSMessage, results: Dict[str, Any]):
        """Analyze security implications"""
        if not message.security_implications:
            return
        
        security_analysis = results['security_analysis']
        
        for implication in message.security_implications:
            if implication.startswith("CRITICAL"):
                security_analysis['critical_issues'].append({
                    'timestamp': message.timestamp.isoformat(),
                    'ecu': message.ecu_address,
                    'service': message.service_id,
                    'issue': implication
                })
            elif implication.startswith("WARNING"):
                security_analysis['warnings'].append({
                    'timestamp': message.timestamp.isoformat(),
                    'ecu': message.ecu_address,
                    'service': message.service_id,
                    'issue': implication
                })
            else:
                security_analysis['info_events'].append({
                    'timestamp': message.timestamp.isoformat(),
                    'ecu': message.ecu_address,
                    'service': message.service_id,
                    'issue': implication
                })


def parse_vehicle_diagnostics(log_content: str) -> Dict[str, Any]:
    """
    Main function to parse vehicle diagnostic logs with UDS message analysis
    
    Args:
        log_content: Raw log content as string
    
    Returns:
        Dictionary containing parsed messages, sessions, security analysis, and summaries
    """
    parser = UDSMessageParser()
    lines = log_content.split('\n')
    
    # Filter lines that likely contain UDS messages
    uds_lines = []
    for line in lines:
        if any(pattern in line.lower() for pattern in [
            'diag service', 'request', 'response', '7d0', '716', 
            'apim', 'gwm', 'uds', 'can', 'service'
        ]):
            uds_lines.append(line)
    
    return parser.parse_uds_messages(uds_lines)


# Example usage and testing
if __name__ == "__main__":
    # Test the parser with sample data
    sample_log = """
    2025-10-14T17:58:06,313 INFO - LOG>> Pinging node = 7D0
    2025-10-14T17:58:06,331 INFO - LOG>> Diag service request : 000007D022D100
    2025-10-14T17:58:06,410 INFO - LOG>> Diag service response: 000007D862D10001
    2025-10-14T17:58:06,443 INFO - LOG>> Diag service request : 000007D022806C
    2025-10-14T17:58:06,527 INFO - LOG>> Diag service response: 000007D862806C000000...
    2025-10-14T17:58:07,100 INFO - LOG>> Diag service request : 000007D02701
    2025-10-14T17:58:07,150 INFO - LOG>> Diag service response: 000007D8677001ABCD1234
    2025-10-14T17:58:07,200 INFO - LOG>> Diag service request : 000007D02702DEADBEEF
    2025-10-14T17:58:07,250 INFO - LOG>> Diag service response: 000007D867020000
    """
    
    results = parse_vehicle_diagnostics(sample_log)
    print(json.dumps(results, indent=2, default=str))