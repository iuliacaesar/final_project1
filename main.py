import math
import random as rd
import numpy as np

import pygame

FPS = 100

WHITE = (255, 255, 255)
COLOR = (95, 189, 51)
WIDTH = 800
HEIGHT = 600

class Buildings():
    def __init__(self, x, y, type):
        self.type = type
        self.x = x
        self.y = y

    def draw():
        # FIXME-Лера подгрузка картинок домов и их отрисовка
        pass

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
buildings = []
finished = False
page = 'start'

clock = pygame.time.Clock()

while not finished:
    if page == 'start':
        screen.fill(WHITE)
        
        for b in buildings:
            b.draw()

        pygame.display.update()

        for event in pygame.event.get():                               
            if event.type == pygame.QUIT:
                finished = True

    if page == 'main':        
        screen.fill(COLOR)
        pygame.display.update()

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
