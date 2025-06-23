from time import sleep

from DanteStartScreen import *
from DanteBlackjackStartScreen import *
from LobbyScreen import *
from LoginDanteScreen import *
from RulesScreen import *
from DanteScreen import *
from GameScreen import GameScreen
# ustawienie klienta
from Client import Client
from TableManager import TableManager
client = Client()
tableManager = TableManager()
client.set_table_manager(tableManager=tableManager)

window = pygame.display.set_mode(resolutions[choice])

login_dante_screen = LoginDanteScreen(client)
dante_start_screen = DanteStartScreen()
dante_blackjack_start_screen = DanteBlackjackStartScreen(client)
lobby_screen = LobbyScreen(client)
rules_screen = RulesScreen()
GameScreen = GameScreen(client)
dante_screen = DanteScreen()
current_screen = login_dante_screen
button_stop = False

#Creating basic text for blackjack





while running:
    current_screen.Start(window, choice)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # ekran logowania
            if button_log.tool_click_left() and current_screen == login_dante_screen:
                # dodanie możliwości logowania do gry
                login_dante_screen.login()
                while client.received_logging_answer is False:
                    pass
                if client.is_logged:
                    username.status_set_0()
                    current_screen = dante_start_screen
            if username.tool_click_left() and current_screen == login_dante_screen:
                username.status_set_1()
                password.status_set_0()
            if password.tool_click_left() and current_screen == login_dante_screen:
                password.status_set_1()
                username.status_set_0()
            # ekran startowy dante
            if dante_start_screen_to_dante_blackjack_start_screen.tool_click_left() and current_screen == dante_start_screen:
                current_screen = dante_blackjack_start_screen
            if topics_button.tool_click_left() and current_screen == dante_start_screen:
                current_screen = dante_screen
            # ekran dante
            if house_button.tool_click_left() and current_screen == dante_screen:
                current_screen = dante_start_screen
            # ekran startu gry
            if ExitGameButton.tool_click_left() and current_screen == dante_blackjack_start_screen:
                current_screen = dante_start_screen
            if StartGameButton.tool_click_left() and current_screen == dante_blackjack_start_screen:
                button_stop = True
                current_screen = lobby_screen

            # ekran zasad
            if RulesButton.tool_click_left() and current_screen == dante_blackjack_start_screen:
                current_screen = rules_screen

            if RulesScreen_back.tool_click_left() and current_screen == rules_screen:
                current_screen = dante_blackjack_start_screen

            # ekran wybor stolu
            if current_screen == lobby_screen:
                current_screen.Start(window, choice)
                if current_screen.lobby_add_table is not None and current_screen.lobby_add_table.tool_click_left():
                    poz_x, poz_y = scale_position(current_screen.tables_positions[current_screen.number_of_tables][0],
                                                  current_screen.tables_positions[current_screen.number_of_tables][
                                                      1] + 200, choice)
                    get_min_bet = Button(poz_x, poz_y, "hit.png")
                    if get_min_bet.tool_click_left():
                        client.create_table(1)
                        sleep(2)
                        GameScreen.set_table(client.table)
                        current_screen = GameScreen
                        print("33")
                if current_screen != GameScreen:
                    for i in range(len(current_screen.table_button_array)):
                        if current_screen.table_button_array[i].tool_click_left() and button_stop == False:
                            print(i)
            if lobby_to_Menu_button.tool_click_left() and current_screen == lobby_screen:
                current_screen = dante_blackjack_start_screen
            #if current_screen == GameScreen:
            #    GameScreen.Start(window, choice)

        # ekran logowania
        if current_screen == login_dante_screen:
            username.writing(event)
            password.writing(event)
        button_stop = False
