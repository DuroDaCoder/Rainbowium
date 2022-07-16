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
import winshell
import os.path
import webbrowser
import colorama
from pynput.keyboard import Key, Controller
pdi.FAILSAFE = False

from pypresence import Presence
from random import randint
from time import sleep
from colorama import Fore, Back, Style
from playsound import playsound
colorama.init()
bad_colors = ['BLACK', 'LIGHTBLACK_EX', 'GREY', 'RESET', 'WHITE']
stm = "Steam"
upl = "Ubisoft_Connect"
url = "uplay://launch/635"
url1 = "steam://rungameid/359550"
client_id = '922380828540026880'
roundcount = 0
keyboard = Controller()
key = "0"

text = """   
        ██████╗  █████╗ ██╗███╗   ██╗██████╗  ██████╗ ██╗    ██╗██╗██╗   ██╗███╗   ███╗
        ██╔══██╗██╔══██╗██║████╗  ██║██╔══██╗██╔═══██╗██║    ██║██║██║   ██║████╗ ████║
        ██████╔╝███████║██║██╔██╗ ██║██████╔╝██║   ██║██║ █╗ ██║██║██║   ██║██╔████╔██║
        ██╔══██╗██╔══██║██║██║╚██╗██║██╔══██╗██║   ██║██║███╗██║██║██║   ██║██║╚██╔╝██║
        ██║  ██║██║  ██║██║██║ ╚████║██████╔╝╚██████╔╝╚███╔███╔╝██║╚██████╔╝██║ ╚═╝ ██║
        ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝

    """

text2 = """   

  _                     _ _             
 | |                   | (_)            
 | |     ___   __ _  __| |_ _ __   __ _ 
 | |    / _ \ / _` |/ _` | | '_ \ / _` |
 | |___| (_) | (_| | (_| | | | | | (_| |
 |______\___/ \__,_|\__,_|_|_| |_|\__, |
                                   __/ |
                                  |___/ 

    """

codes = vars(colorama.Fore)
colors = [codes[color] for color in codes if color not in bad_colors]
colored_chars = [random.choice(colors) + char for char in text2]
print(''.join(colored_chars))
print('\033[39m')

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
                small_image="bobthecoder",
                small_text="BobTheCoder#6210",

                buttons = [
                    {"label": "Visit the Github", "url": "https://github.com/DuroDaCoder/Rainbowium"},
                    {"label": "Join Creator's Discord", "url": "https://discord.gg/uSttY72hB9"}

        ]
)
    except Exception:
        pass

def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def error_pic(name, x, y):
    global error
    print(Fore.CYAN+ "[.] LOOKING FOR "+str(name)+" BUTTON...")
    for i in range(120):
        try:
            if pyautogui.locateOnScreen(f'assets\\{name}.png', confidence=0.8):
                print(Fore.GREEN+ "[-] FOUND "+str(name)+""+" BUTTON!")
                print('\033[39m')
                return
            else:
                time.sleep(0.5)
        except IOError:
            print("[!] UAC detected!")
            time.sleep(2)
            pass
    error()

def search_widget(name, x, y):
    global error
    print(Fore.CYAN+ "[.] LOOKING FOR "+str(name)+""+" BUTTON...")
    for i in range(120):
        try:
            if pyautogui.locateOnScreen(f'assets\\{name}.png', confidence=0.6):
                print(Fore.GREEN+ "[-] FOUND "+str(name)+""+" BUTTON!")
                print('\033[39m')
                return
            else:
                time.sleep(0.5)
        except IOError:
            print("[!] UAC detected!")
            time.sleep(2)
            pass
    error()
    
    
def spec_doc(name, x, y):
    global error
    print(Fore.CYAN+ "[.] LOOKING FOR "+str(name)+""+" BUTTON...")
    for i in range(120):
        try:
            if pyautogui.locateOnScreen(f'assets\\{name}.png', confidence=0.5):
                print(Fore.GREEN+ "[-] FOUND "+str(name)+""+" BUTTON!")
                print('\033[39m')
                return
            else:
                time.sleep(0.5)
        except IOError:
            print("[!] UAC detected!")
            time.sleep(2)
            pass
    error()
    
def longwait(name, x, y):
    global error
    print(Fore.CYAN+ "[.] LOOKING FOR "+str(name)+""+" BUTTON...")
    for i in range(500):
        try:
            if pyautogui.locateOnScreen(f'assets\\{name}.png', confidence=0.9):
                print(Fore.GREEN+ "[-] FOUND "+str(name)+""+" BUTTON!")
                print('\033[39m')
                return
            else:
                time.sleep(0.5)
        except IOError:
            print("[!] UAC detected!")
            time.sleep(2)
            pass
    error()
    
