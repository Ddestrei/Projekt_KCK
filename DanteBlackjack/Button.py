from GameButton import GameButton
from Tool import *


class Button(Tool):
    def __init__(self, x, y, button_name):
        super().__init__(x, y, button_name)
        # super._init_.tool_image = pygame.image.load(f"DanteBlackJack/Grafika/Obiekty/{image_name}")
        # super().__init__().tool_image = (pygame.Surface((100, 50))) #tymczasowe
        # super().__init__().hitbox = pygame.Rect(super._init_.x,super._init_.y,super._init_.tool_image.get_width(),super._init_.tool_image.get_height())


x_button = 486
y_button = 452
x_button, y_button = scale_position(x_button, y_button, choice)
button_log = Button(x_button, y_button, "P_Zaloguj.png")

x_button = 1114
y_button = 5
x_button, y_button = scale_position(x_button, y_button, choice)
dante_start_screen_to_dante_blackjack_start_screen = Button(x_button, y_button, "dp.png")

x_button = 1097
y_button = 242
x_button, y_button = scale_position(x_button, y_button, choice)
topics_button = Button(x_button, y_button, "topics_button.png")

x_button = 223
y_button = 94
x_button, y_button = scale_position(x_button, y_button, choice)
house_button = Button(x_button, y_button, "house.png")

x_button = 512
y_button = 95
x_button, y_button = scale_position(x_button, y_button, choice)
wiwd = Button(x_button, y_button, "wiwd.png")

x_button = 262
y_button = 95
x_button, y_button = scale_position(x_button, y_button, choice)
pp1 = Button(x_button, y_button, "pp1.png")

x_button = 518
y_button = 269
x_button, y_button = scale_position(x_button, y_button, choice)
help = Button(x_button, y_button, "pomoc.png")


x_button = 1140
y_button = 289
x_button, y_button = scale_position(x_button, y_button, choice)
task_list_button = Button(x_button, y_button, "lista.png")


x_button = 1156
y_button = 241
x_button, y_button = scale_position(x_button, y_button, choice)
do_1 = Button(x_button, y_button, "wykonaj.png")

x_button = 1156
y_button = 311
x_button, y_button = scale_position(x_button, y_button, choice)
do_2 = Button(x_button, y_button, "wykonaj.png")

x_button = 1156
y_button = 381
x_button, y_button = scale_position(x_button, y_button, choice)
do_3 = Button(x_button, y_button, "wykonaj.png")

x_button = 1156
y_button = 451
x_button, y_button = scale_position(x_button, y_button, choice)
do_4 = Button(x_button, y_button, "wykonaj.png")

x_button = 1156
y_button = 521
x_button, y_button = scale_position(x_button, y_button, choice)
do_5 = Button(x_button, y_button, "wykonaj.png")


x_button = 650
y_button = 350
x_button, y_button = scale_position(x_button, y_button, choice)
StartGameButton = Button(x_button, y_button, "StartScreenGraphics/StartScreen_start_button.png")

x_button = 650
y_button = 440
x_button, y_button = scale_position(x_button, y_button, choice)
RulesButton = Button(x_button, y_button, "StartScreenGraphics/StartScreen_rules_button.png")

x_button = 650
y_button = 527
x_button, y_button = scale_position(x_button, y_button, choice)
SettingsButton = Button(x_button, y_button, "StartScreenGraphics/StartScreen_settings_button.png")

x_button = 650
y_button = 613
x_button, y_button = scale_position(x_button, y_button, choice)
ExitGameButton = Button(x_button, y_button, "StartScreenGraphics/StartScreen_exit_button.png")

x_button = 650
y_button = 699
x_button, y_button = scale_position(x_button, y_button, choice)
StatisticsButton = Button(x_button, y_button, "StartScreenGraphics/StartScreen_statistics_button.png")

x_button = 20
y_button = 20
x_button, y_button = scale_position(x_button, y_button, choice)
lobby_to_Menu_button = Button(x_button, y_button, "lobby_to_Menu_button.png")

x_button = 651
y_button = 955
x_button, y_button = scale_position(x_button, y_button, choice)
RulesScreen_back = Button(x_button, y_button, "RulesScreen_back_button.png")

x_button = 651
y_button = 955
x_button, y_button = scale_position(x_button, y_button, choice)
SettingsScreen_back = Button(x_button, y_button, "RulesScreen_back_button.png")

x_button = 651
y_button = 955
x_button, y_button = scale_position(x_button, y_button, choice)
StatisticsScreen_back = Button(x_button, y_button, "RulesScreen_back_button.png")

x_button = 240
y_button = 268
x_button, y_button = scale_position(x_button, y_button, choice)
mode_0_button = Button(x_button, y_button, "tresc.png")


def brighten_surface(surface, brightness=40):
    hover = surface.copy()
    brighten_layer = pygame.Surface(surface.get_size())
    brighten_layer.fill((brightness, brightness, brightness, 0))  # RGB only
    hover.blit(brighten_layer, (0, 0), special_flags=pygame.BLEND_RGB_ADD)
    return hover


# buttons for blackjack
screenWidth, screenHeight = resolutions[choice]
halfWidth, halfHeight = screenWidth / 2, screenHeight / 2
bet15_img = pygame.image.load(bet15_img_path)
bet1_img = pygame.image.load(bet1_img_path)
bet05_img = pygame.image.load(bet05_img_path)
hit_img = pygame.image.load(hit_img_path)
stand_img = pygame.image.load(stand_img_path)
double_img = pygame.image.load(double_img_path)
bet05_button = GameButton(halfWidth - round(300 * percents[choice]),
                          screenHeight - round(100 * percents[choice]), bet05_img, percents[choice],
                          hover_image=brighten_surface(bet05_img))
bet1_button = GameButton(halfWidth - round(100 * percents[choice]),
                         screenHeight - round(105 * percents[choice]), bet1_img, percents[choice],
                         hover_image=brighten_surface(bet1_img))
bet15_button = GameButton(halfWidth + round(100 * percents[choice]),
                          screenHeight - round(102 * percents[choice]), bet15_img, percents[choice],
                          hover_image=brighten_surface(bet15_img))
adjusted_center = halfWidth - 150 * percents[choice] + 50
button_spacing = 160 * percents[choice]
card_height = round(144 * percents[choice])

hit_button = GameButton(adjusted_center - button_spacing, screenHeight - 70, hit_img, percents[choice],
                        hover_image=brighten_surface(hit_img))
stand_button = GameButton(adjusted_center, screenHeight - 70, stand_img, percents[choice],
                          hover_image=brighten_surface(stand_img))
double_button = GameButton(adjusted_center + button_spacing, screenHeight - 70, double_img, percents[choice],
                           hover_image=brighten_surface(double_img))
card_back_img = pygame.image.load(card_back_img_path)
card_back_img = pygame.transform.scale(card_back_img, (round(96 * percents[choice]), round(144 * percents[choice])))
leave_img = pygame.image.load(leave_img_path)
leave_button = GameButton(10, 10, leave_img, round(percents[choice] * 1.5))
leave_button.set_enabled(True)
hit_button.set_enabled(True)
stand_button.set_enabled(True)
double_button.set_enabled(True)
