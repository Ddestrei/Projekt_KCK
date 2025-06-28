import pygame

pygame.init()
from Screen import *
from slider import *


class SettingsScreen(Screen):
    def __init__(self):
        self.initial_val = 0.3

    def Start(self, window, choice):
        pygame.time.Clock().tick(60)
        background = pygame.image.load(Rules_background_path)
        background = pygame.transform.scale(background, (resolutions[choice]))
        window.blit(background, (0, 0))

        x, y = scale_position(481, 466, choice)
        speaker_image = Tool(x, y, "speaker_image.png")
        speaker_image.tool_draw(window)

        mouse_pos = pygame.mouse.get_pos()

        x, y = scale_position(748, 516, choice)
        slider = Slider(x, y, 305, 38, self.initial_val, 0, 100)

        if slider.container_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.initial_val = slider.move_slider(mouse_pos)/100
        slider.slider_render(window)
        SettingsScreen_back.tool_draw(window)

        pygame.display.update()

    def get_volume(self):
        return self.initial_val*100
