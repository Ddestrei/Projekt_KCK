import pygame
pygame.init()

class Slider:
    def __init__(self, poz_x: int, poz_y: int, size_x, size_y, initial_val: float, minimum: int, maximum: int):
        self.poz_x = poz_x
        self.poz_y = poz_y
        self.size_x = size_x
        self.size_y = size_y

        self.slider_left_poz = self.poz_x - (size_x//2)
        self.slider_right_poz = self.poz_x + (size_x//2)
        self.slider_top_poz = self.poz_y - (size_y//2)

        self.minimum = minimum
        self.maximum = maximum

        self.initial_val = (self.slider_right_poz-self.slider_left_poz)*initial_val # percentage

        self.container_rect = pygame.Rect(self.slider_left_poz, self.slider_top_poz, self.size_x, self.size_y)
        self.button_rect = pygame.Rect(self.slider_left_poz + self.initial_val - 5, self.slider_top_poz, 10,
                                       self.size_y)

    def slider_render(self, window):
        pygame.draw.rect(window, "gray", self.container_rect)
        pygame.draw.rect(window, "darkgray", self.button_rect)

    def move_slider(self, mouse_pos):
        pos = mouse_pos[0]
        if pos < self.slider_left_poz:
            pos = self.slider_left_poz
        if pos > self.slider_right_poz:
            pos = self.slider_right_poz
        self.button_rect.centerx = pos

        val_range = self.slider_right_poz - self.slider_left_poz - 1
        button_val = self.button_rect.centerx - self.slider_left_poz
        return (button_val / val_range) * (self.maximum - self.minimum) + self.minimum



    def get_value(self):
        val_range = self.slider_right_poz - self.slider_left_poz - 1
        button_val = self.button_rect.centerx - self.slider_left_poz
        return (button_val / val_range) * (self.maximum - self.minimum) + self.minimum