def longwait2(name, x, y):
    global error
    print(Fore.CYAN+ "[.] LOOKING FOR "+str(name)+""+" BUTTON...")
    for i in range(500):
        try:
            if pyautogui.locateOnScreen(f'assets\\{name}.png', confidence=0.9):
                print(Fore.GREEN+ "[-] FOUND "+str(name)+""+" BUTTON!")
                print('\033[39m')
                return
            else:
                time.sleep(0.5)
        except IOError:
            print("[!] UAC detected!")
            time.sleep(2)
            pass
    error()
    
def error():
    print()
    print("We were unable to find the button, restarting code.")
    print("Please Wait...")
    time.sleep(5)
    script_path = os.path.abspath(__file__)
    os.startfile(script_path)
    sys.exit()

def one():
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

def two():
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

def shootfunction():
    global error
    try:
        for i in range(50):
            try:
                if pyautogui.locateOnScreen('assets\\reinforce.png', confidence=0.9):
                    print(Fore.GREEN+ "[-] FOUND REINFORCE ICON!")
                    print('\033[39m')
                    break
                else:
                    time.sleep(0.5)
            except IOError:
                print("[!] UAC detected!")
                time.sleep(2)
                pass
    except Exception:
        error()
    print(Fore.CYAN+ "Shooting whole Primary weapon...")
    print('\033[39m')
    try:
        for i in range(20):
            for i in range(120):
                keyboard.press(key)
                time.sleep(0.2)
                keyboard.release(key)
            if pyautogui.locateOnScreen('assets\\primary.png', confidence=0.9):
                break
    except Exception:
        error()

    print(Fore.CYAN+ "Shooting whole Secondary weapon...")
    print('\033[39m')
    try:
        for i in range(42):
            for i in range(1000):
                keyboard.press(key)
                keyboard.release(key)
        if pyautogui.locateOnScreen('assets\\sec.png', confidence=0.9):
            return
    except Exception:
        error()

def round_print():
    global roundcount
    roundcount = roundcount + 1
    print(Fore.MAGENTA+ "---------", "[Round:" ,str(roundcount)+"]", "---------")
    print('\033[39m')

if os.path.isfile('scripts\launcher_config.txt'):
    print("Config was found!")
    print()
else:
    print("You didn't ran Setup.bat correctly, rerun it and complete instalation to proceed.")
    time.sleep(30)
    sys.exit()
    
if checkIfProcessRunning('RainbowSix'):
    os.system('start cmd /c "taskkill /f /im RainbowSix.exe /t"')
    print("Killed RainbowSixSiege, waiting 10sec for Cloud Sync.")
    time.sleep(10)
else:
    print('RainbowSixSiege is not running, starting it.')
    time.sleep(2)

with open('scripts\launcher_config.txt') as f:
    if 'stm' in f.read():
        webbrowser.open_new_tab(url1)
    else:
        with open('scripts\launcher_config.txt') as f:
            if 'upl' in f.read():
                webbrowser.open_new_tab(url)
            else:
                print()
                print("You didn't ran Setup.bat correctly, rerun it and complete instalation to proceed.")
                time.sleep(30)
                sys.exit()

start_time=time.time()

try:
    RPC = Presence(client_id)
except Exception:
        pass

os.system('cls' if os.name == 'nt' else 'clear')
codes = vars(colorama.Fore)
colors = [codes[color] for color in codes if color not in bad_colors]
colored_lines = [random.choice(colors) + line for line in text.split('\n')]
print('\n'.join(colored_lines))
print('\033[39m')

longwait('Menu', 172, 319)
one()
error_pic('Training', 1333, 382)
pdi.press("left")
pdi.press("enter")
time.sleep(1)
search_widget('LoneWolf', 1333, 382)
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
    round_print()
    search_widget('Locations', 278, 392)
    pdi.press("down")
    time.sleep(0.2)
    pdi.press("down")
    time.sleep(0.2)
    pdi.press("down")
    time.sleep(0.2)
    pdi.press("enter")
    spec_doc('Operators', 520, 419)
    two()
    search_widget('Loadout', 292, 302)
    pdi.press("down")
    pdi.press("right")
    pdi.press("right")
    pdi.press("down")
    pdi.press("left")
    pdi.press("up")
    pdi.press("up")
    pdi.press("enter")
    shootfunction()
    longwait2('Bonus', 461, 171)
    time.sleep(0.2)
    pdi.press("tab")
    search_widget('Retry', 1053, 817)
    time.sleep(0.5)
    pdi.press("enter")
    pdi.press("enter")
