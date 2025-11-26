@echo off
REM Log Parser Pro - GUI Launcher
REM This script ensures the GUI starts from the correct directory

cd /d "%~dp0"
echo Starting Log Parser Pro from: %CD%
echo.

python gui_app_enhanced.py

if errorlevel 1 (
    echo.
    echo ERROR: Failed to start the GUI
    echo.
    echo Possible issues:
    echo 1. Python not installed or not in PATH
    echo 2. Missing dependencies
    echo.
    echo To fix, run: pip install matplotlib tkinterdnd2
    echo.
    pause
)
