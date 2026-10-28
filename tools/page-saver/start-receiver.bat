@echo off
rem Usage: start-receiver.bat [folder]
rem No folder given: uses the one line in folder.txt next to this file, else StuffIt\OfficialDocs beside this tool.
set "DEST=%~1"
if "%DEST%"=="" if exist "%~dp0folder.txt" set /p DEST=<"%~dp0folder.txt"
if "%DEST%"=="" (python "%~dp0receiver.py") else (python "%~dp0receiver.py" "%DEST%")
pause
