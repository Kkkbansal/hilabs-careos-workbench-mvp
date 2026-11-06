@echo off
echo Starting HiLabs Case Management Workbench MVP...
python app.py
if %ERRORLEVEL% NEQ 0 (
    echo Python server failed to start, opening index.html directly in browser...
    start index.html
)
pause

