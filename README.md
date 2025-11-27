# Ford FDRS Security Analyzer
## Professional Automotive Cybersecurity & Diagnostic Log Analysis Tool

**Enterprise-level cybersecurity and diagnostic analysis platform for Ford FDRS (Ford Diagnostic and Repair System)**

A comprehensive security and diagnostic analysis tool designed specifically for Ford vehicle systems. This professional-grade tool combines expert-level diagnostics with built-in cybersecurity threat detection.



A professional-grade diagnostic log analysis tool for Ford FDRS (Ford Diagnostic and Repair System) that combines expert-level diagnostics with built-in training features for technicians.A comprehensive tool for parsing **XML and text logs** with automatic filtering for errors, failures, successes, and passes. It also explains hex codes and NRC (Negative Response Codes) commonly used in automotive diagnostics.



## 🎯 What It Does## 🎉 Now Supports Both XML and Text Logs!



This tool analyzes FDRS diagnostic log files and generates comprehensive, easy-to-read reports that:Parse any log format - XML, TXT, LOG files - all in one application!

- **Identify root causes** of flash failures, software mismatches, and diagnostic errors

- **Teach while diagnosing** with built-in hex decoding guides and failure pattern recognition## Features

- **Deduplicate noise** (NRC-31 storms, repeated validation failures)

- **Provide actionable recommendations** for field technicians- **Universal Log Parsing**: 

  - XML files (.xml) - Hierarchical parsing with path tracking

## 📋 Features  - Text files (.txt, .log) - Line-by-line parsing with context

  - Automatic format detection

### Core Analysis- **Smart Filtering**: Filters for keywords like error, failure, success, pass (customizable)

- ✅ **Root Cause Analysis**: Identifies why flashes fail (skipped, validation errors, USB issues)- **Hex Code Decoder**: Automatically detects and explains hex values with:

- ✅ **Software Mismatch Detection**: Shows which DIDs need updating with current vs. target part numbers  - Decimal conversion

- ✅ **DTC Analysis**: Decodes and explains Diagnostic Trouble Codes with freeze-frame links  - Binary representation

- ✅ **Timeline View**: Shows critical events (ApplicationState changes, NRC-31 bursts, validation failures)  - ASCII interpretation

- ✅ **Health Metrics**: Success rates, error counts, voltage status  - Multi-byte analysis

- **NRC Code Explainer**: Identifies and explains Negative Response Codes (UDS/OBD diagnostic codes)

### Educational Features- **Advanced Text Log Features**:

- 📚 **Training Snapshot**: Hex frame decoder with byte-by-byte explanations  - Timestamp extraction

- 📚 **Failure Signatures**: Pattern recognition guide (flash skipped, validation burst, NRC-31 storm)  - Severity level detection (CRITICAL, ERROR, WARNING, SUCCESS, etc.)

- 📚 **Inline Explanations**: "Why this matters" call-outs for key findings  - Context lines (shows lines before/after matches)

- 📚 **DTC Primer**: System prefixes explained (B=Body, P=Powertrain, etc.)  - Structured field parsing (key=value pairs)

- **Multiple Interfaces**:

### Smart Deduplication  - Unified GUI for both XML and text logs

- Collapses 50+ identical NRC-31 errors into a summary with DID frequency  - Command-line interface for scripting

- Groups repeated ValidateFlashAction failures with counts  - Standalone decoders (hex & NRC)

- Deduplicates software mismatch table (shows each DID once with occurrence count)- **Export Options**: Export results to JSON or TXT format

- **Real-time Decoding**: Standalone hex and NRC decoders in the GUI

## 🚀 Quick Start

## Installation

### Prerequisites

- **Python 3.8+** (3.10 or higher recommended)### Requirements

- **Windows 10/11** (tested on Windows; may work on Linux/Mac with minor adjustments)- Python 3.7 or higher

- **No additional packages required** - uses only Python standard library (tkinter, xml, re, etc.)- tkinter (usually comes with Python)



### Installation### Setup

1. Ensure Python is installed:

1. **Verify Python Installation**   ```powershell

   ```powershell   python --version

   python --version   ```

   # Should show Python 3.8 or higher

   ```2. All required libraries are part of Python's standard library, no additional installation needed!



2. **Navigate to the Tool Directory**## Usage

   ```powershell

   cd C:\path\to\xml_log_parser### GUI Application (Recommended)

   ```

Run the GUI application:

3. **Launch the Application**```powershell

   ```powershellpython gui_app.py

   python professional_diagnostic_analyzer.py```

   ```

