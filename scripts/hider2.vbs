Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "scripts\kill_if_running.bat" & Chr(34), 0
Set WshShell = Nothing