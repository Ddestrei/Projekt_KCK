import pygame

pygame.init()
from Screen import *


class StatisticsScreen(Screen):
    def __init__(self):
        self.start_poz_x = 126
        self.start_poz_y = 60
        self.USERS = [("Adrian", "123456", 3, 5, 5),
                      ("Maciej", "654321", 2, 3, 0),
                      ("Dorota", "135790", 6, 2, 5),
                      ("Andrzej", "323223", 6, 2, 5),
                      ("Marek", "543255", 6, 2, 5),
                      ("Adrian1", "123456", 3, 5, 5),
                      ("Maciej1", "654321", 2, 3, 0),
                      ("Dorota1", "135790", 6, 2, 5),
                      ("Andrzej1", "323223", 6, 2, 5),
                      ("Marek12", "543255", 6, 2, 5),
                      ("Adrian2", "123456", 3, 5, 5),
                      ("Maciej2", "654321", 2, 3, 0),
                      ("Dorota2", "135790", 6, 2, 5),
                      ("Andrzej2", "323223", 6, 2, 5),
                      ("Marek2", "543255", 6, 2, 5)
                      ]

    def Start(self, window, choice):
        self.window = window
        self.choice = choice

        pygame.time.Clock().tick(60)
        background = pygame.image.load(Rules_background_path)
        background = pygame.transform.scale(background, (resolutions[choice]))
        window.blit(background, (0, 0))

        StatisticsScreen_back.tool_draw(window)
        self.create_title_box()
        self.display_users()

        pygame.display.update()

    def create_title_box(self):
        pos_x, pos_y = scale_position(126, 60, self.choice)
        statistics_box = Tool(pos_x, pos_y, "statistics_box.png")
        statistics_box.tool_draw(self.window)
        name_text = pygame.font.Font(text_lobby_blackspace_path,
                                     scale_font(36, self.choice)).render(
            "NAME", True, (246, 181, 9))
        button_x, button_y = scale_position(176, 75, self.choice)
        self.window.blit(name_text, (button_x, button_y))

        index_text = pygame.font.Font(text_lobby_blackspace_path,
                                      scale_font(36, self.choice)).render(
            "INDEX", True, (5, 22, 160))
        button_x, button_y = scale_position(376, 75, self.choice)
        self.window.blit(index_text, (button_x, button_y))

        help_points_text = pygame.font.Font(text_lobby_blackspace_path,
                                            scale_font(36, self.choice)).render(
            "HELP_POINTS", True, (169, 1, 187))
        button_x, button_y = scale_position(576, 75, self.choice)
        self.window.blit(help_points_text, (button_x, button_y))

        wins_text = pygame.font.Font(text_lobby_blackspace_path,
                                     scale_font(36, self.choice)).render(
            "WINS", True, (9, 168, 13))
        button_x, button_y = scale_position(876, 75, self.choice)
        self.window.blit(wins_text, (button_x, button_y))

        loses_text = pygame.font.Font(text_lobby_blackspace_path,
                                      scale_font(36, self.choice)).render(
            "LOSES", True, (187, 4, 4))
        button_x, button_y = scale_position(1076, 75, self.choice)
        self.window.blit(loses_text, (button_x, button_y))

    def create_box(self, pos_y, name, index, help_points, wins, loses):
        pos_x, pos_y = scale_position(126, pos_y, self.choice)
        statistics_box = Tool(pos_x, pos_y, "statistics_box.png")
        statistics_box.tool_draw(self.window)

        name_text = pygame.font.Font(text_lobby_blackspace_path,
                                     scale_font(30, self.choice)).render(
            f"{name}", True, (246, 181, 9))
        button_x, button_y = scale_position(176, pos_y + 15, self.choice)
        self.window.blit(name_text, (button_x, button_y))

        index_text = pygame.font.Font(text_lobby_blackspace_path,
                                      scale_font(30, self.choice)).render(
            f"{index}", True, (5, 22, 160))
        button_x, button_y = scale_position(376, pos_y + 15, self.choice)
        self.window.blit(index_text, (button_x, button_y))

        help_points_text = pygame.font.Font(text_lobby_blackspace_path,
                                            scale_font(36, self.choice)).render(
            f"{help_points}", True, (169, 1, 187))
        button_x, button_y = scale_position(676, pos_y + 15, self.choice)
        self.window.blit(help_points_text, (button_x, button_y))

        wins_text = pygame.font.Font(text_lobby_blackspace_path,
                                     scale_font(36, self.choice)).render(
            f"{wins}", True, (9, 168, 13))
        button_x, button_y = scale_position(901, pos_y + 15, self.choice)
        self.window.blit(wins_text, (button_x, button_y))

        loses_text = pygame.font.Font(text_lobby_blackspace_path,
                                      scale_font(36, self.choice)).render(
            f"{loses}", True, (187, 4, 4))
        button_x, button_y = scale_position(1120, pos_y + 15, self.choice)
        self.window.blit(loses_text, (button_x, button_y))

    def display_users(self):
        i = 1
        for user in self.USERS:
            if i > 10:
                break
            self.create_box(i * 80 + 60, user[0], user[1], user[2], user[3], user[4])
            i += 1
