"""
Pattern Learning Module for Diagnostic Log Analysis
Uses ML to identify normal vs abnormal patterns in automotive logs
"""
import json
import os
from collections import Counter, defaultdict
from typing import Dict, List, Tuple, Any
from datetime import datetime
import pickle


class DiagnosticPatternLearner:
    """
    Learns patterns from successful/failed diagnostic sessions to identify anomalies.
    
    Features:
    - Learns normal DID/NRC patterns for each ECU/module
    - Identifies unusual error sequences
    - Tracks common part number/calibration combinations
    - Detects anomalous timing patterns
    """
    
    def __init__(self, knowledge_base_path: str = "diagnostic_patterns.pkl"):
        self.knowledge_base_path = knowledge_base_path
        self.patterns = {
            'normal_dids_by_ecu': defaultdict(Counter),  # ECU -> {DID: count}
            'normal_nrcs_by_did': defaultdict(Counter),  # DID -> {NRC: count}
            'successful_calibrations': defaultdict(list),  # ECU -> [calibration_ids]
            'error_sequences': Counter(),  # Sequences of errors
            'session_outcomes': {'success': 0, 'failure': 0},
            'failure_patterns': defaultdict(Counter),  # What caused failures
            'timing_stats': defaultdict(list),  # Operation -> [durations]
        }
        self.load_patterns()
    
    def load_patterns(self):
        """Load existing pattern knowledge base"""
        if os.path.exists(self.knowledge_base_path):
            try:
                with open(self.knowledge_base_path, 'rb') as f:
                    loaded = pickle.load(f)
                    # Update patterns with loaded data
                    for key in self.patterns:
                        if key in loaded:
                            self.patterns[key] = loaded[key]
                print(f"✓ Loaded pattern knowledge from {self.knowledge_base_path}")
            except Exception as e:
                print(f"⚠ Could not load patterns: {e}")
    
    def save_patterns(self):
        """Save learned patterns to disk"""
        try:
            with open(self.knowledge_base_path, 'wb') as f:
                pickle.dump(self.patterns, f)
            print(f"✓ Saved pattern knowledge to {self.knowledge_base_path}")
        except Exception as e:
            print(f"⚠ Could not save patterns: {e}")
    
    def learn_from_session(self, scan_results: Dict[str, Any], outcome: str = 'unknown'):
        """
        Learn from a diagnostic session.
        
        Args:
            scan_results: Results from _scan_ecu_and_dids()
            outcome: 'success' or 'failure' or 'unknown'
        """
        primary_ecu = scan_results.get('primary_ecu', 'Unknown')
        
        # Learn normal DID patterns for this ECU
        for did, count in scan_results.get('did_counts', {}).items():
            self.patterns['normal_dids_by_ecu'][primary_ecu][did] += count
        
        # Learn NRC patterns per DID
        for did, errors in scan_results.get('did_to_errors', {}).items():
            if did != '(UNKNOWN)':
                for nrc_code, count in scan_results.get('nrc_counts', {}).items():
                    self.patterns['normal_nrcs_by_did'][did][nrc_code] += count
        
        # Learn calibration patterns
        if outcome == 'success' and scan_results.get('calibrations'):
            for cal in scan_results['calibrations'][:10]:  # Top 10
                if cal not in self.patterns['successful_calibrations'][primary_ecu]:
                    self.patterns['successful_calibrations'][primary_ecu].append(cal)
        
        # Track outcomes
        if outcome in ['success', 'failure']:
            self.patterns['session_outcomes'][outcome] += 1
        
        # Learn failure patterns
        if outcome == 'failure':
            # What DIDs had the most errors?
            did_error_counts = {did: len(errs) for did, errs in scan_results.get('did_to_errors', {}).items() if did != '(UNKNOWN)'}
            if did_error_counts:
                top_error_did = max(did_error_counts.items(), key=lambda x: x[1])[0]
                self.patterns['failure_patterns'][primary_ecu][top_error_did] += 1
        
        self.save_patterns()
    
    def analyze_anomalies(self, scan_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze scan results for anomalies compared to learned patterns.
        
        Returns:
            Dict with anomaly scores and explanations
        """
        primary_ecu = scan_results.get('primary_ecu', 'Unknown')
        anomalies = {
            'anomaly_score': 0.0,  # 0-100, higher = more unusual
            'unusual_dids': [],
            'unusual_nrcs': [],
            'unexpected_errors': [],
            'recommendations': []
        }
        
        # Check if we have knowledge about this ECU
        if primary_ecu not in self.patterns['normal_dids_by_ecu']:
            anomalies['recommendations'].append(
                f"⚠️ First time seeing ECU {primary_ecu}. Building baseline pattern..."
            )
            return anomalies
        
        # Analyze DIDs
        known_dids = set(self.patterns['normal_dids_by_ecu'][primary_ecu].keys())
        observed_dids = set(scan_results.get('did_counts', {}).keys())
        unusual_dids = observed_dids - known_dids
        
        if unusual_dids:
            anomalies['unusual_dids'] = list(unusual_dids)
            anomalies['anomaly_score'] += len(unusual_dids) * 5
            anomalies['recommendations'].append(
                f"🔍 Detected {len(unusual_dids)} DIDs not seen before in {primary_ecu}: {', '.join(list(unusual_dids)[:5])}"
            )
        
        # Analyze error counts
        error_count = sum(len(errs) for errs in scan_results.get('did_to_errors', {}).values())
        total_sessions = self.patterns['session_outcomes']['success'] + self.patterns['session_outcomes']['failure']
        
        if total_sessions > 5:  # Need baseline
            avg_errors_per_session = sum(
                count for patterns in self.patterns['failure_patterns'].values() 
                for count in patterns.values()
            ) / max(1, self.patterns['session_outcomes']['failure'])
            
            if error_count > avg_errors_per_session * 2:
                anomalies['anomaly_score'] += 30
                anomalies['recommendations'].append(
                    f"❌ Error count ({error_count}) is significantly higher than typical ({avg_errors_per_session:.0f})"
                )
        
        # Check calibrations
        current_cals = set(scan_results.get('calibrations', []))
        known_cals = set(self.patterns['successful_calibrations'].get(primary_ecu, []))
        
        if known_cals:
            matching_cals = current_cals & known_cals
            if len(matching_cals) == 0:
                anomalies['anomaly_score'] += 20
                anomalies['recommendations'].append(
                    f"⚠️ None of the current calibrations match previously successful ones for {primary_ecu}"
                )
            elif len(matching_cals) > 0:
                anomalies['recommendations'].append(
                    f"✓ Found {len(matching_cals)} calibrations matching successful sessions"
                )
        
        # Check common failure DIDs
        if primary_ecu in self.patterns['failure_patterns']:
            common_failure_dids = self.patterns['failure_patterns'][primary_ecu]
            error_dids = set(scan_results.get('did_to_errors', {}).keys()) - {'(UNKNOWN)'}
            
            for did in error_dids:
                if did in common_failure_dids:
                    anomalies['unexpected_errors'].append(did)
                    anomalies['recommendations'].append(
                        f"⚠️ DID {did} has caused {common_failure_dids[did]} previous failures in {primary_ecu}"
                    )
        
        # Cap anomaly score
        anomalies['anomaly_score'] = min(100, anomalies['anomaly_score'])
        
        # Overall assessment
        if anomalies['anomaly_score'] < 20:
            anomalies['assessment'] = "NORMAL - Session appears typical based on learned patterns"
        elif anomalies['anomaly_score'] < 50:
            anomalies['assessment'] = "UNUSUAL - Some atypical patterns detected"
        else:
            anomalies['assessment'] = "HIGHLY ABNORMAL - Significant deviations from normal patterns"
        
        return anomalies
    
    def get_statistics(self) -> str:
        """Get a summary of learned patterns"""
        total_ecus = len(self.patterns['normal_dids_by_ecu'])
        total_sessions = self.patterns['session_outcomes']['success'] + self.patterns['session_outcomes']['failure']
        success_rate = (self.patterns['session_outcomes']['success'] / max(1, total_sessions)) * 100
        
        stats = f"""
📊 Pattern Learning Statistics
═══════════════════════════════════════
• ECUs in knowledge base: {total_ecus}
• Total analyzed sessions: {total_sessions}
• Success rate: {success_rate:.1f}%
• Successful sessions: {self.patterns['session_outcomes']['success']}
• Failed sessions: {self.patterns['session_outcomes']['failure']}

Most common failure DIDs by ECU:
"""
        for ecu, did_counts in list(self.patterns['failure_patterns'].items())[:5]:
            top_did = did_counts.most_common(1)[0] if did_counts else ('N/A', 0)
            stats += f"  • {ecu}: DID {top_did[0]} ({top_did[1]} failures)\n"
        
        return stats