**GUI Features:**

### First Use1. **File Selection**: Browse and select your XML log file

2. **Filters**: Customize filter keywords (comma-separated)

1. **Launch the Application**3. **Options**: Toggle hex and NRC explanations

   ```powershell4. **Results Tab**: View parsed results with color-coded formatting

   python professional_diagnostic_analyzer.py5. **Hex Decoder Tab**: Standalone hex value decoder

   ```6. **NRC Decoder Tab**: Standalone NRC code explainer with reference table

7. **Export**: Save results as JSON or TXT

2. **Load a Log File**

   - Click **"📂 Browse"** button### Command-Line Interface

   - Select your FDRS log file (`.txt` format)

   - Supported formats:Basic usage:

     - FDRS diagnostic logs```powershell

     - PMI (Programmable Module Installation) logspython xml_log_parser.py sample_log.xml

     - Software update logs```



3. **Analyze**With custom filters:

   - Click **"🔍 Analyze"** button```powershell

   - Wait for processing (typically 5-30 seconds depending on log size)python xml_log_parser.py sample_log.xml error failure warning success

   - Review the comprehensive report```



4. **Navigate the Report**## Examples

   - **Health Metrics**: Overview with success rate and error summary

   - **Training Snapshot**: Learn hex patterns and failure signatures### Example 1: Parse Sample Log

   - **Active DTCs**: Click 🔗 for Ford Service Info```powershell

   - **Error Buckets**: Deduplicated error summarypython xml_log_parser.py sample_log.xml

   - **Config & Flash**: Flash operation details```

   - **Critical Timeline**: Key events with timestamps

### Example 2: Filter Specific Keywords

## 📁 Key Files```powershell

python xml_log_parser.py mylog.xml error critical failure

``````

xml_log_parser/

├── professional_diagnostic_analyzer.py  ⭐ Main application - START HERE### Example 3: Use GUI for Interactive Parsing

├── critical_diagnostic_view.py          # Report formatting engine```powershell

├── enhanced_uds_parser.py               # UDS protocol parserpython gui_app.py

├── ecu_reference.py                     # ECU database```

├── test4.txt                            # Sample log for testing

└── README.md                            # This file## NRC Codes Reference

```

The application recognizes and explains common NRC codes:

## 🧪 Testing with Sample Data

| Code | Description |

A sample log file (`test4.txt`) is included for testing:|------|-------------|

| 0x10 | General Reject - Service not supported |

1. Launch: `python professional_diagnostic_analyzer.py`| 0x11 | Service Not Supported |

2. Click **"📂 Browse"** → select `test4.txt`| 0x12 | Sub-Function Not Supported |

3. Click **"🔍 Analyze"**| 0x13 | Incorrect Message Length Or Invalid Format |

| 0x21 | Busy Repeat Request |

**Expected Results:**| 0x22 | Conditions Not Correct |

- Status: FAILED| 0x31 | Request Out Of Range |

- Success Rate: ~64%| 0x33 | Security Access Denied |

- Key Finding: Flash step bypassed (ApplicationState = SKIPPED)| 0x35 | Invalid Key |

- Software Mismatches: 3 DIDs out-of-date (F188, 8068, 8033)| 0x72 | General Programming Failure |

- Educational training snapshot with hex decoder| 0x73 | Wrong Block Sequence Counter |

| 0x78 | Request Correctly Received - Response Pending |

## 📖 Understanding the Report

...and many more!

### 1. Health Metrics

```## Output Format

• Success rate: 64.1% (66 of 103)

  Success rate = successful diagnostic frames ÷ total frames### JSON Export

• Unique errors: 16 (NRC-31: 3, Java: 10, XML: 3)Structured data with complete information:

• Battery: Voltage not queried – Bench or KOEO session```json

• Active DTCs: 8 occurrences / 4 unique codes{

```  "timestamp": "2025-10-14T10:30:00",

  "path": "/TestLog/TestSession/TestCase",

### 2. Training Snapshot (Educational)  "tag": "Status",

Learn to decode hex frames and recognize failure patterns:  "match_type": "text",

  "text": "Failure",

**Hex Frame Breakdown:**  "hex_explanations": [...],

```  "nrc_explanations": [...]

Raw frame:     00 00 07 D8 7F 22 31}

Break-down:    00 00 07 D8  = CAN header (target ECU 7D8)```

               7F           = Negative response

               22           = Service "ReadDataByIdentifier"### TXT Export

               31           = NRC-31 "Request out of range"Human-readable format with sections for each match.

