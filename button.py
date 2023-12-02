import pygame

pygame.init()

class Button:
    '''
    x, y - int-координаты кнопки
    width, height - int - размеры кнопки
    color - цвет кнопки
    text - string - надпись на кнопке
    size_text - размер надписи на кнопке
    '''
    def __init__(self, x=10, y=10, width=100, height=10, color='grey', color_text ='black', text='Ведите текст параметром text', size_text=36):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.size_text = size_text
        self.color_text = color_text
        self.pressed = False

    def draw(self, window: pygame.Surface):
        '''
        функция рисует кнопку, красная - если кнопка нажата, свой цвет - если не нажата
        '''
        if self.pressed:
            pygame.draw.rect(window, 'RED', (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

        font = pygame.font.Font(None, self.size_text)
        text = font.render(self.text, True, self.color_text)
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        window.blit(text, text_rect)

    def get_pressed(self, event):
        '''
        возвращает True, если кнопка была нажата, False - если не нажата
        '''
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
                self.pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.pressed = False