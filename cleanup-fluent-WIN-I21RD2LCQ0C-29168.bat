echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYS Inc\v222\fluent/ntbin/win64/winkill.exe"

"C:\PROGRA~1\ANSYS Inc\v222\fluent\ntbin\win64\tell.exe" WIN-I21RD2LCQ0C 10281 CLEANUP_EXITING
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 24824) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 29640) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 25052) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 12460) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 19584) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 24308) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 29412) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 3336) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 25172) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 25772) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 25180) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 29168) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 8288)
del "E:\1-python-in-daily-use\cleanup-fluent-WIN-I21RD2LCQ0C-29168.bat"
