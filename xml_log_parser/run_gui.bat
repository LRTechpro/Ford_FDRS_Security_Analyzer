@echo off
REM Quick Start Script for XML Log Parser GUI
REM This script launches the GUI application

echo =====================================
echo   XML Log Parser - GUI Launcher
echo =====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7 or higher from https://www.python.org/
    pause
    exit /b 1
)

echo Starting XML Log Parser GUI...
echo.

REM Launch the GUI application
python gui_app.py

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Failed to start the application
    echo Please check if all files are present
    pause
)
