# Ford FDRS Security Analyzer

**Professional automotive cybersecurity diagnostic tool for Ford vehicles**

A comprehensive security and diagnostic analysis platform designed specifically for Ford diagnostic logs. This tool combines advanced security threat detection, ECU analysis, and intelligent diagnostics to provide professional-grade automotive cybersecurity assessments.

## 🔐 Key Features

### Security Analysis
- **Cybersecurity Scanning** - Detect unauthorized access attempts, protocol anomalies, and security bypass attempts
- **Threat Assessment** - Comprehensive risk evaluation and attack vector identification
- **Protocol Analysis** - Deep inspection of CAN, UDS, and other automotive protocols
- **Vulnerability Detection** - Identify security vulnerabilities and weaknesses in diagnostic logs

### Diagnostic Capabilities
- **Multi-Format Support** - Analyze XML logs, text logs, FDRS output, and raw diagnostic data
- **ECU Analysis** - Detailed module communication analysis with status tracking
- **Error Detection** - NRC codes, DTC errors, and diagnostic failure analysis
- **Timeline Correlation** - Event sequence analysis and temporal relationships

### Advanced Features
- **Cross-Report Correlation** - Compare multiple diagnostic reports for pattern analysis
- **Intelligent Analysis Engine** - AI-powered diagnostic recommendations
- **Professional Reporting** - Generate detailed security and diagnostic reports
- **Batch Processing** - Analyze multiple files simultaneously
- **Dark Mode & Themes** - Customizable interface for extended work sessions

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- tkinter (usually included with Python)
- Required packages (see requirements.txt)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/lrtecpro/Ford_FDRS_Security_Analyzer.git
cd Ford_FDRS_Security_Analyzer
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python professional_diagnostic_analyzer.py
```

## 📖 Usage

### Basic Analysis
1. Open the application
2. Click "Browse..." to select your Ford diagnostic log file
3. Choose analysis mode (Basic, Comprehensive, Expert, or Cross-Correlation)
4. Click "Analyze" to begin the analysis
5. Review results in the Analysis Results tab

### Security Analysis
1. Load a diagnostic log file
2. Navigate to the "Cybersecurity" tab
3. Click "Run Security Scan" to detect threats
4. Review security findings and recommendations

### Multi-Report Correlation
1. Load your primary diagnostic log
2. Add additional reports in the "Additional Reports" section
3. Click "Correlate All Reports" to cross-analyze
4. View correlation results and common patterns

## 📊 Analysis Tabs

- **Analysis Results** - Primary diagnostic findings and raw analysis output
- **ECU Analysis** - Module-by-module communication and status breakdown
- **Error Analysis** - Detailed error code analysis and explanations
- **Timeline** - Event sequence and temporal analysis
- **Statistics** - Metrics and summary statistics
- **Cybersecurity** - Security threat analysis and vulnerability assessment
- **Intelligent Analysis** - AI-powered diagnostic conclusions (requires API key)

## 🔧 Configuration

### API Keys (Optional)
To enable AI-powered features, configure your OpenAI API key:

1. Create a `config.local.json` file in the project root
2. Add your API key:
```json
{
  "openai_api_key": "your-api-key-here"
}
```

### Settings
Application settings are auto-saved to `analyzer_settings.json` and include:
- Window size and position
- Font preferences
- Recent files
- Analysis preferences
- Display options

## 📁 Project Structure

```
Ford_FDRS_Security_Analyzer/
├── professional_diagnostic_analyzer.py    # Main application
├── requirements.txt                       # Python dependencies
├── config_manager.py                      # Configuration handling
├── database_manager.py                    # Data management
├── enhanced_uds_parser.py                 # UDS protocol parsing
├── ecu_reference.py                       # ECU database
├── critical_diagnostic_view.py            # Critical diagnostics view
└── xml_log_parser/                        # Core parsing modules
    ├── xml_log_parser.py                  # XML log parsing
    ├── text_log_parser.py                 # Text log parsing
    ├── intelligent_diagnostic_engine.py   # AI diagnostics
    ├── ai_diagnostic_assistant.py         # AI assistant
    ├── cybersecurity_analyzer.py          # Security analysis
    └── [100+ supporting modules]
```

## 🛠️ Supported Log Formats

- **XML Logs** - Standard Ford FDRS XML format
- **Text Logs** - Plain text diagnostic output
- **FDRS Output** - Native Ford diagnostic tool output
- **Session Logs** - ECU communication sessions
- **Security Logs** - Access and authentication logs
- **CSV/JSON** - Structured data formats

## 🔍 Diagnostic Codes Supported

### NRC Codes
- **NRC 0x22** - Conditions Not Correct (Vehicle Condition Issues)
- **NRC 0x7F** - Service Not Supported (Session Management)
- **NRC 0x31** - Request Out of Range
- **NRC 0x33** - Security Access Denied
- And 50+ more NRC codes with detailed explanations

### DTC Categories
- Powertrain (P-codes)
- Chassis (C-codes)
- Body (B-codes)
- Network (U-codes)

## 📚 Documentation

- **QUICKSTART.md** - Quick start guide
- **INSTALL_CHECKLIST.md** - Installation verification
- **xml_log_parser/README.md** - Detailed module documentation
- **xml_log_parser/CYBERSECURITY_GUIDE.md** - Security features guide

## 🔐 Security Features

### Threat Detection
- Unauthorized diagnostic access attempts
- Anomalous protocol behavior
- Security bypass attempts
- Authentication failures
- Network spoofing indicators
- ECU flash security violations

### Compliance Analysis
- Security standard compliance
- Best practice verification
- Risk scoring
- Remediation recommendations

## 🤖 AI Features (Optional)

When configured with an OpenAI API key, the tool provides:
- Intelligent diagnostic conclusions
- Root cause analysis
- Repair recommendations
- Pattern learning and prediction

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl+O | Open log file |
| Ctrl+S | Save analysis |
| F5 | Run analysis |
| Ctrl+A | Select all text |
| Ctrl+C | Copy selection |
| Ctrl+H | Explain hex data |
| Ctrl+F | Find in results |
| Ctrl++ | Zoom in |
| Ctrl+- | Zoom out |
| Ctrl+0 | Reset zoom |

## 📊 System Requirements

- **OS**: Windows, macOS, Linux
- **Python**: 3.8 or higher
- **RAM**: Minimum 4GB recommended
- **Disk**: 500MB for application and dependencies
- **Display**: 1280x800 minimum resolution

## 🐛 Troubleshooting

### GUI Won't Start
```bash
python -m tkinter  # Test tkinter installation
```

### Import Errors
```bash
pip install -r requirements.txt --upgrade
```

### Performance Issues
- Try "Basic Analysis" mode for large files
- Close other applications to free up RAM
- Check that antivirus isn't interfering with file access

## 📝 License

This project is provided as-is for automotive diagnostic and security research purposes.

## 👨‍💻 Author

**lrtecpro** - Professional automotive cybersecurity specialist

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📞 Support

For issues, feature requests, or questions:
1. Check existing issues in the repository
2. Create a detailed bug report or feature request
3. Contact the maintainer

## 🌟 Features Roadmap

- [ ] Real-time CAN bus monitoring
- [ ] Cloud-based log analysis
- [ ] Mobile app interface
- [ ] Advanced machine learning threat detection
- [ ] ISO 26262 compliance checking
- [ ] Automated report generation for dealers

---

**Version**: 2.1.0  
**Last Updated**: November 2025  
**Status**: Production Ready

For the latest updates and documentation, visit: https://github.com/lrtecpro/Ford_FDRS_Security_Analyzer
