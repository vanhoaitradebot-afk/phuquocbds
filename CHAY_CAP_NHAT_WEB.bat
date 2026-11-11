@echo off
chcp 65001 >nul
echo ========================================================
echo   DANG CAP NHAT WEBSITE LEN https://phuquocbds.surge.sh
echo ========================================================
set SURGE_LOGIN=phuquocbds4878@fldubai.com
set SURGE_TOKEN=2ba1fad35a72227eb6fe2dae2afdac00
call npx.cmd surge "%~dp0" phuquocbds.surge.sh
echo.
echo Hoan tat!
pause
