"""
Professional Setup and Installation Script
Sets up the professional-grade diagnostic analyzer environment
"""

import os
import sys
import subprocess
import json
import shutil
from pathlib import Path
import logging
from datetime import datetime


class ProfessionalSetup:
    """Professional setup and installation manager"""
    
    def __init__(self):
        self.setup_dir = Path.cwd()
        self.config_dir = self.setup_dir / "config"
        self.logs_dir = self.setup_dir / "logs"
        self.reports_dir = self.setup_dir / "reports"
        self.templates_dir = self.setup_dir / "templates"
        self.data_dir = self.setup_dir / "data"
        
        # Setup logging
        self._setup_logging()
        self.logger = logging.getLogger(__name__)
    
    def _setup_logging(self):
        """Setup logging for installation"""
        os.makedirs("logs", exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(f'logs/setup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
    
    def run_full_setup(self):
        """Run complete professional setup"""
        print("🚗 Professional Automotive Diagnostic Analyzer Setup")
        print("=" * 60)
        
        try:
            self.logger.info("Starting professional setup")
            
            # Step 1: Check system requirements
            print("\n📋 Step 1: Checking System Requirements...")
            self._check_system_requirements()
            
            # Step 2: Create directory structure
            print("\n📁 Step 2: Creating Directory Structure...")
            self._create_directory_structure()
            
            # Step 3: Install dependencies
            print("\n📦 Step 3: Installing Dependencies...")
            self._install_dependencies()
            
            # Step 4: Initialize configuration
            print("\n⚙️ Step 4: Initializing Configuration...")
            self._initialize_configuration()
            
            # Step 5: Create sample data
            print("\n🧪 Step 5: Creating Sample Data...")
            self._create_sample_data()
            
            # Step 6: Setup templates
            print("\n📄 Step 6: Setting Up Templates...")
            self._setup_templates()
            
            # Step 7: Create desktop shortcuts
            print("\n🔗 Step 7: Creating Shortcuts...")
            self._create_shortcuts()
            
            # Step 8: Run initial tests
            print("\n🧪 Step 8: Running Initial Tests...")
            self._run_initial_tests()
            
            print("\n✅ Professional Setup Complete!")
            print("\n🎉 Your Professional Automotive Diagnostic Analyzer is ready!")
            print(f"📁 Installation Directory: {self.setup_dir.absolute()}")
            print(f"📊 Launch Application: python professional_diagnostic_analyzer.py")
            print(f"📚 Documentation: {self.setup_dir / 'docs' / 'user_guide.html'}")
            
        except Exception as e:
            self.logger.error(f"Setup failed: {e}")
            print(f"\n❌ Setup failed: {e}")
            print("Check the log file for detailed error information.")
            sys.exit(1)
    
    def _check_system_requirements(self):
        """Check system requirements"""
        requirements = {
            "python_version": (3, 8),
            "required_modules": ["tkinter", "sqlite3", "json", "threading"],
            "recommended_modules": ["matplotlib", "pandas", "numpy"],
            "disk_space_mb": 500,
            "memory_mb": 1024
        }
        
        # Check Python version
        python_version = sys.version_info[:2]
        if python_version < requirements["python_version"]:
            raise Exception(f"Python {requirements['python_version'][0]}.{requirements['python_version'][1]}+ required, found {python_version[0]}.{python_version[1]}")
        
        print(f"  ✅ Python {python_version[0]}.{python_version[1]} - OK")
        
        # Check required modules
        missing_modules = []
        for module in requirements["required_modules"]:
            try:
                __import__(module)
                print(f"  ✅ {module} - OK")
            except ImportError:
                missing_modules.append(module)
                print(f"  ❌ {module} - Missing")
        
        if missing_modules:
            raise Exception(f"Missing required modules: {', '.join(missing_modules)}")
        
        # Check recommended modules
        for module in requirements["recommended_modules"]:
            try:
                __import__(module)
                print(f"  ✅ {module} - OK (recommended)")
            except ImportError:
                print(f"  ⚠️ {module} - Missing (recommended for advanced features)")
        
        # Check disk space (simplified)
        try:
            free_space = shutil.disk_usage(self.setup_dir).free / (1024 * 1024)
            if free_space < requirements["disk_space_mb"]:
                print(f"  ⚠️ Disk space: {free_space:.0f}MB available, {requirements['disk_space_mb']}MB recommended")
            else:
                print(f"  ✅ Disk space: {free_space:.0f}MB available - OK")
        except:
            print("  ⚠️ Could not check disk space")
        
        self.logger.info("System requirements check completed")
    
    def _create_directory_structure(self):
        """Create professional directory structure"""
        directories = [
            self.config_dir,
            self.logs_dir,
            self.reports_dir,
            self.templates_dir,
            self.data_dir,
            self.setup_dir / "docs",
            self.setup_dir / "scripts",
            self.setup_dir / "backup",
            self.setup_dir / "plugins",
            self.reports_dir / "batch",
            self.reports_dir / "exports",
            self.data_dir / "samples",
            self.data_dir / "test_data",
            self.templates_dir / "reports",
            self.templates_dir / "configs"
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
            print(f"  📁 Created: {directory.name}/")
        
        self.logger.info("Directory structure created")
    
    def _install_dependencies(self):
        """Install Python dependencies"""
        
        # Core requirements
        core_requirements = [
            "requests>=2.25.0",
            "python-dateutil>=2.8.0",
            "Pillow>=8.0.0",
        ]
        
        # Optional requirements for advanced features
        optional_requirements = [
            "matplotlib>=3.3.0",
            "pandas>=1.2.0",
            "numpy>=1.19.0",
            "openpyxl>=3.0.0",
            "reportlab>=3.5.0",
            "lxml>=4.6.0"
        ]
        
        print("  Installing core dependencies...")
        for requirement in core_requirements:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", requirement], 
                                    capture_output=True, text=True)
                print(f"    ✅ Installed: {requirement}")
            except subprocess.CalledProcessError as e:
                print(f"    ⚠️ Failed to install: {requirement}")
                self.logger.warning(f"Failed to install {requirement}: {e}")
        
        print("  Installing optional dependencies...")
        for requirement in optional_requirements:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", requirement], 
                                    capture_output=True, text=True)
                print(f"    ✅ Installed: {requirement}")
            except subprocess.CalledProcessError as e:
                print(f"    ⚠️ Optional: {requirement} (install manually for advanced features)")
                self.logger.warning(f"Optional dependency not installed {requirement}: {e}")
        
        self.logger.info("Dependencies installation completed")
    
    def _initialize_configuration(self):
        """Initialize professional configuration files"""
        
        # Main application config
        app_config = {
            "version": "2.1.0",
            "installation_date": datetime.now().isoformat(),
            "features": {
                "batch_processing": True,
                "advanced_reporting": True,
                "real_time_monitoring": True,
                "api_access": True,
                "plugin_system": True
            },
            "security": {
                "audit_enabled": True,
                "secure_logs": True,
                "user_authentication": False,  # Can be enabled later
                "encryption_enabled": False
            },
            "performance": {
                "max_worker_threads": 4,
                "cache_size_mb": 256,
                "auto_cleanup_days": 30,
                "backup_retention_days": 90
            }
        }
        
        with open(self.config_dir / "app_config.json", 'w') as f:
            json.dump(app_config, f, indent=2)
        
        # Database configuration
        db_config = {
            "engine": "sqlite",
            "connection": {
                "database": "diagnostic_analyzer.db",
                "timeout": 30,
                "journal_mode": "WAL",
                "synchronous": "NORMAL"
            },
            "backup": {
                "auto_backup": True,
                "backup_interval_hours": 24,
                "max_backups": 7
            }
        }
        
        with open(self.config_dir / "database.json", 'w') as f:
            json.dump(db_config, f, indent=2)
        
        # Logging configuration
        logging_config = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {
                    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                },
                "detailed": {
                    "format": "%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s"
                }
            },
            "handlers": {
                "file": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "filename": "logs/diagnostic_analyzer.log",
                    "maxBytes": 10485760,
                    "backupCount": 5,
                    "formatter": "detailed"
                },
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "standard"
                }
            },
            "loggers": {
                "": {
                    "handlers": ["file", "console"],
                    "level": "INFO",
                    "propagate": False
                }
            }
        }
        
        with open(self.config_dir / "logging.json", 'w') as f:
            json.dump(logging_config, f, indent=2)
        
        print("  ✅ Configuration files created")
        self.logger.info("Configuration initialized")
    
    def _create_sample_data(self):
        """Create sample data for testing and demonstration"""
        
        # Create sample XML log
        sample_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<DiagnosticSession>
    <SessionInfo>
        <Date>2025-10-16T14:30:00</Date>
        <Vehicle>
            <Make>Ford</Make>
            <Model>F-150</Model>
            <Year>2023</Year>
            <VIN>1FTFW1E50PFC12345</VIN>
        </Vehicle>
    </SessionInfo>
    <Communications>
        <Message>
            <Timestamp>14:30:01.123</Timestamp>
            <Direction>Request</Direction>
            <ECU>PCM</ECU>
            <Data>10 03</Data>
            <Description>Diagnostic Session Control</Description>
        </Message>
        <Message>
            <Timestamp>14:30:01.145</Timestamp>
            <Direction>Response</Direction>
            <ECU>PCM</ECU>
            <Data>50 03</Data>
            <Description>Positive Response</Description>
        </Message>
        <Message>
            <Timestamp>14:30:02.001</Timestamp>
            <Direction>Request</Direction>
            <ECU>ABS</ECU>
            <Data>22 F1 90</Data>
            <Description>Read DID - VIN</Description>
        </Message>
        <Message>
            <Timestamp>14:30:02.025</Timestamp>
            <Direction>Response</Direction>
            <ECU>ABS</ECU>
            <Data>7F 22 31</Data>
            <Description>Negative Response - Request Out of Range</Description>
        </Message>
    </Communications>
