import pygame

pygame.init()
from Screen import *


class DanteBlackjackStartScreen(Screen):
    def __init__(self):
        self.name = "Whatever"
        self.points = 10
        self.IsAdmin = False

    def Start(self, window, choice):
        pygame.time.Clock().tick(60)
        background = pygame.image.load('DanteBlackJack/Grafika/Tla/StartScreen_background.png')
        background = pygame.transform.scale(background, (resolutions[choice]))
        window.blit(background, (0, 0))

        x, y = scale_position(586, 35, choice)
        logo = Tool(x, y, "/StartScreenGraphics/logo.png")
        logo.tool_draw(window)

        x, y = scale_position(179, 148, choice)
        name_box = Tool(x, y, "/StartScreenGraphics/StartScreen_info.png")
        name_box.tool_draw(window)

        x, y = scale_position(179, 213, choice)
        points_box = Tool(x, y, "/StartScreenGraphics/StartScreen_info.png")
        points_box.tool_draw(window)

        x, y = scale_position(139, 148, choice)
        icon_box = Tool(x, y, "/StartScreenGraphics/icon.png")
        icon_box.tool_draw(window)

        name_text = pygame.font.Font("DanteBlackJack/Grafika/Czcionki/Aptos.ttf",
                                     scale_font(34, choice)).render(
            self.name, True,
            (255, 255, 255))
        window.blit(name_text, scale_position(199, 145, choice))

        points_text = pygame.font.Font("DanteBlackJack/Grafika/Czcionki/Aptos.ttf",
                                       scale_font(30, choice)).render(
            "POINTS: " + str(self.points), True,
            (255, 255, 255))
        window.blit(points_text, scale_position(199, 215, choice))



        StartGameButton.tool_draw(window)
        RulesButton.tool_draw(window)
        SettingsButton.tool_draw(window)
        ExitGameButton.tool_draw(window)

        if self.IsAdmin:
            StatisticsButton.tool_draw(window)

        pygame.display.update()

    def getIsAdmin(self):  # temporary method
        return self.IsAdmin
