import pygame
from visual import *

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
        self.time=0

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
        self.time = 0
        self.angle = 0


class Roads():
    def __init__(self, x, y, type, screen):
        self.screen = screen
        self.type = [1, 1, 1, 0]
        self.x = x
        self.y = y

class Tracts():
    def __init__(self,screen):
        self.screen = screen
        self.tract=[]

        '''
        x,y - координаты ВЕРХНЕГО ЛЕВОГО угла квадрата, где располагается 
        '''


class Parks():
    def __init__(self, x, y, type, level, screen):
        self.screen = screen
        self.type = type
        self.level = level
        self.x = x
        self.y = y
        self.time = 0


class Problems():
    def __init__(self, x, y, type, level, screen):
        self.screen = screen
        self.type = type
        self.level = level
        self.x = x
        self.y = y
        self.time = 0