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

x_button = 50
y_button = 50
x_button, y_button = scale_position(x_button, y_button, choice)
button_0 = Button(x_button, y_button, "PP.png")

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

x_button = 200
y_button = 200
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
