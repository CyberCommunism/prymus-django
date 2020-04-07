import os
from time import sleep
import sys
import random
from pathlib import Path
def pobierz_slowo():
    filepath = Path("dane.txt")
    if filepath.is_file():
        data = open(filepath, 'r').read()
        lines = data.split('\n')
        ile_lini = len(lines)
        number = random.randint(0, ile_lini)
        wynik = lines[number]
    else :
        print("nie ma takiego pliku")
    return wynik
def wisielec_3():
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬████████████████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬██╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬█╬╬╬╬╬╬█╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬█████████████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬██╬╬╬██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬████████████████████████████╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
def wisielec_2_1():
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬████████████████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬█╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬████████████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬████████████████████████████╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
def wisielec_2_2():
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬████████████████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬██╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬█╬╬╬╬╬╬█╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬█████████████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬████████████████████████████╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
def wisielec_2():
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬████████████████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬██╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬█╬╬╬╬╬╬█╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬█████████████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬████████████████████████████╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
def wisielec_1():
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬████████████████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬████████████████████████████╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
def wisielec_0():
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬████████████████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬████████████████████████████╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")

def wypisz_postep(czy_ok,litera,slowo,postep):
    if czy_ok == 0:
        return postep
    else:
        result = ""
        for i in range(len(slowo)):
            if litera == slowo[i]:
                result = result + litera
            else:
                result = result + postep[i]
        return result



if __name__ == '__main__':
    #===============================================================
    flaga = 1
    ile_prob_zostalo_int = 0
    poziom = 0
    while flaga:
        os.system("cls")

        print("Cześć jestem Hangman :D")
        print("Wybierz poziom trudności (wpisz 1 lub 2 lub 3):")
        print("1. łatwy")
        print("2. średni")
        print("3. trudny")
        poziom = str(input("wybieram: "))
        if len(poziom) == 1:
            if ord(poziom) >= 49 and ord(poziom) <= 51:
                poziom = ord(poziom) - 48
                flaga = 0
            else:
                print("To nie jest liczba naturalna od 1 do 3 włącznie")
                sleep(3)
        else:
            print("To nie jest liczba naturalna od 1 do 3 włącznie")
            sleep(3)
    # ==============================================================
    slowo_str = str(pobierz_slowo())
    jeszcze_gram_bool = 1
    if poziom == 1:
        ile_prob_zostalo_int = 5
    elif poziom == 2:
        ile_prob_zostalo_int = 4
    elif poziom == 3:
        ile_prob_zostalo_int = 3
    postep = "_" * len(slowo_str)
    uzyte_znaki_arr = []
    #===============================================================
    os.system("cls")
    print("Wylosowalem jakies slowo o dlugosci: ", len(slowo_str))
    print("Wpisz literkę a ja powiem Ci czy trafiłes, jak pomylisz się ", ile_prob_zostalo_int, " razy przegrywasz!")
    sleep(4)
    os.system("cls")
    while jeszcze_gram_bool:
        print("Zostalo Ci ",ile_prob_zostalo_int," prób.")
        print("========================================")
        print(postep)
        print("========================================")
        if poziom == 1:
            if ile_prob_zostalo_int == 5:
                wisielec_0()
            elif ile_prob_zostalo_int == 4:
                wisielec_1()
            elif ile_prob_zostalo_int == 3:
                wisielec_2_1()
            elif ile_prob_zostalo_int == 2:
                wisielec_2_2()
            elif ile_prob_zostalo_int == 1:
                wisielec_2()
        elif poziom == 2:
            if ile_prob_zostalo_int == 4:
                wisielec_0()
            elif ile_prob_zostalo_int == 3:
                wisielec_1()
            elif ile_prob_zostalo_int == 2:
                wisielec_2()
            elif ile_prob_zostalo_int == 1:
                wisielec_2_2()
        elif poziom == 3:
            if ile_prob_zostalo_int == 3:
                wisielec_0()
            elif ile_prob_zostalo_int == 2:
                wisielec_2()
            elif ile_prob_zostalo_int == 1:
                wisielec_2_2()
        print("========================================")

        znak_uzytkownika_str = str(input("wpisz literkę: "))

        if len(znak_uzytkownika_str) != 1:
            print("Zła długość twojej odpowiedzi, wpisz literkę jeszcze raz")
            if poziom == 3 or poziom == 2:
                ile_prob_zostalo_int-=1
        else:
            znak_uzytkownika_int = ord(znak_uzytkownika_str)
            if (znak_uzytkownika_int >= 65 and znak_uzytkownika_int <= 90) or ( znak_uzytkownika_int >= 97 and znak_uzytkownika_int <= 122 ) or znak_uzytkownika_int == 45:
                if znak_uzytkownika_str in uzyte_znaki_arr:
                    print("już to podałeś")
                    if poziom == 3:
                        ile_prob_zostalo_int-=1
                else:
                    uzyte_znaki_arr.append(znak_uzytkownika_str)
                    if znak_uzytkownika_str in slowo_str:
                        print("Trafiles")
                        postep = wypisz_postep(1,znak_uzytkownika_str,slowo_str,postep)
                        k = bool('_' in postep)
                        if not k:
                            sleep(1)
                            os.system("cls")
                            print("WYGRALES")
                            sleep(3)
                            sys.exit(0)
                    else:
                        print("Pudło")
                        postep = wypisz_postep(1, znak_uzytkownika_str, slowo_str,postep)
                        ile_prob_zostalo_int-=1
                        if ile_prob_zostalo_int==0:
                            jeszcze_gram_bool = 0
                            os.system("cls")
                            print("========================================")
                            wisielec_3()
                            print("========================================")
                            print("Przegrałeś")
                            sleep(3)
                            sys.exit(0)
            else:
                if poziom==3 or poziom == 2:
                    ile_prob_zostalo_int-=1
                print("zly znak, wpisz jeszcze raz jakąś LITERE !!!")
        sleep(1)
        os.system("cls")
