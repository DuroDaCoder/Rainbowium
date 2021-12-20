@echo off
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"="
    echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
PUSHD %~DP0 & cd /d "%~dp0"
%1 %2
mshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :runas","","runas",1)(window.close)&goto :eof
:runas

if exist "%TEMP%\consoleSettingsBackup.reg" regedit /S "%TEMP%\consoleSettingsBackup.reg"&DEL /F /Q "%TEMP%\consoleSettingsBackup.reg"&goto :mainstart
regedit /S /e "%TEMP%\consoleSettingsBackup.reg" "HKEY_CURRENT_USER\Console"
echo REGEDIT4>"%TEMP%\disablequickedit.reg"
echo [HKEY_CURRENT_USER\Console]>>"%TEMP%\disablequickedit.reg"
(echo "QuickEdit"=dword:00000000)>>"%TEMP%\disablequickedit.reg"
regedit /S "%TEMP%\disablequickedit.reg"
DEL /F /Q "%TEMP%\disablequickedit.reg"
start "" "cmd" /c "%~dpnx0"&exit

:mainstart

mkdir scripts
cls
goto some_continue


:some_continue
if not exist scripts\python-3.9.0.exe goto py
:git
goto rerun
cls

:unsure
goto match
:run_check
:successfully_ran

:match
:rerun
del scripts\launcher_config.txt
cls
CHOICE /C SU /M "Do you have R6S installed by Steam or Ubisoft Connect (S/U)?"
IF %ERRORLEVEL% EQU 1 echo stm > scripts\launcher_config.txt
IF %ERRORLEVEL% EQU 2 echo upl > scripts\launcher_config.txt
cls
CHOICE /C YN /M "Do you have Python 3.9.0 installed ? (If you are not sure, press 'N' on keyboard.)"
IF %ERRORLEVEL% EQU 2 goto instalation
IF %ERRORLEVEL% EQU 1 goto modules

:py
color 0f
cls
echo Downloading Python, Established time of running: 20sec.
echo Please wait...
powershell -Command Invoke-WebRequest https://www.python.org/ftp/python/3.9.0/python-3.9.0.exe -OutFile scripts\python-3.9.0.exe
cls
goto git

:instalation
cls
color 4
cls
echo Please wait...
scripts\python-3.9.0.exe /quiet InstallAllUsers=1 PrependPath=1
goto installed2

:installed2
goto modules

:modules
color 0f
cls
echo Installing needed modules
py -3.9 -m pip install --upgrade pip
py -3.9 -m pip install psutil
py -3.9 -m pip install colorama
py -3.9 -m pip install keyboard
py -3.9 -m pip install pyautogui
py -3.9 -m pip install unipath
py -3.9 -m pip install mouse
py -3.9 -m pip install pydirectinput
py -3.9 -m pip install winshell
py -3.9 -m pip install pypiwin32
py -3.9 -m pip install Pillow
py -3.9 -m pip install opencv-python
py -3.9 -m pip install anonfile
py -3.9 -m pip install pypresence
:regit
:skip2
:skip
cls
echo Instalation done.
pause
exit
cls

:exit_stop
exit