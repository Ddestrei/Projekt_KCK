import pygame
pygame.init()
from Button import *

class EkranStartuGry:
    def Start(self, window, choice):
        pygame.time.Clock().tick(60)
        window.fill((255, 0, 255)) #tymczasowe
        button_1.button_draw(window)
        button_2.button_draw(window)
        pygame.display.update()
