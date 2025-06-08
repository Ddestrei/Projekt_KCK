import pygame
pygame.init()
from Screen import *

class DanteBlackjackStartScreen(Screen):
    def Start(self, window, choice):
        pygame.time.Clock().tick(60)
        window.fill((255, 0, 255)) #tymczasowe
        ExitGameButton.tool_draw(window)
        StartGameButton.tool_draw(window)
        pygame.display.update()





