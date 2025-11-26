"""
Enhanced Diagnostic Analyzer
Extracts critical diagnostic information often missed in standard analysis
"""

import re
from typing import Dict, List, Any, Optional
from collections import defaultdict


class EnhancedDiagnosticAnalyzer:
    """
    Extracts critical diagnostic details that are often overlooked:
    - Battery voltage levels
    - State of charge (SOC)
    - Temperature readings
    - Programming preconditions
    - Module power states
    - DTC codes
    - Software versions
    """
    
    def __init__(self):
        self.voltage_readings = []
        self.soc_readings = []
        self.temperature_readings = []
        self.dtc_codes = []
        self.software_versions = {}
        self.power_states = {}
        self.preconditions = {}
        
    def analyze(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Perform enhanced diagnostic analysis
        
        Returns:
            Dictionary with critical diagnostic information
        """
        self.voltage_readings = []
        self.soc_readings = []
        self.temperature_readings = []
        self.dtc_codes = []
        self.software_versions = {}
        self.power_states = {}
        self.preconditions = {}
        
        for idx, result in enumerate(results):
            text = str(result)
            
            # Extract voltage information
            self._extract_voltage(text, idx)
            
            # Extract state of charge
            self._extract_soc(text, idx)
            
            # Extract temperature
            self._extract_temperature(text, idx)
            
            # Extract DTC codes
            self._extract_dtc(text, idx)
            
            # Extract software versions
            self._extract_software_version(text, idx)
            
            # Extract power states
            self._extract_power_state(text, idx)
            
            # Extract programming preconditions
            self._extract_preconditions(text, idx)
        
        return {
            'voltage': self._analyze_voltage(),
            'state_of_charge': self._analyze_soc(),
            'temperature': self._analyze_temperature(),
            'dtc_codes': self.dtc_codes,
            'software_versions': self.software_versions,
            'power_states': self.power_states,
            'preconditions': self.preconditions,
            'critical_issues': self._identify_critical_issues()
        }
    
    def _extract_voltage(self, text: str, index: int):
        """Extract voltage readings"""
        patterns = [
            r'voltage[:\s]+(\d+\.?\d*)\s*V',
            r'battery[:\s]+(\d+\.?\d*)\s*V',
            r'(\d+\.?\d*)\s*volts?',
            r'VBATT[:\s]+(\d+\.?\d*)',
            r'V\s*=\s*(\d+\.?\d*)',
            r'supply[:\s]+(\d+\.?\d*)\s*V',
        ]
        
        for pattern in patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                voltage = float(match.group(1))
                self.voltage_readings.append({
                    'value': voltage,
                    'index': index,
                    'context': self._get_context(text, match)
                })
    
    def _extract_soc(self, text: str, index: int):
        """Extract state of charge readings"""
        patterns = [
            r'(?:state of charge|SOC|soc)[:\s]+(\d+\.?\d*)\s*%?',
            r'charge[:\s]+(\d+\.?\d*)\s*%',
            r'battery.*?(\d+)\s*%',
        ]
        
        for pattern in patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                soc = float(match.group(1))
                self.soc_readings.append({
                    'value': soc,
                    'index': index,
                    'context': self._get_context(text, match)
                })
    
    def _extract_temperature(self, text: str, index: int):
        """Extract temperature readings"""
        patterns = [
            r'temp(?:erature)?[:\s]+(-?\d+\.?\d*)\s*[°CcFf]',
            r'(-?\d+\.?\d*)\s*degrees?',
            r'thermal[:\s]+(-?\d+\.?\d*)',
        ]
        
        for pattern in patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                temp = float(match.group(1))
                self.temperature_readings.append({
                    'value': temp,
                    'index': index,
                    'context': self._get_context(text, match)
                })
    
    def _extract_dtc(self, text: str, index: int):
        """Extract DTC codes"""
        # Standard DTC format: P0123, B1234, C0456, U0789
        pattern = r'\b([PBCU][0-9A-Fa-f]{4})\b'
        matches = re.finditer(pattern, text)
        
        for match in matches:
            dtc = match.group(1).upper()
            self.dtc_codes.append({
                'code': dtc,
                'index': index,
                'context': self._get_context(text, match)
            })
    
    def _extract_software_version(self, text: str, index: int):
        """Extract software/firmware versions"""
        patterns = [
            r'(?:software|firmware|SW|FW)[:\s]+version[:\s]+([\w\.\-]+)',
            r'version[:\s]+([\w\.\-]+)',
            r'(?:SW|FW)[:\s]+([\w\.\-]+)',
        ]
        
        # Also look for module identification
        module_match = re.search(r'(?:module|ECU)[:\s]+(0x[0-9A-Fa-f]+)', text, re.IGNORECASE)
        module = module_match.group(1) if module_match else 'Unknown'
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                version = match.group(1)
                if module not in self.software_versions:
                    self.software_versions[module] = []
                self.software_versions[module].append({
                    'version': version,
                    'index': index
                })
                break
    
    def _extract_power_state(self, text: str, index: int):
        """Extract module power states"""
        patterns = [
            (r'(?:power|pwr)[:\s]+(on|off|sleep|awake|standby)', 'state'),
            (r'ignition[:\s]+(on|off|acc|run)', 'ignition'),
            (r'wake-?up', 'wakeup'),
            (r'sleep\s+mode', 'sleep'),
        ]
        
        module_match = re.search(r'(?:module|ECU)[:\s]+(0x[0-9A-Fa-f]+)', text, re.IGNORECASE)
        module = module_match.group(1) if module_match else 'Unknown'
        
        for pattern, state_type in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                if module not in self.power_states:
                    self.power_states[module] = []
                self.power_states[module].append({
                    'type': state_type,
                    'state': match.group(1) if match.lastindex else state_type,
                    'index': index
                })
    
    def _extract_preconditions(self, text: str, index: int):
        """Extract programming preconditions"""
        conditions = [
            'ignition on',
            'engine off',
            'voltage stable',
            'no active faults',
            'transmission in park',
            'doors closed',
            'key present',
        ]
        
        for condition in conditions:
            if re.search(condition, text, re.IGNORECASE):
                if condition not in self.preconditions:
                    self.preconditions[condition] = []
                
                # Determine if condition is met or not
                met = not any(neg in text.lower() for neg in ['not', 'missing', 'failed', 'incorrect'])
                
                self.preconditions[condition].append({
                    'met': met,
                    'index': index,
                    'context': text[:200]
                })
    
    def _get_context(self, text: str, match) -> str:
        """Get context around a match"""
        start = max(0, match.start() - 40)
        end = min(len(text), match.end() + 40)
        return text[start:end].strip()
    
    def _analyze_voltage(self) -> Dict[str, Any]:
        """Analyze voltage readings"""
        if not self.voltage_readings:
            return {'status': 'unknown', 'message': 'No voltage data found'}
        
        voltages = [v['value'] for v in self.voltage_readings]
        avg_voltage = sum(voltages) / len(voltages)
        min_voltage = min(voltages)
        max_voltage = max(voltages)
        
        # Determine status
        if min_voltage < 11.5:
            status = 'critical'
            message = f'⚠️ CRITICAL: Low voltage detected ({min_voltage:.1f}V) - Battery may be failing'
        elif min_voltage < 12.0:
            status = 'warning'
            message = f'⚠️ WARNING: Voltage below recommended ({min_voltage:.1f}V) - Check charging system'
        elif max_voltage > 14.5:
            status = 'warning'
            message = f'⚠️ WARNING: High voltage detected ({max_voltage:.1f}V) - Possible overcharging'
        elif avg_voltage < 12.5:
            status = 'caution'
            message = f'ℹ️ CAUTION: Average voltage slightly low ({avg_voltage:.1f}V)'
        else:
            status = 'good'
            message = f'✅ GOOD: Voltage stable ({avg_voltage:.1f}V)'
        
        return {
            'status': status,
            'message': message,
            'average': round(avg_voltage, 2),
            'min': round(min_voltage, 2),
            'max': round(max_voltage, 2),
            'readings': self.voltage_readings
        }
    
    def _analyze_soc(self) -> Dict[str, Any]:
        """Analyze state of charge readings"""
        if not self.soc_readings:
            return {'status': 'unknown', 'message': 'No state of charge data found'}
        
        socs = [s['value'] for s in self.soc_readings]
        avg_soc = sum(socs) / len(socs)
        min_soc = min(socs)
        
        # Determine status
        if min_soc < 20:
            status = 'critical'
            message = f'⚠️ CRITICAL: Low state of charge ({min_soc:.0f}%) - Battery critically low'
        elif min_soc < 50:
            status = 'warning'
            message = f'⚠️ WARNING: State of charge low ({min_soc:.0f}%) - Recharge recommended'
        elif avg_soc < 70:
            status = 'caution'
            message = f'ℹ️ CAUTION: State of charge moderate ({avg_soc:.0f}%)'
        else:
            status = 'good'
            message = f'✅ GOOD: State of charge adequate ({avg_soc:.0f}%)'
        
        return {
            'status': status,
            'message': message,
            'average': round(avg_soc, 1),
            'min': round(min_soc, 1),
            'readings': self.soc_readings
        }
    
    def _analyze_temperature(self) -> Dict[str, Any]:
        """Analyze temperature readings"""
        if not self.temperature_readings:
            return {'status': 'unknown', 'message': 'No temperature data found'}
        
        temps = [t['value'] for t in self.temperature_readings]
        avg_temp = sum(temps) / len(temps)
        max_temp = max(temps)
        min_temp = min(temps)
        
        # Determine status (assuming Celsius)
        if max_temp > 85:
            status = 'critical'
            message = f'⚠️ CRITICAL: High temperature ({max_temp:.0f}°C) - Overheating risk'
        elif max_temp > 70:
            status = 'warning'
            message = f'⚠️ WARNING: Elevated temperature ({max_temp:.0f}°C)'
        elif min_temp < -20:
            status = 'warning'
            message = f'⚠️ WARNING: Very low temperature ({min_temp:.0f}°C)'
        else:
            status = 'good'
            message = f'✅ GOOD: Temperature normal ({avg_temp:.0f}°C)'
        
        return {
            'status': status,
            'message': message,
            'average': round(avg_temp, 1),
            'min': round(min_temp, 1),
            'max': round(max_temp, 1),
            'readings': self.temperature_readings
        }
    
    def _identify_critical_issues(self) -> List[Dict[str, str]]:
        """Identify critical issues from all diagnostics"""
        issues = []
        
        # Check voltage
        voltage_analysis = self._analyze_voltage()
        if voltage_analysis['status'] in ['critical', 'warning']:
            issues.append({
                'type': 'voltage',
                'severity': voltage_analysis['status'],
                'message': voltage_analysis['message'],
                'icon': '🔋'
            })
        
        # Check SOC
        soc_analysis = self._analyze_soc()
        if soc_analysis['status'] in ['critical', 'warning']:
            issues.append({
                'type': 'state_of_charge',
                'severity': soc_analysis['status'],
                'message': soc_analysis['message'],
                'icon': '⚡'
            })
        
        # Check temperature
        temp_analysis = self._analyze_temperature()
        if temp_analysis['status'] in ['critical', 'warning']:
            issues.append({
                'type': 'temperature',
                'severity': temp_analysis['status'],
                'message': temp_analysis['message'],
                'icon': '🌡️'
            })
        
        # Check for DTCs
        if self.dtc_codes:
            issues.append({
                'type': 'dtc',
                'severity': 'warning',
                'message': f'⚠️ {len(self.dtc_codes)} Diagnostic Trouble Code(s) found',
                'icon': '🔧'
            })
        
        # Check preconditions
        unmet_preconditions = [
            cond for cond, checks in self.preconditions.items()
            if any(not check['met'] for check in checks)
        ]
        if unmet_preconditions:
            issues.append({
                'type': 'preconditions',
                'severity': 'warning',
                'message': f'⚠️ {len(unmet_preconditions)} programming precondition(s) not met',
                'icon': '⚙️'
            })
        
        return issues


if __name__ == "__main__":
    # Test the analyzer
    analyzer = EnhancedDiagnosticAnalyzer()
    
    test_data = [
        {'message': 'Battery voltage: 11.2V - WARNING: Low voltage'},
        {'message': 'State of charge: 35% - Below recommended level'},
        {'message': 'Module 0x730 temperature: 78°C'},
        {'message': 'DTC P0420: Catalyst System Efficiency Below Threshold'},
    ]
    
    results = analyzer.analyze(test_data)
    
    print("Enhanced Diagnostic Analysis:")
    print(f"\nVoltage: {results['voltage']['message']}")
    print(f"SOC: {results['state_of_charge']['message']}")
    print(f"Temperature: {results['temperature']['message']}")
    print(f"\nCritical Issues: {len(results['critical_issues'])}")
    for issue in results['critical_issues']:
        print(f"  {issue['icon']} {issue['message']}")
