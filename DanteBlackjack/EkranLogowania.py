import pygame
pygame.init()
from Button import *

class EkranLogowania:
    def Start(self, window):
        pygame.time.Clock().tick(60)
        window.fill((0, 0, 0)) #tymczasowe
        button_log.button_draw(window)
        pygame.display.update()