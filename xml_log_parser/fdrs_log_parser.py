"""
FDRS Log Parser - Specialized parser for Ford Diagnostic and Repair System logs
Handles FDRS-specific formats, dependencies, and diagnostic communications
"""

import re
import json
from datetime import datetime
from typing import List, Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class FDRSSystemInfo:
    """FDRS System Information"""
    fdrs_version: str
    fdsp_server_url: str
    dependencies: Dict[str, str]
    timestamp: Optional[datetime] = None

@dataclass
class DiagnosticService:
    """UDS Diagnostic Service Information"""
    service_code: str
    service_name: str
    description: str
    request_data: str
    response_data: str
    timestamp: datetime
    status: str  # SUCCESS, ERROR, NRC
    nrc_code: Optional[str] = None
    nrc_description: Optional[str] = None

class FDRSLogParser:
    """Specialized parser for FDRS diagnostic logs"""
    
    # UDS Service codes and descriptions
    UDS_SERVICES = {
        "10": "Diagnostic Session Control",
        "11": "ECU Reset",
        "14": "Clear Diagnostic Information",
        "19": "Read DTC Information",
        "22": "Read Data By Identifier",
        "23": "Read Memory By Address",
        "24": "Read Scaling Data By Identifier",
        "27": "Security Access",
        "28": "Communication Control",
        "2A": "Read Data By Periodic Identifier",
        "2C": "Dynamically Define Data Identifier",
        "2E": "Write Data By Identifier",
        "2F": "Input Output Control By Identifier",
        "31": "Routine Control",
        "34": "Request Download",
        "35": "Request Upload",
        "36": "Transfer Data",
        "37": "Request Transfer Exit",
        "3D": "Write Memory By Address",
        "3E": "Tester Present",
        "83": "Access Timing Parameter",
        "84": "Secured Data Transmission",
        "85": "Control DTC Setting",
        "86": "Response On Event",
        "87": "Link Control"
    }
    
    # Enhanced NRC codes with FDRS-specific context
    NRC_CODES = {
        "10": "General Reject - Service not supported",
        "11": "Service Not Supported - ECU doesn't support this service",
        "12": "Sub-Function Not Supported - Invalid sub-function parameter",
        "13": "Incorrect Message Length Or Invalid Format",
        "14": "Response Too Long - Response exceeds buffer size",
        "21": "Busy Repeat Request - ECU busy, retry later",
        "22": "Conditions Not Correct - Prerequisites not met",
        "24": "Request Sequence Error - Wrong order of operations",
        "25": "No Response From Subnet Component",
        "26": "Failure Prevents Execution Of Requested Action",
        "31": "Request Out Of Range - DID/Address/Parameter outside valid range",
        "33": "Security Access Denied - Authentication required",
        "35": "Invalid Key - Wrong security key provided",
        "36": "Exceed Number Of Attempts - Too many failed attempts",
        "37": "Required Time Delay Not Expired - Must wait longer",
        "70": "Upload Download Not Accepted",
        "71": "Transfer Data Suspended",
        "72": "General Programming Failure",
        "73": "Wrong Block Sequence Counter",
        "78": "Request Correctly Received - Response Pending",
        "7E": "Sub-Function Not Supported In Active Session",
        "7F": "Service Not Supported In Active Session",
    }
    
    def __init__(self):
        self.system_info: Optional[FDRSSystemInfo] = None
        self.diagnostic_services: List[DiagnosticService] = []
        self.parsed_data: Dict[str, Any] = {}
    
    def parse_log_text(self, log_text: str) -> Dict[str, Any]:
        """Parse FDRS log text format"""
        lines = log_text.strip().split('\n')
        
        # Parse system information
        self._parse_system_info(lines)
        
        # Parse diagnostic communications
        self._parse_diagnostic_communications(lines)
        
        # Generate summary
        summary = self._generate_summary()
        
        return {
            "system_info": self.system_info,
            "diagnostic_services": self.diagnostic_services,
            "summary": summary,
            "parsed_data": self.parsed_data
        }
    
    def _parse_system_info(self, lines: List[str]) -> None:
        """Extract FDRS system information"""
        for line in lines:
            if "[SYSTEM]" in line and "fdrsVersion" in line:
                try:
                    # Extract JSON part
                    json_match = re.search(r'\{.*\}', line)
                    if json_match:
                        system_data = json.loads(json_match.group())
                        self.system_info = FDRSSystemInfo(
                            fdrs_version=system_data.get("fdrsVersion", "Unknown"),
                            fdsp_server_url=system_data.get("fdspServerURL", "Unknown"),
                            dependencies=system_data.get("dependency", {})
                        )
                except (json.JSONDecodeError, KeyError) as e:
                    print(f"Error parsing system info: {e}")
    
    def _parse_diagnostic_communications(self, lines: List[str]) -> None:
        """Parse UDS diagnostic service communications"""
        current_service = {}
        
        for i, line in enumerate(lines):
            # Extract timestamp
            timestamp_match = re.match(r'^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2},\d{3})', line)
            if timestamp_match:
                try:
                    timestamp = datetime.strptime(timestamp_match.group(1), "%Y-%m-%dT%H:%M:%S,%f")
                    current_service['timestamp'] = timestamp
                except ValueError:
                    pass
            
            # Parse diagnostic service requests
            if "Diag service request" in line:
                hex_match = re.search(r'([0-9A-Fa-f]+)$', line.strip())
                if hex_match:
                    request_data = hex_match.group(1)
                    current_service['request_data'] = request_data
                    
                    # Extract service code (usually byte 4-5 in the message)
                    if len(request_data) >= 10:  # At least 5 bytes
                        service_code = request_data[8:10]  # Bytes 4-5
                        current_service['service_code'] = service_code
                        current_service['service_name'] = self.UDS_SERVICES.get(service_code.upper(), f"Unknown Service 0x{service_code}")
            
            # Parse diagnostic service responses
            elif "Diag service response" in line:
                hex_match = re.search(r'([0-9A-Fa-f]+)$', line.strip())
                if hex_match:
                    response_data = hex_match.group(1)
                    current_service['response_data'] = response_data
                    
                    # Check if it's a negative response (7F)
                    if len(response_data) >= 10:
                        response_type = response_data[8:10]  # Byte 4
                        if response_type.upper() == "7F":
                            current_service['status'] = "NRC_ERROR"
                            # NRC code is typically the next byte
                            if len(response_data) >= 12:
                                nrc_code = response_data[10:12]
                                current_service['nrc_code'] = nrc_code
                                current_service['nrc_description'] = self.NRC_CODES.get(nrc_code.upper(), f"Unknown NRC: {nrc_code}")
                        else:
                            current_service['status'] = "SUCCESS"
            
            # Parse NRC information
            elif "NRC =" in line:
                nrc_match = re.search(r'NRC = ([0-9A-Fa-f]+)', line)
                if nrc_match:
                    nrc_code = nrc_match.group(1)
                    current_service['nrc_code'] = nrc_code
                    current_service['nrc_description'] = self.NRC_CODES.get(nrc_code.upper(), f"Unknown NRC: {nrc_code}")
                    current_service['status'] = "NRC_ERROR"
            
            # Parse DID information
            elif "Type =" in line and "ECU Configuration" in line:
                current_service['data_type'] = "ECU Configuration"
            
            # When we hit the end of a diagnostic sequence, save it
            if ("END ~~" in line or "BEGIN ~~" in line) and current_service:
                if 'service_code' in current_service and 'timestamp' in current_service:
                    diagnostic_service = DiagnosticService(
                        service_code=current_service.get('service_code', 'Unknown'),
                        service_name=current_service.get('service_name', 'Unknown Service'),
                        description=current_service.get('data_type', 'Diagnostic Communication'),
                        request_data=current_service.get('request_data', ''),
                        response_data=current_service.get('response_data', ''),
                        timestamp=current_service.get('timestamp', datetime.now()),
                        status=current_service.get('status', 'UNKNOWN'),
                        nrc_code=current_service.get('nrc_code'),
                        nrc_description=current_service.get('nrc_description')
                    )
                    self.diagnostic_services.append(diagnostic_service)
                
                # Reset for next service
                if "BEGIN ~~" in line:
                    current_service = {'timestamp': current_service.get('timestamp')}
                else:
                    current_service = {}
        
        # Save any remaining service at the end of log
        if current_service and 'service_code' in current_service:
            diagnostic_service = DiagnosticService(
                service_code=current_service.get('service_code', 'Unknown'),
                service_name=current_service.get('service_name', 'Unknown Service'),
                description=current_service.get('data_type', 'Diagnostic Communication'),
                request_data=current_service.get('request_data', ''),
                response_data=current_service.get('response_data', ''),
                timestamp=current_service.get('timestamp', datetime.now()),
                status=current_service.get('status', 'UNKNOWN'),
                nrc_code=current_service.get('nrc_code'),
                nrc_description=current_service.get('nrc_description')
            )
            self.diagnostic_services.append(diagnostic_service)
    
    def _generate_summary(self) -> Dict[str, Any]:
        """Generate parsing summary"""
        total_services = len(self.diagnostic_services)
        success_count = sum(1 for s in self.diagnostic_services if s.status == "SUCCESS")
        nrc_errors = sum(1 for s in self.diagnostic_services if s.status == "NRC_ERROR")
        
        # Count by service type
        service_counts = {}
        for service in self.diagnostic_services:
            service_counts[service.service_name] = service_counts.get(service.service_name, 0) + 1
        
        # Count NRC types
        nrc_counts = {}
        for service in self.diagnostic_services:
            if service.nrc_code:
                nrc_counts[service.nrc_code] = nrc_counts.get(service.nrc_code, 0) + 1
        
        return {
            "total_diagnostic_services": total_services,
            "successful_services": success_count,
            "nrc_errors": nrc_errors,
            "success_rate": (success_count / total_services * 100) if total_services > 0 else 0,
            "service_breakdown": service_counts,
            "nrc_breakdown": nrc_counts,
            "fdrs_version": self.system_info.fdrs_version if self.system_info else "Unknown",
            "dependency_modules": len(self.system_info.dependencies) if self.system_info else 0
        }
    
    def get_detailed_analysis(self) -> Dict[str, Any]:
        """Get detailed analysis of the FDRS log"""
        analysis = {
            "system_analysis": self._analyze_system_info(),
            "communication_analysis": self._analyze_communications(),
            "error_analysis": self._analyze_errors(),
            "recommendations": self._generate_recommendations()
        }
        return analysis
    
    def _analyze_system_info(self) -> Dict[str, Any]:
        """Analyze FDRS system information"""
        if not self.system_info:
            return {"status": "No system information found"}
        
        return {
            "fdrs_version": self.system_info.fdrs_version,
            "server_connection": "Connected" if self.system_info.fdsp_server_url else "Not configured",
            "dependency_modules": len(self.system_info.dependencies),
            "key_modules": {
                "core": self.system_info.dependencies.get("core", "Unknown"),
                "comms": self.system_info.dependencies.get("comms", "Unknown"),
                "framework": self.system_info.dependencies.get("framework", "Unknown")
            }
        }
    
    def _analyze_communications(self) -> Dict[str, Any]:
        """Analyze diagnostic communications"""
        if not self.diagnostic_services:
            return {"status": "No diagnostic communications found"}
        
        # Find the most recent communication
        latest_service = max(self.diagnostic_services, key=lambda x: x.timestamp)
        
        # Analyze service 0x22 (Read Data By Identifier) specifically
        read_did_services = [s for s in self.diagnostic_services if s.service_code.upper() == "22"]
        
        return {
            "latest_communication": {
                "service": latest_service.service_name,
                "status": latest_service.status,
                "timestamp": latest_service.timestamp.isoformat(),
                "nrc_error": latest_service.nrc_description if latest_service.nrc_code else None
            },
            "read_did_analysis": {
                "total_attempts": len(read_did_services),
                "failed_attempts": sum(1 for s in read_did_services if s.status == "NRC_ERROR"),
                "success_rate": (sum(1 for s in read_did_services if s.status == "SUCCESS") / len(read_did_services) * 100) if read_did_services else 0
            }
        }
    
    def _analyze_errors(self) -> Dict[str, Any]:
        """Analyze error patterns"""
        errors = [s for s in self.diagnostic_services if s.status == "NRC_ERROR"]
        
        if not errors:
            return {"status": "No errors found"}
        
        # Analyze NRC 31 specifically (Request Out Of Range)
        nrc_31_errors = [e for e in errors if e.nrc_code and e.nrc_code.upper() == "31"]
        
        error_analysis = {
            "total_errors": len(errors),
            "nrc_31_errors": len(nrc_31_errors),
            "error_breakdown": {}
        }
        
        # Count each NRC type
        for error in errors:
            nrc = error.nrc_code or "Unknown"
            error_analysis["error_breakdown"][nrc] = error_analysis["error_breakdown"].get(nrc, 0) + 1
        
        return error_analysis
    
    def _generate_recommendations(self) -> List[str]:
        """Generate troubleshooting recommendations"""
        recommendations = []
        
        # Check for NRC 31 errors
        nrc_31_errors = [s for s in self.diagnostic_services if s.nrc_code and s.nrc_code.upper() == "31"]
        if nrc_31_errors:
            recommendations.append("🔍 NRC 31 (Request Out Of Range) detected:")
            recommendations.append("  • Check if the Data Identifier (DID) is supported by this ECU")
            recommendations.append("  • Verify the ECU is in the correct diagnostic session")
            recommendations.append("  • Confirm the ECU variant supports the requested data")
        
        # Check for security access issues
        security_errors = [s for s in self.diagnostic_services if s.nrc_code and s.nrc_code.upper() in ["33", "35", "36"]]
        if security_errors:
            recommendations.append("🔐 Security access issues detected:")
            recommendations.append("  • Ensure proper authentication with the ECU")
            recommendations.append("  • Check if security access is required for this operation")
        
        # Check for communication issues
        comm_errors = [s for s in self.diagnostic_services if s.nrc_code and s.nrc_code.upper() in ["21", "22", "78"]]
        if comm_errors:
            recommendations.append("📡 Communication issues detected:")
            recommendations.append("  • Check vehicle bus communication stability")
            recommendations.append("  • Verify ECU is responsive and not busy")
        
        if not recommendations:
            recommendations.append("✅ No major issues detected in diagnostic communications")
        
        return recommendations

