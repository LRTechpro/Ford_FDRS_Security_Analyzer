"""
XML Log Parser Application
Parses XML logs, filters for errors/failures/success/pass, and explains hex codes and NRC codes
"""

import xml.etree.ElementTree as ET
import re
from datetime import datetime
from typing import List, Dict, Any
import json

class NRCCodeExplainer:
    """Explains Negative Response Codes (NRC) commonly used in automotive diagnostics"""
    
    NRC_CODES = {
        "0x10": "General Reject - Service not supported",
        "0x11": "Service Not Supported",
        "0x12": "Sub-Function Not Supported",
        "0x13": "Incorrect Message Length Or Invalid Format",
        "0x14": "Response Too Long",
        "0x21": "Busy Repeat Request",
        "0x22": "Conditions Not Correct",
        "0x24": "Request Sequence Error",
        "0x25": "No Response From Subnet Component",
        "0x26": "Failure Prevents Execution Of Requested Action",
        "0x31": "Request Out Of Range",
        "0x33": "Security Access Denied",
        "0x35": "Invalid Key",
        "0x36": "Exceed Number Of Attempts",
        "0x37": "Required Time Delay Not Expired",
        "0x70": "Upload Download Not Accepted",
        "0x71": "Transfer Data Suspended",
        "0x72": "General Programming Failure",
        "0x73": "Wrong Block Sequence Counter",
        "0x78": "Request Correctly Received - Response Pending",
        "0x7E": "Sub-Function Not Supported In Active Session",
        "0x7F": "Service Not Supported In Active Session",
    }
    
    @staticmethod
    def explain(nrc_code: str) -> str:
        """Explain an NRC code"""
        nrc_code = nrc_code.upper()
        if not nrc_code.startswith("0X"):
            nrc_code = "0x" + nrc_code
        return NRCCodeExplainer.NRC_CODES.get(nrc_code, f"Unknown NRC Code: {nrc_code}")


class HexExplainer:
    """Explains common hex patterns in logs"""
    
    @staticmethod
    def explain_byte(hex_value: str) -> Dict[str, Any]:
        """Explain a hex byte value"""
        try:
            # Remove 0x prefix if present
            hex_clean = hex_value.replace("0x", "").replace("0X", "")
            decimal = int(hex_clean, 16)
            binary = bin(decimal)[2:].zfill(8)
            
            explanation = {
                "hex": f"0x{hex_clean.upper()}",
                "decimal": decimal,
                "binary": binary,
                "ascii": chr(decimal) if 32 <= decimal <= 126 else "Non-printable"
            }
            
            return explanation
        except ValueError:
            return {"error": f"Invalid hex value: {hex_value}"}
    
    @staticmethod
    def explain_multi_byte(hex_values: str) -> Dict[str, Any]:
        """Explain multiple hex bytes"""
        # Split by common separators
        bytes_list = re.findall(r'[0-9A-Fa-f]{2}', hex_values)
        
        if not bytes_list:
            return {"error": "No valid hex bytes found"}
        
        explanations = []
        for byte_val in bytes_list:
            explanations.append(HexExplainer.explain_byte(byte_val))
        
        # Try to interpret as ASCII string
        ascii_str = ""
        for byte_val in bytes_list:
            decimal = int(byte_val, 16)
            ascii_str += chr(decimal) if 32 <= decimal <= 126 else "."
        
        return {
            "bytes": explanations,
            "total_bytes": len(bytes_list),
            "ascii_interpretation": ascii_str
        }


