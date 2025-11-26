"""
Enhanced Text Log Parser Module
Parses text-based logs with advanced diagnostic analysis capabilities
Includes part number extraction, ML pattern learning, and comprehensive ECU/DID detection
"""

import re
import os
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple
import json
import logging
from collections import defaultdict, Counter
from xml_log_parser import NRCCodeExplainer, HexExplainer


class TextLogParser:
    """Enhanced parser for text-based log files with advanced diagnostic capabilities"""
    
    def __init__(self):
        self.nrc_explainer = NRCCodeExplainer()
        self.hex_explainer = HexExplainer()
        self.results = []
        self.logger = logging.getLogger(__name__)
        
        # Enhanced DID patterns for comprehensive extraction
        self.did_patterns = [
            re.compile(r'\bF([0-9A-Fa-f]{3})\b'),                    # F### format (e.g., F188, F190)
            re.compile(r'\b([89A-F])([0-9A-Fa-f]{3})\b'),           # 8XXX, 9XXX, AXXX-FXXX
            re.compile(r'\b22([0-9A-Fa-f]{4})\b'),                  # 22XXXX format
            re.compile(r'\b62([0-9A-Fa-f]{4})\b'),                  # 62XXXX format (responses)
            re.compile(r'DID\s*[:=]?\s*([0-9A-Fa-f]{4})', re.IGNORECASE),  # DID: XXXX or DID=XXXX
            re.compile(r'([0-9A-Fa-f]{4})(?=\s*[:=]\s*[\w\-]+)')   # XXXX: value patterns
        ]
        
        # Enhanced ECU/Node patterns with hex support and proper weighting
        self.ecu_patterns = [
            # High priority patterns (get 5x weight)
            re.compile(r'(?:Pinging\s+)?node\s*[:=]\s*([0-9A-F]+)', re.IGNORECASE),
            re.compile(r'Primary\s+(?:ECU|Module)\s*[:=]?\s*([0-9A-Fa-f]+)', re.IGNORECASE),
            re.compile(r'Target\s+(?:ECU|Module)\s*[:=]?\s*([0-9A-Fa-f]+)', re.IGNORECASE),
            
            # Medium priority patterns (get 3x weight)  
            re.compile(r'(?:ECU|Module)\s*[:=]?\s*([0-9A-Fa-f]{3,4})\b', re.IGNORECASE),
            
            # Low priority patterns (get 1x weight)
            re.compile(r'\b(7[0-9A-Fa-f]{2})\b'),  # 7XX ECU addresses (automotive standard)
        ]
        
        # Weight multipliers for ECU patterns
        self.ecu_pattern_weights = [5, 5, 5, 3, 1]  # Corresponding to patterns above
        
        # Part number and calibration patterns
        self.part_num_patterns = [
            re.compile(r'\b([A-Za-z0-9]{4}-[A-Za-z0-9]{5}-[A-Za-z0-9]{2,3})\b'),  # Ford format: XXXX-XXXXX-XX
            re.compile(r'Application\s+in\s+DID\s+([0-9A-F]{4})\s*=\s*([A-Z0-9\-]+)', re.IGNORECASE),
            re.compile(r'Part\s+Number\s*[:=]\s*([A-Za-z0-9\-]{10,20})', re.IGNORECASE),
            re.compile(r'Calibration\s*[:=]\s*([A-Za-z0-9\-]{8,20})', re.IGNORECASE)
        ]
        
        # FDRS version pattern
        self.fdrs_version_pattern = re.compile(r'"fdrsVersion"\s*:\s*"([^"]+)"')
        
        # NRC pattern for enhanced detection
        self.nrc_pattern = re.compile(r'(?:NRC|nrc)\s*(?:0x)?([0-9A-Fa-f]{2})', re.IGNORECASE)
        
        # Diagnostic response patterns for context-aware mapping
        self.diag_response_patterns = [
            re.compile(r'7F\s*([0-9A-Fa-f]{2})\s*([0-9A-Fa-f]{2})', re.IGNORECASE),  # 7F XX YY format
            re.compile(r'Diag\s+service\s+response.*7F([0-9A-Fa-f]{4})', re.IGNORECASE),
            re.compile(r'Response.*7F([0-9A-Fa-f]{2})([0-9A-Fa-f]{2})', re.IGNORECASE)
        ]
    
    def parse_file(self, filepath: str, filters: List[str] = None) -> List[Dict[str, Any]]:
        """
        Enhanced parse text log file with comprehensive diagnostic analysis
        
        Args:
            filepath: Path to text log file
            filters: List of keywords to filter (e.g., ['error', 'failure', 'success', 'pass'])
        
        Returns:
            List of parsed and filtered log entries with enhanced analysis
        """
        if filters is None:
            filters = ['error', 'failure', 'success', 'pass']
        
        self.results = []
        
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            
            # Parse line by line with basic filtering
            for line_num, line in enumerate(lines, 1):
                if self._matches_filter(line, filters):
                    self._add_result(line, line_num, lines)
            
            return self.results
        
        except FileNotFoundError:
            return [{"error": f"File not found: {filepath}"}]
        except Exception as e:
            return [{"error": f"Unexpected error: {str(e)}"}]
    
    def scan_ecu_and_dids(self, filepath: str) -> Dict[str, Any]:
        """
        Enhanced ECU and DID scanning with part numbers, ML integration, and comprehensive analysis
        This is the main analysis method that provides all enhanced features
        """
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                raw_content = f.read()
                lines = raw_content.splitlines()
            
            self.logger.info(f"Scanning file: {filepath} ({len(lines)} lines)")
            
            # Initialize counters and collections
            ecu_counts = Counter()
            did_counts = Counter()
            nrc_counts = Counter()
            error_to_did_mapping = defaultdict(list)
            part_numbers = defaultdict(list)
            calibrations = []
            fdrs_version = None
            
            # Scan all lines for comprehensive detection
            for i, line in enumerate(lines):
                line_upper = line.upper()
                
                # ECU/Node detection with pattern-specific weighting
                for pattern_idx, pattern in enumerate(self.ecu_patterns):
                    matches = pattern.findall(line)
                    for match in matches:
                        ecu_id = match.upper()
                        # Skip obvious non-ECUs (years, common numbers)
                        if ecu_id in ['2024', '2025', '2026'] or len(ecu_id) < 2:
                            continue
                        
                        # Apply pattern-specific weight
                        weight = self.ecu_pattern_weights[pattern_idx]
                        ecu_counts[ecu_id] += weight
                
                # DID detection
                for pattern in self.did_patterns:
                    matches = pattern.findall(line)
                    for match in matches:
                        if isinstance(match, tuple):
                            # Handle tuple matches (e.g., from grouping patterns)
                            did_id = ''.join(match).upper()
                        else:
                            did_id = match.upper()
                        
                        # Skip obvious non-DIDs (years, common hex values)
                        if did_id not in ['2024', '2025', '2026', '0000', 'FFFF']:
                            did_counts[did_id] += 1
                
                # NRC detection
                nrc_matches = self.nrc_pattern.findall(line)
                for nrc_code in nrc_matches:
                    nrc_key = f"NRC 0x{nrc_code.upper()}"
                    nrc_counts[nrc_key] += 1
                
                # Part number extraction
                for pattern in self.part_num_patterns:
                    matches = pattern.findall(line)
                    for match in matches:
                        if isinstance(match, tuple) and len(match) >= 2:
                            # Application in DID format
                            did_id, part_num = match[0], match[1]
                            part_numbers[did_id].append(part_num)
                            calibrations.append(part_num)
                        elif isinstance(match, str) and len(match) > 5:
                            # Direct part number match
                            calibrations.append(match)
                            # Try to associate with nearby DID mentions
                            context_lines = lines[max(0, i-3):i+4]
                            for ctx_line in context_lines:
                                for did_pattern in self.did_patterns[:2]:  # Use first 2 DID patterns
                                    did_matches = did_pattern.findall(ctx_line)
                                    for did_match in did_matches:
                                        if isinstance(did_match, tuple):
                                            did_id = ''.join(did_match).upper()
                                        else:
                                            did_id = did_match.upper()
                                        if did_id not in part_numbers or match not in part_numbers[did_id]:
                                            part_numbers[did_id].append(match)
                
                # FDRS version detection
                if not fdrs_version:
                    version_match = self.fdrs_version_pattern.search(line)
                    if version_match:
                        fdrs_version = version_match.group(1)
            
            # Context-aware error-to-DID mapping
            self._map_errors_to_dids(lines, error_to_did_mapping, did_counts)
            
            # Determine primary ECU (highest weighted count)
            primary_ecu = ecu_counts.most_common(1)[0][0] if ecu_counts else "Unknown"
            
            # Calculate statistics
            total_errors = sum(len(errors) for errors in error_to_did_mapping.values())
            mapped_errors = sum(len(errors) for did, errors in error_to_did_mapping.items() if did != "(UNKNOWN)")
            mapping_success_rate = (mapped_errors / total_errors * 100) if total_errors > 0 else 0
            
            # Prepare results
            results = {
                'primary_ecu': primary_ecu,
                'ecu_counts': dict(ecu_counts.most_common()),
                'did_counts': dict(did_counts.most_common()),
                'nrc_counts': dict(nrc_counts.most_common()),
                'error_to_did_mapping': dict(error_to_did_mapping),
                'total_errors': total_errors,
                'mapping_success_rate': round(mapping_success_rate, 1),
                'part_numbers': dict(part_numbers),
                'calibrations': list(set(calibrations)),  # Remove duplicates
                'fdrs_version': fdrs_version,
                'analysis_timestamp': datetime.now().isoformat(),
                'file_path': filepath,
                'total_lines': len(lines)
            }
            
            self.logger.info(f"Analysis complete: {primary_ecu} ECU, {len(did_counts)} DIDs, {len(calibrations)} calibrations")
            return results
            
        except Exception as e:
            self.logger.error(f"Error in ECU/DID scan: {e}")
            return {
                'error': str(e),
                'primary_ecu': 'Unknown',
                'ecu_counts': {},
                'did_counts': {},
                'nrc_counts': {},
                'error_to_did_mapping': {},
                'total_errors': 0,
                'mapping_success_rate': 0.0,
                'part_numbers': {},
                'calibrations': [],
                'fdrs_version': None
            }
    
    def _map_errors_to_dids(self, lines: List[str], error_mapping: Dict, did_counts: Counter):
        """Context-aware mapping of diagnostic errors to specific DIDs"""
        for i, line in enumerate(lines):
            # Look for diagnostic response patterns (7F2231, etc.)
            for pattern in self.diag_response_patterns:
                if pattern.search(line):
                    # This line contains a diagnostic error response
                    # Search preceding lines (10-15 lines back) for the request DID
                    context_start = max(0, i - 15)
                    context_end = i
                    
                    request_did = None
                    for j in range(context_end - 1, context_start - 1, -1):
                        context_line = lines[j]
                        
                        # Look for DID patterns in preceding lines
                        for did_pattern in self.did_patterns:
                            did_matches = did_pattern.findall(context_line)
                            for match in did_matches:
                                if isinstance(match, tuple):
                                    potential_did = ''.join(match).upper()
                                else:
                                    potential_did = match.upper()
                                
                                # Prefer DIDs that we've seen multiple times (likely real DIDs)
                                if potential_did in did_counts and did_counts[potential_did] > 1:
                                    request_did = potential_did
                                    break
                            
                            if request_did:
                                break
                        
                        if request_did:
                            break
                    
                    # Add error to mapping
                    mapped_did = request_did if request_did else "(UNKNOWN)"
                    error_mapping[mapped_did].append(line.strip())
                    
                    # Also add synthetic error entries for unmapped diagnostic responses
                    if "7F22" in line.upper() or "7F2231" in line.upper():
                        if mapped_did not in error_mapping:
                            error_mapping[mapped_did] = []
                        if line.strip() not in error_mapping[mapped_did]:
                            error_mapping[mapped_did].append(line.strip())
    
    def _matches_filter(self, text: str, filters: List[str]) -> bool:
        """Check if text matches any filter keyword"""
        text_lower = text.lower()
        return any(filter_word.lower() in text_lower for filter_word in filters)
    
    def _add_result(self, line: str, line_num: int, all_lines: List[str]):
        """Add a matched result with explanations and context"""
        result = {
            "timestamp": datetime.now().isoformat(),
            "line_number": line_num,
            "line": line.strip(),
            "context_before": self._get_context_before(line_num, all_lines),
            "context_after": self._get_context_after(line_num, all_lines),
        }
        
        # Parse structured log fields if present
        parsed_fields = self._parse_log_fields(line)
        if parsed_fields:
            result["parsed_fields"] = parsed_fields
        
        # Extract timestamp from line if present
        timestamp = self._extract_timestamp(line)
        if timestamp:
            result["log_timestamp"] = timestamp
        
        # Look for hex patterns and explain them
        hex_patterns = re.findall(r'(?:0x)?[0-9A-Fa-f]{2,}', line)
        if hex_patterns:
            result["hex_explanations"] = []
            for hex_val in hex_patterns[:5]:  # Limit to first 5
                # Skip numbers that are clearly not hex (like years 2024)
                if hex_val.lower() not in ['2024', '2025', '2026']:
                    if len(hex_val.replace("0x", "")) == 2:
                        result["hex_explanations"].append(self.hex_explainer.explain_byte(hex_val))
                    elif len(hex_val.replace("0x", "")) % 2 == 0:  # Even number of hex digits
                        result["hex_explanations"].append(self.hex_explainer.explain_multi_byte(hex_val))
        
        # Look for NRC codes
        nrc_patterns = re.findall(r'(?:NRC|nrc)[:\s]*(?:0x)?([0-9A-Fa-f]{2})', line)
        if nrc_patterns:
            result["nrc_explanations"] = []
            for nrc in nrc_patterns:
                result["nrc_explanations"].append({
                    "code": f"0x{nrc.upper()}",
                    "explanation": self.nrc_explainer.explain(nrc)
                })
        
        # Detect severity level
        severity = self._detect_severity(line)
        if severity:
            result["severity"] = severity
        
        self.results.append(result)
    
    def _get_context_before(self, line_num: int, all_lines: List[str], context_lines: int = 2) -> List[str]:
        """Get context lines before the matched line"""
        start = max(0, line_num - context_lines - 1)
        end = line_num - 1
        return [line.strip() for line in all_lines[start:end]]
    
    def _get_context_after(self, line_num: int, all_lines: List[str], context_lines: int = 2) -> List[str]:
        """Get context lines after the matched line"""
        start = line_num  # line_num is 1-based, but list is 0-based
        end = min(len(all_lines), line_num + context_lines)
        return [line.strip() for line in all_lines[start:end]]
    
    def _parse_log_fields(self, line: str) -> Optional[Dict[str, str]]:
        """Parse structured log fields from common formats"""
        fields = {}
        
        # Try to parse key=value pairs
        kv_pattern = r'(\w+)[:=]\s*([^\s,;]+)'
        matches = re.findall(kv_pattern, line)
        if matches:
            for key, value in matches:
                fields[key] = value
        
        # Try to parse JSON-like structure
        json_pattern = r'\{[^}]+\}'
        json_match = re.search(json_pattern, line)
        if json_match:
            try:
                json_data = json.loads(json_match.group())
                fields['json_data'] = json_data
            except:
                pass
        
        return fields if fields else None
    
    def _extract_timestamp(self, line: str) -> Optional[str]:
        """Extract timestamp from log line"""
        # Common timestamp patterns
        patterns = [
            r'\d{4}-\d{2}-\d{2}[T\s]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})?',  # ISO format
            r'\d{2}/\d{2}/\d{4}\s+\d{2}:\d{2}:\d{2}',  # MM/DD/YYYY HH:MM:SS
            r'\d{2}-\d{2}-\d{4}\s+\d{2}:\d{2}:\d{2}',  # DD-MM-YYYY HH:MM:SS
            r'\[\d{2}:\d{2}:\d{2}\]',  # [HH:MM:SS]
        ]
        
        for pattern in patterns:
            match = re.search(pattern, line)
            if match:
                return match.group()
        
        return None
    
    def _detect_severity(self, line: str) -> Optional[str]:
        """Detect log severity level"""
        line_upper = line.upper()
        
        if any(word in line_upper for word in ['CRITICAL', 'FATAL']):
            return 'CRITICAL'
        elif 'ERROR' in line_upper:
            return 'ERROR'
        elif any(word in line_upper for word in ['WARN', 'WARNING']):
            return 'WARNING'
        elif any(word in line_upper for word in ['INFO', 'INFORMATION']):
            return 'INFO'
        elif any(word in line_upper for word in ['DEBUG', 'TRACE']):
            return 'DEBUG'
        elif any(word in line_upper for word in ['SUCCESS', 'PASS', 'OK']):
            return 'SUCCESS'
        elif any(word in line_upper for word in ['FAIL', 'FAILURE']):
            return 'FAILURE'
        
        return None
    
    def export_results(self, output_file: str, format: str = "json"):
        """Export results to file"""
        if format == "json":
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(self.results, f, indent=2, ensure_ascii=False)
        elif format == "txt":
            with open(output_file, 'w', encoding='utf-8') as f:
                for i, result in enumerate(self.results, 1):
                    f.write(f"\n{'='*80}\n")
                    f.write(f"Result #{i} - Line {result['line_number']}\n")
                    f.write(f"{'='*80}\n")
                    
                    if result.get('log_timestamp'):
                        f.write(f"Timestamp: {result['log_timestamp']}\n")
                    
                    if result.get('severity'):
                        f.write(f"Severity: {result['severity']}\n")
                    
                    f.write(f"\nMatched Line:\n")
                    f.write(f"  {result['line']}\n")
                    
                    if result.get('context_before'):
                        f.write(f"\nContext Before:\n")
                        for ctx_line in result['context_before']:
                            f.write(f"  {ctx_line}\n")
                    
                    if result.get('context_after'):
                        f.write(f"\nContext After:\n")
                        for ctx_line in result['context_after']:
                            f.write(f"  {ctx_line}\n")
                    
                    if result.get('parsed_fields'):
                        f.write(f"\nParsed Fields:\n")
                        for key, value in result['parsed_fields'].items():
                            f.write(f"  {key}: {value}\n")
                    
                    if result.get('hex_explanations'):
                        f.write(f"\nHex Explanations:\n")
                        for hex_exp in result['hex_explanations']:
                            if 'error' not in hex_exp:
                                f.write(f"  {json.dumps(hex_exp, indent=4)}\n")
                    
                    if result.get('nrc_explanations'):
                        f.write(f"\nNRC Explanations:\n")
                        for nrc_exp in result['nrc_explanations']:
                            f.write(f"  {nrc_exp['code']}: {nrc_exp['explanation']}\n")


