import math
import random as rd
import numpy as np
from button import *
from objects import *
from visual import*

import pygame

FPS = 100

# FIXME-Лера настройка значений всех параметров ниже, для адекватного расположенияэ всех элементов
# Такое редактировнаие нужно будет сделать не только здесь, а во всех частях где рисуются объекты, места подобных редактирований отмечаю "FIXME-Лера-настройка"

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLOR = (95, 189, 51)
WIDTH = 800
HEIGHT = 600

BUTTON_WIDTH = 200
BUTTON_HIGHT = 60

# Просто хорошая функция, чтобы выводить многострочные тексты, Лера не благодари, можешь, кстати, в vist запихнуть
def blit_text(surface, text, pos, font, color = BLACK):
    words = [word.split(' ') for word in text.splitlines()] 
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height 
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height

def upload_data_from_file():
    '''
    Файл устроен: 
    1ое значение - water, 2ое значение - electricity через "\n\n"
    далее данные для buildings вида "type,level,x,y\n"
    '''
    global buildings, water, electricity, screen
    with open("previous_game.txt", "r") as f:
        data = f.read()
    data = data.split('\n\n')
    water = int(data[0])
    electricity = int(data[1])
    data = data[2].split('\n')
    data = [i.split(',') for i in data]
    data = [[float(j) for j in i] for i in data]
    for i in data:
        new_bilding = Buildings(i[2], i[3], i[0], i[1], screen)
        buildings.append(new_bilding)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
buildings = []
water = 0
electricity = 0

# FIXME-Лера-настройка
button_start_new = Button(x = 300, y=200, width=BUTTON_WIDTH, height=BUTTON_HIGHT, text='start_new')
button_continue = Button(x = 300, y=100, width=BUTTON_WIDTH, height=BUTTON_HIGHT, text='continue')

finished = False
page = 'start'
clock = pygame.time.Clock()

while not finished:

    # '''Эти функции рисования написаны по приколу, в дальнейшем функции 
    # рисования объектов будут принимать только объект'''
    # draw_fon(screen, 0, 0)
    # draw_setka(screen, WIDTH, HEIGHT)
    # draw_building(screen, 100, 200)
    # pygame.display.update()
    
    if page == 'start':
        screen.fill(WHITE)

        # FIXME-Лера-настройка и тексты
        font0 = pygame.font.SysFont(None, 64)
        img0 = font0.render('Страница - start', True, BLACK)
        screen.blit(img0, (200, 20))
        begginingtext = 'Правила игры: \n прописывай Лера'
        font = pygame.font.SysFont("Calibri", 18)
        blit_text(screen, begginingtext, (WIDTH*0.02, HEIGHT*0.2), font)

        button_start_new.draw(window=screen)
        button_continue.draw(window=screen)

        pygame.display.update()

        for event in pygame.event.get():  

            button_start_new.get_pressed(event)
            button_continue.get_pressed(event)

            if event.type == pygame.QUIT:
                finished = True

            if button_continue.pressed and event.type == pygame.MOUSEBUTTONDOWN:
                upload_data_from_file()
                page = 'main'
                # print(water, electricity, buildings)

            if button_start_new.pressed and event.type == pygame.MOUSEBUTTONDOWN:
                page = 'main'

            if event.type == pygame.QUIT:
                finished = True

    if page == 'main':        
        screen.fill(COLOR)

        for b in buildings:
            b.draw()

        # FIXME-Лера-настройка
        font0 = pygame.font.SysFont(None, 64)
        img0 = font0.render('Cтраница - main', True, BLACK)
        screen.blit(img0, (200, 20))
        font1 = pygame.font.SysFont(None, 24)
        img1 = font1.render('Вода:  ' + str(water), True, BLACK)
        screen.blit(img1, (20, 20))
        font2 = pygame.font.SysFont(None, 24)
        img2 = font2.render('Электричество:  ' + str(electricity), True, BLACK)
        screen.blit(img2, (20, 50))

        pygame.display.update()

        for event in pygame.event.get():                               
            if event.type == pygame.QUIT:
                finished = True

    if page == 'build':

        screen.fill(BLACK)
        pygame.display.update()

        # FIXME-Юля реализвать всплывающее окно с объектами для строительства

        for event in pygame.event.get():                               
            if event.type == pygame.QUIT:
                finished = True

pygame.quit()
