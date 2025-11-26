"""
Log Comparison Engine
Compares two log files and identifies differences
"""

import json
from typing import List, Dict, Any


class LogComparator:
    """Compares two parsed log files and identifies differences"""
    
    def __init__(self):
        pass
    
    def compare_logs(self, log1_results: List[Dict], log2_results: List[Dict]) -> Dict[str, Any]:
        """
        Compare two parsed log result sets
        
        Args:
            log1_results: Results from first log file
            log2_results: Results from second log file
        
        Returns:
            Dictionary with comparison results
        """
        # Normalize entries for comparison
        log1_normalized = [self._normalize_entry(entry) for entry in log1_results]
        log2_normalized = [self._normalize_entry(entry) for entry in log2_results]
        
        # Convert to sets for comparison
        log1_set = set(log1_normalized)
        log2_set = set(log2_normalized)
        
        # Find unique and common entries
        unique_to_log1 = log1_set - log2_set
        unique_to_log2 = log2_set - log1_set
        common = log1_set & log2_set
        
        # Convert back to readable format
        unique_to_log1_list = [self._denormalize_entry(entry) for entry in unique_to_log1]
        unique_to_log2_list = [self._denormalize_entry(entry) for entry in unique_to_log2]
        common_list = [self._denormalize_entry(entry) for entry in common]
        
        return {
            'unique_to_log1': unique_to_log1_list,
            'unique_to_log1_count': len(unique_to_log1_list),
            'unique_to_log2': unique_to_log2_list,
            'unique_to_log2_count': len(unique_to_log2_list),
            'common': common_list,
            'common_count': len(common_list),
            'log1_total': len(log1_results),
            'log2_total': len(log2_results),
            'similarity_score': self._calculate_similarity(log1_set, log2_set)
        }
    
    def _normalize_entry(self, entry: Dict) -> str:
        """
        Normalize a log entry for comparison
        Converts dict to a comparable string representation
        """
        try:
            # Extract key fields for comparison
            key_fields = []
            
            # Try to get line content
            if 'line' in entry:
                key_fields.append(str(entry['line']))
            elif 'text' in entry:
                key_fields.append(str(entry['text']))
            
            # Add severity if present
            if 'severity' in entry:
                key_fields.append(str(entry['severity']))
            
            # Add NRC codes if present
            if 'nrc_explanations' in entry:
                nrc_codes = [nrc.get('code', '') for nrc in entry['nrc_explanations']]
                key_fields.extend(nrc_codes)
            
            # Create normalized string
            normalized = '|'.join(key_fields)
            return normalized
            
        except Exception as e:
            # Fallback to JSON representation
            return json.dumps(entry, sort_keys=True)
    
    def _denormalize_entry(self, normalized: str) -> str:
        """Convert normalized entry back to readable format"""
        parts = normalized.split('|')
        if len(parts) > 0:
            return parts[0]  # Return main content
        return normalized
    
    def _calculate_similarity(self, set1: set, set2: set) -> float:
        """
        Calculate similarity score between two sets (Jaccard similarity)
        Returns value between 0.0 (completely different) and 1.0 (identical)
        """
        if not set1 and not set2:
            return 1.0
        
        if not set1 or not set2:
            return 0.0
        
        intersection = len(set1 & set2)
        union = len(set1 | set2)
        
        return intersection / union if union > 0 else 0.0
    
    def generate_diff_report(self, comparison: Dict) -> str:
        """Generate a human-readable diff report"""
        report = []
        
        report.append("=" * 80)
        report.append("LOG COMPARISON REPORT")
        report.append("=" * 80)
        report.append("")
        
        # Summary
        report.append("SUMMARY:")
        report.append(f"  Log 1 Total Items: {comparison['log1_total']}")
        report.append(f"  Log 2 Total Items: {comparison['log2_total']}")
        report.append(f"  Common Items: {comparison['common_count']}")
        report.append(f"  Unique to Log 1: {comparison['unique_to_log1_count']}")
        report.append(f"  Unique to Log 2: {comparison['unique_to_log2_count']}")
        report.append(f"  Similarity Score: {comparison['similarity_score']:.2%}")
        report.append("")
        
        # Unique to Log 1
        if comparison['unique_to_log1']:
            report.append("-" * 80)
            report.append("UNIQUE TO LOG 1:")
            report.append("-" * 80)
            for item in comparison['unique_to_log1'][:20]:  # Limit to first 20
                report.append(f"  - {item}")
            if comparison['unique_to_log1_count'] > 20:
                report.append(f"  ... and {comparison['unique_to_log1_count'] - 20} more")
            report.append("")
        
        # Unique to Log 2
        if comparison['unique_to_log2']:
            report.append("-" * 80)
            report.append("UNIQUE TO LOG 2:")
            report.append("-" * 80)
            for item in comparison['unique_to_log2'][:20]:  # Limit to first 20
                report.append(f"  + {item}")
            if comparison['unique_to_log2_count'] > 20:
                report.append(f"  ... and {comparison['unique_to_log2_count'] - 20} more")
            report.append("")
        
        # Common items (summary only)
        if comparison['common']:
            report.append("-" * 80)
            report.append(f"COMMON ITEMS: {comparison['common_count']}")
            report.append("-" * 80)
            report.append("  (Items present in both logs)")
            report.append("")
        
        report.append("=" * 80)
        
        return "\n".join(report)
