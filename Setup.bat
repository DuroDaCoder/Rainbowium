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
goto py
cls

:rerun
if exist del scripts\launcher_config.txt
if exist scripts\launcher_config.txt goto averror
cls
CHOICE /C SU /M "Do you have R6S installed by Steam or Ubisoft Connect (S/U)?"
IF %ERRORLEVEL% EQU 1 echo stm > scripts\launcher_config.txt
IF %ERRORLEVEL% EQU 2 echo upl > scripts\launcher_config.txt
if not exist scripts\launcher_config.txt goto averror
cls
:skipback
cls
CHOICE /C YNM /M "Do you have Python 3.9.0 installed ? (If you are not sure, press 'M' on keyboard.)"
IF %ERRORLEVEL% EQU 3 goto guide
IF %ERRORLEVEL% EQU 2 goto instalation
IF %ERRORLEVEL% EQU 1 goto modules

:py
color 0f
cls
if exist scripts\python-3.9.0.exe goto continue_python_exists
:boom_python
cls
echo Downloading Python, Established time of running: 20sec.
echo Please wait...
powershell -Command Invoke-WebRequest https://www.python.org/ftp/python/3.9.0/python-3.9.0.exe -OutFile scripts\python-3.9.0.exe
timeout /t 1 /NOBREAK >nul
:continue_python_exists
set file="scripts\python-3.9.0.exe"
set maxbytesize=26433000
FOR /F "usebackq" %%A IN ('%file%') DO set size=%%~zA
if %size% LSS %maxbytesize% (
    SET sizepython=fileissmall
) ELSE (
    SET sizepython=fileisok
)

timeout /t 1 /NOBREAK >nul
if %sizepython%==fileissmall goto badpython
if %sizepython%==fileisok goto continuepythoncheck
:badpython
del scripts\python-3.9.0.exe
echo Python installer is corrupted, redownloading...
timeout /t 7 /NOBREAK
goto boom_python
:continuepythoncheck
cls
goto rerun

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
py -3.9 -m pip install playsound==1.2.2
py -3.9 -m pip install PyQt5
py -3.9 -m pip install pyfiglet
py -3.9 -m pip install pynput
cls
echo Instalation done.
pause
exit
cls

:exit_stop
exit

:guide
cls
echo So... You don't know what Python you have installed?
echo.
echo I will now guide you, how to check Python version.
pause
:reguide
cls
echo Please open Windows Start, search "Cmd" without Quotation marks ("") and open it.
pause
cls
echo Type: "python --version" in terminal without Quotation marks ("") and press enter.
echo.
echo If you will see command not found or different version than 3.9.0, press N in installation menu to install Python.
echo.
echo If you will see Python Version: 3.9.0, than press Y in installation menu to install needed modules.
echo.
pause
cls
CHOICE /C YN /M "Do you now know, if you have Python 3.9.0 installed ? (If not, press 'N' on keyboard.)"
IF %ERRORLEVEL% EQU 2 goto reguide
IF %ERRORLEVEL% EQU 1 goto skipback

:averror
cls
echo We had an error with writing, please disable your AntiVirus (Ransomware Shield) to continue.
timeout /t 20
goto rerun