import pygame
from visual import *

BLUE = (0, 119, 255)

HOUSE_COST = 10
HOUSE_POFIT = 1
ROAD_COST = 1
PARK_COST = 20
WATER_ROAD_COST = 1
ELECTRICITY_ROAD_COST = 1
WATER_COST = 50
ELECTRICITY_COST = 50

def check_score(score, what_you_build):
    if what_you_build == 'house' and score >= HOUSE_COST:
        return True
    if what_you_build == 'road' and score >= ROAD_COST:
        return True
    if what_you_build == 'water' and score >= WATER_COST:
        return True
    if what_you_build == 'electricity' and score >= ELECTRICITY_COST:
        return True
    if what_you_build == 'park' and score >= PARK_COST:
        return True
    return False

def get_score(what_you_build):
    if what_you_build == 'house':
        return HOUSE_COST
    if what_you_build == 'road':
        return ROAD_COST
    if what_you_build == 'water':
        return WATER_COST
    if what_you_build == 'electricity':
        return ELECTRICITY_COST
    if what_you_build == 'park':
        return PARK_COST


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
        self.type =  type
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
