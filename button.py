import pygame

pygame.init()
class button:
    '''
    x, y - int-координаты кнопки
    width, height - int - размеры кнопки
    color - цвет кнопки
    text - string - надпись на кнопке
    '''
    def __init__(self, x, y, width, height, color, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.pressed = False
    def draw(self,button_pressed):
        '''
        функция рисует кнопку,красная - если кнопка нажата, свой цвет - если не нажата
        '''
        if button_pressed:
            pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(window, 'RED', (self.x, self.y, self.width, self.height))

        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, 'BLACK')
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        window.blit(text, text_rect)



    def get_pressed(self):
        '''
        возвращает True, если кнопка была нажата, False - если не нажата
        '''
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
                self.pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.pressed = False
        return self.pressed

