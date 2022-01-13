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
from playsound import playsound

client_id = '922380828540026880'
start_time=time.time()

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
    for i in range(120):
        if pyautogui.locateOnScreen(f'assets\\{name}.png', confidence=0.8):
            print(f"I found {name} button.")
            print()
            return
        else:
            time.sleep(0.5)
    error()

def search_widget(name, x, y):
    print(f"Looking for {name} button.")
    for i in range(120):
        if pyautogui.locateOnScreen(f'assets\\{name}.png', confidence=0.6):
            print(f"I found {name} button.")
            print()
            return
        else:
            time.sleep(0.5)
    error()
    
    
def spec_doc(name, x, y):
    print(f"Looking for {name} button.")
    for i in range(120):
        if pyautogui.locateOnScreen(f'assets\\{name}.png', confidence=0.5):
            print(f"I found {name} button.")
            print()
            return
        else:
            time.sleep(0.5)
    error()
    
def longwait(name, x, y):
    print(f"Looking for {name} button.")
    for i in range(500):
        if pyautogui.locateOnScreen(f'assets\\{name}.png', confidence=0.6):
            print(f"I found {name} button.")
            print()
            return
        else:
            time.sleep(0.5)
    error()
    
def longwait2(name, x, y):
    print(f"Looking for {name} button.")
    for i in range(500):
        if pyautogui.locateOnScreen(f'assets\\{name}.png', confidence=0.8):
            print(f"I found {name} button.")
            print()
            return
        else:
            time.sleep(0.5)
    error()
    
def error():
    if os.path.isfile("configs\\soundconfig.txt"):
        print()
        print ("We were unable to find the button, restarting code.")
        print ("Please Wait...")
        time.sleep(10)
        os.startfile("R6Bot.py")
        sys.exit()
    else:
        try:
            playsound("sound\\error.mp3", False)
        except Exception:
            pass
        print()
        print ("We were unable to find the button, restarting code.")
        print ("Please Wait...")
        time.sleep(10)
        os.startfile("R6Bot.py")
        sys.exit()
        

time.sleep(5)

longwait('Menu', 172, 319)
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
    pdi.press("down")
    time.sleep(2)
    pdi.press("right")
    time.sleep(0.2)
    pdi.press("right")
    time.sleep(0.2)
    pdi.press("right")
    time.sleep(0.2)
    pdi.press("right")
    time.sleep(0.2)
    pdi.press("enter")
    search_widget('loadout', 292, 302)
    pdi.press("enter")
    longwait2('bonus', 461, 171)
    time.sleep(0.2)
    pdi.press("tab")
    search_widget('retry', 1053, 817)
    time.sleep(0.5)
    pdi.press("enter")
    pdi.press("enter")