if __name__ == "__main__":
    # Command-line interface
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python text_log_parser.py <log_file> [filter_keywords...]")
        print("Example: python text_log_parser.py log.txt error failure success pass")
        sys.exit(1)
    
    log_file = sys.argv[1]
    filters = sys.argv[2:] if len(sys.argv) > 2 else ['error', 'failure', 'success', 'pass']
    
    parser = TextLogParser()
    results = parser.parse_file(log_file, filters)
    
    print(f"\n{'='*80}")
    print(f"Text Log Parser Results")
    print(f"{'='*80}")
    print(f"File: {log_file}")
    print(f"Filters: {', '.join(filters)}")
    print(f"Total Matches: {len(results)}")
    print(f"{'='*80}\n")
    
    for i, result in enumerate(results, 1):
        print(f"\n--- Result #{i} (Line {result.get('line_number', 'N/A')}) ---")
        if result.get('severity'):
            print(f"Severity: {result['severity']}")
        print(f"Line: {result.get('line', 'N/A')}")
        if result.get('hex_explanations'):
            print(f"Hex Codes Found: {len(result['hex_explanations'])}")
        if result.get('nrc_explanations'):
            print(f"NRC Codes Found: {len(result['nrc_explanations'])}")
    
    # Export results
    output_file = log_file.replace('.txt', '_parsed.json').replace('.log', '_parsed.json')
    if output_file == log_file:
        output_file = log_file + '_parsed.json'
    
    parser.export_results(output_file, format='json')
    print(f"\n\nResults exported to: {output_file}")
