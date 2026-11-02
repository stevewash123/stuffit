@echo off
rem Starts the StuffIt API (port 5259) in the background and the answer-key viewer server (port 8765) in THIS window, so the login prompt is
rem where you can see it (over SSH or VS Code Remote a separate window would open on the server's desktop, where you cannot).
rem   .\start-viewer.bat            normal
rem   .\start-viewer.bat nobrowser  do not open a browser on this machine (use this over SSH / VS Code Remote; forward port 8765 and open it on your laptop)
rem The viewer server asks for the test user's login: email (Enter keeps stevewash123.test@gmail.com), then the password, hidden.
rem Press Ctrl+C to stop the viewer. The API keeps running; stop it with:  Stop-Process -Name StuffIt.Api -Force   (its output is in %TEMP%\stuffit-api.log)
setlocal
set "HERE=%~dp0"
set "API=%HERE%..\..\..\StuffIt_API"

if not exist "%API%\src\StuffIt.Api\StuffIt.Api.csproj" (
  echo Cannot find the API project at "%API%".
  pause
  exit /b 1
)
where python >nul 2>nul || ( echo python is not on the PATH. & pause & exit /b 1 )
where dotnet >nul 2>nul || ( echo dotnet is not on the PATH. & pause & exit /b 1 )

netstat -ano | findstr /R /C:":8765 .*LISTENING" >nul && (
  echo Something is already listening on 8765 - an older viewer server? Stop it first ^(Ctrl+C in its window, or Stop-Process -Name python^), then run this again.
  exit /b 1
)

set ASPNETCORE_ENVIRONMENT=Development

netstat -ano | findstr /R /C:":5259 .*LISTENING" >nul && (
  echo API already running on 5259.
) || (
  echo Starting the API in the background. The first build takes about a minute; its log is %TEMP%\stuffit-api.log
  start "" /b /d "%API%" cmd /c "dotnet run --project src\StuffIt.Api --urls http://localhost:5259 > %TEMP%\stuffit-api.log 2>&1"
)

if /I not "%~1"=="nobrowser" start "" http://localhost:8765/key-viewer.html
echo.
echo Viewer: http://localhost:8765/key-viewer.html   (over SSH: forward port 8765, then open it on your own machine)
echo TEST THIS works once the API log says "Now listening on: http://localhost:5259".
echo.
cd /d "%HERE%"
python serve-viewer.py
endlocal
