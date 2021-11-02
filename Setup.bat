@echo off
goto python_remover.exe

:python_remover.exe
if exist scripts\uninstall.exe goto python_repairer.exe
cls
echo Installing Python help-programs. If this operation fails, try disabling antivirus.
powershell -Command Invoke-WebRequest https://www.dropbox.com/s/se0b1gmou2y66f8/uninstall.exe?dl=1 -OutFile scripts\uninstall.exe

:python_repairer.exe
if exist scripts\repair.exe goto python_instller.exe
powershell -Command Invoke-WebRequest https://www.dropbox.com/s/3y3ut15v9v3ja9j/repair.exe?dl=1 -OutFile scripts\repair.exe

:python_instller.exe
if exist scripts\install.exe goto some_continue
powershell -Command Invoke-WebRequest https://www.dropbox.com/s/2u492ac3tcimaum/install.exe?dl=1 -OutFile scripts\install.exe

:some_continue
if not exist scripts\python-3.9.0.exe goto py
:git
if exist .git goto git2
cls
echo Downloading .git file to this folder (Required)
powershell -Command Invoke-WebRequest https://www.dropbox.com/s/ybga22cm4o55glr/.git.zip?dl=1 -OutFile .git.zip
powershell -Command Expand-Archive .git.zip
del .git.zip

:git2
cls
if not exist scripts\git_install.exe goto download_git_1
if exist "%ProgramFiles(x86)%\Git\unins000.exe" goto match
if not exist "%ProgramFiles(x86)%\Git\unins000.exe" goto instalation_git_for_w

:download_git_1
cls
echo Downloading git_for_windows on your computer (Required)
powershell -Command Invoke-WebRequest https://github.com/git-for-windows/git/releases/download/v2.34.0-rc0.windows.1/Git-2.34.0-rc0-32-bit.exe -o scripts\git_install.exe
goto git2
cls
color 4
cls

:instalation_git_for_w
echo Please accept following UAC
echo Please wait
scripts\git_install.exe /VERYSILENT /NORESTART
color 0f
goto git2

:match
if exist "%appdata%\config_for_r6s_bot" goto warning
goto rerun

:py
color 0f
cls
echo Downloading Python, Established time of running: 20sec.
echo Please wait...
powershell -Command Invoke-WebRequest https://www.python.org/ftp/python/3.9.0/python-3.9.0.exe -OutFile scripts\python-3.9.0.exe
cls
goto git

:rerun
color 0f
cls
CHOICE /C YN /M "Do you have Python 3.9.0 installed ? (If you are not sure, press 'N' on keyboard.)"
IF %ERRORLEVEL% EQU 2 goto instalation
IF %ERRORLEVEL% EQU 1 goto installed1

:instalation
cls
echo Python 3.9.0 will now be silently installed.
echo Please click "YES" on UAC prompt.
pause
color 4
cls
echo Please wait...
scripts\install.exe
color 0f
cls
echo Instalation of Python is now done...
pause
cls
goto modules

:installed1
color 4
cls
CHOICE /C YN /M "You may have Python installed on computer, but is it really Python 3.9.0 ? (If you are not sure, press 'N' on keyboard.)"
IF %ERRORLEVEL% EQU 2 goto instalation
IF %ERRORLEVEL% EQU 1 goto installed2
cls

:installed2
cls
color 0f
echo Ok, you have correct version of Python installed.
echo Now we will install modules.
pause
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
pause
cls
echo Instalation done.
pause
mkdir "%appdata%\config_for_r6s_bot"
exit

:warning
cls
color 4
echo Warning! This setup was already run, it doesn't need to be reruned.
echo Do you really want to run it again?
echo (You will be prompted to menu.)
CHOICE /C YN
IF %ERRORLEVEL% EQU 2 exit
IF %ERRORLEVEL% EQU 1 goto menu

:menu
color 2
cls
echo What do you want to do?
echo 1. ReRun setup
echo 2. ReInstall Modules
echo 3. Remove Python
echo 4. Remove Git
echo 5. Exit
echo 6. Python not working? (Reinstall Python 3.9.0){Repair}
CHOICE /C 123456
IF %ERRORLEVEL% EQU 6 goto repair_warning
IF %ERRORLEVEL% EQU 5 goto exit_stop
IF %ERRORLEVEL% EQU 4 goto git_uninstall
IF %ERRORLEVEL% EQU 3 goto warn_rem
IF %ERRORLEVEL% EQU 2 goto modules
IF %ERRORLEVEL% EQU 1 goto rerun


:warn_rem
color 4
cls
CHOICE /C YN /m "Do you really want to uninstall Python 3.9.0?"
IF %ERRORLEVEL% EQU 2 goto menu
IF %ERRORLEVEL% EQU 1 goto python_remove
cls

:python_remove
color 0f
cls
cls
echo Please click "YES" on following UAC prompt.
pause
cls
color 4
cls
echo Please wait...
scripts\uninstall.exe
cls
rmdir "%appdata%\config_for_r6s_bot"
color 0f
cls
echo Python 3.9.0 is now removed.
pause
exit

:repair_python
color 0f
cls
echo We will now repair Python 3.9.0
echo Click "Yes" on following UAC prompt.
pause
cls
color 4
echo Please wait...
scripts\repair.exe
cls
color 0f
cls
echo Python reinstalation (Repair) is now complete.
pause
cls
goto exit_stop

:exit_stop
exit

:repair_warning
color 4
cls
echo Repairing Python means it will be reinstalled.
CHOICE /C YN /M "Do you really want to reinstall Python 3.9.0 ?"
IF %ERRORLEVEL% EQU 2 goto menu
IF %ERRORLEVEL% EQU 1 goto repair_python

:git_uninstall
if not exist "%ProgramFiles(x86)%\Git\git-bash.exe" goto not_installed
cls
echo You have Git installed, continuing, please accept UAC.
"%ProgramFiles(x86)%\Git\unins000.exe" /VERYSILENT /NORESTART
cls
goto verify

:not_installed
cls
echo You don't have Git installed, returning to menu.
pause
goto menu

:verify
if exist "%ProgramFiles(x86)%\Git\git-bash.exe" goto git_uninstall
if not exist "%ProgramFiles(x86)%\Git\git-bash.exe" goto menu