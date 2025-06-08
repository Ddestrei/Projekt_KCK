from DanteStartScreen import *
from DanteBlackjackStartScreen import *
from LobbyScreen import *
from LoginDanteScreen import *


window = pygame.display.set_mode(resolutions[choice])

login_dante_screen = LoginDanteScreen()
dante_start_screen = DanteStartScreen()
dante_blackjack_start_screen = DanteBlackjackStartScreen()
lobby_screen = LobbyScreen()
current_screen = login_dante_screen

running = True
while running:
    current_screen.Start(window, choice)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #ekran logowania
            if button_log.tool_click_left() and current_screen == login_dante_screen:
                username.status_set_0()
                current_screen = dante_start_screen
            if username.tool_click_left() and current_screen == login_dante_screen:
                username.status_set_1()
                password.status_set_0()
            if password.tool_click_left() and current_screen == login_dante_screen:
                password.status_set_1()
                username.status_set_0()
            #ekran startowy dante
            if button_0.tool_click_left() and current_screen == dante_start_screen:
                current_screen = dante_blackjack_start_screen
            #ekran startu gry
            if ExitGameButton.tool_click_left() and current_screen == dante_blackjack_start_screen:
                current_screen = dante_start_screen
            if StartGameButton.tool_click_left() and current_screen == dante_blackjack_start_screen:
                current_screen = lobby_screen
            #ekran wybor stolu
            if lobby_to_Menu_button.tool_click_left() and current_screen == lobby_screen:
                current_screen = dante_blackjack_start_screen
        #ekran logowania
        if(current_screen == login_dante_screen):
            username.writing(event)
            password.writing(event)