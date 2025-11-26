"""
Smart Filter Engine for Log Parser Pro
Provides context-aware search, auto-complete, and intelligent filtering suggestions
"""

import re
import json
from collections import defaultdict, Counter
from typing import List, Dict, Set, Tuple
from pathlib import Path


class SmartFilterEngine:
    """
    Intelligent filtering engine with AI-powered suggestions and context-aware search
    """
    
    def __init__(self, config_dir=None):
        """Initialize the smart filter engine"""
        self.config_dir = Path(config_dir) if config_dir else Path.home() / '.logparser'
        self.config_dir.mkdir(exist_ok=True)
        self.presets_file = self.config_dir / 'filter_presets.json'
        self.history_file = self.config_dir / 'filter_history.json'
        
        # Built-in filter presets
        self.builtin_presets = {
            "Security Issues": {
                "keywords": ["security", "access", "denied", "authentication", "seed", "key"],
                "description": "Find security-related errors and access issues",
                "icon": "🔒"
            },
            "Communication Errors": {
                "keywords": ["timeout", "no response", "bus off", "communication", "lost", "disconnect"],
                "description": "Find communication failures and timeouts",
                "icon": "📡"
            },
            "Programming Failures": {
                "keywords": ["programming", "flash", "write", "erase", "verification", "checksum"],
                "description": "Find programming and flashing errors",
                "icon": "⚙️"
            },
            "Critical Errors": {
                "keywords": ["critical", "fatal", "abort", "failure", "failed", "error"],
                "description": "Show only critical failures",
                "icon": "🔴"
            },
            "Successful Operations": {
                "keywords": ["success", "pass", "ok", "complete", "verified"],
                "description": "Show successful operations only",
                "icon": "✅"
            },
            "NRC Errors": {
                "keywords": ["NRC", "negative response", "0x", "service not supported", "conditions not correct"],
                "description": "Find negative response codes",
                "icon": "⚠️"
            },
            "Module Issues": {
                "keywords": ["module", "ECU", "0x7", "address", "offline", "unavailable"],
                "description": "Find module-specific problems",
                "icon": "📦"
            },
            "Integrity Violations": {
                "keywords": ["integrity", "checksum", "CRC", "verification", "mismatch", "corrupt"],
                "description": "Find data integrity issues",
                "icon": "🛡️"
            }
        }
        
        # Context patterns for intelligent suggestions
        self.context_patterns = {
            "error_codes": r'\b(?:0x[0-9A-Fa-f]{1,4}|NRC[:\s]*(?:0x)?[0-9A-Fa-f]{2})\b',
            "module_ids": r'\b(?:ECU|Module)[:\s]*(?:0x)?[0-9A-Fa-f]{2,3}\b',
            "services": r'\b(?:Service|SID)[:\s]*(?:0x)?[0-9A-Fa-f]{2}\b',
            "did_ids": r'\bDID[:\s]*(?:0x)?[0-9A-Fa-f]{2,4}\b',
            "timestamps": r'\d{2}:\d{2}:\d{2}[.,]\d{3}',
        }
        
        # Common UDS services for suggestions
        self.uds_services = {
            "0x10": "Diagnostic Session Control",
            "0x11": "ECU Reset",
            "0x27": "Security Access",
            "0x28": "Communication Control",
            "0x31": "Routine Control",
            "0x34": "Request Download",
            "0x36": "Transfer Data",
            "0x37": "Request Transfer Exit",
            "0x3E": "Tester Present",
            "0x22": "Read Data By Identifier",
            "0x2E": "Write Data By Identifier",
            "0x14": "Clear Diagnostic Information",
            "0x19": "Read DTC Information"
        }
        
        # Common NRC codes
        self.nrc_codes = {
            "0x11": "Service Not Supported",
            "0x12": "Sub-Function Not Supported",
            "0x13": "Incorrect Message Length",
            "0x22": "Conditions Not Correct",
            "0x24": "Request Sequence Error",
            "0x31": "Request Out Of Range",
            "0x33": "Security Access Denied",
            "0x35": "Invalid Key",
            "0x36": "Exceed Number Of Attempts",
            "0x37": "Required Time Delay Not Expired",
            "0x70": "Upload/Download Not Accepted",
            "0x71": "Transfer Data Suspended",
            "0x72": "General Programming Failure",
            "0x78": "Response Pending"
        }
        
        # Load user presets and history
        self.user_presets = self._load_presets()
        self.search_history = self._load_history()
        
        # Learning data
        self.frequent_terms = Counter()
        self.term_contexts = defaultdict(set)
        
    def _load_presets(self) -> Dict:
        """Load user-defined filter presets"""
        if self.presets_file.exists():
            try:
                with open(self.presets_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def _save_presets(self):
        """Save user-defined presets"""
        try:
            with open(self.presets_file, 'w') as f:
                json.dump(self.user_presets, f, indent=2)
        except Exception as e:
            print(f"Failed to save presets: {e}")
    
    def _load_history(self) -> List[Dict]:
        """Load search history"""
        if self.history_file.exists():
            try:
                with open(self.history_file, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def _save_history(self):
        """Save search history (keep last 100)"""
        try:
            with open(self.history_file, 'w') as f:
                json.dump(self.search_history[-100:], f, indent=2)
        except Exception as e:
            print(f"Failed to save history: {e}")
    
    def add_to_history(self, query: str, results_count: int = 0):
        """Add a search to history"""
        entry = {
            "query": query,
            "results": results_count,
            "timestamp": None  # Could add datetime if needed
        }
        self.search_history.append(entry)
        self._save_history()
    
    def learn_from_content(self, content: str):
        """Analyze content to learn common terms and patterns"""
        # Extract and count error codes
        error_codes = re.findall(self.context_patterns['error_codes'], content)
        self.frequent_terms.update(error_codes)
        
        # Extract module IDs
        module_ids = re.findall(self.context_patterns['module_ids'], content)
        self.frequent_terms.update(module_ids)
        
        # Extract common words (3+ chars, alphanumeric)
        words = re.findall(r'\b[a-zA-Z]{3,}\b', content.lower())
        self.frequent_terms.update(words)
    
    def get_suggestions(self, partial_query: str, max_suggestions: int = 10) -> List[Dict]:
        """
        Get intelligent search suggestions based on partial query
        
        Returns:
            List of suggestion dictionaries with 'text', 'type', and 'description'
        """
        suggestions = []
        query_lower = partial_query.lower().strip()
        
        if not query_lower:
            # Show popular/recent searches when empty
            if self.search_history:
                recent = list(reversed(self.search_history[-5:]))
                for entry in recent:
                    suggestions.append({
                        "text": entry['query'],
                        "type": "history",
                        "description": f"Recent search ({entry.get('results', 0)} results)",
                        "icon": "🕐"
                    })
            return suggestions
        
        # Match against built-in presets
        for name, preset in self.builtin_presets.items():
            if query_lower in name.lower() or any(query_lower in kw.lower() for kw in preset['keywords']):
                suggestions.append({
                    "text": ", ".join(preset['keywords'][:3]),
                    "type": "preset",
                    "description": f"{preset['icon']} {name}: {preset['description']}",
                    "icon": preset['icon'],
                    "preset_name": name
                })
        
        # Match against UDS services
        for code, service in self.uds_services.items():
            if query_lower in code.lower() or query_lower in service.lower():
                suggestions.append({
                    "text": f"{code} {service}",
                    "type": "service",
                    "description": f"UDS Service: {service}",
                    "icon": "🔧"
                })
        
        # Match against NRC codes
        for code, meaning in self.nrc_codes.items():
            if query_lower in code.lower() or query_lower in meaning.lower():
                suggestions.append({
                    "text": f"NRC {code} {meaning}",
                    "type": "nrc",
                    "description": f"Negative Response: {meaning}",
                    "icon": "⚠️"
                })
        
        # Match against learned frequent terms
        if self.frequent_terms:
            matching_terms = [
                term for term, count in self.frequent_terms.most_common(50)
                if query_lower in term.lower()
            ]
            for term in matching_terms[:5]:
                suggestions.append({
                    "text": term,
                    "type": "learned",
                    "description": f"Frequently seen term ({self.frequent_terms[term]}x)",
                    "icon": "💡"
                })
        
        # Match against search history
        matching_history = [
            entry for entry in reversed(self.search_history)
            if query_lower in entry['query'].lower()
        ]
        for entry in matching_history[:3]:
            suggestions.append({
                "text": entry['query'],
                "type": "history",
                "description": f"Previous search ({entry.get('results', 0)} results)",
                "icon": "🕐"
            })
        
        # Remove duplicates while preserving order
        seen = set()
        unique_suggestions = []
        for s in suggestions:
            if s['text'] not in seen:
                seen.add(s['text'])
                unique_suggestions.append(s)
        
        return unique_suggestions[:max_suggestions]
    
    def get_all_presets(self) -> Dict:
        """Get all available presets (built-in + user)"""
        all_presets = dict(self.builtin_presets)
        all_presets.update(self.user_presets)
        return all_presets
    
    def save_preset(self, name: str, keywords: List[str], description: str = "", icon: str = "🔖"):
        """Save a user-defined filter preset"""
        self.user_presets[name] = {
            "keywords": keywords,
            "description": description,
            "icon": icon
        }
        self._save_presets()
    
    def delete_preset(self, name: str):
        """Delete a user preset"""
        if name in self.user_presets:
            del self.user_presets[name]
            self._save_presets()
    
    def apply_filter(self, content: str, keywords: List[str], case_sensitive: bool = False) -> Tuple[str, int]:
        """
        Apply filter keywords to content
        
        Returns:
            (filtered_content, match_count)
        """
        if not keywords:
            return content, 0
        
        lines = content.split('\n')
        matched_lines = []
        match_count = 0
        
        for line in lines:
            line_to_check = line if case_sensitive else line.lower()
            keywords_to_check = keywords if case_sensitive else [k.lower() for k in keywords]
            
            if any(kw in line_to_check for kw in keywords_to_check):
                matched_lines.append(line)
                match_count += 1
        
        return '\n'.join(matched_lines), match_count
    
    def highlight_matches(self, text: str, keywords: List[str], case_sensitive: bool = False) -> List[Tuple[int, int, str]]:
        """
        Find match positions for highlighting
        
        Returns:
            List of (start_pos, end_pos, keyword) tuples
        """
        matches = []
        text_to_search = text if case_sensitive else text.lower()
        keywords_to_search = keywords if case_sensitive else [k.lower() for k in keywords]
        
        for keyword in keywords_to_search:
            start = 0
            while True:
                pos = text_to_search.find(keyword, start)
                if pos == -1:
                    break
                matches.append((pos, pos + len(keyword), keyword))
                start = pos + 1
        
        return sorted(matches, key=lambda x: x[0])
    
    def get_quick_stats(self, content: str) -> Dict:
        """Get quick statistics about content for smart filtering"""
        stats = {
            "total_lines": len(content.split('\n')),
            "error_count": len(re.findall(r'\berror\b', content, re.IGNORECASE)),
            "success_count": len(re.findall(r'\bsuccess\b', content, re.IGNORECASE)),
            "nrc_count": len(re.findall(r'\bNRC\b', content, re.IGNORECASE)),
            "module_count": len(set(re.findall(self.context_patterns['module_ids'], content))),
            "unique_services": len(set(re.findall(r'(?:Service|SID)[:\s]*(?:0x)?[0-9A-Fa-f]{2}', content))),
        }
        return stats
    
    def suggest_filters_for_content(self, content: str, max_suggestions: int = 5) -> List[Dict]:
        """
        Analyze content and suggest relevant filters
        
        Returns:
            List of suggested preset names with rationale
        """
        suggestions = []
        stats = self.get_quick_stats(content)
        
        # Suggest based on content analysis
        if stats['error_count'] > stats['total_lines'] * 0.1:
            suggestions.append({
                "preset": "Critical Errors",
                "reason": f"Found {stats['error_count']} errors in log",
                "relevance": stats['error_count'] / stats['total_lines']
            })
        
        if stats['nrc_count'] > 0:
            suggestions.append({
                "preset": "NRC Errors",
                "reason": f"Found {stats['nrc_count']} negative response codes",
                "relevance": stats['nrc_count'] / stats['total_lines']
            })
        
        # Check for security keywords
        security_count = len(re.findall(r'\b(?:security|access|denied|authentication)\b', content, re.IGNORECASE))
        if security_count > 0:
            suggestions.append({
                "preset": "Security Issues",
                "reason": f"Detected {security_count} security-related entries",
                "relevance": security_count / stats['total_lines']
            })
        
        # Check for communication issues
        comm_count = len(re.findall(r'\b(?:timeout|no response|communication|lost)\b', content, re.IGNORECASE))
        if comm_count > 0:
            suggestions.append({
                "preset": "Communication Errors",
                "reason": f"Found {comm_count} communication issues",
                "relevance": comm_count / stats['total_lines']
            })
        
        # Check for programming issues
        prog_count = len(re.findall(r'\b(?:programming|flash|write|erase)\b', content, re.IGNORECASE))
        if prog_count > 0:
            suggestions.append({
                "preset": "Programming Failures",
                "reason": f"Detected {prog_count} programming-related entries",
                "relevance": prog_count / stats['total_lines']
            })
        
        # Sort by relevance
        suggestions.sort(key=lambda x: x['relevance'], reverse=True)
        
        return suggestions[:max_suggestions]


if __name__ == "__main__":
    # Test the smart filter engine
    engine = SmartFilterEngine()
    
    print("Testing Smart Filter Engine\n")
    print("=" * 60)
    
    # Test suggestions
    print("\n1. Testing suggestions for 'security':")
    suggestions = engine.get_suggestions("security")
    for s in suggestions[:5]:
        print(f"   {s['icon']} {s['text']}")
        print(f"      {s['description']}")
    
    print("\n2. Testing suggestions for '0x27':")
    suggestions = engine.get_suggestions("0x27")
    for s in suggestions[:3]:
        print(f"   {s['icon']} {s['text']}")
        print(f"      {s['description']}")
    
    print("\n3. Available presets:")
    presets = engine.get_all_presets()
    for name, preset in list(presets.items())[:5]:
        print(f"   {preset['icon']} {name}")
        print(f"      Keywords: {', '.join(preset['keywords'][:4])}")
    
    print("\n" + "=" * 60)
    print("Smart Filter Engine initialized successfully!")
