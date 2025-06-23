from Screen import *

class DanteScreen(Screen):
    def Start(self, window, choice):
        Dante_background = pygame.image.load('Grafika/Tla/danteekran.png')
        Dante_background = pygame.transform.scale(Dante_background, (resolutions[choice]))
        window.blit(Dante_background, (0, 0))
        house_button.tool_draw(window)
        pygame.display.update()

