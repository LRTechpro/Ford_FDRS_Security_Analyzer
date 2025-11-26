"""
Automated Verification Script for Intelligent Analysis & AI Assistant Tabs
Verifies that all functions exist and are properly wired
"""

import sys
import inspect
from pathlib import Path

def verify_tab_functions():
    """Verify all required functions exist in the Professional Diagnostic Analyzer"""
    
    print("=" * 80)
    print("AUTOMATED VERIFICATION - Intelligent Analysis & AI Assistant Tabs")
    print("=" * 80)
    print()
    
    # Import the main class
    try:
        from professional_diagnostic_analyzer import ProfessionalDiagnosticAnalyzer
        print("OK - Successfully imported ProfessionalDiagnosticAnalyzer")
    except Exception as e:
        print(f"FAIL - Failed to import: {e}")
        return False
    
    print()
    print("-" * 80)
    print("INTELLIGENT ANALYSIS TAB - Function Verification")
    print("-" * 80)
    
    intelligent_functions = [
        '_create_intelligent_tab',
        '_add_evidence_document',
        '_remove_evidence_document',
        '_view_evidence_document',
        '_filter_documents',
        '_refresh_document_list',
        '_run_intelligent_analysis',
        '_clear_intelligent_analysis',
        '_save_intelligent_conclusion',
    ]
    
    passed = 0
    failed = 0
    
    for func_name in intelligent_functions:
        if hasattr(ProfessionalDiagnosticAnalyzer, func_name):
            func = getattr(ProfessionalDiagnosticAnalyzer, func_name)
            print(f"OK  {func_name:<35} - EXISTS")
            passed += 1
        else:
            print(f"FAIL {func_name:<35} - MISSING")
            failed += 1
    
    print()
    print(f"Intelligent Analysis Functions: {passed} passed, {failed} failed")
    
    print()
    print("-" * 80)
    print("AI ASSISTANT TAB - Function Verification")
    print("-" * 80)
    
    ai_functions = [
        '_create_ai_assistant_tab',
        '_set_ai_api_key',
        '_test_ai_connection',
        '_update_ai_status',
        '_ai_analyze_current_log',
        '_ai_multi_source_analysis',
        '_ai_ask_question',
        '_ai_generate_report',
        '_ai_explain_error_code',
        '_save_ai_analysis',
        '_export_ai_analysis',
        '_clear_ai_results',
        '_ensure_ai_results',
        '_build_offline_summary',
        '_build_offline_report',
        '_offline_explain_code',
    ]
    
    ai_passed = 0
    ai_failed = 0
    
    for func_name in ai_functions:
        if hasattr(ProfessionalDiagnosticAnalyzer, func_name):
            print(f"OK  {func_name:<35} - EXISTS")
            ai_passed += 1
        else:
            print(f"FAIL {func_name:<35} - MISSING")
            ai_failed += 1
    
    print()
    print(f"AI Assistant Functions: {ai_passed} passed, {ai_failed} failed")
    
    print()
    print("-" * 80)
    print("HELPER FUNCTIONS - Verification")
    print("-" * 80)
    
    helper_functions = [
        '_entry_to_text',
        '_is_error',
        '_is_warning',
        '_format_diagnostic_entry',
        '_count_unique_ecus',
        '_generate_professional_recommendations',
        '_update_error_tab',
        '_update_statistics_tab',
    ]
    
    helper_passed = 0
    helper_failed = 0
    
    for func_name in helper_functions:
        if hasattr(ProfessionalDiagnosticAnalyzer, func_name):
            print(f"OK  {func_name:<35} - EXISTS")
            helper_passed += 1
        else:
            print(f"FAIL {func_name:<35} - MISSING")
            helper_failed += 1
    
    print()
    print(f"Helper Functions: {helper_passed} passed, {helper_failed} failed")
    
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    total_passed = passed + ai_passed + helper_passed
    total_failed = failed + ai_failed + helper_failed
    total_tests = total_passed + total_failed
    
    print(f"Total Functions Verified: {total_tests}")
    print(f"Passed: {total_passed}")
    print(f"Failed: {total_failed}")
    
    if total_failed == 0:
        print()
        print("SUCCESS - ALL FUNCTIONS EXIST AND ARE PROPERLY DEFINED!")
        print()
        print("OK - Intelligent Analysis Tab: All functions implemented")
        print("OK - AI Assistant Tab: All functions implemented")
        print("OK - Helper Functions: All functions implemented")
        print()
        print("Note: This verifies function existence only.")
        print("Manual testing required to verify runtime behavior.")
        return True
    else:
        print()
        print("WARNING - SOME FUNCTIONS ARE MISSING!")
        print("Review the failed items above and implement missing functions.")
        return False

if __name__ == "__main__":
    success = verify_tab_functions()
    sys.exit(0 if success else 1)
