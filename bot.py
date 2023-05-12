import cv2
import psutil
import pyautogui
import os
import time
import random
import sys
import pydirectinput as pdi
import os.path
import webbrowser
import colorama
import logging
from pynput.keyboard import Controller
from colorama import Fore

pdi.FAILSAFE = False
colorama.init()
keyboard = Controller()
logging.basicConfig(filename="log.txt",
                    filemode='a',
                    format='%(asctime)s - %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
logging.info("Fresh Start of The Script!")
bad_colors = ['BLACK', 'LIGHTBLACK_EX', 'GREY', 'RESET', 'WHITE']
ubisoft_connect, steam, client_id, round_count = "uplay://launch/635", "steam://rungameid/359550", '922380828540026880', 0
cloud_sync_delay = 10
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


def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def locate_onScreen(name, confidence, length):
    if not confidence > 0 < 1.1:
        return False
    if not os.path.isfile(f"assets\\{name}"):
        return False
    print(Fore.CYAN + "[.] LOOKING FOR " + str(name) + "" + " BUTTON...")
    for i in range(length):
        try:
            if pyautogui.locateOnScreen(f'assets\\{name}', confidence=confidence):
                print(Fore.GREEN + "[-] FOUND " + str(name) + "" + " BUTTON!")
                print('\033[39m')
                return True
            else:
                time.sleep(1)
                pass
        except IOError:
            print("[!] UAC detected!")
            logging.info(
                "User Account Control (UAC) detected on a screen, returning one scan of the image (This may be spammed in a log for a while)!")
            time.sleep(2)
            pass
    error()


def press_buttons(button, amount, delay_between, delay_on_the_end):
    for i in range(int(amount)):
        pdi.press(str(button))
        if delay_between is not None:
            time.sleep(delay_between)
    if delay_on_the_end is not None:
        time.sleep(delay_on_the_end)
    return True


def press_button(button, delay_on_the_end):
    pdi.press(str(button))
    if delay_on_the_end is not None:
        time.sleep(delay_on_the_end)
    return True


def error():
    logging.info("Error was triggered, script will probably restart!")
    print("\nWe were unable to find the button, restarting code.\nPlease Wait...")
    time.sleep(5)
    if not os.path.exists(os.getcwd() + "\Run.bat") and not os.stat(str(os.getcwd() + "\Run.bat")):
        print(
            '\nIt looks like you deleted/renamed/moved "Run.bat" file.\nPlease move this file back or rename it!')
        input("Press any key to exit...")
        sys.exit(1)
    os.startfile(os.getcwd()+"\\Run.bat")
    sys.exit(1)


def round_print():
    global round_count
    round_count = round_count + 1
    print(Fore.MAGENTA + "---------", "[Round:", str(round_count) + "]", "---------")
    print('\033[39m')


def setup():
    if not os.path.isfile("config.txt"):
        result = input(Fore.YELLOW + "Do you use Steam or Ubisoft Connect as an R6S Game Launcher? s/u: ")
        print('\033[39m')
        if result != "s" and result != "u":
            logging.info("Wrong option selected in the config.txt setup, exiting!")
            print(Fore.RED + "Wrong option selected!")
            input("Press any key to exit...")
            sys.exit(1)
        f = open("config.txt", "a")
        f.write(result)
        f.close()
    if checkIfProcessRunning('RainbowSix'):
        os.system('start cmd /c "taskkill /f /im RainbowSix.exe /t"')
        print(f"Killed Rainbow Six Siege, waiting {cloud_sync_delay}sec. for Ubisoft/Steam Cloud Sync.")
        time.sleep(cloud_sync_delay)
    else:
        print('RainbowSixSiege is not running, starting it.')
        time.sleep(2)
    print_empty(20)
    with open('config.txt') as f:
        config_content = f.read()
        if 's' in config_content:
            webbrowser.open_new_tab(steam)
            return True
        if 'u' in config_content:
            webbrowser.open_new_tab(ubisoft_connect)
            return True
        else:
            print("Config Error!")
            logging.info("There was no u/s written in the config, but the script ran here? Fascinating!")
            sys.exit(1)


def print_empty(amount):
    for i in range(amount):
        print()


def enter_the_game():
    if locate_onScreen("cogs.png", 0.8, 500):
        press_buttons("up", 10, 0.2, None)
        press_button("down", 0.2)
        press_button("enter", 1)
        press_buttons("right", 2, 0.2, None)
        press_button("down", 0.2)
        press_button("enter", 1)
        press_button("right", 0.3)
        press_button("enter", 1)
        press_buttons("f", 2, 0.5, None)
        press_button("right", 0.2)
    if locate_onScreen("difficulty.png", 0.8, 20):
        press_button("enter", None)


def game_loop():
    while True:
        round_print()
        if locate_onScreen("cogs.png", 0.8, 100):
            press_buttons("enter", 3, 0.5, None)
        if locate_onScreen("bonus.png", 0.8, 500):
            press_button("tab", 1)
            press_button("enter", None)


print(''.join(colored_chars))
print('\033[39m')
setup()
start_time = time.time()

codes = vars(colorama.Fore)
colors = [codes[color] for color in codes if color not in bad_colors]
colored_lines = [random.choice(colors) + line for line in text.split('\n')]
print('\n'.join(colored_lines))
print('\033[39m')

enter_the_game()
time.sleep(5)

try:
    game_loop()
except Exception as e:
    print(e)
    error()

logging.info("You got to the end of the script, Fascinating!")
