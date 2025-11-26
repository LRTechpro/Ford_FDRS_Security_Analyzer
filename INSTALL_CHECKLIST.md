# Installation & Testing Checklist
# Ford FDRS Diagnostic Log Analyzer
# ==================================

## ✅ Pre-Installation Checklist

- [ ] Windows 10 or 11 (or Linux with tkinter support)
- [ ] Python 3.8 or higher installed
- [ ] Administrator access (if installing Python)
- [ ] At least 100MB free disk space
- [ ] FDRS log file ready for testing (or use included test4.txt)

---

## 📦 Installation Steps

### Step 1: Verify Python
```powershell
python --version
```
**Expected output:** Python 3.8.x or higher

**If Python is not installed:**
1. Download from https://python.org
2. Run installer
3. ✅ Check "Add Python to PATH"
4. ✅ Check "Install tcl/tk and IDLE"
5. Click "Install Now"

- [ ] Python version verified

---

### Step 2: Verify tkinter (GUI library)
```powershell
python -m tkinter
```
**Expected result:** Small test window opens

**If error "No module named tkinter":**
- **Windows**: Reinstall Python with "tcl/tk" checked
- **Linux**: Run `sudo apt-get install python3-tk`

- [ ] tkinter test window opens successfully

---

### Step 3: Extract/Download Tool Files

Extract the zip file or clone the repository to a folder:
```
C:\Ford_Tools\xml_log_parser\
```

**Required files:**
- [ ] professional_diagnostic_analyzer.py (main application)
- [ ] critical_diagnostic_view.py (report engine)
- [ ] enhanced_uds_parser.py (protocol parser)
- [ ] ecu_reference.py (ECU database)
- [ ] test4.txt (sample log)
- [ ] README.md (documentation)
- [ ] QUICKSTART.md (this file)

---

### Step 4: Test Launch
```powershell
cd C:\Ford_Tools\xml_log_parser
python professional_diagnostic_analyzer.py
```

**Expected result:** GUI window opens with title "Professional Diagnostic Analyzer"

- [ ] Application launches successfully
- [ ] GUI window appears
- [ ] "Browse" and "Analyze" buttons visible

---

## 🧪 Testing with Sample Log

### Step 5: Load Sample Log
1. Click "📂 Browse" button
2. Navigate to tool directory
3. Select "test4.txt"
4. File path should appear in text field

- [ ] File browser opens
- [ ] test4.txt is visible
- [ ] Path displays in GUI after selection

---

### Step 6: Run Analysis
1. Click "🔍 Analyze" button
2. Wait 5-30 seconds (progress shown in console)
3. Report appears in main window

**Expected sections in report:**
- [ ] Executive Summary box (Status: FAILED)
- [ ] Health Metrics (~64% success rate)
- [ ] Training Snapshot (hex decoder)
- [ ] Active DTCs (4 unique codes)
- [ ] Error Buckets (NRC-31 summary)
- [ ] Software Mismatch Table (3 DIDs: F188, 8068, 8033)
- [ ] Config & Flash section
- [ ] Critical Timeline

---

### Step 7: Verify Educational Features

**Training Snapshot should include:**
- [ ] Hex frame breakdown example
- [ ] Common hex patterns table
- [ ] Three boxed failure signatures

**Key findings should include:**
- [ ] "Flash step was bypassed" or similar
- [ ] 💡 "Why this matters" call-out appears

**Software Mismatch Table should show:**
- [ ] DID | Current P/N | → | Target P/N | Status
- [ ] Three rows (F188, 8068, 8033)
- [ ] "(repeated across X application files)" footnote

---

## ✅ Post-Installation Checklist

### Basic Functionality
- [ ] Tool launches without errors
- [ ] Sample log (test4.txt) loads successfully
- [ ] Analysis completes within 30 seconds
- [ ] Report displays all expected sections
- [ ] Text is readable (not cut off)
- [ ] Scrolling works smoothly

### Educational Features
- [ ] Training Snapshot section present
- [ ] Hex decoder shows example frame
- [ ] Three failure signatures in boxes
- [ ] "Why this matters" call-outs appear
- [ ] DTC primer explains system prefixes

### Report Accuracy (using test4.txt)
- [ ] Success rate shows ~64%
- [ ] Total messages: 103
- [ ] Unique errors: 16
- [ ] Active DTCs: 4 unique codes
- [ ] Software mismatches: 3 DIDs
- [ ] Status shows: FAILED

---

## 🔧 Troubleshooting Installation Issues

### Issue: Python not recognized
```powershell
# Symptom: 'python' is not recognized as a command

# Fix: Add Python to PATH
1. Find Python install location (usually C:\Python39 or C:\Users\YourName\AppData\Local\Programs\Python\Python39)
2. Add to System PATH environment variable
3. Restart PowerShell
```
- [ ] Fixed or N/A

---

### Issue: tkinter not found
```powershell
# Symptom: ModuleNotFoundError: No module named 'tkinter'

# Fix Windows:
1. Uninstall Python
2. Reinstall from python.org
3. ✅ Check "tcl/tk and IDLE"
4. Complete installation

# Fix Linux:
sudo apt-get install python3-tk
```
- [ ] Fixed or N/A

---

### Issue: Import errors (other modules)
```powershell
# Symptom: ModuleNotFoundError: No module named 'xxx'

# Check: All required files in same directory?
dir

# Should see:
# - professional_diagnostic_analyzer.py
# - critical_diagnostic_view.py
# - enhanced_uds_parser.py
# - ecu_reference.py
# - config_manager.py
# - database_manager.py
```
- [ ] All files present
- [ ] Fixed or N/A

---

### Issue: Application crashes during analysis
```powershell
# Symptom: Tool freezes or closes unexpectedly

# Check console for error messages:
python professional_diagnostic_analyzer.py
# (look for red error text)

# Common causes:
1. Log file corrupted → Try test4.txt
2. Insufficient memory → Close other apps
3. Large log file (>100MB) → Try smaller file first
```
- [ ] Fixed or N/A

---

### Issue: Report appears but is blank/incomplete
```powershell
# Symptom: Report window opens but shows little/no data

# Possible causes:
1. Log file is not FDRS format
   → Try test4.txt to verify tool works
   
2. Log file is too small/incomplete
   → Use full session log (start to finish)
   
3. Wrong file type
   → Ensure .txt file, not .xml or other format
```
- [ ] Fixed or N/A

---

## 🎉 Installation Complete!

If all checklist items are marked:
- ✅ Tool is installed correctly
- ✅ Sample log works
- ✅ Educational features display
- ✅ Ready for real log analysis

### Next Steps:
1. Read QUICKSTART.md for usage tips
2. Review README.md for full documentation
3. Analyze your first real FDRS log file
4. Share with your team!

---

## 📊 Verification Results

Installation Date: _______________
Python Version: _______________
Operating System: _______________
Tested By: _______________

**Overall Status:**
- [ ] ✅ PASS - Tool fully functional
- [ ] ⚠️ PARTIAL - Some features work, needs troubleshooting
- [ ] ❌ FAIL - Major issues, see troubleshooting section

**Notes:**
_________________________________________
_________________________________________
_________________________________________

---

## 📞 Need Help?

If you're stuck after following this checklist:

1. **Check README.md** - Comprehensive troubleshooting section
2. **Review console output** - Error messages give clues
3. **Test with test4.txt** - Verifies tool vs. log file issue
4. **Collect info for support:**
   - Python version: `python --version`
   - OS version: Windows 10/11, etc.
   - Full error message from console
   - Screenshot of problem

---

*Installation checklist complete! Ready to analyze! 🚗*
