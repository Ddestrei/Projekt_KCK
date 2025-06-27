import pygame

pygame.init()
from path import *

resolutions = [(874, 620), (1166, 826), (1457, 1033)]
percents = [0.6, 0.8, 1]

print("Wybierz rozdzielczość aby rozpocząć:")
for i, res in enumerate(resolutions):
    print(f"{i + 1}. {res[0]}x{res[1]}")

choice = int(input("Twój wybór: ")) - 1

running = True


class Tool():
    def __init__(self, x, y, image_name):
        self.x = x
        self.y = y
        image_path = root_path / "Grafika" / "Obiekty" / image_name
        self.tool_image = pygame.image.load(image_path)
        if choice != 2:
            self.tool_image = pygame.transform.scale(self.tool_image, (
            int(percents[choice] * self.tool_image.get_width()), int(percents[choice] * self.tool_image.get_height())))
        self.hitbox = pygame.Rect(self.x, self.y, self.tool_image.get_width(), self.tool_image.get_height())
        self.visible = True
    def click_left(self):
        return pygame.mouse.get_pressed()[0]

    def click_right(self):
        return pygame.mouse.get_pressed()[2]

    def cursor_in_hitbox(self):
        return self.hitbox.collidepoint(pygame.mouse.get_pos())

    def tool_click_left(self):
        return self.click_left() and self.cursor_in_hitbox()

    def tool_click_right(self):
        return self.click_right() and self.cursor_in_hitbox()

    def tool_draw(self, window):
        # if self.cursor_in_hitbox():
        # self.tool_image.fill((255, 0, 0)) #tymczasowe
        if self.visible == True:
            window.blit(self.tool_image, (self.x, self.y))


def scale_position(x, y, choice):
    if choice != 2:
        if choice == 0:
            x = 0.6 * x
            y = 0.6 * y
            return round(x), round(y)
        elif choice == 1:
            x = 0.8 * x
            y = 0.8 * y
            return round(x), round(y)
    return x, y


def scale_font(font_size, choice):
    if choice != 2:
        if choice == 0:
            font_size = 0.6 * font_size
            return round(font_size)
        elif choice == 1:
            font_size = 0.8 * font_size
            return round(font_size)
    return round(font_size)
