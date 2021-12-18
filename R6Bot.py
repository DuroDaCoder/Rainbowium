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

from random import randint
from time import sleep
from colorama import Fore, Style
from colorama import init


if os.path.isfile('temp.txt'):
    print("Update Done!")
else:
    os.startfile("scripts\hider.vbs")
    sys.exit()


os.system('start scripts\hider2.vbs')
time.sleep(3)

a_file = open("output.txt")

lines = a_file.readlines()
for line in lines:
    print(line)
a_file.close()

print("[-] STARTING R6S")
time.sleep(3)
os.remove("output.txt")
os.startfile("scripts\shortcutmaker.py")
time.sleep(2)
os.startfile("R6S")
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
os.remove("R6S.lnk")
