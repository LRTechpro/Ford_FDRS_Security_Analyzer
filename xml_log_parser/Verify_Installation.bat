@echo off
REM System Verification Script
REM Checks all components are properly installed and configured

title Professional Diagnostic Analyzer - System Verification

echo.
echo ================================================================================
echo   Professional Diagnostic Analyzer - System Verification
echo ================================================================================
echo.

set PYTHON_PATH=C:\Users\HWATKI16\AppData\Local\Python\pythoncore-3.14-64\python.exe
set ERRORS=0

echo [1/6] Checking Python installation...
"%PYTHON_PATH%" --version >nul 2>&1
if errorlevel 1 (
    echo     [FAIL] Python not found at expected location
    set /a ERRORS+=1
) else (
    for /f "tokens=*" %%i in ('"%PYTHON_PATH%" --version') do echo     [PASS] %%i
)
echo.

echo [2/6] Checking core packages...
"%PYTHON_PATH%" -c "import tkinter; print('     [PASS] tkinter available')" 2>nul
if errorlevel 1 (
    echo     [FAIL] tkinter not available
    set /a ERRORS+=1
)

"%PYTHON_PATH%" -c "import lxml; print('     [PASS] lxml available')" 2>nul
if errorlevel 1 (
    echo     [WARN] lxml not installed
)

"%PYTHON_PATH%" -c "import requests; print('     [PASS] requests available')" 2>nul
if errorlevel 1 (
    echo     [WARN] requests not installed
)
echo.

echo [3/6] Checking OpenAI installation...
"%PYTHON_PATH%" -c "import openai; print('     [PASS] OpenAI', openai.__version__)" 2>nul
if errorlevel 1 (
    echo     [FAIL] OpenAI package not installed
    set /a ERRORS+=1
)
echo.

echo [4/6] Checking application modules...
"%PYTHON_PATH%" -c "import professional_diagnostic_analyzer; print('     [PASS] Main application module')" 2>nul
if errorlevel 1 (
    echo     [FAIL] professional_diagnostic_analyzer.py not found or has errors
    set /a ERRORS+=1
)

"%PYTHON_PATH%" -c "import ai_diagnostic_assistant; print('     [PASS] AI assistant module')" 2>nul
if errorlevel 1 (
    echo     [FAIL] ai_diagnostic_assistant.py not found or has errors
    set /a ERRORS+=1
)

"%PYTHON_PATH%" -c "import intelligent_diagnostic_engine; print('     [PASS] Intelligent analysis module')" 2>nul
if errorlevel 1 (
    echo     [FAIL] intelligent_diagnostic_engine.py not found or has errors
    set /a ERRORS+=1
)
echo.

echo [5/6] Checking required files...
if exist "professional_diagnostic_analyzer.py" (
    echo     [PASS] professional_diagnostic_analyzer.py
) else (
    echo     [FAIL] professional_diagnostic_analyzer.py not found
    set /a ERRORS+=1
)

if exist "requirements_professional.txt" (
    echo     [PASS] requirements_professional.txt
) else (
    echo     [WARN] requirements_professional.txt not found
)

if exist "README_PROFESSIONAL.md" (
    echo     [PASS] README_PROFESSIONAL.md
) else (
    echo     [WARN] README_PROFESSIONAL.md not found
)
echo.

echo [6/6] Checking sample files...
if exist "sample_system_log.log" (
    echo     [PASS] sample_system_log.log
) else (
    echo     [INFO] sample_system_log.log not found
)

if exist "sample_health_report.txt" (
    echo     [PASS] sample_health_report.txt
) else (
    echo     [INFO] sample_health_report.txt not found
)
echo.

echo ================================================================================
echo   Verification Summary
echo ================================================================================
echo.

if %ERRORS%==0 (
    echo     STATUS: [PASS] All critical components verified
    echo.
    echo     Your system is ready to run the Professional Diagnostic Analyzer!
    echo.
    echo     To launch the application:
    echo       - Double-click: Launch_Professional_Analyzer.bat
    echo       - Or run: python professional_diagnostic_analyzer.py
    echo.
) else (
    echo     STATUS: [FAIL] %ERRORS% critical error(s) detected
    echo.
    echo     Please address the failures above before running the application.
    echo.
    echo     To install missing packages:
    echo       python -m pip install -r requirements_professional.txt
    echo.
)

echo ================================================================================
echo.
pause
