"""
Automated test to analyze test2.txt and show results
"""
import sys
sys.path.insert(0, r'C:\Users\HWATKI16\Downloads\xml_log_parser')

from text_log_parser import TextLogParser
from professional_diagnostic_analyzer import ProfessionalDiagnosticAnalyzer
import tkinter as tk

# Setup
test_file = r"C:\Users\HWATKI16\Downloads\xml_log_parser\test2.txt"
output_file = r"C:\Users\HWATKI16\Downloads\xml_log_parser\test2_analysis_output.txt"

print("=" * 80)
print("TEST2.TXT ANALYSIS")
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

# DEBUG: Check top ECU counts
print("\n[DEBUG] Top 10 ECU counts:")
for ecu, count in sorted(scan['ecu_counts'].items(), key=lambda x: -x[1])[:10]:
    print(f"  {repr(ecu)}: {count}")
print()

# Show new features
print("[NEW] Part Numbers by DID:")
if scan.get('part_numbers'):
    for did, parts in list(scan['part_numbers'].items())[:5]:
        print(f"  DID {did}: {', '.join(parts[:3])}")
else:
    print("  None detected")
print()

print("[NEW] Calibrations/Part Numbers:")
if scan.get('calibrations'):
    print(f"  Total: {len(scan['calibrations'])}")
    print(f"  First 5: {', '.join(scan['calibrations'][:5])}")
else:
    print("  None detected")
print()

if scan.get('fdrs_version'):
    print(f"[NEW] FDRS Version: {scan['fdrs_version']}")
print()

# Print results
output = []
output.append("=" * 80)
output.append("TEST2.TXT ANALYSIS RESULTS")
output.append("=" * 80)
output.append("")
output.append(f"PRIMARY ECU/MODULE: {scan['primary_ecu']}")
output.append("")

output.append(f"ECU COUNTS ({len(scan['ecu_counts'])} unique):")
if scan['ecu_counts']:
    for ecu, count in sorted(scan['ecu_counts'].items(), key=lambda x: -x[1])[:15]:
        output.append(f"  {ecu}: {count} occurrences")
    if len(scan['ecu_counts']) > 15:
        output.append(f"  ... and {len(scan['ecu_counts']) - 15} more ECUs")
else:
    output.append("  No ECUs detected")
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
if scan['nrc_counts']:
    for nrc, count in sorted(scan['nrc_counts'].items(), key=lambda x: -x[1])[:20]:
        output.append(f"  NRC 0x{nrc}: {count} occurrences")
    if len(scan['nrc_counts']) > 20:
        output.append(f"  ... and {len(scan['nrc_counts']) - 20} more NRCs")
else:
    output.append("  No NRCs detected")
output.append("")

output.append(f"ERROR-TO-DID MAPPING ({len(scan['did_to_errors'])} DIDs with errors):")
if scan['did_to_errors']:
    did_error_counts = [(did, len(errors)) for did, errors in scan['did_to_errors'].items()]
    did_error_counts.sort(key=lambda x: -x[1])
    
    for did, count in did_error_counts[:20]:
        output.append(f"  {did}: {count} errors")
        # Show first error for context
        if count > 0:
            first_error = scan['did_to_errors'][did][0]
            error_text = analyzer._entry_to_text(first_error)[:100]
            output.append(f"    Example: {error_text}...")
    
    if len(did_error_counts) > 20:
        output.append(f"  ... and {len(did_error_counts) - 20} more DIDs")
    
    # Calculate mapping success rate
    unmapped_count = len(scan['did_to_errors'].get('(UNKNOWN)', []))
    total_errors = sum(len(errors) for errors in scan['did_to_errors'].values())
    mapped_count = total_errors - unmapped_count
    success_rate = (mapped_count / total_errors * 100) if total_errors > 0 else 0
    
    output.append("")
    output.append(f"MAPPING SUMMARY:")
    output.append(f"  Total errors: {total_errors}")
    output.append(f"  Mapped to specific DIDs: {mapped_count}")
    output.append(f"  Unmapped (UNKNOWN): {unmapped_count}")
    output.append(f"  Mapping success rate: {success_rate:.1f}%")
else:
    output.append("  No errors detected")
output.append("")

output.append("=" * 80)

# Print to console
for line in output:
    print(line)

# Save to file
try:
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output))
    print(f"\nResults saved to: {output_file}")
except Exception as e:
    print(f"\nError saving results: {e}")

print("\n" + "=" * 80)
