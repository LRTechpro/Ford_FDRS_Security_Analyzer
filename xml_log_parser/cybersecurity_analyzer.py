"""
Enhanced Cybersecurity Analyzer for Vehicle Logs
Detects security threats, unauthorized access attempts, and vulnerabilities
Includes comprehensive UDS message analysis and failure explanations
"""

from typing import Dict, List, Any, Tuple
import re
from collections import Counter, defaultdict
from datetime import datetime

# Import enhanced UDS parser and failure analyzer
try:
    from enhanced_uds_parser import UDSMessageParser, parse_vehicle_diagnostics
    from failure_success_analyzer import analyze_diagnostic_results, FailureSuccessAnalyzer
    UDS_PARSER_AVAILABLE = True
except ImportError:
    UDS_PARSER_AVAILABLE = False


class CybersecurityAnalyzer:
    """Analyzes logs for cybersecurity threats and vulnerabilities"""
    
    # Security threat patterns
    SECURITY_PATTERNS = {
        'unauthorized_access': [
            r'unauthorized',
            r'access\s+denied',
            r'authentication\s+failed',
            r'invalid\s+credentials',
            r'security\s+access\s+denied',
            r'negative\s+response.*(?:33|35|37)',  # NRC 33, 35, 37 are security-related
        ],
        'seed_key_issues': [
            r'seed.*key',
            r'security\s+access',
            r'0x27',  # Security Access service
            r'service\s+27',
            r'requestSeed',
            r'sendKey',
        ],
        'reprogramming_threats': [
            r'unauthorized.*(?:flash|program|update)',
            r'(?:flash|program).*failed.*security',
            r'invalid.*signature',
            r'verification.*failed',
            r'bootloader.*error',
        ],
        'communication_anomalies': [
            r'unexpected\s+message',
            r'malformed.*(?:frame|packet|message)',
            r'invalid\s+(?:can|lin|ethernet)',
            r'bus\s+off',
            r'communication\s+lost',
            r'jamming',
        ],
        'dos_attacks': [
            r'(?:flood|flooding)',
            r'excessive.*(?:requests|messages)',
            r'rate\s+limit',
            r'timeout.*repeated',
            r'buffer\s+overflow',
        ],
        'diagnostic_vulnerabilities': [
            r'diagnostic.*disabled',
            r'dtc.*(?:cleared|erased).*unauthorized',
            r'illegal\s+request',
            r'service.*not\s+supported.*unexpected',
        ],
        'firmware_integrity': [
            r'checksum.*(?:failed|mismatch)',
            r'crc.*(?:error|invalid)',
            r'hash.*mismatch',
            r'integrity.*(?:check|verification).*failed',
            r'tampering.*detected',
        ],
    }
    
    # Critical security-related NRC codes
    SECURITY_NRC_CODES = {
        '33': 'Security Access Denied',
        '35': 'Invalid Key',
        '36': 'Exceeded Number of Attempts',
        '37': 'Required Time Delay Not Expired',
        '7F': 'Service Not Supported in Active Session',
        '22': 'Conditions Not Correct (Potential Security)',
        '24': 'Request Sequence Error (Potential Attack)',
    }
    
    # Critical DIDs that could be security targets
    SENSITIVE_DIDS = {
        '8071': 'Software Version',
        'F188': 'ECU Software Number',
        'F18C': 'ECU Serial Number',
        '8033': 'Part Number',
        'F124': 'System Supplier Code',
        'DE01': 'ECU Hardware Number',
    }
    
    def __init__(self):
        self.threats = []
        self.threat_counts = Counter()
        self.timeline = []
        self.affected_modules = set()
        self.severity_stats = {'critical': 0, 'high': 0, 'medium': 0, 'low': 0}
        
    def analyze(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Analyze log results for cybersecurity threats
        
        Args:
            results: List of parsed log entries
            
        Returns:
            Dictionary containing threat analysis
        """
        self.threats = []
        self.threat_counts = Counter()
        self.timeline = []
        self.affected_modules = set()
        self.severity_stats = {'critical': 0, 'high': 0, 'medium': 0, 'low': 0}
        
        for idx, result in enumerate(results):
            self._analyze_entry(result, idx)
        
        return {
            'threats': self.threats,
            'threat_summary': dict(self.threat_counts),
            'timeline': self.timeline,
            'affected_modules': list(self.affected_modules),
            'severity_stats': self.severity_stats,
            'total_threats': len(self.threats),
        }
    
    def _analyze_entry(self, entry: Dict[str, Any], index: int):
        """Analyze a single log entry for security threats"""
        text = str(entry).lower()
        original_text = str(entry)
        
        # Check each threat category
        for category, patterns in self.SECURITY_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    severity = self._determine_severity(category, text)
                    threat = {
                        'index': index,
                        'category': category,
                        'severity': severity,
                        'description': self._get_threat_description(category),
                        'details': self._extract_threat_details(original_text, pattern),
                        'timestamp': self._extract_timestamp(entry),
                        'affected_modules': self._extract_modules(original_text),
                    }
                    
                    self.threats.append(threat)
                    self.threat_counts[category] += 1
                    self.severity_stats[severity] += 1
                    self.affected_modules.update(threat['affected_modules'])
                    self.timeline.append({
                        'time': threat['timestamp'],
                        'category': category,
                        'severity': severity,
                    })
                    break  # Only count once per category per entry
        
        # Check for security NRC codes
        self._check_security_nrcs(original_text, index)
        
        # Check for sensitive DID access
        self._check_sensitive_dids(original_text, index)
    
    def _determine_severity(self, category: str, text: str) -> str:
        """Determine threat severity based on category and context"""
        # Critical severity
        if category in ['unauthorized_access', 'firmware_integrity', 'reprogramming_threats']:
            if any(kw in text for kw in ['failed', 'denied', 'invalid', 'tamper']):
                return 'critical'
        
        # High severity
        if category in ['seed_key_issues', 'dos_attacks']:
            if any(kw in text for kw in ['repeated', 'multiple', 'exceeded']):
                return 'high'
        
        # Medium severity
        if category in ['communication_anomalies', 'diagnostic_vulnerabilities']:
            return 'medium'
        
        # Default to medium
        return 'medium'
    
    def _get_threat_description(self, category: str) -> str:
        """Get human-readable description for threat category"""
        descriptions = {
            'unauthorized_access': 'Unauthorized Access Attempt',
            'seed_key_issues': 'Security Access (Seed-Key) Issue',
            'reprogramming_threats': 'Unauthorized Reprogramming Attempt',
            'communication_anomalies': 'Communication Anomaly Detected',
            'dos_attacks': 'Potential Denial-of-Service Attack',
            'diagnostic_vulnerabilities': 'Diagnostic Security Vulnerability',
            'firmware_integrity': 'Firmware Integrity Violation',
        }
        return descriptions.get(category, 'Unknown Security Threat')
    
    def _extract_threat_details(self, text: str, pattern: str) -> str:
        """Extract relevant details about the threat"""
        # Get context around the match
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            start = max(0, match.start() - 50)
            end = min(len(text), match.end() + 50)
            context = text[start:end].strip()
            return context if len(context) < 200 else context[:197] + '...'
        return text[:200] if len(text) < 200 else text[:197] + '...'
    
    def _extract_timestamp(self, entry: Dict[str, Any]) -> str:
        """Extract timestamp from entry"""
        if isinstance(entry, dict):
            return entry.get('timestamp', entry.get('time', 'Unknown'))
        return 'Unknown'
    
    def _extract_modules(self, text: str) -> List[str]:
        """Extract ECU modules mentioned in the text"""
        modules = []
        # Look for 3-char hex that could be ECU addresses
        ecu_pattern = r'\b(7[0-9A-Fa-f]{2}|6[EF][0-7])\b'
        matches = re.findall(ecu_pattern, text)
        return [m.upper() for m in matches]
    
    def _check_security_nrcs(self, text: str, index: int):
        """Check for security-related negative response codes"""
        for nrc_code, description in self.SECURITY_NRC_CODES.items():
            pattern = rf'\b(?:0x)?{nrc_code}\b'
            if re.search(pattern, text, re.IGNORECASE):
                threat = {
                    'index': index,
                    'category': 'security_nrc',
                    'severity': 'high' if nrc_code in ['33', '35', '36'] else 'medium',
                    'description': f'Security NRC {nrc_code}: {description}',
                    'details': text[:200] if len(text) < 200 else text[:197] + '...',
                    'timestamp': 'Unknown',
                    'affected_modules': self._extract_modules(text),
                }
                self.threats.append(threat)
                self.threat_counts['security_nrc'] += 1
                self.severity_stats[threat['severity']] += 1
    
    def _check_sensitive_dids(self, text: str, index: int):
        """Check for access to sensitive DIDs"""
        for did, description in self.SENSITIVE_DIDS.items():
            pattern = rf'\bDID\s*(?:0x)?{did}\b'
            if re.search(pattern, text, re.IGNORECASE):
                # Check if it's a read/write operation
                if any(kw in text.lower() for kw in ['read', 'write', 'request', '0x22', '0x2e']):
                    threat = {
                        'index': index,
                        'category': 'sensitive_did_access',
                        'severity': 'medium',
                        'description': f'Access to Sensitive DID {did}: {description}',
                        'details': text[:200] if len(text) < 200 else text[:197] + '...',
                        'timestamp': 'Unknown',
                        'affected_modules': self._extract_modules(text),
                    }
                    self.threats.append(threat)
                    self.threat_counts['sensitive_did_access'] += 1
                    self.severity_stats['medium'] += 1
    
    def format_report_text(self) -> str:
        """Generate a text report of cybersecurity findings"""
        if not self.threats:
            return "✅ NO SECURITY THREATS DETECTED\n\nThe log analysis found no cybersecurity threats or vulnerabilities."
        
        lines = []
        lines.append("=" * 80)
        lines.append("🔒 CYBERSECURITY THREAT ANALYSIS REPORT")
        lines.append("=" * 80)
        lines.append("")
        
        # Summary
        lines.append("📊 THREAT SUMMARY")
        lines.append("-" * 80)
        lines.append(f"Total Threats Detected: {len(self.threats)}")
        lines.append(f"Critical: {self.severity_stats['critical']} | High: {self.severity_stats['high']} | "
                    f"Medium: {self.severity_stats['medium']} | Low: {self.severity_stats['low']}")
        lines.append("")
        
        # Affected modules
        if self.affected_modules:
            lines.append("🎯 AFFECTED MODULES")
            lines.append("-" * 80)
            lines.append(", ".join(sorted(self.affected_modules)))
            lines.append("")
        
        # Threat categories
        lines.append("📋 THREAT CATEGORIES")
        lines.append("-" * 80)
        for category, count in self.threat_counts.most_common():
            category_name = self._get_threat_description(category)
            lines.append(f"  • {category_name}: {count} occurrence(s)")
        lines.append("")
        
        # Detailed threats
        lines.append("🚨 DETAILED THREAT LOG")
        lines.append("=" * 80)
        
        # Sort by severity
        severity_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
        sorted_threats = sorted(self.threats, key=lambda t: severity_order.get(t['severity'], 99))
        
        for i, threat in enumerate(sorted_threats, 1):
            severity_icon = {
                'critical': '🔴',
                'high': '🟠',
                'medium': '🟡',
                'low': '🟢'
            }.get(threat['severity'], '⚪')
            
            lines.append(f"\n{severity_icon} Threat #{i} - {threat['severity'].upper()}")
            lines.append("-" * 80)
            lines.append(f"Category: {threat['description']}")
            if threat.get('affected_modules'):
                lines.append(f"Modules: {', '.join(threat['affected_modules'])}")
            lines.append(f"Details: {threat['details']}")
            lines.append("")
        
        # Recommendations
        lines.append("=" * 80)
        lines.append("💡 SECURITY RECOMMENDATIONS")
        lines.append("=" * 80)
        lines.append(self._generate_recommendations())
        
        return "\n".join(lines)
    
    def _generate_recommendations(self) -> str:
        """Generate security recommendations based on detected threats"""
        recommendations = []
        
        if self.threat_counts.get('unauthorized_access', 0) > 0:
            recommendations.append("• Review and strengthen security access controls")
            recommendations.append("• Verify seed-key algorithm implementation")
        
        if self.threat_counts.get('reprogramming_threats', 0) > 0:
            recommendations.append("• Implement firmware signature verification")
            recommendations.append("• Enable secure boot if not already active")
        
        if self.threat_counts.get('communication_anomalies', 0) > 0:
            recommendations.append("• Investigate CAN/network communication integrity")
            recommendations.append("• Check for physical bus issues or interference")
        
        if self.threat_counts.get('dos_attacks', 0) > 0:
            recommendations.append("• Implement rate limiting on diagnostic services")
            recommendations.append("• Review message flooding patterns")
        
        if self.threat_counts.get('firmware_integrity', 0) > 0:
            recommendations.append("• Verify firmware checksums and signatures")
            recommendations.append("• Investigate potential tampering or corruption")
        
        if not recommendations:
            recommendations.append("• Continue monitoring for security anomalies")
            recommendations.append("• Maintain security best practices")
        
        return "\n".join(recommendations)
    
    def analyze_with_uds_parser(self, raw_log_content: str) -> Dict[str, Any]:
        """
        Enhanced analysis using UDS parser and failure analyzer
        
        Args:
            raw_log_content: Raw log file content
            
        Returns:
            Comprehensive security analysis with detailed explanations
        """
        results = {}
        
        if not UDS_PARSER_AVAILABLE:
            results['uds_analysis'] = {
                'error': 'UDS parser not available - using basic analysis only'
            }
            # Fall back to basic analysis
            basic_results = self.analyze([{'content': raw_log_content}])
            results.update(basic_results)
            return results
        
        try:
            # Parse with enhanced UDS parser
            uds_results = parse_vehicle_diagnostics(raw_log_content)
            
            # Analyze failures and successes
            failure_success_analysis = analyze_diagnostic_results(uds_results)
            
            # Perform basic threat analysis on raw content
            basic_analysis = self.analyze([{'content': raw_log_content}])
            
            # Combine analyses
            results.update({
                'basic_threat_analysis': basic_analysis,
                'uds_message_analysis': uds_results,
                'failure_success_analysis': failure_success_analysis,
                'enhanced_security_assessment': self._assess_enhanced_security(
                    uds_results, failure_success_analysis
                ),
                'simple_explanations': failure_success_analysis.get('simple_explanations', {}),
                'detailed_recommendations': self._generate_enhanced_recommendations(
                    uds_results, failure_success_analysis
                )
            })
            
        except Exception as e:
            results['uds_analysis'] = {
                'error': f'UDS analysis failed: {str(e)}'
            }
            # Fall back to basic analysis
            basic_results = self.analyze([{'content': raw_log_content}])
            results.update(basic_results)
        
        return results
    
    def _assess_enhanced_security(self, uds_results: Dict[str, Any], 
                                failure_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Enhanced security assessment using UDS and failure analysis"""
        security_assessment = {
            'security_score': 100,  # Start with perfect score, deduct for issues
            'risk_level': 'LOW',
            'security_issues': [],
            'attack_indicators': [],
            'authentication_analysis': {},
            'data_access_analysis': {},
            'programming_analysis': {}
        }
        
        # Analyze failures for security implications
        failures = failure_analysis.get('detailed_failures', [])
        successes = failure_analysis.get('detailed_successes', [])
        
        # Check for authentication failures
        auth_failures = [f for f in failures if f.get('service_id') == '27']
        if auth_failures:
            security_assessment['security_score'] -= len(auth_failures) * 10
            security_assessment['authentication_analysis'] = {
                'total_attempts': len(auth_failures),
                'failure_rate': 100,  # All auth attempts failed
                'security_implications': 'Multiple authentication failures may indicate brute force attack'
            }
            security_assessment['security_issues'].append(
                f"{len(auth_failures)} security access failures detected"
            )
        
        # Check for successful authentications
        auth_successes = [s for s in successes if s.get('service_id') == '27']
        if auth_successes:
            total_auth = len(auth_failures) + len(auth_successes)
            failure_rate = (len(auth_failures) / total_auth) * 100 if total_auth > 0 else 0
            security_assessment['authentication_analysis'] = {
                'total_attempts': total_auth,
                'failure_rate': failure_rate,
                'successful_auths': len(auth_successes),
                'security_implications': 'Authentication successful - authorized access'
            }
        
        # Analyze data access patterns
        read_operations = [s for s in successes if s.get('service_id') == '22']
        write_operations = [s for s in successes if s.get('service_id') == '2E']
        
        security_assessment['data_access_analysis'] = {
            'read_operations': len(read_operations),
            'write_operations': len(write_operations),
            'data_modified': len(write_operations) > 0,
            'sensitive_data_accessed': self._check_sensitive_data_access(read_operations + write_operations)
        }
        
        # Analyze programming operations
        programming_ops = [s for s in successes if s.get('service_id') in ['34', '35', '36', '37']]
        programming_failures = [f for f in failures if f.get('service_id') in ['34', '35', '36', '37']]
        
        if programming_ops or programming_failures:
            security_assessment['programming_analysis'] = {
                'programming_attempted': True,
                'successful_programming': len(programming_ops),
                'failed_programming': len(programming_failures),
                'security_implications': 'ECU programming detected - verify authorization'
            }
            if programming_ops:
                security_assessment['security_score'] -= 20  # Programming is high-risk
                security_assessment['security_issues'].append("ECU programming operations detected")
        
        # Check for attack indicators
        if len(failures) > 10:
            security_assessment['attack_indicators'].append("High number of failed operations")
            security_assessment['security_score'] -= 15
        
        # Determine risk level based on score
        if security_assessment['security_score'] >= 80:
            security_assessment['risk_level'] = 'LOW'
        elif security_assessment['security_score'] >= 60:
            security_assessment['risk_level'] = 'MEDIUM'
        elif security_assessment['security_score'] >= 40:
            security_assessment['risk_level'] = 'HIGH'
        else:
            security_assessment['risk_level'] = 'CRITICAL'
        
        return security_assessment
    
    def _check_sensitive_data_access(self, operations: List[Dict[str, Any]]) -> List[str]:
        """Check if any sensitive data was accessed"""
        sensitive_data = []
        
        for op in operations:
            data_accessed = op.get('data_accessed', '')
            if data_accessed:
                # Check against known sensitive DIDs
                for did, description in self.SENSITIVE_DIDS.items():
                    if did in data_accessed:
                        sensitive_data.append(f"DID {did}: {description}")
        
        return sensitive_data
    
    def _generate_enhanced_recommendations(self, uds_results: Dict[str, Any], 
                                         failure_analysis: Dict[str, Any]) -> List[str]:
        """Generate enhanced recommendations based on detailed analysis"""
        recommendations = []
        
        failures = failure_analysis.get('detailed_failures', [])
        successes = failure_analysis.get('detailed_successes', [])
        
        # Authentication-specific recommendations
        auth_failures = [f for f in failures if f.get('service_id') == '27']
        if len(auth_failures) > 3:
            recommendations.append(
                "🔐 CRITICAL: Multiple security access failures detected. "
                "Investigate potential unauthorized access attempts."
            )
            recommendations.append(
                "🔍 Verify that seed-key algorithms are implemented correctly and securely."
            )
        
        # Programming recommendations
        programming_ops = [s for s in successes if s.get('service_id') in ['34', '35', '36', '37']]
        if programming_ops:
            recommendations.append(
                "⚠️  ECU programming detected. Verify that firmware modifications are authorized."
            )
            recommendations.append(
                "🔒 Ensure programming operations use proper authentication and encryption."
            )
        
        # Communication recommendations
        comm_failures = [f for f in failures if f.get('failure_type') in ['TIMEOUT', 'COMMUNICATION_ERROR']]
        if len(comm_failures) > 5:
            recommendations.append(
                "🌐 High number of communication failures detected. "
                "Check network integrity and potential DoS attacks."
            )
        
        # Data access recommendations
        write_ops = [s for s in successes if s.get('service_id') == '2E']
        if write_ops:
            recommendations.append(
                "📝 Data modification operations detected. Verify authorization for configuration changes."
            )
        
        # General security recommendations
        total_failures = len(failures)
        total_operations = len(failures) + len(successes)
        if total_operations > 0:
            failure_rate = (total_failures / total_operations) * 100
            if failure_rate > 30:
                recommendations.append(
                    f"📊 High failure rate ({failure_rate:.1f}%) detected. "
                    "Investigate potential security issues or system problems."
                )
        
        if not recommendations:
            recommendations.append("✅ No immediate security concerns identified.")
            recommendations.append("🛡️  Continue monitoring for unusual diagnostic activity.")
        
        return recommendations
    
    def generate_comprehensive_report(self, enhanced_analysis: Dict[str, Any]) -> str:
        """Generate comprehensive security report with UDS analysis"""
        lines = []
        lines.append("=" * 100)
        lines.append("🔒 COMPREHENSIVE CYBERSECURITY ANALYSIS REPORT")
        lines.append("=" * 100)
        lines.append("")
        
        # Enhanced Security Assessment
        if 'enhanced_security_assessment' in enhanced_analysis:
            assessment = enhanced_analysis['enhanced_security_assessment']
            lines.append("🎯 SECURITY ASSESSMENT")
            lines.append("-" * 100)
            lines.append(f"Security Score: {assessment['security_score']}/100")
            lines.append(f"Risk Level: {assessment['risk_level']}")
            lines.append("")
            
            if assessment['security_issues']:
                lines.append("🚨 SECURITY ISSUES IDENTIFIED:")
                for issue in assessment['security_issues']:
                    lines.append(f"  • {issue}")
                lines.append("")
            
            if assessment['attack_indicators']:
                lines.append("⚠️  ATTACK INDICATORS:")
                for indicator in assessment['attack_indicators']:
                    lines.append(f"  • {indicator}")
                lines.append("")
        
        # Simple Explanations
        if 'simple_explanations' in enhanced_analysis:
            explanations = enhanced_analysis['simple_explanations']
            lines.append("💡 WHAT HAPPENED (SIMPLE EXPLANATIONS)")
            lines.append("-" * 100)
            
            if explanations.get('what_worked'):
                lines.append("✅ SUCCESSFUL OPERATIONS:")
                for explanation in explanations['what_worked'][:5]:  # Show top 5
                    lines.append(f"  • {explanation}")
                lines.append("")
            
            if explanations.get('what_failed'):
                lines.append("❌ FAILED OPERATIONS:")
                for explanation in explanations['what_failed'][:5]:  # Show top 5
                    lines.append(f"  • {explanation}")
                lines.append("")
            
            if explanations.get('why_failed'):
                lines.append("🤔 WHY OPERATIONS FAILED:")
                for reason in set(explanations['why_failed'][:5]):  # Unique reasons
                    lines.append(f"  • {reason}")
                lines.append("")
        
        # Enhanced Recommendations
        if 'detailed_recommendations' in enhanced_analysis:
            lines.append("🛡️  DETAILED SECURITY RECOMMENDATIONS")
            lines.append("-" * 100)
            for recommendation in enhanced_analysis['detailed_recommendations']:
                lines.append(f"  {recommendation}")
            lines.append("")
        
        # UDS Message Summary
        if 'uds_message_analysis' in enhanced_analysis:
            uds_data = enhanced_analysis['uds_message_analysis']
            lines.append("📡 UDS MESSAGE ANALYSIS SUMMARY")
            lines.append("-" * 100)
            lines.append(f"Total Messages Analyzed: {len(uds_data.get('messages', []))}")
            
            ecu_sessions = uds_data.get('ecu_sessions', {})
            if ecu_sessions:
                lines.append(f"ECUs Involved: {len(ecu_sessions)}")
                for ecu_addr, session_info in list(ecu_sessions.items())[:5]:  # Show top 5
                    lines.append(f"  • ECU {ecu_addr}: {session_info.get('name', 'Unknown')}")
            lines.append("")
        
        # Failure/Success Analysis Summary
        if 'failure_success_analysis' in enhanced_analysis:
            fs_analysis = enhanced_analysis['failure_success_analysis']
            summary = fs_analysis.get('summary', {})
            
            lines.append("📊 OPERATION RESULTS SUMMARY")
            lines.append("-" * 100)
            
            failure_summary = summary.get('failure_summary', {})
            success_summary = summary.get('success_summary', {})
            
            lines.append(f"Total Failures: {failure_summary.get('total_failures', 0)}")
            lines.append(f"  - Critical: {failure_summary.get('critical_failures', 0)}")
            lines.append(f"  - High Impact: {failure_summary.get('high_impact_failures', 0)}")
            lines.append(f"  - Timeouts: {failure_summary.get('timeout_failures', 0)}")
            lines.append("")
            
            lines.append(f"Total Successes: {success_summary.get('total_successes', 0)}")
            lines.append(f"  - Read Operations: {success_summary.get('read_operations', 0)}")
            lines.append(f"  - Write Operations: {success_summary.get('write_operations', 0)}")
            lines.append(f"  - Security Operations: {success_summary.get('security_operations', 0)}")
            lines.append("")
            
            overall_success_rate = summary.get('overall_success_rate', 0) * 100
            lines.append(f"Overall Success Rate: {overall_success_rate:.1f}%")
            lines.append("")
        
        return "\n".join(lines)


if __name__ == '__main__':
    # Test with sample data
    analyzer = CybersecurityAnalyzer()
    
    test_data = [
        {'line': 'Security access denied - NRC 0x33', 'timestamp': '2025-01-01 10:00:00'},
        {'line': 'Seed-key authentication failed', 'timestamp': '2025-01-01 10:00:05'},
        {'line': 'Unauthorized flash programming attempt on ECU 7E0', 'timestamp': '2025-01-01 10:00:10'},
        {'line': 'Read DID 0x8071 Software Version', 'timestamp': '2025-01-01 10:00:15'},
    ]
    
    results = analyzer.analyze(test_data)
    print(analyzer.format_report_text())
