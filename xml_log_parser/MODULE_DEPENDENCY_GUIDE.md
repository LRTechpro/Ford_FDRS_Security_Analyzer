# Module Dependency Tracking Feature

## Overview

The **Module Dependency Tracker** is a powerful new feature that analyzes communication patterns between ECU modules during diagnostic sessions, programming operations, and system updates. This helps identify missing dependencies that can cause module update failures.

## Why This Matters

When updating or programming vehicle modules, success depends on proper communication with dependency modules. For example:

- **PCM (7E0)** requires communication with Gateway (732), BCM (726), and BECM (7E4)
- **APIM (7D0)** needs Gateway (732), BCM (726), and ACM (727)
- **TCU (754)** depends on PCM (7E0), Gateway (732), and BCM (726)

If a required dependency module is missing, has incorrect software, or fails to communicate, the target module update will fail.

## What It Tracks

### 1. **Module Communications**
- All modules that communicated during the session
- Success/failure status of each communication
- Programming-related operations (Service 0x34, 0x36, 0x37, etc.)

### 2. **Dependency Relationships**
- Which modules communicated with each other
- Known dependency requirements for common modules
- Visual dependency graph showing relationships

### 3. **Missing Dependencies**
- Compares actual communications against known requirements
- Identifies critical missing dependencies (especially Gateway)
- Severity levels: HIGH (Gateway, critical modules), MEDIUM (supporting modules)

### 4. **Failed Communications**
- Timeout errors
- NRC (Negative Response Code) errors
- Communication failures during programming

### 5. **Recommendations**
- Prioritized action items based on analysis
- Specific guidance for Gateway issues
- Suggestions for resolving timeout/communication problems

## How to Use

### In the Enhanced GUI

1. **Parse a log file** containing diagnostic/programming session data
2. **Click the "🔗 Dependencies" tab** to view the analysis
3. **Review the sections:**
   - **Summary**: Total modules, programming attempts, failures
   - **Recommendations**: Prioritized action items
   - **Module Communication Analysis**: Detailed stats per module
   - **Missing Dependencies**: Modules that should communicate but didn't
   - **Failed Communications**: Specific errors to investigate

### Example Output

```
================================================================================
🔗 MODULE DEPENDENCY ANALYSIS
================================================================================

📊 SUMMARY
--------------------------------------------------------------------------------
Total Modules Involved: 12
Programming Attempts: 1
Failed Programming: 1
Failed Dependencies: 3

💡 RECOMMENDATIONS
--------------------------------------------------------------------------------
  • ⚠️ Gateway Support Module (732) has failed communications. This is a 
    critical dependency for most modules. Resolve Gateway issues first.
  • ❌ 1 programming/update attempts failed. Check that all dependency modules 
    are present and have correct software versions.
  • 🔍 2 critical module dependencies missing. Update may fail if these modules 
    are not properly configured.

📡 MODULE COMMUNICATION ANALYSIS
--------------------------------------------------------------------------------

PCM (Powertrain Control Module) (7E0)
  Total Communications: 8
  ✅ Successful: 6
  ❌ Failed: 2
  💾 Programming Related: 1
  🔗 Communicated With: 732, 726, 7E4

Gateway Support Module (732)
  Total Communications: 15
  ✅ Successful: 12
  ❌ Failed: 3
  💾 Programming Related: 0
  🔗 Communicated With: 7E0, 726, 7D0, 754, 760, 737

⚠️ POTENTIALLY MISSING DEPENDENCIES
--------------------------------------------------------------------------------
🔴 PCM (Powertrain Control Module) (7E0) missing dependency:
   → BECM (Battery Energy Control Module) (7E4)
🟡 APIM (Accessory Protocol Interface Module) (7D0) missing dependency:
   → ACM (Audio Control Module) (727)

❌ FAILED COMMUNICATIONS
--------------------------------------------------------------------------------

BCM (Body Control Module) (726) - TIMEOUT
  Related Modules: Gateway Support Module (732)
  BCM (726) - Communication timeout
```

## Programming Service IDs Tracked

The tracker automatically recognizes programming-related operations:

| Service ID | Description |
|------------|-------------|
| 0x10 | Diagnostic Session Control |
| 0x11 | ECU Reset |
| 0x27 | Security Access |
| 0x28 | Communication Control |
| 0x31 | Routine Control |
| 0x34 | Request Download |
| 0x35 | Request Upload |
| 0x36 | Transfer Data |
| 0x37 | Request Transfer Exit |
| 0x38 | Request File Transfer |
| 0x85 | Control DTC Setting |

## Known Module Dependencies

The tracker includes a database of known dependencies:

### Critical Dependencies (HIGH severity if missing)

- **Gateway Support Module (732)** - Required by nearly all modules
- **BCM (726)** - Required by most comfort/convenience modules
- **PCM (7E0)** - Required by powertrain-related modules
- **BECM (7E4)** - Required for battery/power management

### Example Dependency Chains

