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


class Resource_roads():
    def __init__(self, x1, y1, x2, y2, type, screen):
        self.screen = screen
        self.type = type
        self.beginning_x = x1
        self.beginning_y = y1
        self.ending_x = x2
        self.ending_y = y2

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
