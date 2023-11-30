import math
#import random as rd
#import numpy as np

from visual import*

import pygame

FPS = 100

WHITE = (255, 255, 255)
COLOR = (95, 189, 51)
WIDTH = 1300
HEIGHT = 700

class Buildings():
    def __init__(self, x, y, type, level):
        self.type = type
        self.level = level
        self.x = x
        self.y = y
        '''
        type - тип здания
        level - уровень 
        x,y - координаты ВЕРХНЕГО ЛЕВОГО угла квадрата, где располагается здание
        '''

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

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
buildings = []
finished = False
page = 'start'

clock = pygame.time.Clock()

while not finished:

    '''Эти функции рисования написаны по приколу, в дальнейшем функции 
    рисования объектов будут принимать только объект'''
    draw_fon(screen, 0, 0)
    draw_setka(screen, WIDTH, HEIGHT)
    draw_building(screen, 100, 200)
    pygame.display.update()

    if page == 'start':
        screen.fill(WHITE)
        
        for b in buildings:
            b.draw()

        for event in pygame.event.get():                               
            if event.type == pygame.QUIT:
                finished = True

    if page == 'main':        
        screen.fill(COLOR)

        for event in pygame.event.get():                               
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN:
                page = 'main'
            if event.type == pygame.MOUSEBUTTONDOWN:
                page = 'main'

    if page == 'build':
        # FIXME-Юля реализвать всплывающее окно с объектами для строительства

        for event in pygame.event.get():                               
            if event.type == pygame.QUIT:
                finished = True

pygame.quit()
