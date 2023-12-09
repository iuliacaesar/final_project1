import pygame
from visual import *

pygame.init()

class Button:
    '''
    x, y - int-координаты кнопки
    width, height - int - размеры кнопки
    color - цвет кнопки
    text - string - надпись на кнопке
    size_text - размер надписи на кнопке
    '''
    def __init__(self, x=10, y=10, width=100, height=10, color=(100, 0, 150, 100), color_text ='black', text='Ведите текст параметром text', size_text=36):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.size_text = size_text
        self.color_text = color_text
        self.pressed = False
        self.time=1



    def draw(self, window: pygame.Surface):
        '''
        функция рисует кнопку, красная - если кнопка нажата, свой цвет - если не нажата
        '''
        if self.text=="START" or self.text=="CONTINUE" or self.text=="close":
            pygame.draw.rect(window, (90, 0, 150, 100), (self.x, self.y, self.width, self.height), 10, 12 )
            pygame.draw.rect(window, (150, 140, 255, 100), (self.x+5, self.y+5, self.width-10, self.height-10), 20, 12 )
            font = pygame.font.Font(None, self.size_text)
            text = font.render(self.text, True, self.color_text)
            text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
            window.blit(text, text_rect)

        elif self.text=="castle 1" or self.text=="castle 2" or self.text=="castle 3" or self.text=="road" or self.text=="lake"  or self.text=="park" or self.text=="mile" or self.text=="connect_water":
            draw_button(self, window)
            pygame.draw.rect(window, (90, 0, 150, 100), (self.x, self.y, self.width, self.height), 10, 12)
            font = pygame.font.Font(None, self.size_text)
            text = font.render(self.text, True, self.color_text)
            text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height + self.size_text // 3))
            window.blit(text, text_rect)
        elif self.text=="SAVE" or self.text=="CLOSE" or self.text=="FINISH":
            pygame.draw.rect(window, (90, 0, 150, 100), (self.x, self.y, self.width, self.height+1), 8, 10)
            pygame.draw.rect(window, (150, 140, 255, 100), (self.x + 4, self.y + 4, self.width - 8, self.height - 8),
                             11, 5)
            font = pygame.font.Font(None, self.size_text)
            text = font.render(self.text, True, self.color_text)
            text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
            window.blit(text, text_rect)
        elif self.text=="ХУЙ":
            draw_huina(self, window)


        else:
            pygame.draw.rect(window, (100, 0, 150, 100), (self.x, self.y, self.width, self.height))



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