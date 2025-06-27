import pygame
pygame.init()
from Screen import *

class DanteStartScreen(Screen):
    def __init__(self):
        self.punkty_pomocy = 10 #tymczasowe
    def Start(self, window, choice):
        pygame.time.Clock().tick(60)
        background = pygame.image.load(StartScreen_background_path)
        background = pygame.transform.scale(background, (resolutions[choice]))
        window.blit(background, (0, 0))
        dante_start_screen_to_dante_blackjack_start_screen.tool_draw(window)
        topics_button.tool_draw(window)
        #punkty_pomocy_image = pygame.font.Font.render(pygame.font.SysFont("arial", 48),f"Punkty pomocy: {self.punkty_pomocy}", True,(0, 0, 0)) #tymczasowe
        # pygame
        pygame.display.update()
