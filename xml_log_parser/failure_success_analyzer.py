"""
Enhanced Failure Analysis and NRC (Negative Response Code) Explanation System
Provides detailed analysis of what failed, why it failed, and proximate causes
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from collections import Counter, defaultdict
import re


@dataclass
class FailureAnalysis:
    """Detailed failure analysis for diagnostic operations"""
    operation_type: str
    ecu_address: str
    ecu_name: str
    service_id: str
    service_name: str
    failure_type: str  # NRC, TIMEOUT, COMMUNICATION_ERROR, etc.
    failure_code: Optional[str]
    proximate_cause: str
    root_cause: str
    impact_level: str  # CRITICAL, HIGH, MEDIUM, LOW
    recommended_action: str
    simple_explanation: str
    technical_details: str
    timestamp: str


@dataclass
class SuccessAnalysis:
    """Analysis of successful operations"""
    operation_type: str
    ecu_address: str
    ecu_name: str
    service_id: str
    service_name: str
    operation_details: str
    security_level: str
    data_accessed: Optional[str]
    simple_explanation: str
    timestamp: str


class NRCExplainer:
    """Explains NRC (Negative Response Codes) in simple terms"""
    
    def __init__(self):
        self.nrc_explanations = {
            "10": {
                "name": "General Reject",
                "simple": "ECU doesn't understand or support this request",
                "cause": "Service not implemented in this ECU",
                "impact": "LOW",
                "action": "Check if you're using the correct service for this ECU type",
                "details": "The ECU firmware doesn't include support for the requested diagnostic service"
            },
            "11": {
                "name": "Service Not Supported", 
                "simple": "This ECU doesn't have this feature",
                "cause": "ECU variant doesn't include this service",
                "impact": "LOW",
                "action": "Verify ECU part number and software version support this service",
                "details": "The specific ECU hardware/software configuration doesn't implement this UDS service"
            },
            "12": {
                "name": "Sub-Function Not Supported",
                "simple": "The ECU supports the service but not this specific option",
                "cause": "Invalid or unsupported sub-function parameter",
                "impact": "MEDIUM", 
                "action": "Check the sub-function value - use supported options only",
                "details": "Service is implemented but the specific sub-function ID is not supported"
            },
            "13": {
                "name": "Incorrect Message Length/Format",
                "simple": "The request message is the wrong size or format",
                "cause": "Message too short, too long, or malformed",
                "impact": "MEDIUM",
                "action": "Check message format and length according to UDS specification",
                "details": "Message doesn't conform to expected structure for this service"
            },
            "14": {
                "name": "Response Too Long",
                "simple": "ECU can't send the response - it's too big",
                "cause": "Response data exceeds ECU buffer capacity",
                "impact": "MEDIUM",
                "action": "Request smaller data chunks or increase buffer size",
                "details": "Response would exceed maximum message length or buffer constraints"
            },
            "21": {
                "name": "Busy Repeat Request",
                "simple": "ECU is busy - try again later",
                "cause": "ECU is processing another operation",
                "impact": "LOW",
                "action": "Wait and retry the request after a short delay",
                "details": "ECU is executing another diagnostic routine and cannot process new requests"
            },
            "22": {
                "name": "Conditions Not Correct",
                "simple": "Something needs to be done first before this will work",
                "cause": "Prerequisites not met (wrong session, vehicle state, etc.)",
                "impact": "HIGH",
                "action": "Check diagnostic session, vehicle conditions, and security access",
                "details": "Required preconditions not satisfied - may need session change or authentication"
            },
            "24": {
                "name": "Request Sequence Error",
                "simple": "You're doing things in the wrong order",
                "cause": "Operations performed out of required sequence",
                "impact": "HIGH",
                "action": "Follow the correct sequence: session → security → operation",
                "details": "Diagnostic operations must follow specific order (e.g., security access before programming)"
            },
            "25": {
                "name": "No Response From Subnet Component",
                "simple": "A required component isn't responding",
                "cause": "Dependent ECU or module not communicating",
                "impact": "CRITICAL",
                "action": "Check network connections and dependent module health",
                "details": "Operation requires communication with another ECU that's not responding"
            },
            "26": {
                "name": "Failure Prevents Execution",
                "simple": "An internal problem is blocking this operation",
                "cause": "Internal ECU failure or fault condition",
                "impact": "CRITICAL",
                "action": "Check for DTCs and ECU health before retrying",
                "details": "ECU has detected an internal fault that prevents operation execution"
            },
            "31": {
                "name": "Request Out Of Range",
                "simple": "The requested value is outside allowed limits",
                "cause": "Parameter, address, or value outside valid range",
                "impact": "MEDIUM",
                "action": "Check parameter values against ECU specifications",
                "details": "Data identifier, memory address, or parameter value exceeds ECU limits"
            },
            "33": {
                "name": "Security Access Denied",
                "simple": "You need permission to do this (security locked)",
                "cause": "Authentication required for this operation",
                "impact": "HIGH",
                "action": "Perform security access (seed/key) authentication first",
                "details": "Operation requires elevated security level - must authenticate before proceeding"
            },
            "35": {
                "name": "Invalid Key",
                "simple": "Wrong password/key provided",
                "cause": "Incorrect security key sent to ECU",
                "impact": "HIGH",
                "action": "Verify security key algorithm and calculation",
                "details": "Security key doesn't match expected value - authentication failed"
            },
            "36": {
                "name": "Exceed Number Of Attempts",
                "simple": "Too many wrong passwords - ECU is now locked",
                "cause": "Multiple failed security access attempts",
                "impact": "CRITICAL",
                "action": "Wait for lockout timer to expire or cycle power",
                "details": "ECU has locked security access due to repeated authentication failures"
            },
            "37": {
                "name": "Required Time Delay Not Expired",
                "simple": "You need to wait longer before trying again",
                "cause": "Mandatory delay period not completed",
                "impact": "MEDIUM",
                "action": "Wait for the required delay period before retrying",
                "details": "ECU enforces timing delays between certain operations for security"
            },
            "70": {
                "name": "Upload Download Not Accepted",
                "simple": "ECU won't accept file transfer right now",
                "cause": "Programming conditions not met",
                "impact": "HIGH",
                "action": "Check voltage, session type, and security access",
                "details": "Programming operation rejected - verify prerequisites like voltage, session, security"
            },
            "71": {
                "name": "Transfer Data Suspended", 
                "simple": "File transfer was stopped",
                "cause": "Data transfer operation halted",
                "impact": "HIGH",
                "action": "Restart transfer from beginning or resume if supported",
                "details": "Programming data transfer interrupted - may need to restart operation"
            },
            "72": {
                "name": "General Programming Failure",
                "simple": "Programming/flashing failed",
                "cause": "Programming operation unsuccessful",
                "impact": "CRITICAL",
                "action": "Check power supply, connections, and retry programming",
                "details": "ECU programming failed - could be due to power, data corruption, or hardware issues"
            },
            "73": {
                "name": "Wrong Block Sequence Counter",
                "simple": "File transfer blocks are out of order",
                "cause": "Data blocks transferred in wrong sequence",
                "impact": "HIGH", 
                "action": "Restart transfer with correct block sequence",
                "details": "Programming data blocks must be sent in specific order - sequence error detected"
            },
            "78": {
                "name": "Request Correctly Received - Response Pending",
                "simple": "ECU is working on it - please wait",
                "cause": "Operation in progress, response delayed",
                "impact": "LOW",
                "action": "Wait for final response or timeout",
                "details": "ECU acknowledges request and is processing - final response will follow"
            },
            "7E": {
                "name": "Sub-Function Not Supported In Active Session",
                "simple": "This option isn't available in the current mode",
                "cause": "Sub-function not supported in current diagnostic session",
                "impact": "MEDIUM",
                "action": "Change to appropriate diagnostic session first",
                "details": "Sub-function requires different diagnostic session (e.g., programming session)"
            },
            "7F": {
                "name": "Service Not Supported In Active Session",
                "simple": "This service isn't available in the current mode",
                "cause": "Service not supported in current diagnostic session",
                "impact": "MEDIUM", 
                "action": "Change to appropriate diagnostic session for this service",
                "details": "Service requires different diagnostic session (e.g., default, extended, programming)"
            }
        }
    
    def explain_nrc(self, nrc_code: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Provide detailed explanation of NRC code"""
        nrc_code = nrc_code.upper()
        
        if nrc_code not in self.nrc_explanations:
            return {
                "name": f"Unknown NRC {nrc_code}",
                "simple": f"ECU returned error code {nrc_code} - check documentation",
                "cause": "Unknown error condition",
                "impact": "MEDIUM",
                "action": "Consult ECU documentation for this error code",
                "details": f"Negative Response Code {nrc_code} not in standard UDS specification"
            }
        
        explanation = self.nrc_explanations[nrc_code].copy()
        
        # Add context-specific details if available
        if context:
            explanation = self._add_context_details(explanation, context)
        
        return explanation
    
    def _add_context_details(self, explanation: Dict[str, str], context: Dict[str, Any]) -> Dict[str, str]:
        """Add context-specific details to explanation"""
        service_id = context.get('service_id', '')
        ecu_type = context.get('ecu_type', '')
        
        # Service-specific enhancements
        if service_id == "27" and explanation["name"] == "Security Access Denied":
            explanation["details"] += " - Security access is required for programming and calibration operations"
            explanation["action"] = "Use proper seed/key algorithm for this ECU type"
        
        elif service_id == "22" and explanation["name"] == "Request Out Of Range":
            explanation["details"] += " - Data Identifier (DID) not supported by this ECU"
            explanation["action"] = "Check ECU documentation for supported DIDs"
        
        elif service_id in ["34", "35", "36", "37"] and "programming" in explanation["simple"].lower():
            explanation["details"] += " - Programming operations require specific conditions"
            explanation["action"] += " - Ensure 12V+ supply and stable communication"
        
        # ECU-specific enhancements
        if ecu_type == "APIM":
            if service_id == "27":
                explanation["action"] += " - APIM security may require ignition on"
        elif ecu_type == "GWM":
            if service_id == "28":
                explanation["details"] += " - Gateway communication control affects entire network"
        
        return explanation


