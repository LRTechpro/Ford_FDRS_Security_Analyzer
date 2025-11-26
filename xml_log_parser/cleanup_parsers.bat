@echo off
REM Remove redundant GUI parser files - Keep only Professional Diagnostic Analyzer

cd /d "c:\Users\HWATKI16\Downloads\xml_log_parser"

echo Removing redundant GUI parser files...

if exist gui_app.py (
    del /f gui_app.py
    echo Removed gui_app.py
)

if exist gui_app_enhanced.py (
    del /f gui_app_enhanced.py  
    echo Removed gui_app_enhanced.py
)

if exist gui_app_enhanced_clean.py (
    del /f gui_app_enhanced_clean.py
    echo Removed gui_app_enhanced_clean.py
)

if exist gui_app_enhanced_corrupted_backup.py (
    del /f gui_app_enhanced_corrupted_backup.py
    echo Removed gui_app_enhanced_corrupted_backup.py
)

echo.
echo ✅ Cleanup complete!
echo.
echo Your main application is: professional_diagnostic_analyzer.py
echo Launch with: python professional_diagnostic_analyzer.py
echo Or use: Launch_Professional_Analyzer.bat
echo.
pause