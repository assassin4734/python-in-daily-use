echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYS Inc\v222\fluent/ntbin/win64/winkill.exe"

"C:\PROGRA~1\ANSYS Inc\v222\fluent\ntbin\win64\tell.exe" WIN-I21RD2LCQ0C 9044 CLEANUP_EXITING
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 25780) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 4256) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 27312) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 29388) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 29216) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 29360) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 28232) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 21708) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 29032) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 27728) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 28844) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 27632) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 15020)
del "E:\1-python-in-daily-use\cleanup-fluent-WIN-I21RD2LCQ0C-27632.bat"