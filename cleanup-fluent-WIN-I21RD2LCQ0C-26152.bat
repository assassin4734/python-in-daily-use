echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYS Inc\v222\fluent/ntbin/win64/winkill.exe"

"C:\PROGRA~1\ANSYS Inc\v222\fluent\ntbin\win64\tell.exe" WIN-I21RD2LCQ0C 7902 CLEANUP_EXITING
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 28024) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 8224) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 22116) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 26024) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 28224) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 27392) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 27768) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 28236) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 27524) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 17540) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 26204) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 26152) 
if /i "%LOCALHOST%"=="WIN-I21RD2LCQ0C" (%KILL_CMD% 27040)
del "E:\1-python-in-daily-use\cleanup-fluent-WIN-I21RD2LCQ0C-26152.bat"