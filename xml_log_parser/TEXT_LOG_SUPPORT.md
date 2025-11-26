# TEXT LOG SUPPORT - User Guide

## 📝 Good News!

The application now supports **BOTH** XML and text-based log files!

---

## 🎯 What's New

### Supported File Types
- ✅ **XML files** (.xml) - Original functionality
- ✅ **Text files** (.txt) - NEW!
- ✅ **Log files** (.log) - NEW!
- ✅ **Any text format** - Plain text, structured logs, diagnostic logs

---

## 🚀 How to Use with Text Logs

### Method 1: GUI (Easiest)

1. **Start the application:**
   ```powershell
   cd c:\Users\HWATKI16\Downloads\xml_log_parser
   python gui_app.py
   ```

2. **Load your text log:**
   - Click "Browse..."
   - Select your .txt or .log file
   - The app automatically detects the format!

3. **Parse:**
   - Set filters (default: `error, failure, success, pass`)
   - Click "Parse Log" (button works for both XML and text!)
   - View results

### Method 2: Command Line

```powershell
# For text logs
python text_log_parser.py yourlog.txt

# With custom filters
python text_log_parser.py yourlog.txt error failure warning critical

# For .log files
python text_log_parser.py system.log error exception
```

---

## 📊 Text Log Features

### What the Text Parser Detects:

1. **Filter Keywords**
   - error, failure, success, pass
   - Any custom keywords you specify

2. **Hex Codes**
   - Automatically finds: `0x1234`, `ABCD1234`, etc.
   - Explains: decimal, binary, ASCII

3. **NRC Codes**
   - Detects: `NRC: 0x35`, `nrc 0x22`, etc.
   - Explains automotive diagnostic codes

4. **Timestamps**
   - Extracts from log lines
   - Formats: ISO, US date/time, [HH:MM:SS]

5. **Severity Levels**
   - CRITICAL, ERROR, WARNING, INFO, DEBUG
   - SUCCESS, PASS, FAILURE

6. **Context**
   - Shows 2 lines before and after each match
   - Helps understand what happened

7. **Structured Fields**
   - Parses key=value pairs
   - Extracts JSON data

---

## 📝 Sample Text Log

A sample file `sample_log.txt` is included with:
- ECU diagnostic session logs
- Success and failure messages
- NRC codes (0x35, 0x22, 0x31, 0x72, 0x73, 0x7F, 0x78)
- Hex data with explanations
- Timestamps
- Severity levels

**Try it:**
```powershell
python text_log_parser.py sample_log.txt
```

Or use the GUI and browse to `sample_log.txt`

---

## 🎨 GUI Differences for Text Logs

### Results Display Shows:

**For Text Logs:**
- Line Number
- Severity (color-coded)
- Timestamp (if found)
- Matched line
- Context before/after
- Hex explanations
- NRC explanations

**For XML Logs:**
- Path in XML tree
- Tag name
- Match type
- Text content
- Attributes
- Hex explanations
- NRC explanations

The GUI automatically adapts to the file type!

---

## 💡 Common Text Log Formats Supported

### 1. Timestamped Logs
```
2025-10-14 10:30:15 [ERROR] Connection failed
2025-10-14 10:30:16 [INFO] Retrying...
2025-10-14 10:30:17 [SUCCESS] Connected
```

### 2. Diagnostic Logs
```
Request: Service=0x22 DID=0xF190
Response: 0x62 0xF1 0x90 56 31 32 33
ERROR: NRC 0x35 - Invalid Key
```

### 3. Structured Logs
```
timestamp=2025-10-14T10:30:15 level=ERROR message=Failed code=0x1234
```

### 4. Plain Text Logs
```
Starting test...
Test 1: PASS
Test 2: FAIL - Error code 0x22
Test 3: SUCCESS
```

All formats work! The parser is flexible.

---

## 🔍 Example Use Cases

### Use Case 1: Automotive Diagnostic Log
**File:** ecu_test.log  
**Filters:** `error, failure, NRC, 0x`

