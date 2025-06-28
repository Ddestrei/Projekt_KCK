from time import sleep

# ustawienie klienta
from DanteBlackjackStartScreen import *
from DanteScreen import *
from DanteStartScreen import *
from DanteTaskScreen import *
from DanteWorkScreen import *
from GameScreen import GameScreen
from LobbyScreen import *
from LoginDanteScreen import *
from RulesScreen import *
from SettingsScreen import *
from StatisticsScreen import *
from TableManager import TableManager
from Task import Task
from Task import torch_table

client = Client()
tableManager = TableManager()
client.set_table_manager(tableManager=tableManager)

window = pygame.display.set_mode(resolutions[choice])

background_music = pygame.mixer.Sound(background_music_path)
background_music.set_volume(0.1)

login_dante_screen = LoginDanteScreen(client)
dante_start_screen = DanteStartScreen()
dante_blackjack_start_screen = DanteBlackjackStartScreen(client)
lobby_screen = LobbyScreen(client)
rules_screen = RulesScreen()
current_screen = login_dante_screen
game_screen = GameScreen(client)
dante_screen = DanteScreen()
dante_task_screen = DanteTaskScreen()
dante_work_screen = DanteWorkScreen()
settings_screen = SettingsScreen(background_music)
statistics_screen = StatisticsScreen()
button_stop = False

# Creating basic text for blackjack
flaga = 0
running = True

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
                button_stop = True
            # ekran dante
            if house_button.tool_click_left() and current_screen == dante_screen:
                current_screen = dante_start_screen
            if task_list_button.tool_click_left() and current_screen == dante_screen:
                current_screen = dante_task_screen
                button_stop = True
            # ekran zadan dante
            if house_button.tool_click_left() and current_screen == dante_task_screen:
                current_screen = dante_start_screen
            if button_stop == False:
                if do_1.tool_click_left() and current_screen == dante_task_screen:
                    Task.task_number = 1
                    Task.work_mode = 0
                    current_screen = dante_work_screen
                if do_2.tool_click_left() and current_screen == dante_task_screen:
                    Task.task_number = 2
                    Task.work_mode = 0
                    current_screen = dante_work_screen
                if do_3.tool_click_left() and current_screen == dante_task_screen:
                    Task.task_number = 3
                    Task.work_mode = 0
                    current_screen = dante_work_screen
                if do_4.tool_click_left() and current_screen == dante_task_screen:
                    Task.task_number = 4
                    Task.work_mode = 0
                    current_screen = dante_work_screen
                if do_5.tool_click_left() and current_screen == dante_task_screen:
                    Task.task_number = 5
                    Task.work_mode = 0
                    current_screen = dante_work_screen
                if pp1.tool_click_left() and current_screen == dante_task_screen:
                    current_screen = dante_screen
            # ekran do zadan
            if house_button.tool_click_left() and current_screen == dante_work_screen:
                current_screen = dante_start_screen
            if wiwd.tool_click_left() and current_screen == dante_work_screen:
                current_screen = dante_task_screen
            if pp1.tool_click_left() and current_screen == dante_work_screen:
                current_screen = dante_screen
            if help.tool_click_left() and current_screen == dante_work_screen:
                Task.work_mode = 1
            if mode_0_button.tool_click_left() and current_screen == dante_work_screen:
                Task.work_mode = 0
            if unlock_button.tool_click_left() and current_screen == dante_work_screen and torch_table[Task.task_number-1] == 0:
                torch_table[Task.task_number-1] = 1

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

            # ekran opcji
            if SettingsButton.tool_click_left() and current_screen == dante_blackjack_start_screen:
                current_screen = settings_screen

            if SettingsScreen_back.tool_click_left() and current_screen == settings_screen:
                current_screen = dante_blackjack_start_screen

            # ekran statystyk
            if StatisticsButton.tool_click_left() and current_screen == dante_blackjack_start_screen:
                current_screen = statistics_screen

            if StatisticsScreen_back.tool_click_left() and current_screen == statistics_screen:
                current_screen = dante_blackjack_start_screen

            # ekran wybor stolu
            if current_screen == lobby_screen:
                current_screen.Start(window, choice)
                if current_screen.lobby_add_table is not None and current_screen.lobby_add_table.tool_click_left():
                    client.create_table()
                    sleep(5)
                    game_screen.set_table(client.table)
                    current_screen = game_screen
                if current_screen != game_screen:
                    for i in range(len(current_screen.table_button_array)):
                        if current_screen.table_button_array[i].tool_click_left() and button_stop == False:
                            client.join_to_table(current_screen.tables[i].table_id)
                            sleep(5)
                            game_screen.set_table(client.table)
                            current_screen = game_screen
                            print(i)
            if lobby_to_Menu_button.tool_click_left() and current_screen == lobby_screen:
                current_screen = dante_blackjack_start_screen
            # if current_screen == GameScreen:
            #    GameScreen.Start(window, choice)
        if current_screen == dante_blackjack_start_screen:
            if flaga == 0:
                background_music.play(-1)
                flaga = 1
        if current_screen == dante_start_screen:
            if flaga == 1:
                background_music.stop()
                flaga = 0
        # ekran logowania
        if current_screen == login_dante_screen:
            username.writing(event)
            password.writing(event)
        button_stop = False
