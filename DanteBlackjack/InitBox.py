from Tool import *

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

font_0_size = round(20 * percents[choice])

font_0 = pygame.font.Font("DanteBlackjack/Grafika/Czcionki/Aptos.ttf", font_0_size)

x_button = 486
y_button = 318
x_button, y_button = scale_position(x_button,y_button,choice)
username = InitBox(x_button,y_button,"username.png",font_0, 7)
x_button = 486
y_button = 369
x_button, y_button = scale_position(x_button,y_button,choice)
password = InitBox(x_button,y_button,"username.png",font_0, 7)