```powershell
python text_log_parser.py ecu_test.log error failure NRC
```

**Results:**
- All error lines
- NRC codes explained
- Hex data decoded
- Context around failures

### Use Case 2: Application Error Log
**File:** app.log  
**Filters:** `exception, error, critical`

```powershell
python text_log_parser.py app.log exception error critical
```

**Results:**
- Critical errors highlighted
- Timestamps extracted
- Severity levels shown
- Context for debugging

### Use Case 3: Test Results Log
**File:** test_results.txt  
**Filters:** `pass, fail, success, error`

```powershell
python text_log_parser.py test_results.txt pass fail success error
```

**Results:**
- All test outcomes
- Pass/fail summary
- Error details
- Line numbers for reference

---

## 📤 Export Options

Both formats support export:

### JSON Export
- Structured data
- Machine-readable
- All fields preserved
- Good for further processing

### TXT Export
- Human-readable
- Formatted report
- Includes context
- Good for documentation

**In GUI:**
1. Parse your log
2. Click "Export JSON" or "Export TXT"
3. Choose location
4. Done!

---

## 🎯 Comparison: XML vs Text

| Feature | XML Logs | Text Logs |
|---------|----------|-----------|
| File Types | .xml | .txt, .log, any text |
| Structure | Hierarchical | Line-by-line |
| Context | XML path | Lines before/after |
| Timestamps | In XML tags | Extracted from text |
| Severity | In attributes | Detected from keywords |
| Hex Codes | ✅ Both supported | ✅ Both supported |
| NRC Codes | ✅ Both supported | ✅ Both supported |
| Export | ✅ Both supported | ✅ Both supported |

---

## 🛠️ Advanced Tips

### For Large Text Logs
Use specific filters to reduce noise:
```powershell
python text_log_parser.py huge.log critical fatal error
```

### For Mixed Format Logs
The parser handles various formats in one file:
```powershell
python text_log_parser.py mixed.log error success
```

### For Real-time Monitoring
Parse the latest version of a growing log file:
```powershell
python text_log_parser.py current.log error warning
```

### Custom Filters for Your Domain
```powershell
# Network logs
python text_log_parser.py network.log timeout retry disconnect

# Database logs
python text_log_parser.py db.log deadlock error transaction

# Build logs
python text_log_parser.py build.log error failed warning
```

---

## ⚡ Quick Command Reference

### Text Logs
```powershell
# Basic
python text_log_parser.py log.txt

# With filters
python text_log_parser.py log.txt error failure

# GUI (both XML and text)
python gui_app.py
```

### XML Logs
```powershell
# Basic
python xml_log_parser.py log.xml

# With filters
python xml_log_parser.py log.xml error failure

# GUI (both XML and text)
python gui_app.py
```

---

## 📋 Files Updated

- **gui_app.py** - Now supports both XML and text logs
- **text_log_parser.py** - NEW! Text log parser
- **sample_log.txt** - NEW! Sample text log with examples
- **sample_log.xml** - Original XML sample (still works!)

---

## ✅ Benefits of Text Log Support

1. **More Flexible** - Works with any text-based log
2. **Real-world Ready** - Most logs are plain text
3. **Same Features** - Hex decoder, NRC explainer
4. **One Tool** - Parse both XML and text
5. **Same GUI** - No need to learn new interface

---

## 🎉 Ready to Use!

Your application now handles:
- ✅ XML logs (original feature)
- ✅ Text logs (NEW!)
- ✅ Hex code decoding
- ✅ NRC code explanation
- ✅ Export to JSON/TXT
- ✅ GUI and CLI interfaces

**Try it now:**
```powershell
cd c:\Users\HWATKI16\Downloads\xml_log_parser
python gui_app.py
# Browse to sample_log.txt and click Parse Log!
```

---

**Questions?** Check:
- `HOW_TO_USE.md` - General usage
- `README.md` - All features
- `NRC_REFERENCE.md` - Diagnostic codes
