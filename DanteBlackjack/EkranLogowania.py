import pygame
pygame.init()
from Button import *

class EkranLogowania:
    def Start(self, window, choice):
        pygame.time.Clock().tick(60)
        background = pygame.image.load('DanteBlackJack/Grafika/Tla/Ekran_Logowania.png')
        background = pygame.transform.scale(background, (resolutions[choice]))
        window.blit(background, (0, 0))
        button_log.tool_draw(window)
        pygame.display.update()