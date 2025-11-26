# 📦 Installation Guide - Log Parser Pro v2.0

## Table of Contents
1. [Basic Installation](#basic-installation)
2. [Full Installation (Recommended)](#full-installation-recommended)
3. [Optional Dependencies](#optional-dependencies)
4. [Verification](#verification)
5. [Troubleshooting](#troubleshooting)

---

## Basic Installation

**No installation needed!** The core application runs with Python's standard library only.

### Requirements
- Python 3.7 or higher
- Windows, macOS, or Linux

### Quick Start
```bash
# Just run it!
python gui_app_enhanced.py
```

**What works without dependencies:**
✅ XML & Text log parsing  
✅ Simple Mode & Expert Mode  
✅ ECU database (75+ modules)  
✅ Root cause analysis  
✅ Colorful display  
✅ Export JSON/TXT  
✅ Hex & NRC decoders  
✅ Configuration management  
✅ Database history  
✅ Log comparison  

**What's disabled without dependencies:**
⚠️ Drag & drop (use browse button instead)  
⚠️ Analytics charts (shows installation instructions)  

---

## Full Installation (Recommended)

To enable **ALL** features including drag-and-drop and analytics charts:

### Windows

```powershell
# Install Python (if not already installed)
# Download from: https://www.python.org/downloads/

# Install optional packages
pip install matplotlib tkinterdnd2

# Verify installation
python -c "import matplotlib; import tkinterdnd2; print('All packages installed successfully!')"

# Run enhanced GUI
python gui_app_enhanced.py
```

### macOS / Linux

```bash
# Install Python (if not already installed)
# macOS: Python 3 is usually pre-installed
# Linux: sudo apt-get install python3 python3-pip

# Install optional packages
pip3 install matplotlib tkinterdnd2

# Verify installation
python3 -c "import matplotlib; import tkinterdnd2; print('All packages installed successfully!')"

# Run enhanced GUI
python3 gui_app_enhanced.py
```

---

## Optional Dependencies

### 1. matplotlib (Analytics Charts)

**Purpose:** Enables the Analytics tab with visualizations

**Install:**
```bash
pip install matplotlib
```

**Features unlocked:**
- 📊 Error Timeline Chart
- 🚗 ECU Health Dashboard
- 🥧 NRC Frequency Chart
- 📈 Success Rate Gauge

**Size:** ~50MB

**Without it:** Analytics tab shows "Install matplotlib" message, all other features work normally.

---

### 2. tkinterdnd2 (Drag & Drop)

**Purpose:** Enables drag-and-drop file support

**Install:**
```bash
pip install tkinterdnd2
```

**Features unlocked:**
- 🎯 Drag log files directly onto window
- Faster workflow

**Size:** ~1MB

**Without it:** Use the "Browse" button instead (works identically)

---

## Verification

### Check Python Version
```bash
python --version
# Should show: Python 3.7 or higher
```

### Check Installed Packages
```bash
pip list
# Should show:
#   matplotlib    (if installed)
#   tkinterdnd2   (if installed)
```

### Test Core Functionality
```bash
# Run the app
python gui_app_enhanced.py

# You should see the main window with:
# - File selection area
# - Filter controls
# - 6 tabs: Results, Analytics, Compare, History, Hex Decoder, NRC Decoder
```

### Test Optional Features

**Test Drag & Drop:**
1. Open the app
2. Try dragging a .xml or .txt file onto the window
3. If it opens, drag & drop is working!
4. If nothing happens, tkinterdnd2 is not installed (use Browse button)

**Test Analytics:**
1. Open the app
2. Click the "📈 Analytics" tab
3. If you see chart controls, matplotlib is working!
4. If you see "Analytics not available", install matplotlib

---

## Troubleshooting

### Issue: "python: command not found"

**Solution:**
- **Windows:** Add Python to PATH during installation, or use `py` instead of `python`
- **macOS/Linux:** Use `python3` instead of `python`

### Issue: "pip: command not found"

**Solution:**
```bash
# Windows
python -m pip install matplotlib

# macOS/Linux
python3 -m pip install matplotlib
```

### Issue: "ImportError: No module named 'tkinter'"

**Solution:**
- **Windows:** Reinstall Python with "tcl/tk and IDLE" option checked
- **Linux Ubuntu/Debian:** `sudo apt-get install python3-tk`
- **Linux Fedora:** `sudo dnf install python3-tkinter`
- **macOS:** tkinter is included with Python

### Issue: "Permission denied" when installing packages

**Solution:**
```bash
# Use --user flag
pip install --user matplotlib tkinterdnd2

# Or use sudo (Linux/macOS only)
sudo pip3 install matplotlib tkinterdnd2
```

### Issue: Charts show but are blank/empty

**Solution:**
1. Parse a log file first (charts show history from database)
2. If database is empty, charts will be empty
3. Parse a few logs, then click Analytics tab
4. Click "Refresh Charts" button

### Issue: "Could not resolve import" warnings in IDE

**These are false positives!** The app runs fine. All modules are in the same directory and import correctly at runtime.

To silence IDE warnings:
1. VS Code: Add folder to Python path
2. PyCharm: Mark directory as "Sources Root"

### Issue: Dark mode not working

**Solution:**
1. Toggle dark mode from **View > Toggle Dark Mode**
2. **Restart the application** (theme applies on startup)
3. Check `~/.log_parser/config.json` - should show `"theme": "dark"`

### Issue: Database errors

**Solution:**
```bash
# Delete corrupted database (app will recreate it)
# Windows
del %USERPROFILE%\.log_parser\log_history.db

# macOS/Linux
rm ~/.log_parser/log_history.db

# Restart app - database will be recreated
```

### Issue: App crashes on startup

**Solution:**
1. Check Python version: `python --version` (need 3.7+)
2. Try original version first: `python gui_app.py`
3. If original works but enhanced doesn't, check dependencies
4. Look for error messages in console

---

## Upgrading

### Update to Latest Version

```bash
# Pull latest code or extract new files
# No database migration needed - backward compatible!

# Update dependencies
pip install --upgrade matplotlib tkinterdnd2

# Run enhanced version
python gui_app_enhanced.py
```

### Rollback to Original

```bash
# Original version still available
python gui_app.py

# or use original launcher
run_gui.bat
```

**Both versions can coexist!** They use the same database and config files.

---

## Virtual Environment (Advanced)

For isolated installation:

```bash
# Create virtual environment
python -m venv log_parser_env

# Activate
# Windows:
log_parser_env\Scripts\activate
# macOS/Linux:
source log_parser_env/bin/activate

# Install dependencies
pip install matplotlib tkinterdnd2

# Run app
python gui_app_enhanced.py

# Deactivate when done
deactivate
```

---

## Network/Proxy Issues

If you're behind a corporate firewall:

```bash
# Use proxy
pip install --proxy http://proxy.company.com:8080 matplotlib

# Or use offline installation
# Download wheels from: https://pypi.org/project/matplotlib/#files
pip install matplotlib-*.whl
```

---

## Installation Summary

| Feature | Requires | Command | Size |
|---------|----------|---------|------|
| Core App | Python 3.7+ | (built-in) | ~100KB |
| Analytics | matplotlib | `pip install matplotlib` | ~50MB |
| Drag & Drop | tkinterdnd2 | `pip install tkinterdnd2` | ~1MB |

**Recommendation:** Install both for full experience (~51MB total)

---

## Quick Commands Reference

```bash
# Check what you have
python --version
pip list

# Install everything
pip install matplotlib tkinterdnd2

# Run enhanced app
python gui_app_enhanced.py

# Run original app
python gui_app.py

# Verify installation
python -c "import matplotlib, tkinterdnd2; print('Success!')"
```

---

## Still Having Issues?

1. **Try the original version first:** `python gui_app.py`
2. **Check error messages** in the console/terminal
3. **Verify Python version:** Must be 3.7 or higher
4. **Test basic Python:** `python -c "print('Hello')"`
5. **Contact support** with error message details

---

**Happy Installing! 🚀**
