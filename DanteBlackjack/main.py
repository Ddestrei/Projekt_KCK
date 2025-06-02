import pygame
pygame.init()
from EkranStartowyDante import *
from EkranStartuGry import *
from Lobby_Screen import *
from EkranLogowania import *

window = pygame.display.set_mode(resolutions[choice])

ekran_logowania = EkranLogowania()
ekran_startowy_dante = EkranStartowyDante()
ekran_startu_gry = EkranStartuGry()
ekran_wyboru_stolu = Lobby_Screen()
current_screen = ekran_logowania

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if(current_screen == ekran_logowania):
            username.writing(event)
            password.writing(event)
        

    current_screen.Start(window, choice)
    #ekran logowania
    if button_log.tool_click_left() and current_screen == ekran_logowania:
        username.status_set_0()
        current_screen = ekran_startowy_dante
    if username.tool_click_left() and current_screen == ekran_logowania:
        username.status_set_1()
        password.status_set_0()
    if password.tool_click_left() and current_screen == ekran_logowania:
        password.status_set_1()
        username.status_set_0()
    #ekran startowy dante
    if button_0.tool_click_left() and current_screen == ekran_startowy_dante:
        current_screen = ekran_startu_gry
    #ekran startu gry
    if button_1.tool_click_left() and current_screen == ekran_startu_gry:
        current_screen = ekran_startowy_dante
    if button_2.tool_click_left() and current_screen == ekran_startu_gry:
        current_screen = ekran_wyboru_stolu
    #ekran wybor stolu
    if lobby_to_Menu_button.tool_click_left() and current_screen == ekran_wyboru_stolu:
        current_screen = ekran_startu_gry