class XMLLogParser:
    """Main parser for XML log files"""
    
    def __init__(self):
        self.nrc_explainer = NRCCodeExplainer()
        self.hex_explainer = HexExplainer()
        self.results = []
    
    def parse_file(self, filepath: str, filters: List[str] = None) -> List[Dict[str, Any]]:
        """
        Parse XML log file and filter results
        
        Args:
            filepath: Path to XML log file
            filters: List of keywords to filter (e.g., ['error', 'failure', 'success', 'pass'])
        
        Returns:
            List of parsed and filtered log entries
        """
        if filters is None:
            filters = ['error', 'failure', 'success', 'pass']
        
        self.results = []
        
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            
            # Parse all elements recursively
            self._parse_element(root, filters)
            
            return self.results
        
        except ET.ParseError as e:
            return [{"error": f"XML Parse Error: {str(e)}"}]
        except FileNotFoundError:
            return [{"error": f"File not found: {filepath}"}]
        except Exception as e:
            return [{"error": f"Unexpected error: {str(e)}"}]
    
    def _parse_element(self, element: ET.Element, filters: List[str], parent_path: str = ""):
        """Recursively parse XML elements"""
        current_path = f"{parent_path}/{element.tag}" if parent_path else element.tag
        
        # Check element tag
        if self._matches_filter(element.tag, filters):
            self._add_result(element, current_path, "tag")
        
        # Check element text
        if element.text and element.text.strip():
            if self._matches_filter(element.text, filters):
                self._add_result(element, current_path, "text")
        
        # Check attributes
        for attr_name, attr_value in element.attrib.items():
            if self._matches_filter(attr_name, filters) or self._matches_filter(attr_value, filters):
                self._add_result(element, current_path, "attribute", attr_name, attr_value)
        
        # Recurse into children
        for child in element:
            self._parse_element(child, filters, current_path)
    
    def _matches_filter(self, text: str, filters: List[str]) -> bool:
        """Check if text matches any filter keyword"""
        text_lower = str(text).lower()
        return any(filter_word.lower() in text_lower for filter_word in filters)
    
    def _add_result(self, element: ET.Element, path: str, match_type: str, 
                    attr_name: str = None, attr_value: str = None):
        """Add a matched result with explanations"""
        result = {
            "timestamp": datetime.now().isoformat(),
            "path": path,
            "tag": element.tag,
            "match_type": match_type,
            "text": element.text.strip() if element.text else None,
            "attributes": dict(element.attrib),
        }
        
        if attr_name:
            result["matched_attribute"] = {attr_name: attr_value}
        
        # Look for hex patterns and explain them
        all_text = str(element.text) + " " + " ".join(element.attrib.values())
        hex_patterns = re.findall(r'(?:0x)?[0-9A-Fa-f]{2,}', all_text)
        
        if hex_patterns:
            result["hex_explanations"] = []
            for hex_val in hex_patterns[:5]:  # Limit to first 5
                if len(hex_val.replace("0x", "")) == 2:
                    result["hex_explanations"].append(self.hex_explainer.explain_byte(hex_val))
                else:
                    result["hex_explanations"].append(self.hex_explainer.explain_multi_byte(hex_val))
        
        # Look for NRC codes
        nrc_patterns = re.findall(r'(?:NRC|nrc)[:\s]*(?:0x)?([0-9A-Fa-f]{2})', all_text)
        if nrc_patterns:
            result["nrc_explanations"] = []
            for nrc in nrc_patterns:
                result["nrc_explanations"].append({
                    "code": f"0x{nrc.upper()}",
                    "explanation": self.nrc_explainer.explain(nrc)
                })
        
        self.results.append(result)
    
    def export_results(self, output_file: str, format: str = "json"):
        """Export results to file"""
        if format == "json":
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(self.results, f, indent=2, ensure_ascii=False)
        elif format == "txt":
            with open(output_file, 'w', encoding='utf-8') as f:
                for i, result in enumerate(self.results, 1):
                    f.write(f"\n{'='*80}\n")
                    f.write(f"Result #{i}\n")
                    f.write(f"{'='*80}\n")
                    f.write(f"Path: {result['path']}\n")
                    f.write(f"Tag: {result['tag']}\n")
                    f.write(f"Match Type: {result['match_type']}\n")
                    if result.get('text'):
                        f.write(f"Text: {result['text']}\n")
                    if result.get('attributes'):
                        f.write(f"Attributes: {result['attributes']}\n")
                    if result.get('hex_explanations'):
                        f.write(f"\nHex Explanations:\n")
                        for hex_exp in result['hex_explanations']:
                            f.write(f"  {json.dumps(hex_exp, indent=4)}\n")
                    if result.get('nrc_explanations'):
                        f.write(f"\nNRC Explanations:\n")
                        for nrc_exp in result['nrc_explanations']:
                            f.write(f"  {nrc_exp['code']}: {nrc_exp['explanation']}\n")


if __name__ == "__main__":
    # Command-line interface
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python xml_log_parser.py <xml_file> [filter_keywords...]")
        print("Example: python xml_log_parser.py log.xml error failure success pass")
        sys.exit(1)
    
    xml_file = sys.argv[1]
    filters = sys.argv[2:] if len(sys.argv) > 2 else ['error', 'failure', 'success', 'pass']
    
    parser = XMLLogParser()
    results = parser.parse_file(xml_file, filters)
    
    print(f"\n{'='*80}")
    print(f"XML Log Parser Results")
    print(f"{'='*80}")
    print(f"File: {xml_file}")
    print(f"Filters: {', '.join(filters)}")
    print(f"Total Matches: {len(results)}")
    print(f"{'='*80}\n")
    
    for i, result in enumerate(results, 1):
        print(f"\n--- Result #{i} ---")
        print(json.dumps(result, indent=2))
    
    # Export results
    output_file = xml_file.replace('.xml', '_parsed.json')
    parser.export_results(output_file, format='json')
    print(f"\n\nResults exported to: {output_file}")