class FailureSuccessAnalyzer:
    """Analyzes successes and failures in diagnostic operations"""
    
    def __init__(self):
        self.nrc_explainer = NRCExplainer()
        self.operation_context = {
            "10": "Session Control",
            "11": "ECU Reset", 
            "14": "Clear DTCs",
            "19": "Read DTCs",
            "22": "Read Data",
            "27": "Security Access",
            "28": "Communication Control",
            "2E": "Write Data",
            "31": "Routine Control",
            "34": "Request Download",
            "35": "Request Upload", 
            "36": "Transfer Data",
            "37": "Transfer Exit",
            "3E": "Tester Present",
            "85": "DTC Setting Control"
        }
    
    def analyze_failures(self, messages: List[Dict[str, Any]]) -> List[FailureAnalysis]:
        """Analyze all failure cases"""
        failures = []
        
        for msg in messages:
            if msg.get('status') in ['NRC', 'ERROR', 'TIMEOUT']:
                failure = self._analyze_single_failure(msg)
                if failure:
                    failures.append(failure)
        
        return failures
    
    def analyze_successes(self, messages: List[Dict[str, Any]]) -> List[SuccessAnalysis]:
        """Analyze successful operations"""
        successes = []
        
        for msg in messages:
            if msg.get('status') == 'SUCCESS':
                success = self._analyze_single_success(msg)
                if success:
                    successes.append(success)
        
        return successes
    
    def _analyze_single_failure(self, message: Dict[str, Any]) -> Optional[FailureAnalysis]:
        """Analyze a single failure"""
        try:
            service_id = message.get('service_id', '')
            ecu_address = message.get('ecu_address', '')
            nrc_code = message.get('nrc_code', '')
            
            # Get operation context
            operation_type = self.operation_context.get(service_id, f"Service {service_id}")
            
            # Determine failure type
            if nrc_code:
                failure_type = "NRC"
                failure_code = nrc_code
                
                # Get NRC explanation
                context = {
                    'service_id': service_id,
                    'ecu_type': self._get_ecu_type(ecu_address)
                }
                nrc_explanation = self.nrc_explainer.explain_nrc(nrc_code, context)
                
                proximate_cause = nrc_explanation['cause']
                root_cause = nrc_explanation['details']
                impact_level = nrc_explanation['impact']
                recommended_action = nrc_explanation['action']
                simple_explanation = nrc_explanation['simple']
                technical_details = f"NRC {nrc_code}: {nrc_explanation['name']}"
                
            elif 'timeout' in message.get('raw_data', '').lower():
                failure_type = "TIMEOUT"
                failure_code = None
                proximate_cause = "ECU did not respond within expected time"
                root_cause = "Communication failure or ECU not responding"
                impact_level = "HIGH"
                recommended_action = "Check physical connections and ECU power"
                simple_explanation = "ECU didn't answer - connection problem"
                technical_details = "No response received within timeout period"
                
            else:
                failure_type = "COMMUNICATION_ERROR"
                failure_code = None
                proximate_cause = "Communication protocol error"
                root_cause = "Network or protocol layer failure"
                impact_level = "HIGH"
                recommended_action = "Check CAN bus integrity and termination"
                simple_explanation = "Communication problem between tester and ECU"
                technical_details = "Protocol-level communication failure"
            
            return FailureAnalysis(
                operation_type=operation_type,
                ecu_address=ecu_address,
                ecu_name=message.get('ecu_name', f'ECU {ecu_address}'),
                service_id=service_id,
                service_name=message.get('service_name', f'Service {service_id}'),
                failure_type=failure_type,
                failure_code=failure_code,
                proximate_cause=proximate_cause,
                root_cause=root_cause,
                impact_level=impact_level,
                recommended_action=recommended_action,
                simple_explanation=simple_explanation,
                technical_details=technical_details,
                timestamp=str(message.get('timestamp', ''))
            )
            
        except Exception as e:
            return None
    
    def _analyze_single_success(self, message: Dict[str, Any]) -> Optional[SuccessAnalysis]:
        """Analyze a single successful operation"""
        try:
            service_id = message.get('service_id', '')
            ecu_address = message.get('ecu_address', '')
            
            operation_type = self.operation_context.get(service_id, f"Service {service_id}")
            
            # Determine operation details and security implications
            operation_details, security_level, data_accessed, simple_explanation = self._get_success_details(message)
            
            return SuccessAnalysis(
                operation_type=operation_type,
                ecu_address=ecu_address,
                ecu_name=message.get('ecu_name', f'ECU {ecu_address}'),
                service_id=service_id,
                service_name=message.get('service_name', f'Service {service_id}'),
                operation_details=operation_details,
                security_level=security_level,
                data_accessed=data_accessed,
                simple_explanation=simple_explanation,
                timestamp=str(message.get('timestamp', ''))
            )
            
        except Exception as e:
            return None
    
    def _get_success_details(self, message: Dict[str, Any]) -> Tuple[str, str, Optional[str], str]:
        """Get detailed information about successful operation"""
        service_id = message.get('service_id', '')
        payload = message.get('payload', '')
        
        if service_id == "22":  # Read Data By Identifier
            did = payload[:4] if len(payload) >= 4 else "Unknown"
            return (
                f"Successfully read data from DID {did}",
                "READ_ONLY",
                f"DID {did}",
                f"Read data from ECU successfully"
            )
        
        elif service_id == "27":  # Security Access
            if "01" in payload:
                return (
                    "Security seed requested successfully",
                    "AUTHENTICATION",
                    None,
                    "ECU provided security seed for authentication"
                )
            elif "02" in payload:
                return (
                    "Security key accepted - access granted",
                    "AUTHENTICATED",
                    None,
                    "Successfully authenticated with ECU - elevated access granted"
                )
        
        elif service_id == "10":  # Diagnostic Session Control
            session_types = {
                "01": "Default Session",
                "02": "Programming Session", 
                "03": "Extended Diagnostic Session"
            }
            session = session_types.get(payload[:2], "Unknown Session")
            return (
                f"Changed to {session}",
                "SESSION_CONTROL",
                None,
                f"ECU switched to {session.lower()}"
            )
        
        elif service_id == "31":  # Routine Control
            return (
                "Routine executed successfully",
                "CONTROL_OPERATION",
                f"Routine {payload[2:6] if len(payload) >= 6 else 'Unknown'}",
                "ECU routine/test completed successfully"
            )
        
        elif service_id in ["34", "35", "36", "37"]:  # Programming services
            return (
                "Programming operation successful",
                "PROGRAMMING",
                "Flash Memory",
                "ECU programming/flashing operation completed"
            )
        
        elif service_id == "2E":  # Write Data By Identifier
            did = payload[:4] if len(payload) >= 4 else "Unknown"
            return (
                f"Successfully wrote data to DID {did}",
                "WRITE_OPERATION",
                f"DID {did}",
                f"Modified ECU data successfully"
            )
        
        else:
            return (
                f"Service {service_id} completed successfully",
                "GENERAL",
                None,
                f"ECU operation completed without errors"
            )
    
    def _get_ecu_type(self, ecu_address: str) -> str:
        """Get ECU type from address"""
        ecu_map = {
            "7D0": "APIM",
            "716": "GWM", 
            "726": "BCM",
            "7E0": "PCM",
            "720": "IPC",
            "754": "TCU"
        }
        return ecu_map.get(ecu_address.upper(), "UNKNOWN")
    
    def generate_summary_report(self, failures: List[FailureAnalysis], successes: List[SuccessAnalysis]) -> Dict[str, Any]:
        """Generate comprehensive summary report"""
        # Failure analysis
        failure_summary = {
            'total_failures': len(failures),
            'critical_failures': len([f for f in failures if f.impact_level == 'CRITICAL']),
            'high_impact_failures': len([f for f in failures if f.impact_level == 'HIGH']),
            'nrc_failures': len([f for f in failures if f.failure_type == 'NRC']),
            'timeout_failures': len([f for f in failures if f.failure_type == 'TIMEOUT']),
            'comm_failures': len([f for f in failures if f.failure_type == 'COMMUNICATION_ERROR'])
        }
        
        # Success analysis  
        success_summary = {
            'total_successes': len(successes),
            'read_operations': len([s for s in successes if 'read' in s.operation_details.lower()]),
            'write_operations': len([s for s in successes if 'write' in s.operation_details.lower()]),
            'security_operations': len([s for s in successes if s.security_level in ['AUTHENTICATION', 'AUTHENTICATED']]),
            'programming_operations': len([s for s in successes if s.security_level == 'PROGRAMMING'])
        }
        
        # Top failure causes
        failure_causes = Counter([f.proximate_cause for f in failures])
        top_causes = failure_causes.most_common(5)
        
        # ECU involvement
        failed_ecus = Counter([f.ecu_address for f in failures])
        successful_ecus = Counter([s.ecu_address for s in successes])
        
        return {
            'failure_summary': failure_summary,
            'success_summary': success_summary,
            'top_failure_causes': [{'cause': cause, 'count': count} for cause, count in top_causes],
            'ecu_failure_rates': dict(failed_ecus),
            'ecu_success_rates': dict(successful_ecus),
            'overall_success_rate': len(successes) / (len(successes) + len(failures)) if (successes or failures) else 0
        }


