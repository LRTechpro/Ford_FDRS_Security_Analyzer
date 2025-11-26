@echo off
setlocal EnableExtensions
REM Professional Diagnostic Analyzer Launcher (simplified & robust)

title Professional Diagnostic Analyzer

cd /d "%~dp0"

echo(
echo ================================================================================
echo   Professional Automotive Diagnostic Analyzer
echo   Version 2.1.0 - Enterprise Edition
echo ================================================================================
echo(

echo TRACE: Starting interpreter detection

set "SCRIPT=professional_diagnostic_analyzer.py"
set "PY_EXE="
set "PY_ARGS="

REM Prefer local venv if present
echo TRACE: Checking local venv
if exist "%CD%\.venv\Scripts\python.exe" set "PY_EXE=%CD%\.venv\Scripts\python.exe" & goto :RUN

REM Use python on PATH if available
echo TRACE: Checking python on PATH
where python >nul 2>nul
if %ERRORLEVEL%==0 set "PY_EXE=python" & goto :RUN

REM Use Python Launcher if available
echo TRACE: Checking py launcher
where py >nul 2>nul
if %ERRORLEVEL%==0 set "PY_EXE=py" & set "PY_ARGS=-3" & goto :RUN

REM Fallback to hardcoded path
echo TRACE: Checking hardcoded fallback
if exist "C:\Users\HWATKI16\AppData\Local\Python\pythoncore-3.14-64\python.exe" set "PY_EXE=C:\Users\HWATKI16\AppData\Local\Python\pythoncore-3.14-64\python.exe" & goto :RUN

echo ERROR: Could not find a Python interpreter.
echo Install Python 3.10+ from https://www.python.org/downloads/ or create a venv in .venv
echo(
pause
exit /b 1

:RUN
REM Ensure Tkinter (GUI) is available for this interpreter
echo TRACE: Selected interpreter: %PY_EXE% %PY_ARGS%
if not exist "%SCRIPT%" goto :NOSCRIPT

REM Quick check that Tkinter is importable
"%PY_EXE%" %PY_ARGS% -c "import tkinter" 1>nul 2>nul
if errorlevel 1 goto :NO_TK

set "PYTHONUTF8=1"

echo Using: %PY_EXE% %PY_ARGS%
echo Starting application...
echo(
"%PY_EXE%" %PY_ARGS% "%SCRIPT%"
set "ERR=%ERRORLEVEL%"
if not "%ERR%"=="0" goto :APP_ERROR

exit /b 0

:NOSCRIPT
echo ERROR: Script not found: %SCRIPT%
pause
exit /b 1

:NO_TK
echo ERROR: Your Python installation does not include Tkinter (GUI support).
echo Please install Python with 'tcl/tk' or choose a different interpreter/venv.
echo(
echo Tip: Use the Python.org installer and ensure 'tcl/tk' is selected during install.
pause
exit /b 1

:APP_ERROR
echo(
echo ERROR: Application exited with code %ERR%
echo If the window closed immediately, run this in a Command Prompt to see errors:
echo     "%PY_EXE%" %PY_ARGS% "%~dp0%SCRIPT%"
echo(
pause
exit /b %ERR%

