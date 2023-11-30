import pygame
from visual import*

class Buildings(): 
    '''
    x, y - координаты дома
    type - int от 1 до n (n - кичество типов домов) - тип дома
    '''
    def __init__(self, x, y, type, level, screen):
        self.screen = screen
        self.type = type
        self.level = level
        self.x = x
        self.y = y

    '''
    type - тип здания
    level - уровень 
    x,y - координаты ВЕРХНЕГО ЛЕВОГО угла квадрата, где располагается здание
    '''

    def draw(self):
        # FIXME-Лера подгрузка картинок домов и их отрисовка
        if self.type == 1:
            color = 'red'
        if self.type == 2:
            color = 'orange'
        pygame.draw.circle(
            self.screen,
            color,
            (int(self.x), int(self.y)),
            50
        )

class Roads():
    def __init__(self, x, y, type, level):
        self.type = type
        self.level = level
        self.x = x
        self.y = y
        '''
        type - тип дороги
        level - уровень 
        x,y - координаты ВЕРХНЕГО ЛЕВОГО угла квадрата, где располагается с
        '''


    def draw():
        # FIXME-Лера подгрузка картинок домов и их отрисовка
        # FIXME - все будет в файле visual.py
        pass
