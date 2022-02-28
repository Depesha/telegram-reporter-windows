cd %~dp0install_app
Powershell.exe -executionpolicy remotesigned -File  "%~dp0\install_app\install.ps1"
pause >nul