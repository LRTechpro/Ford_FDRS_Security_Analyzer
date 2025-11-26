"""
Automated test to analyze test.txt and save results
"""
import sys
import os
sys.path.insert(0, r'C:\Users\HWATKI16\Downloads\xml_log_parser')

from text_log_parser import TextLogParser
from professional_diagnostic_analyzer import ProfessionalDiagnosticAnalyzer
import tkinter as tk

# Setup
test_file = r"C:\Users\HWATKI16\Downloads\xml_log_parser\test.txt"
output_file = r"C:\Users\HWATKI16\Downloads\xml_log_parser\test_analysis_output.txt"

print("=" * 80)
print("AUTOMATED ANALYSIS TEST")
print("=" * 80)
print(f"Input file: {test_file}")
print(f"Output file: {output_file}")

# Parse the file
parser = TextLogParser()
results = parser.parse_file(test_file)
print(f"\nParsed {len(results)} entries from log file")

# Create analyzer instance
root = tk.Tk()
root.withdraw()
analyzer = ProfessionalDiagnosticAnalyzer(root)
analyzer.file_path.set(test_file)
analyzer.current_results = results

# Run the DID/ECU scan
print("\nRunning DID/ECU scan...")
scan = analyzer._scan_ecu_and_dids(results)

# Print results
output = []
output.append("=" * 80)
output.append("TEST ANALYSIS RESULTS")
output.append("=" * 80)
output.append("")
output.append(f"PRIMARY ECU/MODULE: {scan['primary_ecu']}")
output.append("")
output.append(f"ECU COUNTS ({len(scan['ecu_counts'])} unique):")
for ecu, count in sorted(scan['ecu_counts'].items(), key=lambda x: -x[1])[:10]:
    output.append(f"  {ecu}: {count} occurrences")
if len(scan['ecu_counts']) > 10:
    output.append(f"  ... and {len(scan['ecu_counts']) - 10} more ECUs")
output.append("")

output.append(f"DID COUNTS ({len(scan['did_counts'])} unique):")
if scan['did_counts']:
    for did, count in sorted(scan['did_counts'].items(), key=lambda x: -x[1])[:30]:
        output.append(f"  {did}: {count} occurrences")
    if len(scan['did_counts']) > 30:
        output.append(f"  ... and {len(scan['did_counts']) - 30} more DIDs")
else:
    output.append("  No DIDs detected")
output.append("")

output.append(f"NRC COUNTS ({len(scan['nrc_counts'])} unique):")
for nrc, count in sorted(scan['nrc_counts'].items(), key=lambda x: -x[1]):
    output.append(f"  NRC 0x{nrc}: {count} occurrences")
output.append("")

output.append(f"MODULE COUNTS ({len(scan['module_counts'])} unique):")
if scan['module_counts']:
    for mod, count in sorted(scan['module_counts'].items(), key=lambda x: -x[1]):
        output.append(f"  {mod}: {count} occurrences")
else:
    output.append("  No modules detected")
output.append("")

output.append("=" * 80)
output.append("VERIFICATION")
output.append("=" * 80)
output.append("")

# Expected results based on manual inspection of test.txt
expected_ecus = ['754']
expected_dids = ['F16B', 'F163', 'F110', 'F120', 'EEFA', 'F15F', 'A01A', 'EEFB', 'F121', 
                 '8068', 'D027', 'F188', '8061', '806B', '8060', '806A', 'F162']
expected_nrcs = ['31', '7F']

output.append("Expected values:")
output.append(f"  Primary ECU should be: {expected_ecus[0]}")
output.append(f"  Should detect DIDs: {', '.join(expected_dids[:10])}...")
output.append(f"  Should detect NRCs: {', '.join(expected_nrcs)}")
output.append("")

# Verify
issues = []
if scan['primary_ecu'] not in expected_ecus and scan['primary_ecu'] != expected_ecus[0]:
    issues.append(f"❌ Primary ECU is {scan['primary_ecu']}, expected {expected_ecus[0]}")
else:
    output.append(f"✅ Primary ECU correct: {scan['primary_ecu']}")

detected_expected_dids = [d for d in expected_dids if d in scan['did_counts']]
if len(detected_expected_dids) < len(expected_dids) * 0.8:  # At least 80% should be detected
    issues.append(f"❌ Only detected {len(detected_expected_dids)}/{len(expected_dids)} expected DIDs")
else:
    output.append(f"✅ DID detection working: {len(detected_expected_dids)}/{len(expected_dids)} expected DIDs found")

detected_expected_nrcs = [n for n in expected_nrcs if n in scan['nrc_counts']]
if len(detected_expected_nrcs) < len(expected_nrcs):
    issues.append(f"❌ Only detected {len(detected_expected_nrcs)}/{len(expected_nrcs)} expected NRCs")
else:
    output.append(f"✅ NRC detection working: {len(detected_expected_nrcs)}/{len(expected_nrcs)} NRCs found")

output.append("")
if issues:
    output.append("ISSUES FOUND:")
    for issue in issues:
        output.append(f"  {issue}")
else:
    output.append("🎉 ALL TESTS PASSED!")

output.append("")
output.append("=" * 80)

# Print to console
result_text = "\n".join(output)
print(result_text)

# Save to file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(result_text)

print(f"\nResults saved to: {output_file}")

root.destroy()
