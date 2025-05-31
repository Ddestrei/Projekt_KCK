import random
from contextlib import nullcontext
import time
import pygame
from pygame.locals import *
import sys

resolutions = [(874, 620), (1166, 826), (1457, 1033)]
percents = [0.6, 0.8, 1]

print("Wybierz rozdzielczość aby rozpocząć:")
for i, res in enumerate(resolutions):
    print(f"{i + 1}. {res[0]}x{res[1]}")

choice = int(input("Twój wybór: ")) - 1

def scale_position(x, y, choice):
    if choice != 2:
        if choice == 0:
            x = 0.6 * x
            y = 0.6 * y
            return round(x), round(y)
        elif choice == 1:
            x = 0.8 * x
            y = 0.8 * y
            return round(x), round(y)
    return x, y


screenWidth, screenHeight = 1457, 1033
screenWidth,screenHeight = scale_position(screenWidth,screenHeight,choice)
screen = pygame.display.set_mode((screenWidth,screenHeight))
