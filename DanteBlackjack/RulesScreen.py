import pygame

pygame.init()
from Screen import *


class RulesScreen(Screen):

    def Start(self, window, choice):
        pygame.time.Clock().tick(60)
        background = pygame.image.load(Rules_background_path)
        background = pygame.transform.scale(background, (resolutions[choice]))

        game_rules = (
            "Goal of the Game\n"
            "The goal is to get a hand total as close to 21 as possible without going over, and to beat the dealer's hand.\n\n"

            "Card Values\n"
            "\tCards 2 through 10 - face values\n"
            "\tJack (J), Queen (Q), King (K) – each counts as 10.\n"
            "\tAce (A) counts as 1 or 11, whichever is more favorable for the player.\n\n"

            "Players\n"
            "\tOne or more players.\n"
            "\tThe dealer (the house, opponent of all players).\n\n"

            "How the Game Works\n"
            "  1. Dealing the Cards:\n"
            "\tEach player and the dealer receive two cards.\n"
            "\tPlayers see both of their own cards.\n"
            "\tThe dealer shows one card face up, the other is hidden (face down)\n\n"

            "  2. Player's Turn:\n"
            "\tHit - take another card.\n"
            "\tStand - stop taking cards,\n"
            "\tDouble - double the bet, take one final card.\n\n"

            "  3. Dealer's Turn:\n"
            "\tDealer reveals the hidden card.\n"
            "\tMust draw cards until the total is 17 or higher.\n"
            "\tDealer must hit on 16 or less, and stand on 17 or more.\n\n"

            "Winning or Losing\n"
            "\tIf a player goes over 21 - bust (automatic loss).\n"
            "\tIf the dealer busts and the player doesn't - player wins.\n"
            "\tIf player has a higher total than the dealer - player wins.\n"
            "\tIf dealer has a higher total - player loses.\n"
            "\tIf both have the same total - it's a push (tie, bet is returned).\n"
        )
        game_rules = game_rules.replace('\t', '        ')  # np. 4 spacje

        window.blit(background, (0, 0))
        game_rules_lines = game_rules.splitlines()  # dzieli tekst po \n
        font = pygame.font.Font(text_lobby_blackspace_path, scale_font(22, choice))
        y = 10  # początkowa pozycja y

        for line in game_rules_lines:
            text_surface = font.render(line, True, (255, 255, 255))
            window.blit(text_surface, (10, y))
            y += font.get_linesize()  # przesunięcie w dół o wysokość linii

        RulesScreen_back.tool_draw(window)

        pygame.display.update()
