import os
import time
import webbrowser


def clear():
   os.system('cls')

#------------------
clear()
print("polska wersja jezykowa wybrana \n")

python = input("masz zainstalowanego pythona na swoim kompie? T/N: ")
lower = python.lower()

if lower == "n":
    clear()
    print("to zainstaluj lol \n")
    time.sleep(1)
    webbrowser.open("https://www.python.org/downloads/")
else:
    print("to git")


instalation = input("czy chcesz zainstalowac wymagane komponenty? T/N:  ")
lower = instalation.lower()

if instalation == "n":
    clear()
    print("no ok jak chcesz, to nie bedzie moja wina jak cos ci dzialac nie bedzie \n")
    time.sleep(2)
else:
    clear()
    print("wspaniale\n w takim razie zaczynam instalajce")

    # installing remaining components
    os.system('pip install pyautogui')
    os.system('pip install keyboard')
    os.system('pip install playsound')
    # --------------------------------

from playsound import playsound
import pyautogui
import keyboard

print("autoclicker sie wlacza")
playsound('start.wav')

x = 3

clear()
cpsAmount = 10
clicks = 0
prefixLower = 'e'
settingsLower = 'a'
off = 0
clickLoop = 0
# ---------------------------

while True:
    # settings
    while True:
        keyboard.press_and_release('backspace')
        clear()
        print("Better auto clicker.exe settings\n"
        "zmiana prefixu kliknij: 'p' \n"
        "zmiana predkosci klikania kliknij: 's' (standardowo cps = 10): \n"
        "zmiana przycisku ustawien kliknij: 'a' \n"
        "jezeli nic nie chcesz zmieniac wpisz: 'd' \n"
        "----------------------------------------- \n"
        f"aktualny cps wynosi: {cpsAmount} \n"
        f"aktualny prefix {prefixLower} \n"
        f"prefix ustawien: {settingsLower}")
        
        settings = keyboard.read_key()
        keyboard.press_and_release('backspace')
        if settings == "d":
            clear()
            x = 3
            for i in range(3):
                print("ok odpalam program za 3 sekundy ")
                print(x)
                time.sleep(1)
                x -= 1
                clear() 
            break
        elif settings == "p":
            clear()
            keyboard.press_and_release('backspace')
            prefix = input("wpisz przycisk na klawiaturze ktory bedzie sluzyl do wlaczania klikera: ")
            prefixLower = prefix.lower()
            keyboard.press_and_release('backspace')
            clear()
        elif settings == "s":
            clear()
            keyboard.press_and_release('backspace')
            cpsAmount = input("nowa liczba cps: ")
            keyboard.press_and_release('backspace')
            clear()
        elif settings == "a":
            clear()
            keyboard.press_and_release('backspace')
            settingsPrefix = input("wpisz przycisk ktory bedzie odpowiadal za wchodzenie do opcji: ")
            settingsLower = settingsPrefix.lower()
            keyboard.press_and_release('backspace')
            clear()
        else:
            continue
    # ----------------------------------

    offLoop = 1
# actual clicker 
    while offLoop == 1:
        clear()
        print("Better auto clicker.exe \n"
            f"aktualny cps wynosi: {cpsAmount} \n"
            f"aktualny prefix: {prefixLower} \n"
            f"prefix ustawien: {settingsLower} \n"
            "------------------------------ \n"
            f"wlacz i wylacz poprzez nacisniecie '{prefixLower}' lub przejdz do opcji poprzez klikniecie '{settingsLower}'")
        escape = keyboard.read_key()
        
        if escape == prefixLower:
            clicksOff = 1
            time.sleep(1)
            playsound('pop.wav')

            while clicksOff == 1:
                if not keyboard.is_pressed(prefixLower):
                    clear()
                    print('kliker klika')
                    pyautogui.click(clicks=int(cpsAmount))
                else: 
                    clicksOff = 0
                    time.sleep(1)

        
        if escape == settingsLower:
            offLoop = 0
            time.sleep(1)