</DiagnosticSession>'''
        
        with open(self.data_dir / "samples" / "sample_diagnostic_log.xml", 'w') as f:
            f.write(sample_xml)
        
        # Create sample text log
        sample_text = '''[2025-10-16 14:30:00.123] INFO: Starting diagnostic session
[2025-10-16 14:30:00.124] INFO: Connected to vehicle PCM
[2025-10-16 14:30:01.100] DEBUG: TX: 10 03 (Diagnostic Session Control)
[2025-10-16 14:30:01.120] DEBUG: RX: 50 03 (Positive Response)
[2025-10-16 14:30:01.500] ERROR: Communication timeout with BCM
[2025-10-16 14:30:02.000] DEBUG: TX: 22 F1 90 (Read VIN)
[2025-10-16 14:30:02.020] DEBUG: RX: 62 F1 90 31 46 54 46 57 31 45 35 30 50 46 43 31 32 33 34 35
[2025-10-16 14:30:03.000] WARN: DTC P0300 detected in engine module
[2025-10-16 14:30:03.100] INFO: Diagnostic session completed successfully'''
        
        with open(self.data_dir / "samples" / "sample_diagnostic_log.txt", 'w') as f:
            f.write(sample_text)
        
        # Create test configuration
        test_config = {
            "test_files": [
                "sample_diagnostic_log.xml",
                "sample_diagnostic_log.txt"
            ],
            "expected_results": {
                "error_count": 2,
                "warning_count": 1,
                "success_count": 3,
                "ecu_count": 3
            }
        }
        
        with open(self.data_dir / "test_data" / "test_config.json", 'w') as f:
            json.dump(test_config, f, indent=2)
        
        print("  ✅ Sample data created")
        self.logger.info("Sample data created")
    
    def _setup_templates(self):
        """Setup report and configuration templates"""
        
        # Create HTML report template
        html_template = '''<!DOCTYPE html>
