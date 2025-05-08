import pygame
pygame.init()

class Tools():
    def __init__(self, x, y, image_name):
        self.x = x
        self.y = y
        self.tool_image = pygame.image.load(f"DanteBlackJack/Grafika/Obiekty/{image_name}")
        #self.tool_image = (pygame.Surface((100, 50))) #tymczasowe
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

class Button(Tools):
    def __init__(self, x, y, button_name):
        super().__init__(x, y, button_name)
        #super._init_.tool_image = pygame.image.load(f"DanteBlackJack/Grafika/Obiekty/{image_name}")
        #super().__init__().tool_image = (pygame.Surface((100, 50))) #tymczasowe
        #super().__init__().hitbox = pygame.Rect(super._init_.x,super._init_.y,super._init_.tool_image.get_width(),super._init_.tool_image.get_height())

class InitBox(Tools):
    def __init__(self, x, y, box_name, font):
        super().__init__(x, y, box_name)

button_log = Button(350,275,"PP.png")
button_0 = Button(50,50,"PP.png")
button_1 = Button(600,50, "PP.png")
button_2 = Button(50,400, "PP.png")
button_3 = Button(600,400,"PP.png")
resolutions = [(874, 620), (1166, 826), (1457, 1033)]
font = pygame.font.Font(None, 40)
