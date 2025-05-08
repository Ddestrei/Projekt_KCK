import pygame
pygame.init()

class Button():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #self.button_image=(pygame.image.load(f"{nazwapliku}"))
        self.button_image = (pygame.Surface((100, 50))) #tymczasowe
        self.hitbox = pygame.Rect(self.x,self.y,self.button_image.get_width(),self.button_image.get_height())
    def click_left(self):
        if pygame.mouse.get_pressed()[0]:
            return True
    def click_right(self):
        if pygame.mouse.get_pressed()[1]:
            return True
    def cursor_in_hitbox(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            return True
    def button_click(self):
        if self.click_left() and self.cursor_in_hitbox():
            return True
        return False
    def button_draw(self,window):
        #if self.cursor_in_hitbox():
        self.button_image.fill((255, 0, 0)) #tymczasowe
        window.blit(self.button_image,(self.x,self.y))

button_log = Button(350,275)
button_0 = Button(50,50)
button_1 = Button(600,50)
button_2 = Button(50,400)
button_3 = Button(600,400)
resolutions = [(874, 620), (1166, 826), (1457, 1033)]
