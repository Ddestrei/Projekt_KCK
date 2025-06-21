from Client import Client
from Screen import *


class LoginDanteScreen(Screen):

    def __init__(self, client: Client):
        self.client = client

    def Start(self, window, choice):
        pygame.time.Clock().tick(60)
        background = pygame.image.load('Grafika/Tla/Ekran_Logowania.png')
        background = pygame.transform.scale(background, (resolutions[choice]))
        window.blit(background, (0, 0))
        button_log.tool_draw(window)
        username.tool_draw(window)
        username.render_text(window)
        password.tool_draw(window)
        password.render_text(window)
        pygame.display.update()

    def login(self):
        self.client.login_to_server(username.get_text(),password.get_text())