import pygame

pygame.init()
from Screen import *


class DanteBlackjackStartScreen(Screen):
    def __init__(self):
        self.isadmin = 0

    def Start(self, window, choice):
        pygame.time.Clock().tick(60)
        background = pygame.image.load('DanteBlackJack/Grafika/Tla/StartScreen_background.png')
        background = pygame.transform.scale(background, (resolutions[choice]))
        window.blit(background, (0, 0))

        logo = pygame.image.load('DanteBlackJack/Grafika/Obiekty/StartScreenGraphics/logo.png')
        window.blit(logo, (589, 22))

        ExitGameButton.tool_draw(window)
        StartGameButton.tool_draw(window)
        pygame.display.update()

        if self.isadmin:
            print("aa")
