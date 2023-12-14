import random

import pygame
from visual import *

BLUE = (0, 119, 255)

HOUSE_COST = 100
HOUSE_POFIT = 1
ROAD_COST = 0
PARK_COST = 70
WATER_ROAD_COST = 10
ELECTRICITY_ROAD_COST = 10
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
    if what_you_build == 'water_road' and score >= WATER_ROAD_COST:
        return True
        return True
    if what_you_build == 'destroy':
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
    if what_you_build == 'water_road':
        return WATER_ROAD_COST
    if what_you_build == 'destroy':
        return 0


class Buildings():
    '''
    x, y - координаты дома
    type - int от 1 до n (n - кичество типов домов) - тип дома
    '''

    def __init__(self, x, y, type, level, screen):
        self.screen = screen
        self.__type = type
        self.level = level
        self.x = x
        self.y = y
        self.park = 0
        self.water = 0
        self.electricity = 0
        self.m = 1
        self.time=1
        self.monstr_time=random.randint(500,2000)
    def get_type(self):
        return self.__type
    def set_type(self, type):
        self.__type = type
    '''
    type - тип здания
    level - уровень 
    x,y - координаты ВЕРХНЕГО ЛЕВОГО угла квадрата, где располагается здание
    '''


class Resources():
    def __init__(self, x, y, type, screen):
        self.screen = screen
        self.__type = type
        self.x = x
        self.y = y
        self.time = 0
        self.angle = 0
        self.castles = 0
    def get_type(self):
        return self.__type
    def set_type(self, type):
        self.__type = type

class Roads():
    def __init__(self, x, y, type, screen):
        self.screen = screen
        self.type = type
        self.x = x
        self.y = y


class Resource_roads(Roads):
    def __init__(self,  x, y, type, screen, x1, y1, x2, y2):
        Roads.__init__(self, x, y, type, screen)
        self.beginning_x = x1
        self.beginning_y = y1
        self.ending_x = x2
        self.ending_y = y2
        if type == 1:
            self.color = (0, 155, 245)
        else:
            self.color = (212, 152, 0)



class Parks():
    def __init__(self, x, y, type, level, screen):
        self.screen = screen
        self.type = type
        self.level = level
        self.x = x
        self.y = y
        self.time = 0


