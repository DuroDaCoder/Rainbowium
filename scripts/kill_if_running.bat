echo off
tasklist /fi "imagename eq RainbowSix.exe" |find ":" > nul & echo R6S isn't running, continuing. > output.txt
if errorlevel 1 taskkill /f /im "RainbowSix.exe" & echo R6S is running, killing it. > output.txt & echo cloud_wait > cloud_wait.txt
exit