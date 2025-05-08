import pygame
pygame.init()
from Button import *

class EkranLogowania:
    def Start(self, window, choice):
        pygame.time.Clock().tick(60)
        background = pygame.image.load('DanteBlackJack/grafika/tla/Ekran_Logowania.png')
        background = pygame.transform.scale(background, (resolutions[choice]))
        window.blit(background, (0, 0))
        button_log.button_draw(window)
        pygame.display.update()