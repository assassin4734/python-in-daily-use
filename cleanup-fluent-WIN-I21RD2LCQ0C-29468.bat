echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYS Inc\v222\fluent/ntbin/win64/winkill.exe"

"C:\PROGRA~1\ANSYS Inc\v222\fluent\ntbin\win64\tell.exe" WIN-I21RD2LCQ0C 9921 CLEANUP_EXITING
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 27840) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 10464) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 28372) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 22344) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 26264) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 28536) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 22500) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 26100) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 18404) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 27900) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 24236) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 29468) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 29512)
del "E:\1-python-in-daily-use\cleanup-fluent-WIN-I21RD2LCQ0C-29468.bat"
