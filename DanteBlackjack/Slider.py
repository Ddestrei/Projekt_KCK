from Tool import *


class Slider:
    def __int__(self, pos: tuple, size: tuple, initial_val: float, min: float, max: float):
        self.pos = pos
        self.size = size

        self.slider_left_pos = self.pos[0] - (size[0]//2)
        self.slider_right_pos = self.pos[0] + (size[0]//2)
        self.slider_top_pos = self.pos[1] - (size[1]//2)

        self.min = min
        self.max = max
        self.initial_val = (self.slider_right_pos-self.slider_left_pos)*initial_val # <- percentage

        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        self.button_rect = pygame.Rect(self.slider_left_pos + self.initial_val - 5, self.slider_top_pos, 10, self.size[1])

    def move_slider(self):
        mouse_pos = pygame.mouse.get_pos()
        self.button_rect.centerx = mouse_pos[0]

    def set_discrete_value(self, step: float):
        """
        Ustawia pozycję suwaka na najbliższą dyskretną wartość.

        Args:
            step (float): Krok, o który wartości mają być dyskretne.
                          Na przykład, jeśli min_val = 0.5, max_val = 2.0 i step = 0.5,
                          możliwe wartości to 0.5, 1.0, 1.5, 2.0.
        """
        current_value = self.get_value()
        # Obliczanie najbliższej dyskretnej wartości
        rounded_value = round((current_value - self.min) / step) * step + self.min

        # Ograniczenie wartości do zakresu min_val i max_val
        discrete_value = max(self.min, min(rounded_value, self.max))

        # Przeliczanie dyskretnej wartości na pozycję pikselową
        # Najpierw obliczamy procentowe położenie wartości w zakresie
        if (self.max - self.min) == 0:  # Zapobieganie dzieleniu przez zero
            percentage = 0
        else:
            percentage = (discrete_value - self.min) / (self.max - self.min)

        # Następnie przeliczamy procent na pozycję x piksela wewnątrz suwaka
        new_button_x = self.slider_left_pos + int(percentage * self.size[0])
        self.button_rect.centerx = new_button_x

    def render(self, window):
        pygame.draw.rect(window, "darkgrey", self.container_rect)
        pygame.draw.rect(window, "grey", self.button_rect)

    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos - 1
        button_val = self.button_rect.centerx - self.slider_left_pos

        return (button_val/val_range) * (self.max - self.min) + self.min