def analyze_diagnostic_results(parsed_uds_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Main function to analyze diagnostic results and provide detailed failure/success analysis
    
    Args:
        parsed_uds_data: Output from enhanced_uds_parser.parse_vehicle_diagnostics()
    
    Returns:
        Comprehensive analysis with simple explanations
    """
    analyzer = FailureSuccessAnalyzer()
    
    messages = parsed_uds_data.get('messages', [])
    
    # Convert message objects to dicts for processing
    message_dicts = []
    for msg in messages:
        if hasattr(msg, '__dict__'):
            message_dicts.append(msg.__dict__)
        else:
            message_dicts.append(msg)
    
    # Analyze failures and successes
    failures = analyzer.analyze_failures(message_dicts)
    successes = analyzer.analyze_successes(message_dicts)
    
    # Generate summary
    summary = analyzer.generate_summary_report(failures, successes)
    
    return {
        'detailed_failures': [failure.__dict__ for failure in failures],
        'detailed_successes': [success.__dict__ for success in successes],
        'summary': summary,
        'simple_explanations': {
            'what_worked': [s.simple_explanation for s in successes],
            'what_failed': [f.simple_explanation for f in failures],
            'why_failed': [f.proximate_cause for f in failures],
            'how_to_fix': [f.recommended_action for f in failures]
        }
    }