```

## Project Structure

**Failure Signatures:**

- ① **Flash Skipped**: `ApplicationState = SKIPPED` → flash bypassed```

- ② **Validation Burst**: 10-30 `ValidateFlashAction` failures → old part numbersxml_log_parser/

- ③ **NRC-31 Storm**: Repeated `7F 22 31` → script probed unsupported DIDs (normal)├── xml_log_parser.py   # Core parsing engine

├── gui_app.py          # GUI application

### 3. Software Mismatch Table├── sample_log.xml      # Sample XML log for testing

```└── README.md           # This file

DID   Current P/N          → Target P/N          Status```

F188  PU5T-14G676-CC  → NU5T-14G676-EC  OUT-OF-DATE

8068  MU5T-14H236-MD  → MU5T-14H236-MC  OUT-OF-DATE## Advanced Usage

(repeated across 108 application files)

```### Custom Filters

You can filter for any keywords:

**What this means:**- Error types: `error`, `fail`, `failure`, `exception`

- **Current P/N**: What the PMI specification requires (flash goal)- Success types: `success`, `pass`, `ok`, `complete`

- **Target P/N**: What's actually on the module right now (needs update)- Status codes: `0x35`, `NRC`, specific hex values

- **OUT-OF-DATE**: Flash is needed to sync module to specification- Custom terms: `timeout`, `retry`, `warning`



### 4. Critical Timeline### Hex Decoder

```The hex decoder can handle:

15:15:33  ApplicationState set to SKIPPED (flash bypassed)- Single bytes: `0x48` or `48`

15:15:34  ValidateFlashAction → FAIL (F188, 8033)- Multiple bytes: `48656C6C6F` (interprets as ASCII)

15:15:35  NRC-31 burst begins (first 7F 22 31)- Space-separated: `0x48 0x65 0x6C`

(+37 similar events suppressed)

```### Programmatic Use



## 🛠️ Troubleshooting```python

from xml_log_parser import XMLLogParser

### "No module named 'tkinter'"

**Windows:**parser = XMLLogParser()

