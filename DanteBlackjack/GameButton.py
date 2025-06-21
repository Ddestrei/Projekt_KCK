import pygame

class GameButton:
    def __init__(self, x, y, image, window, scale=1, hover_image=None, enabled=True):
        width = image.get_width()
        height = image.get_height()
        self.base_image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.hover_image = pygame.transform.scale(hover_image, (
        int(width * scale), int(height * scale))) if hover_image else self.base_image
        self.image = self.base_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False
        self.enabled = enabled
        self.screen = window

    def draw(self):
        action = False
        mouse_pos = pygame.mouse.get_pos()

        if self.enabled:
            self.image = self.hover_image if self.rect.collidepoint(mouse_pos) else self.base_image
        else:
            self.image = self._dim_image(self.base_image)

        self.screen.blit(self.image, (self.rect.x, self.rect.y))

        if self.enabled and pygame.mouse.get_pressed()[0] and self.rect.collidepoint(mouse_pos):
            if not self.clicked:
                self.clicked = True
                action = True
                # Add action
        elif not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        return action

    def set_enabled(self, value: bool):
        self.enabled = value

    def _dim_image(self, image):
        dimmed = image.copy()
        dimmed.fill((180, 180, 180, 200), None, pygame.BLEND_RGBA_MULT)
        return dimmed