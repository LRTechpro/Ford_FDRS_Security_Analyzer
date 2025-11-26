#!/usr/bin/env python3
"""Simple debug test"""

print("🔍 Debug script starting...")

try:
    import os
    print(f"✅ Current directory: {os.getcwd()}")
    
    # List available files
    files = [f for f in os.listdir('.') if f.startswith('[SYSTEM]')]
    print(f"✅ Found {len(files)} system files")
    
    # Test import
    from professional_diagnostic_analyzer import ProfessionalDiagnosticAnalyzer
    print("✅ Import successful")
    
    print("🎉 Debug script completed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()