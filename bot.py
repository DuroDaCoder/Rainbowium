import math
import keyboard
import psutil
import pyautogui
import os
import time
import datetime
import random
import sys
import PIL
import pydirectinput as pdi
import win32gui, win32con
pdi.FAILSAFE = False

from pypresence import Presence
from random import randint
from time import sleep
from colorama import Fore, Style
from colorama import init

client_id = '922380828540026880'
try:
    RPC = Presence(client_id)
except Exception:
        pass

try:
    RPC.close()
except Exception:
        pass

        try:
            RPC.connect()
        except Exception:
                pass
        try:
            RPC.update(
                    details="An open source Python farm bot",
                    state="It is currently Farming",

                    large_image = "r6s_2",
                    large_text="Rainbow Six Siege",
                    small_image="r6s",
                    small_text="Rainbow Six Siege",

                    buttons = [
                        {"label": "Visit the Github", "url": "https://github.com/DuroDaCoder/RainbowSixSiege-Renown-Farm"},
                        {"label": "Join Creator's Discord", "url": "https://discord.gg/uSttY72hB9"}
        ]
)
        except Exception:
                pass

print("[!] Let this window run, this is buttons tracker.")
print()
print("Launching Rainbow Six Siege.")
print()
print("[!] This process will be automated.")
print()
print()
print("[!] Switch onto R6S window and don't touch mouse or keyboard.[!]")
print()
print()
print("To stop farming, just close this window.")
print()
time.sleep(5)

Minimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

def error_pic(name, x, y):
    print(f"Looking for {name} button.")
    while not pyautogui.locateOnScreen(f'assets/{name}.png', confidence=0.8):
        time.sleep(0.5)
    print (f"I found {name} button.")
    print()

def search_widget(name, x, y):
    print(f"Looking for {name} button.")
    while not pyautogui.locateOnScreen(f'assets\{name}.png', confidence=0.6):
        time.sleep(0.5)
    print (f"I found {name} button.")
    print()

def spec_doc(name, x, y):
    print(f"Looking for {name} button.")
    while not pyautogui.locateOnScreen(f'assets\{name}.png', confidence=0.5):
        time.sleep(0.5)
    print (f"I found {name} button.")
    print()

def lock_1(name, x, y):
    print(f"Looking for {name} button.")
    while not pyautogui.locateOnScreen(f'assets\{name}.png', confidence=0.5):
        time.sleep(0.5)
    print (f"I found {name} button.")
    print()

def lock_2(name, x, y):
    print(f"Looking for {name} button.")
    while not pyautogui.locateOnScreen(f'assets\{name}.png', confidence=0.5):
        time.sleep(0.5)
    print (f"I found {name} button.")
    print()

def lock_3(name, x, y):
    print(f"Looking for {name} button.")
    while not pyautogui.locateOnScreen(f'assets\{name}.png', confidence=0.8):
        time.sleep(0.5)
    print (f"I found {name} button.")
    print()

def bonus(name, x, y):
    print(f"Looking for {name} button.")
    while not pyautogui.locateOnScreen(f'assets\{name}.png', confidence=0.9):
        time.sleep(0.5)
    print (f"I found {name} button.")
    print()


lock_3('Shop', 172, 319)
search_widget('Menu', 172, 319)
time.sleep(5)
pdi.press("up")
pdi.press("up")
pdi.press("up")
pdi.press("up")
pdi.press("up")
pdi.press("up")
pdi.press("up")
pdi.press("up")
pdi.press("up")
pdi.press("up")
pdi.press("up")
pdi.press("down")
pdi.press("left")
pdi.press("left")
pdi.press("enter")
time.sleep(1)
error_pic('Training', 1333, 382)
pdi.press("left")
pdi.press("enter")
time.sleep(1)
search_widget('Lone_Wolf', 1333, 382)
pdi.press("f")
pdi.press("f")
pdi.press("left")
pdi.press("enter")

while 1:
    search_widget('Locations', 278, 392)
    pdi.press("down")
    pdi.press("enter")
    spec_doc('Operators', 520, 419)
    time.sleep(0.5)
    pdi.press("enter")
    search_widget('loadout', 292, 302)
    pdi.press("enter")
    bonus('bonus', 465, 169)
    time.sleep(0.4)
    pdi.press("tab")
    error_pic('retry', 1053, 817)
    time.sleep(0.5)
    pdi.press("enter")
    pdi.press("enter")
