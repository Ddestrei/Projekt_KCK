import pygame

pygame.init()
from Screen import *


class DanteBlackjackStartScreen(Screen):
    def __init__(self):
        self.IsAdmin = True

    def Start(self, window, choice):
        pygame.time.Clock().tick(60)
        background = pygame.image.load('DanteBlackJack/Grafika/Tla/StartScreen_background.png')
        background = pygame.transform.scale(background, (resolutions[choice]))
        window.blit(background, (0, 0))

        logo = pygame.image.load('DanteBlackJack/Grafika/Obiekty/StartScreenGraphics/logo.png')
        window.blit(logo, (586, 35))

        StartGameButton.tool_draw(window)
        RulesButton.tool_draw(window)
        SettingsButton.tool_draw(window)
        ExitGameButton.tool_draw(window)

        if self.IsAdmin:
            StatisticsButton.tool_draw(window)

        pygame.display.update()
