# Getting Started with XML Log Parser

## Quick Start Guide

### Step 1: Install Python (if needed)

If Python is not installed, download it from:
**https://www.python.org/downloads/**

During installation:
- ✓ Check "Add Python to PATH"
- ✓ Install for all users (optional)

Verify installation:
```powershell
python --version
```

### Step 2: Navigate to the Application Folder

```powershell
cd c:\Users\HWATKI16\Downloads\xml_log_parser
```

### Step 3: Run the Test (Optional)

Verify everything works:
```powershell
python test_parser.py
```

### Step 4: Start Using the Application

#### Option A: GUI Application (Easiest)
```powershell
python gui_app.py
```
Or simply double-click: **run_gui.bat**

#### Option B: Command Line
```powershell
python xml_log_parser.py sample_log.xml
```

## Using the GUI Application

### Main Window Features

1. **File Selection**
   - Click "Browse..." to select your XML log file
   - Or drag and drop the file path

2. **Filters**
   - Default: `error, failure, success, pass`
   - Customize for your needs: `error, critical, warning, info`
   - Case-insensitive matching

3. **Options**
   - ☑ Explain Hex Codes - Automatically decode hex values
   - ☑ Explain NRC Codes - Show NRC code descriptions

4. **Parse XML Button**
   - Click to analyze the log file
   - Results appear in the Results tab

5. **Export Options**
   - Export JSON - Structured data format
   - Export TXT - Human-readable format

### Hex Decoder Tab

Decode hex values on the fly:
- Enter: `48656C6C6F` or `0x48 0x65 0x6C 0x6C 0x6F`
- Click "Decode"
- See: Decimal, Binary, and ASCII interpretations

### NRC Decoder Tab

Lookup NRC codes:
- Enter: `0x35` or just `35`
- Click "Explain"
- See: Full description
- Reference table included below

## Understanding the Output

### Result Fields

Each match includes:
- **Path**: XML element path (e.g., `/TestLog/TestSession/TestCase`)
- **Tag**: XML tag name
- **Match Type**: Where the match was found (tag/text/attribute)
- **Text**: Element text content
- **Attributes**: XML attributes
- **Hex Explanations**: Decoded hex values found
- **NRC Explanations**: Decoded NRC codes found

### Hex Explanation Format
```json
{
  "hex": "0x48",
  "decimal": 72,
  "binary": "01001000",
  "ascii": "H"
}
```

### NRC Explanation Format
```json
{
  "code": "0x35",
  "explanation": "Invalid Key - Security Access Denied"
}
```

## Common Use Cases

### 1. Find All Errors in Test Log
```powershell
python xml_log_parser.py mytest.xml error failure
```

### 2. Analyze Diagnostic Session
- Filters: `error, failure, NRC`
- Look for NRC codes in failed tests
- Check hex data for anomalies

### 3. Extract Successful Tests
```powershell
python xml_log_parser.py mytest.xml success pass
```

### 4. Custom Analysis
```powershell
python xml_log_parser.py mytest.xml timeout retry abort
```

## Tips and Best Practices

### For Automotive Testing
- Filter for: `NRC, error, failure, 0x` (catches most diagnostic issues)
- Check NRC 0x78 (pending) - might indicate timing issues
- Look for hex patterns in response data

### For General XML Logs
- Start broad: `error, warning, failure`
- Refine filters based on initial results
- Use export to save and share findings

### Performance
- Large files (>10MB): Use specific filters
- Very large files (>100MB): Consider splitting or pre-filtering
- Use command-line for batch processing

## Keyboard Shortcuts (GUI)

- **Ctrl+O**: Browse for file (when file entry is focused)
- **Ctrl+A**: Select all in text areas
- **Ctrl+C**: Copy selected text
- **F5**: Refresh/reparse (if implemented)

## Example Workflow

### Scenario: Analyzing ECU Test Results

1. **Open GUI**
   ```powershell
   python gui_app.py
   ```

2. **Load Test Log**
   - Browse to your test XML file
   - Default filters include common terms

3. **Review Results**
   - Check Results tab for all matches
   - Look for patterns in failures

4. **Decode Issues**
   - Use Hex Decoder for data fields
   - Use NRC Decoder for diagnostic codes

5. **Export Report**
   - Export JSON for further processing
   - Export TXT for documentation

## Troubleshooting

### Python Not Found
- Install Python from python.org
- Restart terminal after installation
- Verify: `python --version`

### No Results Found
- Check if filters match XML content
- Try simpler filters: `test, response, status`
- Verify XML file is valid

### GUI Doesn't Start
- Check Python version (must be 3.7+)
- On Windows, tkinter comes with Python
- Try command-line version instead

### Import Errors
- Ensure all files are in same folder:
  - xml_log_parser.py
  - gui_app.py
  - test_parser.py

## Need Help?

1. Run test script: `python test_parser.py`
2. Check README.md for detailed documentation
3. Review sample_log.xml for expected format
4. Verify XML file is well-formed

## Next Steps

- Customize filters for your domain
- Create scripts for batch processing
- Integrate with CI/CD pipelines
- Export results for reporting tools

---

**Ready to start?** Run: `python gui_app.py`
