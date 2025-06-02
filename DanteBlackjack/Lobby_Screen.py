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
        pygame.time.Clock().tick(60)
        background = pygame.image.load('DanteBlackJack/Grafika/Tla/background_lobby.png')
        background = pygame.transform.scale(background, (resolutions[choice]))
        window.blit(background, (0, 0))

        lobby_to_Menu_button.tool_draw(window)
        lobby_add_table.tool_draw(window)

        lobby_blackspace = pygame.image.load("DanteBlackJack/Grafika/Obiekty/lobby_blackspace.png")

        text = pygame.font.Font("DanteBlackJack/Grafika/Czcionki/Aptos.ttf", 10).render("Choose table to play", True,
    (242, 120, 27))  # Renderowanie tekstu
        window.blit(text, (100, 100))  # Wyświetlenie tekstu

        window.blit(lobby_blackspace, (300, 200))

        pygame.display.update()
