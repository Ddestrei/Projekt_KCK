import pygame
pygame.init()
from Screen import *

class EkranLogowania(Screen):
    def Start(self, window, choice):
        pygame.time.Clock().tick(60)
        background = pygame.image.load('DanteBlackJack/Grafika/Tla/Ekran_Logowania.png')
        background = pygame.transform.scale(background, (resolutions[choice]))
        window.blit(background, (0, 0))
        button_log.tool_draw(window)
        username.tool_draw(window)
        username.render_text(window)
        password.tool_draw(window)
        password.render_text(window)
        pygame.display.update()