<html>
<head>
    <title>Diagnostic Report Template</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .header { background: #1f4e79; color: white; padding: 20px; border-radius: 8px; }
        .section { margin: 20px 0; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }
        .error { color: #d32f2f; }
        .warning { color: #f57c00; }
        .success { color: #388e3c; }
    </style>
</head>
<body>
    <div class="header">
        <h1>Professional Diagnostic Report</h1>
        <p>Generated: {{timestamp}}</p>
    </div>
    
    <div class="section">
        <h2>Executive Summary</h2>
        <p>{{summary}}</p>
    </div>
    
    <div class="section">
        <h2>Analysis Results</h2>
        {{results}}
    </div>
</body>
</html>'''
        
        with open(self.templates_dir / "reports" / "standard_report.html", 'w') as f:
            f.write(html_template)
        
        # Create batch job template
        batch_template = {
            "name": "Standard Analysis",
            "description": "Standard diagnostic analysis template",
            "analysis_profile": "comprehensive",
            "output_format": "html",
            "filters": ["error", "warning", "success", "NRC", "DTC"],
            "options": {
                "include_timestamps": True,
                "include_hex_analysis": True,
                "include_statistics": True,
                "max_results": 10000
            }
        }
        
        with open(self.templates_dir / "configs" / "batch_template.json", 'w') as f:
            json.dump(batch_template, f, indent=2)
        
        print("  ✅ Templates created")
        self.logger.info("Templates setup completed")
    
    def _create_shortcuts(self):
        """Create desktop shortcuts and start menu entries"""
        
        # Create batch file for Windows
        if sys.platform == "win32":
            batch_content = f'''@echo off
cd /d "{self.setup_dir}"
python professional_diagnostic_analyzer.py
pause'''
            
            with open(self.setup_dir / "Launch_Professional_Analyzer.bat", 'w') as f:
                f.write(batch_content)
            
            print("  ✅ Windows batch file created")
        
        # Create shell script for Unix/Linux
        else:
            script_content = f'''#!/bin/bash
cd "{self.setup_dir}"
python3 professional_diagnostic_analyzer.py'''
            
            script_path = self.setup_dir / "launch_analyzer.sh"
            with open(script_path, 'w') as f:
                f.write(script_content)
            
            # Make executable
            os.chmod(script_path, 0o755)
            print("  ✅ Unix shell script created")
        
        self.logger.info("Shortcuts created")
    
    def _run_initial_tests(self):
        """Run initial system tests"""
        print("  Running import tests...")
        
        # Test core imports
        try:
            import tkinter
            print("    ✅ GUI framework - OK")
        except ImportError:
            print("    ❌ GUI framework - Failed")
        
        try:
            import sqlite3
            print("    ✅ Database engine - OK")
        except ImportError:
            print("    ❌ Database engine - Failed")
        
        # Test file access
        try:
            test_file = self.data_dir / "test_write.tmp"
            with open(test_file, 'w') as f:
                f.write("test")
            os.remove(test_file)
            print("    ✅ File system access - OK")
        except Exception:
            print("    ❌ File system access - Failed")
        
        # Test sample data
        sample_xml = self.data_dir / "samples" / "sample_diagnostic_log.xml"
        if sample_xml.exists():
            print("    ✅ Sample data - OK")
        else:
            print("    ❌ Sample data - Missing")
        
        print("  ✅ Initial tests completed")
        self.logger.info("Initial tests completed")
    
    def create_user_documentation(self):
        """Create comprehensive user documentation"""
        
        docs_dir = self.setup_dir / "docs"
        docs_dir.mkdir(exist_ok=True)
        
        # Create user guide
        user_guide = '''# Professional Automotive Diagnostic Analyzer - User Guide

## Quick Start

1. **Launch the Application**
   - Windows: Double-click `Launch_Professional_Analyzer.bat`
   - Linux/Mac: Run `./launch_analyzer.sh` or `python3 professional_diagnostic_analyzer.py`

2. **Load a Log File**
   - Click "Browse..." to select a diagnostic log file
   - Supported formats: XML, TXT, LOG, FDRS
   - Sample files are available in the `data/samples/` directory

3. **Choose Analysis Mode**
   - **Basic**: Quick overview for routine checks
   - **Comprehensive**: Full analysis with learning features
   - **Expert**: Deep forensic analysis for troubleshooting

4. **Run Analysis**
   - Click the "Analyze" button or press F5
   - Results will appear in multiple tabs

## Features

### Analysis Modes
- **Basic Analysis**: Error detection and basic statistics
- **Comprehensive Analysis**: Full ECU analysis with educational content
- **Expert Mode**: Forensic-level analysis with timeline and patterns

### Batch Processing
- Process multiple files automatically
- Schedule recurring analysis tasks
- Export batch results and summaries

### Professional Reporting
- HTML reports with professional formatting
- Executive summaries for management
- Technical details for engineers
- Export to multiple formats (HTML, JSON, XML, CSV)

### ECU Database
- Comprehensive Ford ECU module database
- Real-time ECU communication analysis
- Error pattern recognition

## Troubleshooting

### Common Issues
1. **"No File" Error**: Ensure file exists and is readable
2. **Import Errors**: Check Python dependencies
3. **Performance Issues**: Reduce max results in settings

### Support
- Check log files in `logs/` directory
- Review configuration in `config/` directory
- Sample data available in `data/samples/`

## Configuration

Configuration files are located in the `config/` directory:
- `app_config.json`: Main application settings
- `database.json`: Database configuration
- `logging.json`: Logging configuration

## Advanced Features

### API Access
The application includes REST API endpoints for integration with other systems.

### Plugin System
Custom plugins can be added to extend functionality.

### Real-time Monitoring
Monitor diagnostic sessions in real-time with automatic alerts.

---

© 2025 Professional Automotive Diagnostic Analyzer
Version 2.1.0
'''
        
        with open(docs_dir / "user_guide.md", 'w') as f:
            f.write(user_guide)
        
        # Create HTML version
        html_guide = f'''<!DOCTYPE html>
<html>
<head>
    <title>Professional Diagnostic Analyzer - User Guide</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
        h1, h2, h3 {{ color: #1f4e79; }}
        code {{ background: #f5f5f5; padding: 2px 5px; border-radius: 3px; }}
        pre {{ background: #f5f5f5; padding: 10px; border-radius: 5px; overflow-x: auto; }}
    </style>
</head>
<body>
{user_guide.replace("#", "<h1>").replace("##", "</h1><h2>").replace("###", "</h2><h3>")}
</body>
</html>'''
        
        with open(docs_dir / "user_guide.html", 'w') as f:
            f.write(html_guide)
        
        print("  ✅ User documentation created")
        self.logger.info("User documentation created")


def main():
    """Main setup function"""
    print("Starting Professional Automotive Diagnostic Analyzer Setup...")
    
    try:
        setup = ProfessionalSetup()
        setup.run_full_setup()
        setup.create_user_documentation()
        
        print("\n" + "="*60)
        print("🎉 SETUP COMPLETE!")
        print("="*60)
        print("Your Professional Automotive Diagnostic Analyzer is now ready to use.")
        print("\nNext steps:")
        print("1. Launch the application using the created shortcut")
        print("2. Try analyzing the sample files in data/samples/")
        print("3. Review the user guide in docs/user_guide.html")
        print("4. Configure settings in the config/ directory as needed")
        
    except KeyboardInterrupt:
        print("\n\nSetup interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nSetup failed with error: {e}")
        print("Please check the log files for more details.")
        sys.exit(1)


if __name__ == "__main__":
    main()