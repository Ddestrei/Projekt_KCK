import pygame

pygame.init()
from Screen import *
from Client import Client


class LobbyScreen(Screen):
    def __init__(self, client: Client):
        self.client = client
        self.choice = None
        self.window = None
        self.tables_positions = [
            (99, 195),
            (545, 195),
            (979, 195),
            (99, 577),
            (545, 577),
            (979, 577)
        ]
        self.number_of_tables = 0
        self.array_of_number_of_players = []
        self.array_of_bets = []
        self.tables = None

    def Start(self, window, choice):
        self.initialise()
        self.window = window
        self.choice = choice
        self.table_button_array = []
        self.lobby_add_table = None

        pygame.time.Clock().tick(60)
        background = pygame.image.load(Lobby_background_path)
        background = pygame.transform.scale(background, (resolutions[self.choice]))
        self.window.blit(background, (0, 0))

        lobby_to_Menu_button.tool_draw(self.window)

        x, y = scale_position(498, 34, choice)
        lobby_blackspace_box = Tool(x, y, "lobby_blackspace.png")
        lobby_blackspace_box.tool_draw(window)

        text_lobby_blackspace = pygame.font.Font(text_lobby_blackspace_path,
                                                 scale_font(36, choice)).render(
            "Choose table to play", True,
            (242, 120, 27))  # Renderowanie tekstu
        self.window.blit(text_lobby_blackspace, scale_position(574, 50, choice))  # Wyświetlenie tekstu

        self.table_button_array, self.lobby_add_table = self.display_tables(self.number_of_tables,
                                                                            self.array_of_number_of_players,
                                                                            self.array_of_bets)

        # print(slider.get_value())

        pygame.display.update()

    def create_table(self, table_x, table_y, bet, number_of_players):
        button_x, button_y = scale_position(table_x, table_y, self.choice)
        table_button = Button(button_x, button_y, "lobby_table.png")
        table_button.tool_draw(self.window)

        text_lobby_blackspace = pygame.font.Font(text_lobby_blackspace_path,
                                                 scale_font(36, self.choice)).render(
            f"{bet}", True, (179, 38, 30))
        button_x, button_y = scale_position(table_x + 164, table_y + 8, self.choice)
        self.window.blit(text_lobby_blackspace, (button_x, button_y))

        button_x, button_y = scale_position(table_x + 91, table_y + 263, self.choice)
        match number_of_players:
            case 1:
                x, y = scale_position(table_x + 91, table_y + 263, self.choice)
                lobby_players1 = Tool(x, y, lobby_players1_path)
                lobby_players1.tool_draw(self.window)
            case 2:
                x, y = scale_position(table_x + 91, table_y + 263, self.choice)
                lobby_players2 = Tool(x, y, lobby_players2_path)
                lobby_players2.tool_draw(self.window)
            case 3:
                x, y = scale_position(table_x + 91, table_y + 263, self.choice)
                lobby_players3 = Tool(x, y, lobby_players3_path)
                lobby_players3.tool_draw(self.window)
            case 4:
                x, y = scale_position(table_x + 91, table_y + 263, self.choice)
                lobby_players4 = Tool(x, y, lobby_players4_path)
                lobby_players4.tool_draw(self.window)

        return table_button

    def display_tables(self, number_of_tables, array_of_number_of_players, array_of_bets):
        table_button_array = []
        lobby_add_table = None

        if number_of_tables >= 1:
            button = self.create_table(self.tables_positions[0][0], self.tables_positions[0][1], array_of_bets[0],
                                       array_of_number_of_players[0])
            table_button_array.append(button)

        if number_of_tables >= 2:
            button = self.create_table(self.tables_positions[1][0], self.tables_positions[1][1], array_of_bets[1],
                                       array_of_number_of_players[1])
            table_button_array.append(button)

        if number_of_tables >= 3:
            button = self.create_table(self.tables_positions[2][0], self.tables_positions[2][1], array_of_bets[2],
                                       array_of_number_of_players[2])
            table_button_array.append(button)

        if number_of_tables >= 4:
            button = self.create_table(self.tables_positions[3][0], self.tables_positions[3][1], array_of_bets[3],
                                       array_of_number_of_players[3])
            table_button_array.append(button)

        if number_of_tables >= 5:
            button = self.create_table(self.tables_positions[4][0], self.tables_positions[4][1], array_of_bets[4],
                                       array_of_number_of_players[4])
            table_button_array.append(button)

        if number_of_tables == 6:
            button = self.create_table(self.tables_positions[5][0], self.tables_positions[5][1], array_of_bets[5],
                                       array_of_number_of_players[5])
            table_button_array.append(button)

        if number_of_tables < 6:
            lobby_add_table = Button(self.tables_positions[number_of_tables][0],
                                     self.tables_positions[number_of_tables][1], "lobby_add_table.png")
            lobby_add_table.tool_draw(self.window)

        return table_button_array, lobby_add_table

    def initialise(self):
        self.tables = self.client.tableManager.tables
        self.number_of_tables = self.client.tableManager.tables.__len__()
        for table in self.client.tableManager.tables:
            self.array_of_number_of_players.append(table.amount_users)
            self.array_of_bets.append(0.5)
