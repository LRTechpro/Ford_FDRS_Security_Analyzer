# HOW TO USE - XML Log Parser (Complete Guide)

## ⚠️ STEP 0: Install Python First

**Python is NOT currently installed on your system.** Here's how to install it:

### Install Python (5 minutes)

1. **Download Python**
   - Go to: https://www.python.org/downloads/
   - Click the big yellow button "Download Python 3.x.x"
   - Save the installer

2. **Run the Installer**
   - Double-click the downloaded file
   - ⚠️ **IMPORTANT**: Check the box "Add Python to PATH" (at bottom)
   - Click "Install Now"
   - Wait for installation to complete
   - Click "Close"

3. **Verify Installation**
   - Open a NEW PowerShell window (important - close old ones)
   - Type: `python --version`
   - You should see: `Python 3.x.x`

---

## 📍 YOUR FILES ARE HERE

**Location:** `c:\Users\HWATKI16\Downloads\xml_log_parser\`

**Files you'll use:**
- `gui_app.py` - The main application (GUI)
- `xml_log_parser.py` - Command-line version
- `sample_log.xml` - Example file to test with
- `run_gui.bat` - Quick launcher (after Python is installed)

---

## 🚀 QUICK START (After Python is Installed)

### Method 1: Double-Click Launcher (EASIEST)

1. Open File Explorer
2. Navigate to: `c:\Users\HWATKI16\Downloads\xml_log_parser\`
3. **Double-click:** `run_gui.bat`
4. The GUI will open automatically!

### Method 2: PowerShell (Recommended for first time)

1. Open PowerShell
2. Run these commands:
   ```powershell
   cd c:\Users\HWATKI16\Downloads\xml_log_parser
   python gui_app.py
   ```
3. The GUI window will appear!

---

## 🖥️ USING THE GUI APPLICATION

### Step-by-Step First Use

#### 1. **Open the Application**
```powershell
cd c:\Users\HWATKI16\Downloads\xml_log_parser
python gui_app.py
```

#### 2. **Select Your XML File**
- Click the **"Browse..."** button
- Navigate to your XML log file
- Select it and click "Open"
- Or try the sample: Select `sample_log.xml`

#### 3. **Configure Filters**
The default filters are: `error, failure, success, pass`

**Change them if needed:**
- Click in the "Keywords" text box
- Type your keywords separated by commas
- Examples:
  - `error, failure, critical`
  - `success, pass, complete`
  - `NRC, timeout, abort`

#### 4. **Choose Options**
- ☑️ **Explain Hex Codes** - Shows decoded hex values
- ☑️ **Explain NRC Codes** - Shows diagnostic code explanations

#### 5. **Parse the XML**
- Click **"Parse XML"** button
- Wait for processing (status bar shows progress)
- Results appear in the "Results" tab

#### 6. **Review Results**
Look at the "Results" tab:
- **Blue headers** - Each match found
- **Green sections** - Hex code explanations
- **Red sections** - NRC code explanations
- Scroll through all matches

#### 7. **Export Results** (Optional)
- Click **"Export JSON"** - For data processing
- Click **"Export TXT"** - For human reading
- Choose where to save the file

---

## 📊 EXAMPLE: Using Sample Log

### Try This First (After Python is installed):

```powershell
# Step 1: Navigate to folder
cd c:\Users\HWATKI16\Downloads\xml_log_parser

# Step 2: Open GUI
python gui_app.py
```

**In the GUI:**
1. Click "Browse..." 
2. Select `sample_log.xml`
3. Leave filters as default: `error, failure, success, pass`
4. Click "Parse XML"
5. See results - should find 10+ matches!

**You'll see:**
- ✅ Success and Pass results
- ❌ Error and Failure results
- 🔢 Hex codes decoded (like `0x48656C6C6F` = "Hello")
- 🔴 NRC codes explained (like `0x35` = "Invalid Key")

---

## 🛠️ USING THE TOOL TABS

### **Hex Decoder Tab**

Decode hex values manually:

1. Click the **"Hex Decoder"** tab
2. Enter hex value, examples:
   - `48656C6C6F`
   - `0x48 0x65 0x6C 0x6C 0x6F`
   - `62F190`
3. Click **"Decode"**
4. See results:
   - Hex: `0x48`
   - Decimal: `72`
   - Binary: `01001000`
   - ASCII: `H`

### **NRC Decoder Tab**

Look up diagnostic codes:

1. Click the **"NRC Decoder"** tab
2. Enter NRC code, examples:
   - `0x35`
   - `35`
   - `0x78`
3. Click **"Explain"**
4. See explanation: "Invalid Key - Security Access Denied"

**Scroll down** to see complete NRC reference table!

---

## 💻 COMMAND LINE USAGE

### Basic Command
```powershell
python xml_log_parser.py sample_log.xml
```

### Custom Filters
```powershell
python xml_log_parser.py sample_log.xml error failure warning
```

### Your Own File
```powershell
python xml_log_parser.py "C:\path\to\your\logfile.xml"
```

**Results:**
- Prints to screen
- Auto-exports to JSON file (same name + `_parsed.json`)

---

## 📁 WORKING WITH YOUR OWN XML FILES

### Option A: Move Your XML to the App Folder
```powershell
# Copy your XML to the app folder
copy "C:\your\log\file.xml" "c:\Users\HWATKI16\Downloads\xml_log_parser\"

