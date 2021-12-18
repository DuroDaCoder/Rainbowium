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

from random import randint
from time import sleep
from colorama import Fore, Style
from colorama import init

print("[!] Let this window run, this is buttons tracker.")
print()
print("Launching Rainbow Six Siege.")
print()
print("[!] This process will be automated.")
print()
print()
print("[!] Switch onto R6S window and don't touch mouse or keyboard.[!]")
print()
time.sleep(5)

Minimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

def error_pic(name, x, y):
    print(f"Searching for {name} button.")
    while not pyautogui.locateOnScreen(f'assets/{name}.png', confidence=0.8):
        time.sleep(0.5)
    print (f"I found {name} button.")
    print()

def search_widget(name, x, y):
    print(f"Searching for {name} button.")
    while not pyautogui.locateOnScreen(f'assets\{name}.png', confidence=0.6):
        time.sleep(0.5)
    print (f"I found {name} button.")
    print()

def spec_doc(name, x, y):
    print(f"Searching for {name} button.")
    while not pyautogui.locateOnScreen(f'assets\{name}.png', confidence=0.5):
        time.sleep(0.5)
    print (f"I found {name} button.")
    print()

def lock_1(name, x, y):
    print(f"Searching for {name} button.")
    while not pyautogui.locateOnScreen(f'assets\{name}.png', confidence=0.5):
        time.sleep(0.5)
    print (f"I found {name} button.")
    print()

def lock_2(name, x, y):
    print(f"Searching for {name} button.")
    while not pyautogui.locateOnScreen(f'assets\{name}.png', confidence=0.5):
        time.sleep(0.5)
    print (f"I found {name} button.")
    print()

def lock_3(name, x, y):
    print(f"Searching for {name} button.")
    while not pyautogui.locateOnScreen(f'assets\{name}.png', confidence=0.8):
        time.sleep(0.5)
    print (f"I found {name} button.")
    print()


lock_3('menu_lock', 172, 319)
search_widget('menu', 172, 319)
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
error_pic('train', 1333, 382)
pdi.press("left")
pdi.press("enter")
time.sleep(1)
search_widget('solo', 1333, 382)
pdi.press("f")
pdi.press("f")
pdi.press("left")
pdi.press("enter")

while 1:
    search_widget('location', 278, 392)
    pdi.press("down")
    pdi.press("enter")
    spec_doc('doc', 520, 419)
    time.sleep(0.5)
    pdi.press("down")
    time.sleep(0.3)
    pdi.press("right")
    pdi.press("right")
    pdi.press("right")
    pdi.press("right")
    time.sleep(0.4)
    pdi.press("enter")
    search_widget('loadout', 292, 302)
    pdi.press("enter")
    error_pic('retry', 1053, 817)
    time.sleep(0.5)
    pdi.press("enter")
    pdi.press("enter")
