import pygame

pygame.init()
from Screen import *
from Client import Client


class DanteBlackjackStartScreen(Screen):
    def __init__(self, client: Client):
        self.IsAdmin = None
        self.points = None
        self.name = None
        self.client = client

    def Start(self, window, choice):
        # dodanie informacji o użytkowniku
        self.name = self.client.user.name
        self.points = self.client.user.points
        self.IsAdmin = self.client.user.is_admin
        pygame.time.Clock().tick(60)
        background = pygame.image.load(StartScreenPath)
        background = pygame.transform.scale(background, (resolutions[choice]))
        window.blit(background, (0, 0))

        x, y = scale_position(586, 35, choice)
        logo = Tool(x, y, "StartScreenGraphics/logo.png")
        logo.tool_draw(window)

        x, y = scale_position(179, 148, choice)
        name_box = Tool(x, y, "StartScreenGraphics/StartScreen_info.png")
        name_box.tool_draw(window)

        x, y = scale_position(179, 213, choice)
        points_box = Tool(x, y, "StartScreenGraphics/StartScreen_info.png")
        points_box.tool_draw(window)

        x, y = scale_position(139, 148, choice)
        icon_box = Tool(x, y, "StartScreenGraphics/icon.png")
        icon_box.tool_draw(window)

        name_text = pygame.font.Font(name_text_path,
                                     scale_font(34, choice)).render(
            self.name, True,
            (255, 255, 255))
        window.blit(name_text, scale_position(199, 145, choice))

        points_text = pygame.font.Font(points_text_path,
                                       scale_font(30, choice)).render(
            "POINTS: " + str(self.points), True,
            (255, 255, 255))
        window.blit(points_text, scale_position(199, 215, choice))

        StartGameButton.tool_draw(window)
        RulesButton.tool_draw(window)
        SettingsButton.tool_draw(window)
        ExitGameButton.tool_draw(window)
        StatisticsButton.tool_draw(window)

        # if self.IsAdmin:  < -- add this later
        #     StatisticsButton.tool_draw(window)

        pygame.display.update()
