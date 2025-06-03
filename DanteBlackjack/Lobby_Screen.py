import pygame

pygame.init()
from Screen import *


# to-do list:
# -create screen skeleton with [background], [back-button] in top left corner of screen,
#   [choose table to play] information in the middle of screen, [add_table_button] and [table buttons]
#
# -create method that creates [table-button with information about bet]
#    and below it [number of players in this table]
#
# - create method [display] which displays all current tables and [add_table_button]
#
# - [table-button] have to send [table-number] to server
#
# -create [add_table_button] with [mini-screen]
#    mini-screen have to have: [minimal bets to choose] and [max number of players](?)


class Lobby_Screen(Screen):
    def Start(self, window, choice):
        self.window = window
        self.choice = choice

        pygame.time.Clock().tick(60)
        background = pygame.image.load('DanteBlackJack/Grafika/Tla/background_lobby.png')
        background = pygame.transform.scale(background, (resolutions[self.choice]))
        self.window.blit(background, (0, 0))

        lobby_to_Menu_button.tool_draw(self.window)


        # lobby_add_table.tool_draw(window)

        lobby_blackspace = pygame.image.load("DanteBlackJack/Grafika/Obiekty/lobby_blackspace.png")
        self.window.blit(lobby_blackspace, (498, 34))

        text_lobby_blackspace = pygame.font.Font("DanteBlackJack/Grafika/Czcionki/Aptos.ttf", 36).render("Choose table to play", True,
    (242, 120, 27))  # Renderowanie tekstu
        self.window.blit(text_lobby_blackspace, (574, 50))  # Wyświetlenie tekstu

        self.create_table(99, 165, 0.5, 3)


        pygame.display.update()

    def create_table(self, table_x, table_y, bet, number_of_players):
        button_x, button_y = scale_position(table_x, table_y, self.choice)
        table_button = Button(button_x, button_y, "table.png")
        table_button.tool_draw(self.window)

        text_lobby_blackspace = pygame.font.Font("DanteBlackJack/Grafika/Czcionki/Aptos.ttf", 36).render(
            f"{bet}", True, (179, 38, 30))
        button_x, button_y = scale_position(table_x + 164, table_y + 8, self.choice)
        self.window.blit(text_lobby_blackspace, (button_x, button_y))

        button_x, button_y = scale_position(table_x + 91, table_y + 263, self.choice)
        match number_of_players:
            case 1:
                lobby_players1 = pygame.image.load("DanteBlackJack/Grafika/Obiekty/lobby_players1.png")
                self.window.blit(lobby_players1, (button_x, button_y))
            case 2:
                lobby_players2 = pygame.image.load("DanteBlackJack/Grafika/Obiekty/lobby_players2.png")
                self.window.blit(lobby_players2, (button_x, button_y))
            case 3:
                lobby_players3 = pygame.image.load("DanteBlackJack/Grafika/Obiekty/lobby_players3.png")
                self.window.blit(lobby_players3, (button_x, button_y))
            case 4:
                lobby_players4 = pygame.image.load("DanteBlackJack/Grafika/Obiekty/lobby_players4.png")
                self.window.blit(lobby_players4, (button_x, button_y))

        return table_button