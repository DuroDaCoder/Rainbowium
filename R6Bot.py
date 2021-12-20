import math
import keyboard
import psutil
import pyautogui
import os
import time
import datetime
import random
import sys
import winshell
import os.path
import webbrowser

from random import randint
from time import sleep
from colorama import Fore, Style
from colorama import init

stm = "Steam"
upl = "Ubisoft_Connect"
url = "uplay://launch/635"
url1 = "steam://rungameid/359550"

if os.path.isfile('scripts\launcher_config.txt'):
    print("Config was found!")
else:
    print("You didn't ran Setup.bat correctly, rerun it and complete instalation to proceed.")
    time.sleep(15)
    sys.exit()


os.system('start scripts\hider2.vbs')
time.sleep(3)

a_file = open("output.txt")

lines = a_file.readlines()
for line in lines:
    print(line)
a_file.close()

with open('scripts\launcher_config.txt') as f:
    if 'stm' in f.read():
        webbrowser.open_new_tab(url1)
    else:
        with open('scripts\launcher_config.txt') as f:
            if 'upl' in f.read():
                webbrowser.open_new_tab(url)
            else:
                print("You didn't ran Setup.bat correctly, rerun it and complete instalation to proceed.")
                time.sleep(15)
                sys.exit()

print("[-] STARTING R6S")
time.sleep(3)
os.remove("output.txt")
print()
print("This window will be hidden.")
print()
print("[-] We will detect, if R6S is running.")
print()
print("[!] To turn off farming, just close following window [!]")
print()
print("[!][!] Please, don't touch keyboard or mouse and don't click anything [!][!]")
time.sleep(6)
os.startfile("bot.py")