**For PCM Programming:**
```
PCM (7E0) needs:
  └─ Gateway (732) ← Entry point for all communications
  └─ BCM (726) ← Power management and configuration
  └─ BECM (7E4) ← Battery voltage monitoring
```

**For APIM Programming:**
```
APIM (7D0) needs:
  └─ Gateway (732) ← Network access
  └─ BCM (726) ← Configuration data
  └─ ACM (727) ← Audio system coordination
```

## Troubleshooting Common Issues

### Issue 1: Gateway Failures
**Symptom:** Gateway (732) shows failed communications  
**Impact:** All other module updates will likely fail  
**Solution:**
1. Check physical CAN bus connections
2. Verify Gateway module power supply
3. Update Gateway software first before other modules
4. Check for DTCs in Gateway

### Issue 2: Missing Critical Dependencies
**Symptom:** "Missing dependency" warnings for modules like BCM or BECM  
**Impact:** Target module update may fail mid-process  
**Solution:**
1. Ensure all listed dependency modules are present and powered
2. Verify dependency modules have compatible software versions
3. Update dependency modules first
4. Perform "key cycle" (ignition off/on) between updates

### Issue 3: Timeout Errors
**Symptom:** Multiple "TIMEOUT" statuses in failed communications  
**Impact:** Modules not responding, update cannot proceed  
**Solution:**
1. Check battery voltage (must be 12-14V stable)
2. Verify diagnostic cable connection quality
3. Reduce CAN bus traffic by disabling unnecessary modules
4. Check for physical wiring issues

### Issue 4: Programming Failures
**Symptom:** Programming attempts fail with NRC codes  
**Impact:** Module remains in old software version or partially programmed  
**Solution:**
1. Review all missing dependencies first
2. Ensure battery maintainer is connected
3. Verify correct programming file version
4. Check security access (Service 0x27) succeeds before programming
5. Do not interrupt programming process

## Integration with Simplified Report

The dependency analysis is automatically included in the simplified report when:
1. Errors are detected in the log, OR
2. Programming/update operations are present

This ensures you see dependency issues immediately in context with other diagnostics.

## API Usage

### For Python Scripts

```python
from module_dependency_tracker import ModuleDependencyTracker

# Parse your log first
from text_log_parser import TextLogParser
parser = TextLogParser()
results = parser.parse_file('diagnostic_session.txt')

# Analyze dependencies
tracker = ModuleDependencyTracker()
report = tracker.parse_log_for_dependencies(results)

# Access the report data
print(f"Modules involved: {report['summary']['total_modules_involved']}")
print(f"Failed programming: {report['summary']['failed_programming_attempts']}")

# Get formatted text report
formatted = tracker.format_dependency_report_text(report)
print(formatted)

# Access specific data
for module in report['module_communications']:
    print(f"{module['module_name']}: {module['failed']} failures")

for missing in report['missing_dependencies']:
    print(f"Missing: {missing['dependency_name']} for {missing['target_name']}")
```

### Convenience Function

```python
from module_dependency_tracker import analyze_dependencies

# Quick analysis with both dict and formatted text
report, formatted_text = analyze_dependencies(log_results)
print(formatted_text)
```

## Technical Details

### Module ID Detection

The tracker uses regex patterns to detect ECU addresses:
- 3-character hex patterns (e.g., 7E0, 732, 7D0)
- Validates against known ECU database
- Tracks both source and target modules in communications

### Communication Pattern Analysis

For each log entry, the tracker identifies:
1. **All ECU addresses mentioned** → Track as participants
2. **Service IDs used** → Identify programming operations
3. **Status keywords** → SUCCESS, ERROR, FAIL, TIMEOUT, WARNING
4. **Relationships** → Build dependency graph of who talked to whom

### Dependency Graph Structure

```
{
  "732": {  # Gateway
    "name": "Gateway Support Module",
    "dependencies": [
      {"id": "7E0", "name": "PCM"},
      {"id": "726", "name": "BCM"},
      ...
    ]
  },
  ...
}
```

## Future Enhancements

Potential additions for future versions:

1. **Visual Dependency Graph** - Interactive diagram showing module relationships
2. **Historical Analysis** - Compare dependency patterns across multiple logs
3. **Predictive Failures** - Machine learning to predict update failures
4. **Custom Dependency Rules** - User-defined dependency requirements
5. **Export to Graphviz** - Generate DOT files for visualization tools
6. **Timeline View** - See dependency communications over time

## See Also

- [ENHANCEMENT_SUMMARY.md](ENHANCEMENT_SUMMARY.md) - Overview of all enhancements
- [ecu_reference.py](ecu_reference.py) - ECU module database (75+ modules)
- [simplified_report.py](simplified_report.py) - Report generation with dependency integration
- [text_log_parser.py](text_log_parser.py) - Log parsing engine

---

**Version:** 1.0  
**Created:** January 2025  
**Author:** Log Parser Pro Development Team
