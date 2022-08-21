@echo off
py -3.9 bot.py
IF %ERRORLEVEL% NEQ 0 cls && echo If there was an error with running bot.py script or bot.py window hasn't opened, you may have installed Python *anyversion* (64-bit) version. Please uninstall it, or run this app in virtual environment. && pause && exit
cls
exit
