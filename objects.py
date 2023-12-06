import pygame
from visual import*

BLUE = (0, 119, 255)

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

class Resources():
    def __init__(self, x, y, type, screen):
        self.screen = screen
        self.type = type
        self.x = x
        self.y = y
        self.angle = 0

class Roads():
    def __init__(self, x, y, type, screen):
        self.type = type
        self.x = x
        self.y = y
        self.end_x = x
        self.end_y = y
        '''
        x,y - координаты ВЕРХНЕГО ЛЕВОГО угла квадрата, где располагается 
        '''


    def draw():
        # FIXME-Лера подгрузка картинок домов и их отрисовка
        # FIXME - все будет в файле visual.py
        pass


    
class Parks():
    def __init__(self, x, y, type, level, screen):
        self.screen = screen
        self.type = type
        self.level = level
        self.x = x
        self.y = y



        
class Problems():
    def __init__(self, x, y, type, level, screen):
        self.screen = screen
        self.type = type
        self.level = level
        self.x = x
        self.y = y
