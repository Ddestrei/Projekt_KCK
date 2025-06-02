import pygame
pygame.init()

resolutions = [(874, 620), (1166, 826), (1457, 1033)]
percents = [0.6, 0.8, 1]

print("Wybierz rozdzielczość aby rozpocząć:")
for i, res in enumerate(resolutions):
    print(f"{i + 1}. {res[0]}x{res[1]}")

choice = int(input("Twój wybór: ")) - 1

class Tool():
    def __init__(self, x, y, image_name):
        self.x = x
        self.y = y
        self.tool_image = pygame.image.load(f"DanteBlackJack/Grafika/Obiekty/{image_name}")
        if choice != 2:
            self.tool_image = pygame.transform.scale(self.tool_image, (int(percents[choice] * self.tool_image.get_width()), int(percents[choice] * self.tool_image.get_height())))
        self.hitbox = pygame.Rect(self.x,self.y,self.tool_image.get_width(),self.tool_image.get_height())
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
    def tool_draw(self,window):
        #if self.cursor_in_hitbox():
        #self.tool_image.fill((255, 0, 0)) #tymczasowe
        window.blit(self.tool_image,(self.x,self.y))

class Button(Tool):
    def __init__(self, x, y, button_name):
        super().__init__(x, y, button_name)
        #super._init_.tool_image = pygame.image.load(f"DanteBlackJack/Grafika/Obiekty/{image_name}")
        #super().__init__().tool_image = (pygame.Surface((100, 50))) #tymczasowe
        #super().__init__().hitbox = pygame.Rect(super._init_.x,super._init_.y,super._init_.tool_image.get_width(),super._init_.tool_image.get_height())

class InitBox(Tool):
    def __init__(self, x, y, box_image_name, font, paragraph):
        super().__init__(x, y, box_image_name)
        self.status = 0
        self.font = font
        self.text = ""
        self.paragraph = paragraph
    def status_set_1(self):
        self.status = 1
    def status_set_0(self):
        self.status = 0
    def writing(self,event):
         if event.type == pygame.KEYDOWN and self.status:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                pass
            else:
                self.text += event.unicode
    def render_text(self, window):
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        width, height = self.font.size(self.text)
        window.blit(text_surface, (self.x + self.paragraph, self.y + (self.tool_image.get_height() - height)/2))
    def get_text(self):
        return self.text



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



font_0_size = round(20 * percents[choice])
font_0 = pygame.font.Font("DanteBlackjack/Grafika/Czcionki/Aptos.ttf", font_0_size)

x_button = 486
y_button = 452
x_button, y_button = scale_position(x_button,y_button,choice)
button_log = Button(x_button, y_button,"P_Zaloguj.png")
x_button = 50
y_button = 50
x_button, y_button = scale_position(x_button,y_button,choice)
button_0 = Button(x_button,y_button,"PP.png")
x_button = 600
y_button = 50
x_button, y_button = scale_position(x_button,y_button,choice)
button_1 = Button(x_button,y_button, "PP.png")
x_button = 50
y_button = 400
x_button, y_button = scale_position(x_button,y_button,choice)
button_2 = Button(x_button,y_button, "PP.png")

x_button = 20
y_button = 20
x_button, y_button = scale_position(x_button,y_button,choice)
lobby_to_Menu_button = Button(x_button, y_button, "lobby_to_Menu_button.png")
x_button = 40
y_button = 50
x_button, y_button = scale_position(x_button, y_button, choice)
lobby_add_table = Button(x_button, y_button, "lobby_add_table.png")


x_button = 486
y_button = 318
x_button, y_button = scale_position(x_button,y_button,choice)
username = InitBox(x_button,y_button,"username.png",font_0, 7)
x_button = 486
y_button = 369
x_button, y_button = scale_position(x_button,y_button,choice)
password = InitBox(x_button,y_button,"username.png",font_0, 7)
