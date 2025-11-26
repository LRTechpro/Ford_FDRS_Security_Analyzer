@echo off
REM Enhanced Log Parser Launcher - Version 2.0
REM Runs the enhanced GUI with all new features

echo.
echo ========================================
echo   Log Parser Pro - Enhanced Edition
echo   Version 2.0
echo ========================================
echo.
echo Starting enhanced GUI with all features:
echo   - Dark Mode Support
echo   - Keyboard Shortcuts
echo   - Drag and Drop
echo   - Analytics Charts
echo   - Log Comparison
echo   - Database History
echo.

python gui_app_enhanced.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Failed to start enhanced GUI
    echo.
    echo Possible issues:
    echo   1. Python not installed or not in PATH
    echo   2. Missing optional dependencies
    echo.
    echo To install optional features:
    echo   pip install matplotlib tkinterdnd2
    echo.
    echo Note: The app works without these, but some features are disabled.
    echo.
    pause
)
