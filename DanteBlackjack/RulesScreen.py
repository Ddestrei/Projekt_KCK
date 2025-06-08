import pygame

pygame.init()
from Screen import *


class RulesScreen(Screen):

    def Start(self, window, choice):
        pygame.time.Clock().tick(60)
        background = pygame.image.load('DanteBlackJack/Grafika/Tla/Rules_background.png')
        background = pygame.transform.scale(background, (resolutions[choice]))
        window.blit(background, (0, 0))

        RulesScreen_back.tool_draw(window)

        pygame.display.update()
