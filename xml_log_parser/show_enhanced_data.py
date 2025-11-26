#!/usr/bin/env python3
"""
Simple test to show the enhanced data structure
"""

print("🔧 ENHANCED SCAN DATA ANALYSIS")
print("=" * 50)

try:
    from text_log_parser import TextLogParser
    
    parser = TextLogParser()
    test_file = "C:/Users/HWATKI16/Downloads/Untitled-1.txt"
    result = parser.scan_ecu_and_dids(test_file)
    
    print("✅ ENHANCED SCAN SUCCESS!")
    print(f"Primary ECU: {result.get('primary_ecu', 'Unknown')}")
    
    # Part numbers by DID
    part_numbers = result.get('part_numbers', {})
    print(f"\n📦 PART NUMBERS BY DID ({len(part_numbers)} DIDs):")
    for did, parts in list(part_numbers.items())[:3]:
        print(f"   DID {did}: {parts[:2]}... ({len(parts)} total)")
    
    # Calibrations
    calibrations = result.get('calibrations', [])
    print(f"\n🔧 CALIBRATIONS ({len(calibrations)} found):")
    print(f"   Sample: {calibrations[:3]}")
    
    # FDRS version
    fdrs_ver = result.get('fdrs_version', '')
    if fdrs_ver:
        print(f"\n📊 FDRS VERSION: {fdrs_ver}")
    
    # ECU counts
    ecu_counts = result.get('ecu_counts', {})
    print(f"\n🎯 ECU COUNTS ({len(ecu_counts)} ECUs):")
    for ecu, count in list(ecu_counts.items())[:5]:
        print(f"   {ecu}: {count}")
    
    print(f"\n✅ SUCCESS RATE: {result.get('mapping_success_rate', 0):.1f}%")
    print(f"✅ TOTAL ERRORS: {result.get('total_errors', 0)}")
    
    print("\n🚀 THE FIX IS READY!")
    print("Restart your GUI to see all this enhanced data!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()