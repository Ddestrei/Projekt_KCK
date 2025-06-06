import pygame
pygame.init()
from Screen import *

class EkranStartuGry(Screen):
    def Start(self, window, choice):
        pygame.time.Clock().tick(60)
        window.fill((255, 0, 255)) #tymczasowe
        button_1.tool_draw(window)
        button_2.tool_draw(window)
        pygame.display.update()