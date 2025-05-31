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

class Button:
    def __init__(self, x, y, image, scale=1, hover_image=None, enabled=True):
        width = image.get_width()
        height = image.get_height()
        self.base_image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.hover_image = pygame.transform.scale(hover_image, (int(width * scale), int(height * scale))) if hover_image else self.base_image
        self.image = self.base_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False
        self.enabled = enabled

    def draw(self):
        action = False
        mouse_pos = pygame.mouse.get_pos()

        if self.enabled:
            self.image = self.hover_image if self.rect.collidepoint(mouse_pos) else self.base_image
        else:
            self.image = self._dim_image(self.base_image)

        screen.blit(self.image, (self.rect.x, self.rect.y))

        if self.enabled and pygame.mouse.get_pressed()[0] and self.rect.collidepoint(mouse_pos):
            if not self.clicked:
                self.clicked = True
                action = True
        elif not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        return action

    def set_enabled(self, value: bool):
        self.enabled = value

    def _dim_image(self, image):
        dimmed = image.copy()
        dimmed.fill((180, 180, 180, 200), None, pygame.BLEND_RGBA_MULT)
        return dimmed


