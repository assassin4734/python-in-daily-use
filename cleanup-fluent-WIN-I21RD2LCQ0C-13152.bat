echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYS Inc\v222\fluent/ntbin/win64/winkill.exe"

"C:\PROGRA~1\ANSYS Inc\v222\fluent\ntbin\win64\tell.exe" WIN-I21RD2LCQ0C 3358 CLEANUP_EXITING
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 11548) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 20424) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 14552) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 8272) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 13536) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 9300) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 844) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 15304) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 7996) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 16464) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 3288) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 13152) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 9376)
del "E:\1-python-in-daily-use\cleanup-fluent-WIN-I21RD2LCQ0C-13152.bat"
