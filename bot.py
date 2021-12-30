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
start_time=time.time()

def lock_3(name, x, y):
    print(f"Looking for {name} button INGAME.")
    while not pyautogui.locateOnScreen(f'assets\{name}.png', confidence=0.8):
        time.sleep(0.5)
    print (f"I found {name} button, continuing.")
    print()



try:
    RPC = Presence(client_id)
except Exception:
        pass

def rpc_update():
    try:
        RPC.connect()
    except Exception:
        pass
    try:
        RPC.update(
                details="Rainbowium - R6S Renown Farm",
                state="Farm Runtime:", start=start_time,

                large_image = "rainbowium",
                large_text="Rainbowium",
                small_image="durodacoder",
                small_text="DuroDaCoder#6210",

                buttons = [
                    {"label": "Visit the Github", "url": "https://github.com/DuroDaCoder/Rainbowium"},
                    {"label": "Join Creator's Discord", "url": "https://discord.gg/uSttY72hB9"}

        ]
)
    except Exception:
        pass


    
    
print("[!]Switch onto R6S window and don't touch mouse or keyboard.[!]")
print()
print("To stop farming, just close this window.")
print()
print("Make sure you Minimize this window.")
print()
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


def bonus(name, x, y):
    print(f"Looking for {name} button.")
    while not pyautogui.locateOnScreen(f'assets\{name}.png', confidence=0.9):
        time.sleep(0.5)
    print (f"I found {name} button.")
    print()
    
time.sleep(5)

Minimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
    
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
time.sleep(5)
try:
    rpc_update()
except Exception:
    pass

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