- Reinstall Python from [python.org](https://python.org)results = parser.parse_file('mylog.xml', ['error', 'failure'])

- During installation, ensure "tcl/tk and IDLE" is checked

# Export results

**Linux (Ubuntu/Debian):**parser.export_results('output.json', format='json')

```bash```

sudo apt-get install python3-tk

```## Tips



### "File not found" or "Permission denied"1. **Large Files**: The parser handles large XML files efficiently by streaming

- Ensure the log file path doesn't contain special characters2. **Custom Keywords**: Add domain-specific terms to your filter list

- Use forward slashes `/` or double backslashes `\\` in paths3. **Export Before Closing**: Always export results before closing the GUI

- Run as administrator if accessing protected folders4. **Multiple Runs**: You can parse multiple files in the same session

5. **NRC Reference**: Use the NRC Decoder tab as a quick reference guide

### Application freezes during analysis

- Log files >50MB may take 1-2 minutes to process## Troubleshooting

- Check terminal/console for progress messages

- For very large logs (>100MB), consider splitting into smaller files### Issue: "XML Parse Error"

- Ensure your XML file is well-formed

### Report shows "Unknown" or empty sections- Check for proper opening/closing tags

- Ensure log file is from FDRS/IDS (not generic OBD logs)

- Check that log contains diagnostic frames (look for hex patterns like "22 F1 88")### Issue: "No matches found"

- Some fields may be empty for bench sessions (e.g., battery voltage)- Verify your filter keywords match content in the XML

- Try broader keywords like "test" or "response"

### No timeline events showing- Check if your XML uses different capitalization

- Timeline extracts events from FDRS-specific log patterns

- Ensure log includes timestamps (HH:MM:SS format)### Issue: GUI doesn't open

- May show "Critical events timeline not available" for non-standard logs- Ensure tkinter is installed: `python -m tkinter`

- On Linux, you may need: `sudo apt-get install python3-tk`

## 🎓 For New Users (Learning Mode)

## License

If you're new to automotive diagnostics:

This is a utility tool provided as-is for log analysis purposes.

1. **Start with the Training Snapshot** - Learn common hex patterns first

2. **Read the "Why this matters" call-outs** - Understand each finding's significance## Support

3. **Study the failure signatures** - Learn to spot patterns in future logs

4. **Click DTC links** - Explore Ford Service Info for detailed repair proceduresFor issues or questions:

1. Check the sample_log.xml for expected format

The tool is designed to **teach while you work**. Each report includes:2. Verify Python version compatibility

- Plain-English explanations of technical terms3. Review the output for parsing errors

- Real examples from your actual log
- Pattern recognition training for faster future diagnosis
- Rotating tips (different examples each time)

## 📊 Report Sections Explained

### Executive Summary (Top Box)
- **Status**: FAILED/SUCCESS/INCOMPLETE
- **Success Rate**: Percentage of successful diagnostic frames
- **Unique Errors**: Count after deduplication
- **Warnings**: Non-critical issues detected

### Root Cause Analysis (if flash failed)
- **Session Goal**: What the session was trying to accomplish
- **Key Findings**: Top 3-5 critical issues
- **Software Mismatch Table**: DIDs requiring update
- **Recommended Action**: Step-by-step fix instructions

### Active DTCs
- Lists all Diagnostic Trouble Codes found
- Click 🔗 to open Ford Service Info (if available)
- Click 📊 to view freeze-frame data
- Includes "why it matters" explanations for common codes

### Error Buckets
- **NRC-31**: Normal diagnostic noise (explained why)
- **Java Exceptions**: Parser bugs triggered by NRC-31 (not ECU faults)
- **XML Errors**: Backend logging issues (not ECU problems)
- **Top DIDs**: Shows which DIDs caused most NRC-31 responses

### Config & Flash
- Files calculated vs. flashed
- USB vs. CAN flash method
- Configuration operations performed
- Estimated time for re-flash

### Critical Timeline
- Shows first 5-8 significant events with real timestamps
- Groups repetitive events with counts
- Links to raw log explorer for full details

## 🔒 Privacy & Security

- **100% Local Processing** - No internet connection required
- **No Data Uploaded** - All logs stay on your machine
- **No Telemetry** - Tool doesn't send usage data anywhere
- **No External Dependencies** - Only uses Python standard library

## 💡 Tips & Best Practices

### For Faster Analysis
1. Close other memory-intensive applications
2. Use log files <50MB when possible (split larger files)
3. Keep the tool on an SSD for better performance

### For Better Results
1. Include full session logs (start to finish)
2. Ensure timestamps are present in logs
3. Don't edit/trim log files manually (may break parsing)

### For Learning
1. Run the tool on multiple logs to see different failure patterns
2. Compare successful vs. failed flash sessions side-by-side
3. Use the Training Snapshot as a quick reference card
4. Export reports for team training sessions

## 📞 Support & Feedback

For issues or questions:

1. **Check Troubleshooting** section above first
2. **Review the sample log** (`test4.txt`) to verify tool is working
3. **Collect debug info**:
   - Python version: `python --version`
   - Operating system (Windows 10/11, etc.)
   - Error message from terminal/console
   - Log file size and source (FDRS version if known)

## 📝 Version History

### v1.0 (October 2025)
- ✅ Initial release with comprehensive analysis
- ✅ Root cause detection for flash failures
- ✅ Software mismatch table with deduplication
- ✅ Educational training snapshot with hex decoder
- ✅ DTC analysis with Service Info integration
- ✅ Critical timeline with real timestamps
- ✅ NRC-31 noise suppression and explanation
- ✅ Unified counter calculations (no disagreements)
- ✅ Inline "Why this matters" teaching moments
- ✅ Failure signature pattern recognition guide

## 🚗 Supported Use Cases

- **Flash Failures**: Why PMI didn't complete
- **Software Mismatches**: Which modules need updating
- **DTC Diagnostics**: Active fault code analysis
- **Communication Errors**: CAN bus/protocol issues
- **Training**: Learning diagnostic patterns and hex decoding
- **Audit Logs**: Post-repair verification
- **Troubleshooting**: Root cause for intermittent issues

## 🏆 What Makes This Tool Different

1. **Dual Purpose**: Expert diagnosis + Built-in training
2. **Smart Deduplication**: Filters noise, highlights signal
3. **Real Examples**: Teaches with actual data from your logs
4. **Plain English**: Technical accuracy without jargon overload
5. **Actionable**: Specific fix recommendations, not just problem lists
6. **Self-Contained**: No external dependencies or internet required

---

**Ready to analyze?** 

```powershell
python professional_diagnostic_analyzer.py
```

Then click **📂 Browse**, select your log, and click **🔍 Analyze**!

---

*Built for Ford technicians who need both quick answers and continuous learning tools.*
