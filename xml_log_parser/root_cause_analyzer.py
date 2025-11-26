"""
Advanced Root Cause Analysis Engine
Provides multi-layer correlation, causal chain detection, and proximate cause identification
"""

from typing import Dict, List, Any, Tuple, Optional
import re
from collections import defaultdict, Counter
from datetime import datetime, timedelta


class RootCauseAnalyzer:
    """
    Advanced root cause analysis with multi-layer correlation
    Identifies true proximate causes vs symptoms
    """
    
    # Known causal patterns (cause -> common effects)
    CAUSAL_CHAINS = {
        'security_access_denied': {
            'symptoms': [
                'programming failed', 'flash failed', 'update failed',
                'write failed', 'download failed', 'transfer failed'
            ],
            'severity': 'critical',
            'category': 'Authentication Failure',
            'explanation': 'Security access must be granted before programming operations can proceed.',
            'nrc_codes': ['33', '35', '36', '37'],
        },
        'communication_lost': {
            'symptoms': [
                'timeout', 'no response', 'request failed', 'service timeout',
                'frame lost', 'bus error'
            ],
            'severity': 'critical',
            'category': 'Communication Failure',
            'explanation': 'Loss of communication prevents all subsequent operations.',
            'patterns': [r'communication\s+lost', r'bus\s+off', r'no\s+response'],
        },
        'precondition_not_met': {
            'symptoms': [
                'service not supported', 'request out of range', 'conditions not correct',
                'mode transition failed'
            ],
            'severity': 'high',
            'category': 'Precondition Failure',
            'explanation': 'Required conditions must be met before the operation can execute.',
            'nrc_codes': ['22', '7F', '31'],
        },
        'module_offline': {
            'symptoms': [
                'no response', 'module not responding', 'ecu not found',
                'address not responding'
            ],
            'severity': 'critical',
            'category': 'Module Unavailable',
            'explanation': 'Target module is not accessible or not powered.',
            'patterns': [r'module.*(?:offline|not\s+found|unavailable)'],
        },
        'voltage_issue': {
            'symptoms': [
                'voltage too low', 'voltage too high', 'power supply',
                'battery voltage', 'programming failed'
            ],
            'severity': 'high',
            'category': 'Power Supply Issue',
            'explanation': 'Stable voltage is required for programming and diagnostic operations.',
            'patterns': [r'voltage.*(?:low|high|out\s+of\s+range)', r'battery.*(?:low|critical)'],
        },
        'integrity_failure': {
            'symptoms': [
                'checksum failed', 'crc error', 'verification failed',
                'signature invalid', 'hash mismatch'
            ],
            'severity': 'critical',
            'category': 'Data Integrity Failure',
            'explanation': 'Data corruption or tampering detected, preventing safe operation.',
            'patterns': [r'checksum.*(?:fail|error|mismatch)', r'integrity.*(?:fail|violation)'],
        },
        'insufficient_memory': {
            'symptoms': [
                'memory full', 'out of memory', 'buffer overflow',
                'allocation failed', 'space not available'
            ],
            'severity': 'high',
            'category': 'Resource Exhaustion',
            'explanation': 'Insufficient memory or storage space for the operation.',
            'patterns': [r'(?:memory|buffer|space).*(?:full|insufficient|overflow)'],
        },
    }
    
    # Error propagation patterns (how errors cascade)
    ERROR_PROPAGATION = {
        'programming_failed': ['write_failed', 'verification_failed', 'erase_failed'],
        'write_failed': ['transfer_failed', 'timeout'],
        'erase_failed': ['memory_full', 'protected_memory'],
        'service_failed': ['timeout', 'nrc_error', 'invalid_response'],
    }
    
    # Critical NRC codes that often indicate root causes
    ROOT_CAUSE_NRCS = {
        '13': ('Incorrect Message Length', 'Message format error - likely tool/ECU incompatibility'),
        '22': ('Conditions Not Correct', 'Prerequisites not met - check vehicle state, mode, or security'),
        '31': ('Request Out of Range', 'Invalid parameter value - check requested data or service'),
        '33': ('Security Access Denied', 'Authentication failed - security access required first'),
        '35': ('Invalid Key', 'Wrong security key - potential unauthorized access attempt'),
        '36': ('Exceeded Number of Attempts', 'Too many failed attempts - security lockout triggered'),
        '37': ('Required Time Delay Not Expired', 'Must wait before retrying - anti-brute-force protection'),
        '72': ('General Programming Failure', 'Programming operation failed - check voltage and conditions'),
        '78': ('Request Correctly Received - Response Pending', 'Long operation in progress - not an error'),
    }
    
    def __init__(self):
        self.errors = []
        self.timeline = []
        self.causal_chains = []
        self.root_causes = []
        self.symptoms = []
        
    def analyze(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Perform comprehensive root cause analysis
        
        Returns:
            Dictionary with root causes, causal chains, and recommendations
        """
        self.errors = []
        self.timeline = []
        self.causal_chains = []
        self.root_causes = []
        self.symptoms = []
        
        # Step 1: Extract and categorize all errors
        self._extract_errors(results)
        
        # Step 2: Build timeline and sequence events
        self._build_timeline()
        
        # Step 3: Identify causal relationships
        self._identify_causal_chains()
        
        # Step 4: Distinguish root causes from symptoms
        self._separate_causes_and_symptoms()
        
        # Step 5: Calculate confidence scores
        self._calculate_confidence()
        
        # Step 6: Generate proximate cause statement
        proximate_cause = self._generate_proximate_cause()
        
        # Step 7: Build recommendations
        recommendations = self._generate_recommendations()
        
        return {
            'proximate_cause': proximate_cause,
            'root_causes': self.root_causes,
            'symptoms': self.symptoms,
            'causal_chains': self.causal_chains,
            'timeline': self.timeline,
            'recommendations': recommendations,
            'confidence': self._get_overall_confidence(),
        }
    
    def _extract_errors(self, results: List[Dict[str, Any]]):
        """Extract and categorize all errors from results"""
        for idx, result in enumerate(results):
            text = str(result).lower()
            original_text = str(result)
            
            # Check if this is an error
            is_error = any(kw in text for kw in ['error', 'fail', 'denied', 'invalid', 'nrc'])
            
            if is_error:
                error = {
                    'index': idx,
                    'text': original_text,
                    'text_lower': text,
                    'timestamp': self._extract_timestamp(result, idx),
                    'type': self._classify_error_type(text),
                    'severity': self._determine_error_severity(text),
                    'modules': self._extract_modules(original_text),
                    'nrc_codes': self._extract_nrc_codes(original_text),
                    'services': self._extract_services(original_text),
                    'is_root_cause': False,  # Will be determined later
                    'is_symptom': False,
                    'confidence': 0.0,
                }
                self.errors.append(error)
    
    def _classify_error_type(self, text: str) -> str:
        """Classify error into high-level category"""
        if any(kw in text for kw in ['security', 'access denied', 'invalid key', 'authentication']):
            return 'security'
        elif any(kw in text for kw in ['communication', 'timeout', 'no response', 'bus']):
            return 'communication'
        elif any(kw in text for kw in ['program', 'flash', 'write', 'erase', 'download']):
            return 'programming'
        elif any(kw in text for kw in ['voltage', 'power', 'battery']):
            return 'power'
        elif any(kw in text for kw in ['checksum', 'crc', 'integrity', 'verification']):
            return 'integrity'
        elif any(kw in text for kw in ['memory', 'buffer', 'space']):
            return 'memory'
        else:
            return 'general'
    
    def _determine_error_severity(self, text: str) -> str:
        """Determine error severity"""
        if any(kw in text for kw in ['critical', 'fatal', 'abort', 'severe']):
            return 'critical'
        elif any(kw in text for kw in ['fail', 'denied', 'invalid', 'error']):
            return 'high'
        elif any(kw in text for kw in ['warning', 'warn']):
            return 'medium'
        else:
            return 'low'
    
    def _extract_timestamp(self, result: Any, index: int) -> float:
        """Extract or estimate timestamp"""
        if isinstance(result, dict):
            ts = result.get('timestamp', result.get('time'))
            if ts:
                try:
                    if isinstance(ts, str):
                        # Try parsing timestamp
                        dt = datetime.fromisoformat(ts.replace('T', ' ').replace('Z', ''))
                        return dt.timestamp()
                except:
                    pass
        # Use index as relative time
        return float(index)
    
    def _extract_modules(self, text: str) -> List[str]:
        """Extract ECU module addresses"""
        pattern = r'\b([67][0-9A-Fa-f]{2})\b'
        return list(set(re.findall(pattern, text)))
    
    def _extract_nrc_codes(self, text: str) -> List[str]:
        """Extract NRC codes"""
        pattern = r'(?:NRC|nrc)\s*(?:0x)?([0-9A-Fa-f]{2})\b'
        codes = re.findall(pattern, text, re.IGNORECASE)
        # Also check for standalone hex codes after "negative response"
        if 'negative' in text.lower() or 'response' in text.lower():
            pattern2 = r'\b(?:0x)?([0-9A-Fa-f]{2})\b'
            codes.extend(re.findall(pattern2, text))
        return list(set(codes))
    
    def _extract_services(self, text: str) -> List[str]:
        """Extract UDS service IDs"""
        pattern = r'(?:service|sid)\s*(?:0x)?([0-9A-Fa-f]{2})\b'
        return list(set(re.findall(pattern, text, re.IGNORECASE)))
    
    def _build_timeline(self):
        """Build chronological timeline of events"""
        # Sort errors by timestamp
        sorted_errors = sorted(self.errors, key=lambda e: e['timestamp'])
        
        for i, error in enumerate(sorted_errors):
            self.timeline.append({
                'sequence': i,
                'timestamp': error['timestamp'],
                'type': error['type'],
                'text': error['text'][:100],
                'error_ref': error,
            })
    
    def _identify_causal_chains(self):
        """Identify cause-effect relationships"""
        for cause_type, cause_data in self.CAUSAL_CHAINS.items():
            # Find potential root causes
            for error in self.errors:
                matches_cause = False
                
                # Check patterns
                if 'patterns' in cause_data:
                    for pattern in cause_data['patterns']:
                        if re.search(pattern, error['text_lower']):
                            matches_cause = True
                            break
                
                # Check NRC codes
                if not matches_cause and 'nrc_codes' in cause_data:
                    for nrc in error['nrc_codes']:
                        if nrc.upper() in cause_data['nrc_codes']:
                            matches_cause = True
                            break
                
                # Check keywords
                if not matches_cause:
                    if cause_type.replace('_', ' ') in error['text_lower']:
                        matches_cause = True
                
                if matches_cause:
                    # Find subsequent symptoms
                    symptoms_found = []
                    for symptom_error in self.errors:
                        if symptom_error['timestamp'] > error['timestamp']:
                            for symptom_keyword in cause_data['symptoms']:
                                if symptom_keyword in symptom_error['text_lower']:
                                    symptoms_found.append(symptom_error)
                                    break
                    
                    if symptoms_found:
                        chain = {
                            'root_cause': error,
                            'symptoms': symptoms_found,
                            'category': cause_data['category'],
                            'explanation': cause_data['explanation'],
                            'severity': cause_data['severity'],
                            'confidence': len(symptoms_found) * 0.2 + 0.3,  # Higher with more symptoms
                        }
                        self.causal_chains.append(chain)
    
    def _separate_causes_and_symptoms(self):
        """Distinguish root causes from symptoms"""
        symptom_indices = set()
        
        # Mark all errors in causal chains
        for chain in self.causal_chains:
            # Root cause
            chain['root_cause']['is_root_cause'] = True
            if chain['root_cause'] not in self.root_causes:
                self.root_causes.append(chain['root_cause'])
            
            # Symptoms
            for symptom in chain['symptoms']:
                symptom['is_symptom'] = True
                symptom_indices.add(symptom['index'])
                if symptom not in self.symptoms:
                    self.symptoms.append(symptom)
        
        # Errors not in any chain - analyze independently
        for error in self.errors:
            if not error['is_root_cause'] and not error['is_symptom']:
                # Check if it's likely a root cause
                if self._is_likely_root_cause(error):
                    error['is_root_cause'] = True
                    self.root_causes.append(error)
                else:
                    error['is_symptom'] = True
                    self.symptoms.append(error)
    
    def _is_likely_root_cause(self, error: Dict) -> bool:
        """Determine if an error is likely a root cause"""
        # Check for root cause indicators
        indicators = [
            error['type'] in ['security', 'communication', 'power', 'integrity'],
            any(nrc in self.ROOT_CAUSE_NRCS for nrc in error['nrc_codes']),
            error['severity'] == 'critical',
            any(kw in error['text_lower'] for kw in ['denied', 'lost', 'offline', 'unavailable', 'invalid key']),
        ]
        return sum(indicators) >= 2
    
    def _calculate_confidence(self):
        """Calculate confidence scores for root cause identification"""
        for rc in self.root_causes:
            confidence = 0.5  # Base confidence
            
            # Increase confidence if in causal chain
            in_chain = any(chain['root_cause'] == rc for chain in self.causal_chains)
            if in_chain:
                confidence += 0.3
            
            # Increase confidence if has critical NRC
            if any(nrc in self.ROOT_CAUSE_NRCS for nrc in rc['nrc_codes']):
                confidence += 0.2
            
            # Increase confidence if early in timeline
            if rc['timestamp'] < len(self.errors) * 0.3:  # First 30% of events
                confidence += 0.1
            
            # Increase confidence based on severity
            if rc['severity'] == 'critical':
                confidence += 0.1
            
            rc['confidence'] = min(1.0, confidence)
    
    def _generate_proximate_cause(self) -> Dict[str, Any]:
        """Generate proximate cause statement"""
        if not self.root_causes:
            return {
                'statement': 'No clear root cause identified from log data.',
                'confidence': 0.0,
                'category': 'unknown',
                'details': 'Insufficient error information to determine proximate cause.',
            }
        
        # Get highest confidence root cause
        primary_cause = max(self.root_causes, key=lambda rc: rc['confidence'])
        
        # Build statement
        statement = self._build_cause_statement(primary_cause)
        
        # Find related chain
        related_chain = None
        for chain in self.causal_chains:
            if chain['root_cause'] == primary_cause:
                related_chain = chain
                break
        
        return {
            'statement': statement,
            'confidence': primary_cause['confidence'],
            'category': primary_cause['type'],
            'details': primary_cause['text'][:200],
            'modules_affected': primary_cause['modules'],
            'nrc_codes': primary_cause['nrc_codes'],
            'chain': related_chain,
            'timestamp': primary_cause['timestamp'],
        }
    
    def _build_cause_statement(self, cause: Dict) -> str:
        """Build human-readable proximate cause statement"""
        category = cause['type'].upper()
        
        if cause['type'] == 'security':
            return f"🔐 SECURITY ACCESS FAILURE: Authentication denied before programming could proceed. The system rejected the security credentials, preventing all subsequent operations."
        
        elif cause['type'] == 'communication':
            return f"📡 COMMUNICATION FAILURE: Loss of communication with target module. All subsequent operations failed due to inability to reach the ECU."
        
        elif cause['type'] == 'power':
            return f"⚡ POWER SUPPLY ISSUE: Voltage out of acceptable range. Programming operations require stable power and were aborted for safety."
        
        elif cause['type'] == 'integrity':
            return f"🛡️ DATA INTEGRITY FAILURE: Checksum or verification failed. Data corruption detected, preventing safe operation completion."
        
        elif cause['type'] == 'programming':
            if any(nrc in cause['nrc_codes'] for nrc in ['22', '31']):
                return f"⚙️ PRECONDITION NOT MET: Required conditions for programming were not satisfied. Vehicle state or mode incorrect."
            return f"⚙️ PROGRAMMING OPERATION FAILED: Core programming process encountered an error. Check prerequisites and retry."
        
        elif cause['type'] == 'memory':
            return f"💾 INSUFFICIENT MEMORY: Target module has insufficient space or memory for the operation."
        
        else:
            return f"⚠️ OPERATION FAILED: {cause['text'][:100]}"
    
    def _generate_recommendations(self) -> List[Dict[str, Any]]:
        """Generate actionable recommendations"""
        recommendations = []
        
        for rc in self.root_causes:
            rec = self._get_recommendation_for_cause(rc)
            if rec:
                recommendations.append(rec)
        
        return recommendations
    
    def _get_recommendation_for_cause(self, cause: Dict) -> Optional[Dict]:
        """Get specific recommendation for a root cause"""
        if cause['type'] == 'security':
            return {
                'priority': 'critical',
                'action': 'Obtain Correct Security Credentials',
                'steps': [
                    '1. Verify you have the correct seed-key algorithm',
                    '2. Ensure tool is authorized for this ECU',
                    '3. Check for security lockout (wait 10+ minutes if locked)',
                    '4. Use manufacturer-approved diagnostic tool',
                ],
                'success_rate': 0.85,
            }
        
        elif cause['type'] == 'communication':
            return {
                'priority': 'critical',
                'action': 'Restore Communication Link',
                'steps': [
                    '1. Check physical connections (OBD-II port, cables)',
                    '2. Verify CAN bus termination and wiring',
                    '3. Ensure target module is powered and responding',
                    '4. Check for bus conflicts or other active tools',
                ],
                'success_rate': 0.75,
            }
        
        elif cause['type'] == 'power':
            return {
                'priority': 'critical',
                'action': 'Stabilize Power Supply',
                'steps': [
                    '1. Connect external power supply or battery charger',
                    '2. Ensure voltage is between 12.0-14.5V',
                    '3. Turn off all accessories and loads',
                    '4. Monitor voltage throughout programming',
                ],
                'success_rate': 0.90,
            }
        
        elif cause['type'] == 'integrity':
            return {
                'priority': 'high',
                'action': 'Verify Data Integrity',
                'steps': [
                    '1. Re-download calibration file from source',
                    '2. Verify file checksum matches expected value',
                    '3. Check for file corruption during transfer',
                    '4. Ensure correct file version for target ECU',
                ],
                'success_rate': 0.80,
            }
        
        elif cause['type'] == 'programming':
            return {
                'priority': 'high',
                'action': 'Verify Programming Preconditions',
                'steps': [
                    '1. Ensure vehicle is in Park with engine off',
                    '2. Set ignition to ON position (not ACC)',
                    '3. Verify no DTCs preventing programming',
                    '4. Check that no other modules are being accessed',
                ],
                'success_rate': 0.70,
            }
        
        return None
    
    def _get_overall_confidence(self) -> float:
        """Calculate overall confidence in the analysis"""
        if not self.root_causes:
            return 0.0
        
        # Average confidence of all root causes
        avg_confidence = sum(rc['confidence'] for rc in self.root_causes) / len(self.root_causes)
        
        # Boost if we have causal chains
        if self.causal_chains:
            avg_confidence = min(1.0, avg_confidence + 0.1)
        
        return avg_confidence
    
    def format_analysis_report(self, analysis: Dict) -> str:
        """Format analysis into readable report"""
        lines = []
        lines.append("=" * 80)
        lines.append("🎯 ROOT CAUSE ANALYSIS REPORT")
        lines.append("=" * 80)
        lines.append("")
        
        # Proximate cause
        pc = analysis['proximate_cause']
        lines.append("📍 PROXIMATE CAUSE")
        lines.append("-" * 80)
        lines.append(f"Confidence: {pc['confidence']*100:.0f}%")
        lines.append("")
        lines.append(pc['statement'])
        lines.append("")
        if pc['modules_affected']:
            lines.append(f"Affected Modules: {', '.join(pc['modules_affected'])}")
        if pc['nrc_codes']:
            lines.append(f"NRC Codes: {', '.join(pc['nrc_codes'])}")
        lines.append("")
        
        # Causal chains
        if analysis['causal_chains']:
            lines.append("🔗 CAUSAL CHAINS (Cause → Effect)")
            lines.append("-" * 80)
            for i, chain in enumerate(analysis['causal_chains'], 1):
                lines.append(f"\nChain {i}: {chain['category']} (Confidence: {chain['confidence']*100:.0f}%)")
                lines.append(f"  Root: {chain['root_cause']['text'][:80]}")
                lines.append(f"  Effects: {len(chain['symptoms'])} downstream failures")
                lines.append(f"  Explanation: {chain['explanation']}")
            lines.append("")
        
        # Recommendations
        if analysis['recommendations']:
            lines.append("💡 RECOMMENDED ACTIONS")
            lines.append("-" * 80)
            for i, rec in enumerate(analysis['recommendations'], 1):
                lines.append(f"\n{i}. {rec['action']} ({rec['priority'].upper()} Priority)")
                lines.append(f"   Success Rate: {rec['success_rate']*100:.0f}%")
                for step in rec['steps']:
                    lines.append(f"   {step}")
            lines.append("")
        
        # Analysis metadata
        lines.append("=" * 80)
        lines.append(f"Analysis Confidence: {analysis['confidence']*100:.0f}%")
        lines.append(f"Root Causes Identified: {len(analysis['root_causes'])}")
        lines.append(f"Symptoms Identified: {len(analysis['symptoms'])}")
        lines.append(f"Causal Chains Found: {len(analysis['causal_chains'])}")
        lines.append("=" * 80)
        
        return "\n".join(lines)


if __name__ == '__main__':
    # Test
    analyzer = RootCauseAnalyzer()
    
    test_data = [
        {'line': 'Security access denied - NRC 0x33', 'timestamp': 1.0},
        {'line': 'Programming failed - unable to authenticate', 'timestamp': 2.0},
        {'line': 'Flash write failed', 'timestamp': 3.0},
        {'line': 'Update process aborted', 'timestamp': 4.0},
    ]
    
    analysis = analyzer.analyze(test_data)
    print(analyzer.format_analysis_report(analysis))