# Then use it
cd c:\Users\HWATKI16\Downloads\xml_log_parser
python gui_app.py
```

### Option B: Browse to Any Location
1. Open the GUI
2. Click "Browse..."
3. Navigate anywhere on your computer
4. Select your XML file

---

## 🎯 COMMON USE CASES

### Use Case 1: Find All Errors in Test Log
**Filters:** `error, failure, fail`

1. Open GUI
2. Select your test log XML
3. Set filters: `error, failure, fail`
4. Parse
5. Export TXT for report

### Use Case 2: Extract Successful Tests
**Filters:** `success, pass, ok`

1. Open GUI
2. Select your test log XML
3. Set filters: `success, pass, ok`
4. Parse
5. Review Results tab

### Use Case 3: Decode Diagnostic Codes
**Filters:** `NRC, 0x, error`

1. Open GUI
2. Select diagnostic log
3. Keep default filters
4. Parse
5. Look for "NRC Explanations" sections in red

### Use Case 4: Batch Processing (Command Line)
```powershell
cd c:\Users\HWATKI16\Downloads\xml_log_parser

# Process multiple files
python xml_log_parser.py log1.xml error failure
python xml_log_parser.py log2.xml error failure
python xml_log_parser.py log3.xml error failure
```

---

## 🔍 UNDERSTANDING THE OUTPUT

### What You'll See in Results

```
--- Result #1 ---
Path: /TestLog/TestSession/TestCase
Tag: Status
Match Type: text
Text: Failure
Attributes: {"id": "TC002", "name": "Security Access Test"}

[HEX EXPLANATIONS]
{
  "hex": "0x35",
  "decimal": 53,
  "binary": "00110101",
  "ascii": "5"
}

[NRC EXPLANATIONS]
  0x35: Invalid Key - Security Access Denied
```

**What it means:**
- **Path:** Where in XML this was found
- **Tag:** The XML element name
- **Text:** The content that matched your filter
- **Hex Explanations:** Any hex values decoded
- **NRC Explanations:** Any diagnostic codes explained

---

## ⚡ QUICK REFERENCE

### Open GUI
```powershell
cd c:\Users\HWATKI16\Downloads\xml_log_parser
python gui_app.py
```

### Run Command Line
```powershell
python xml_log_parser.py yourfile.xml
```

### Run Test
```powershell
python test_parser.py
```

### Open Folder in Explorer
```powershell
cd c:\Users\HWATKI16\Downloads\xml_log_parser
explorer .
```

---

## ❓ TROUBLESHOOTING

### "Python was not found"
- Install Python from python.org
- Make sure to check "Add to PATH" during installation
- Restart PowerShell after installing

### "No module named 'xml_log_parser'"
- Make sure you're in the correct folder
- Run: `cd c:\Users\HWATKI16\Downloads\xml_log_parser`

### "No results found"
- Check if your filters match content in XML
- Try simpler filters: `test, response, status`
- Make sure XML file is valid

### GUI doesn't open
- Check Python version: `python --version` (needs 3.7+)
- Try command line version instead: `python xml_log_parser.py sample_log.xml`

---

## 📞 NEED MORE HELP?

1. **Test the Installation:**
   ```powershell
   python test_parser.py
   ```

2. **Read Full Documentation:**
   - `README.md` - Complete features
   - `GETTING_STARTED.md` - Detailed setup
   - `NRC_REFERENCE.md` - Code reference

3. **Try the Sample:**
   ```powershell
   python xml_log_parser.py sample_log.xml
   ```

---

## ✅ CHECKLIST TO GET STARTED

- [ ] Install Python from python.org
- [ ] Check "Add Python to PATH" during install
- [ ] Restart PowerShell
- [ ] Verify: `python --version`
- [ ] Navigate: `cd c:\Users\HWATKI16\Downloads\xml_log_parser`
- [ ] Test: `python test_parser.py`
- [ ] Run: `python gui_app.py`
- [ ] Try sample_log.xml
- [ ] Parse your own XML files!

---

**You're all set!** Once Python is installed, just run:
```powershell
cd c:\Users\HWATKI16\Downloads\xml_log_parser
python gui_app.py
```
