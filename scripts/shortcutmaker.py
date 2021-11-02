import os, winshell
from win32com.client import Dispatch
desktop = winshell.desktop()
path = os.path.join("R6S.lnk")
target = r"uplay://launch/635/0"
wDir = r"uplay://launch/635/0"
icon = r"uplay://launch/635/0"
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()