def parse_fdrs_log(log_content: str) -> Dict[str, Any]:
    """Convenience function to parse FDRS log content"""
    parser = FDRSLogParser()
    return parser.parse_log_text(log_content)

# Example usage
if __name__ == "__main__":
    # Test with the provided log sample
    sample_log = """[SYSTEM] {"fdrsVersion":"45.6.8","fdspServerURL":"https://www.fdspcl.dealerconnection.com","dependency":{"core":"11.10.5","comms":"33.13.1-hf","commsLibraries":"32.12.2-USA","commsRnd":"5.4.0-SNAPSHOT","complexTools":"45.5.16","dspDomain":"15.3.21","framework":"72.31.55","hmi":"73.13.16","otxCommon":"40.21.20"}}

2025-10-13T13:52:07,414 INFO otx.core.BaseApplication - Adding runtime logs appender to COMMS channel logger

2025-10-13T14:35:21,500 INFO class otxcontainer.G2171556.authorLogs - 

LOG>> END ~~ ProcessDidResponseValues

2025-10-13T14:35:21,504 INFO class otxcontainer.G2171556.authorLogs - 

LOG>> F16B (ASCII) =  MU5T-14J003-AF

2025-10-13T14:35:21,506 INFO class otxcontainer.G2171556.authorLogs - 

LOG>> F16B Type =  ECU Configuration

2025-10-13T14:35:21,509 INFO class otxcontainer.G2171556.authorLogs - 

LOG>> BEGIN ~~ ReadDid

2025-10-13T14:35:21,512 INFO class otxcontainer.G2171556.authorLogs - 

LOG>> Diag service request :  000007D022A011

2025-10-13T14:35:21,522 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,000,000,000 - [00,00,07,D0,22,A0,11]

2025-10-13T14:35:21,525 DEBUG api.service.Channel - ISO15765_PS TX      -> 0,784,127,777 - [00,00,07,D0]

2025-10-13T14:35:21,530 DEBUG api.service.Channel - ISO15765_PS RX      <- 0,784,133,615 - [00,00,07,D8,7F,22,31]

2025-10-13T14:35:21,530 INFO class otxcontainer.G2171556.authorLogs - 

LOG>> Diag service response:  000007D87F2231

2025-10-13T14:35:21,534 INFO class otxcontainer.G2171556.authorLogs - 

LOG>> Constant-field byte 4 (hex) : 7F

2025-10-13T14:35:21,538 INFO class otxcontainer.G2171556.authorLogs - 

LOG>> NRC = 31 (requestOutOfRange)"""
    
    parser = FDRSLogParser()
    result = parser.parse_log_text(sample_log)
    
    print("=== FDRS Log Analysis ===")
    print(f"FDRS Version: {result['system_info'].fdrs_version}")
    print(f"Diagnostic Services Found: {len(result['diagnostic_services'])}")
    print(f"Success Rate: {result['summary']['success_rate']:.1f}%")
    print(f"NRC Errors: {result['summary']['nrc_errors']}")
    
    # Get detailed analysis
    analysis = parser.get_detailed_analysis()
    print("\n=== Recommendations ===")
    for rec in analysis['recommendations']:
        print(rec)