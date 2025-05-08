import pygame
pygame.init()
from Button import *

class EkranWyboruStolu:
    def Start(self, window, choice):
        pygame.time.Clock().tick(60)
        window.fill((255, 255, 0)) #tymczasowe
        button_3.tool_draw(window)
        pygame.display.update()