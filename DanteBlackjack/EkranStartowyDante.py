import pygame
pygame.init()
from Button import *

class EkranStartowyDante:
    def __init__(self):
        self.punkty_pomocy = 10 #tymczasowe
    def Start(self, window):
        pygame.time.Clock().tick(60)
        window.fill((255, 255, 255)) #tymczasowe
        button_0.button_draw(window)
        punkty_pomocy_image = pygame.font.Font.render(pygame.font.SysFont("arial", 48),
                                                      f"Punkty pomocy: {self.punkty_pomocy}", True,
                                                      (0, 0, 0)) #tymczasowe

        window.blit(punkty_pomocy_image, (0, 0))
        pygame.display.update()