from EkranLogowania import *
from EkranStartowyDante import *
from EkranStartuGry import *
from EkranWyborStolu import *
from Client import Client

if __name__ == "__main__":
    client = Client()
    pygame.init()
    window = pygame.display.set_mode((800, 600))  # zmienic ilosc pikseli

    ekran_logowania = EkranLogowania()
    ekran_startowy_dante = EkranStartowyDante()
    ekran_startu_gry = EkranStartuGry()
    ekran_wyboru_stolu = EkranWyboruStolu()
    current_screen = ekran_logowania

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_screen.start(window)
        # ekran logowania
        if button_log.button_click() and current_screen == ekran_logowania:
            current_screen = ekran_startowy_dante
        # ekran startowy dante
        if button_0.button_click() and current_screen == ekran_startowy_dante:
            current_screen = ekran_startu_gry
        # ekran startu gry
        if button_1.button_click() and current_screen == ekran_startu_gry:
            current_screen = ekran_startowy_dante
        if button_2.button_click() and current_screen == ekran_startu_gry:
            current_screen = ekran_wyboru_stolu
        # ekran wybor stolu
        if button_3.button_click() and current_screen == ekran_wyboru_stolu:
            current_screen = ekran_startu_gry
