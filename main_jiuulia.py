import math
import random
import random as rd
import numpy as np
from button import *
from objects import *
from visual import *
from inoutput import *
from field_data_functions import *
import pygame

FPS = 60

# FIXME-Лера настройка значений всех параметров ниже, для адекватного расположенияэ всех элементов
# Такое редактировнаие нужно будет сделать не только здесь, а во всех частях где рисуются объекты, места подобных редактирований отмечаю "FIXME-Лера-настройка"

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLOR = (95, 189, 51)
WIDTH = 1200
HEIGHT = 750
len_width = int(WIDTH / (16))
len_height = int(HEIGHT / (10))

BUTTON_WIDTH = WIDTH/3
BUTTON_HIGHT = HEIGHT/15

HOUSE_LEN = len_width * 2
HOUSE_HIGHT = len_height * 1
WATER_LEN = len_width * 1
WATER_HIGHT = len_height * 1
ELECTRICITY_LEN = len_width * 1
ELECTRICITY_HIGHT = len_height * 1
PARK_LEN = len_width * 1
PARK_HIGHT = len_height * 1

HOUSE_COST = 10
HOUSE_POFIT = 1
ROAD_COST = 1
PARK_COST = 20
WATER_ROAD_COST = 1
ELECTRICITY_ROAD_COST = 1
WATER_COST = 50
ELECTRICITY_COST = 50
building_data = []

# Юле: Здесь ты заполняешь None
for i in range(10):
    building_data.append([None] * 16)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
buildings = []
resources = []
roads = []
parks = []
water = 0
electricity = 0
score = 310

finished = False
page = 'start'
what_you_build = 'nothing'
text = ''
texttime = 0

# Юле: А тут после подгрузки данные из файла предыдущей игры нужно изменить и building_data
connection_in(buildings, resources, water, electricity, screen, score)
buildings, resources, water, electricity, screen, score = connection_out()

clock = pygame.time.Clock()
load_fon()
time=0

while not finished:
    real_fps = int(clock.get_fps())
    clock.tick(FPS)

    if page == 'start':
        screen.fill(WHITE)
        # draw_fon_start(screen, time)

        # FIXME-Лера-настройка
        button_start_new = Button(x=125, y=600, width=BUTTON_WIDTH, height=BUTTON_HIGHT, text='START',)
        button_continue = Button(x=675, y=600, width=BUTTON_WIDTH, height=BUTTON_HIGHT, text='CONTINUE', )

        # Вывод реального fps
        font = pygame.font.SysFont(None, 20)
        fps_label = font.render(f"FPS: {real_fps}", True, "RED")
        screen.blit(fps_label, (20, HEIGHT - 20))

        # FIXME-Лера-настройка и тексты
        font0 = pygame.font.SysFont(None, 64)
        img0 = font0.render('Страница - start', True, BLACK)
        screen.blit(img0, (200, 20))

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

            if button_start_new.pressed and event.type == pygame.MOUSEBUTTONDOWN:
                page = 'main'

            if event.type == pygame.QUIT:
                finished = True

    if page == 'main':
        screen.fill(COLOR)

        # FIXME-Лера-настройка
        button_save = Button(x=WIDTH * 0.8, y=HEIGHT * 0.9, width=BUTTON_WIDTH / 2, height=BUTTON_HIGHT / 2,
                             color_text=WHITE, text='Сохранить', size_text=20)

        '''Эти функции рисования написаны по приколу, в дальнейшем функции 
        рисования объектов будут принимать только объект'''
        draw_fon(screen, 0, 0)
        # draw_setka(screen)
        # draw_building(screen, 100, 200)

        # Вывод реального fps
        font = pygame.font.SysFont(None, 20)
        fps_label = font.render(f"FPS: {real_fps}", True, "RED")
        screen.blit(fps_label, (20, HEIGHT - 20))

        for s in roads:
            draw_building(screen, s)
        for b in buildings:
            draw_building(screen, b)
        for r in resources:
            draw_building(screen, r)
        for p in parks:
            draw_park(screen, p)

        button_save.draw(window=screen)

        # FIXME-Лера-настройка
        font0 = pygame.font.SysFont(None, 64)
        img0 = font0.render('Cтраница - main', True, WHITE)
        screen.blit(img0, (200, 20))
        font1 = pygame.font.SysFont(None, 24)
        img1 = font1.render('Вода:  ' + str(water), True, WHITE)
        screen.blit(img1, (20, 20))
        font2 = pygame.font.SysFont(None, 24)
        img2 = font2.render('Электричество:  ' + str(electricity), True, WHITE)
        screen.blit(img2, (20, 50))
        font3 = pygame.font.SysFont(None, 24)
        img3 = font3.render('Счёт:  ' + str(score), True, WHITE)
        screen.blit(img3, (20, 80))

        if pygame.time.get_ticks() - texttime < 500 and text == 'save':
            font_ = pygame.font.SysFont(None, 40)
            img_ = font_.render('Игра сохранена', True, WHITE)
            screen.blit(img_, (WIDTH * 0.4, HEIGHT / 2))

        pygame.display.update()

        for event in pygame.event.get():
            button_save.get_pressed(event)
            if button_save.pressed and event.type == pygame.MOUSEBUTTONDOWN:
                save_to_file()
                text = 'save'
                texttime = pygame.time.get_ticks()
            if event.type == pygame.QUIT:
                finished = True
            # если на странице main нажать правую кнопку мыши, открывается окно build
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                page = 'build'

    if page == 'process of build':

        draw_fon(screen, 0, 0)
        draw_setka(screen)

        # Вывод реального fps
        font = pygame.font.SysFont(None, 20)
        fps_label = font.render(f"FPS: {real_fps}", True, "RED")
        screen.blit(fps_label, (20, HEIGHT - 20))

        for s in roads:
            draw_building(screen, s)
        for b in buildings:
            draw_building(screen, b)
        for r in resources:
            draw_building(screen, r)
        for p in parks:
            draw_park(screen, p)

        if what_you_build == 'house':
            mouse_x, mouse_y = pygame.mouse.get_pos()
            process_building(screen, mouse_x, mouse_y, HOUSE_LEN, HOUSE_HIGHT)
        if what_you_build == 'water':
            mouse_x, mouse_y = pygame.mouse.get_pos()
            process_building(screen, mouse_x, mouse_y, WATER_LEN, WATER_HIGHT)
        if what_you_build == 'electricity':
            mouse_x, mouse_y = pygame.mouse.get_pos()
            process_building(screen, mouse_x, mouse_y, ELECTRICITY_LEN, ELECTRICITY_HIGHT)
        if what_you_build == 'road':
            mouse_x, mouse_y = pygame.mouse.get_pos()
            process_building(screen, mouse_x, mouse_y, 75, 75)
        if what_you_build == 'park':
            mouse_x, mouse_y = pygame.mouse.get_pos()
            process_building(screen, mouse_x, mouse_y, PARK_LEN, PARK_HIGHT)

        # FIXME-Лера-настройка
        font0 = pygame.font.SysFont(None, 64)
        img0 = font0.render('Cтраница - process of build', True, WHITE)
        img3 = font3.render('Счёт:  ' + str(score), True, WHITE)
        screen.blit(img3, (20, 80))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and what_you_build == 'house':
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mouse_x, mouse_y = get_xy(mouse_x, mouse_y)
                if check_the_place(what_you_build, building_data, mouse_x, mouse_y):
                    new_home = Buildings(mouse_x, mouse_y, 1, 1, screen=screen)
                    buildings.append(new_home)
                    building_data = add_data(what_you_build, building_data, new_home)
                    # print(building_data)
                    # print(building_data[new_home.y//len_height][new_home.x//len_width])
                    what_you_build = 'nothing'
                    score -= HOUSE_COST
                    page = 'main'
                else:
                    print('error')
                    page = 'main'
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and what_you_build == 'water':
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mouse_x, mouse_y = get_xy(mouse_x, mouse_y)
                if check_the_place(what_you_build, building_data, mouse_x, mouse_y):
                    new_resource = Resources(mouse_x, mouse_y, 1, screen=screen)
                    resources.append(new_resource)
                    building_data = add_data(what_you_build, building_data, new_resource)
                    # print(building_data)
                    what_you_build = 'nothing'
                    score -= WATER_COST
                    page = 'main'
                else:
                    print('error')
                    page = 'main'

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and what_you_build == 'electricity':
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mouse_x, mouse_y = get_xy(mouse_x, mouse_y)
                if check_the_place(what_you_build, building_data, mouse_x, mouse_y):
                    new_resource = Resources(mouse_x, mouse_y, 2, screen=screen)
                    resources.append(new_resource)
                    building_data = add_data(what_you_build, building_data, new_resource)
                    # print(building_data)
                    what_you_build = 'nothing'
                    score -= ELECTRICITY_COST
                    page = 'main'
                else:
                    print('error')
                    page = 'main'

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and what_you_build == 'road':
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mouse_x, mouse_y = get_xy(mouse_x, mouse_y)
                if check_the_place(what_you_build, building_data, mouse_x, mouse_y):
                    type = which_road(mouse_x, mouse_y, building_data)
                    new_resource = Roads(mouse_x, mouse_y, type, screen=screen)
                    # if proverka_of_road(building_data, mouse_x, mouse_y, new_resource):
                    #     roads.append(new_resource)
                    #     building_data = add_data(what_you_build, building_data, new_resource)
                    roads.append(new_resource)
                    building_data = add_data(what_you_build, building_data, new_resource)
                    what_you_build = 'nothing'
                    score -= ROAD_COST
                    page = 'main'
                else:
                    print('error')
                    page = 'main'

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and what_you_build == 'park':
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mouse_x, mouse_y = get_xy(mouse_x, mouse_y)
                # print(check_the_place(what_you_build, building_data, mouse_x, mouse_y))
                if check_the_place(what_you_build, building_data, mouse_x, mouse_y):
                    new_park = Parks(mouse_x, mouse_y, 1, 1, screen=screen)
                    parks.append(new_park)
                    # print(new_park.x, new_park.y)
                    building_data = add_data(what_you_build, building_data, new_park)
                    # print(building_data)
                    what_you_build = 'nothing'
                    score -= PARK_COST
                    page = 'main'
                else:
                    print('error')
                    page = 'main'

    if page == 'build':

        screen.fill(WHITE)
        # draw_fon_menu(screen)

        # Вывод реального fps
        font = pygame.font.SysFont(None, 20)
        fps_label = font.render(f"FPS: {real_fps}", True, "RED")
        screen.blit(fps_label, (20, HEIGHT - 20))

        # FIXME-Лера-настройка
        button_build_house = Button(x=200, y=200, width=BUTTON_WIDTH, height=BUTTON_HIGHT, text='build_house')
        button_build_road = Button(x=200, y=100, width=BUTTON_WIDTH, height=BUTTON_HIGHT, text='build_road')
        button_build_water = Button(x=400, y=200, width=BUTTON_WIDTH, height=BUTTON_HIGHT, text='build_water')
        button_build_electricity = Button(x=400, y=100, width=BUTTON_WIDTH, height=BUTTON_HIGHT,
                                          text='build_electricity')
        button_build_close = Button(x=300, y=500, width=BUTTON_WIDTH, height=BUTTON_HIGHT, text='close')
        button_build_park = Button(x=400, y=300, width=BUTTON_WIDTH, height=BUTTON_HIGHT, text='build_park')
        button_build_castle1 = Button(x=200, y=200, width=BUTTON_WIDTH, height=BUTTON_HIGHT, text='build_castle1')
        button_build_castle2 = Button(x=200, y=300, width=BUTTON_WIDTH, height=BUTTON_HIGHT, text='build_castle2')
        button_build_castle3 = Button(x=200, y=400, width=BUTTON_WIDTH, height=BUTTON_HIGHT, text='build_castle3')

        
        button_build_house.draw(window=screen)
        button_build_road.draw(window=screen)
        button_build_close.draw(window=screen)
        button_build_water.draw(window=screen)
        button_build_electricity.draw(window=screen)
        button_build_park.draw(window=screen)
        button_build_castle1.draw(window=screen)
        button_build_castle2.draw(window=screen)
        button_build_castle3.draw(window=screen)

        # FIXME-Лера-настройка
        if pygame.time.get_ticks() - texttime < 500 and text == 'not enough':
            font_ = pygame.font.SysFont(None, 40)
            img_ = font_.render('Недостаточно счёта для строительства', True, BLACK)
            screen.blit(img_, (WIDTH * 0.4, 10))

        pygame.display.update()

        for event in pygame.event.get():
            button_build_castle1.get_pressed(event)
            button_build_castle2.get_pressed(event)
            button_build_castle3.get_pressed(event)
            button_build_road.get_pressed(event)
            button_build_close.get_pressed(event)
            button_build_water.get_pressed(event)
            button_build_electricity.get_pressed(event)
            button_build_park.get_pressed(event)

            # строительсто дорог, домов, водяных вышек, электростанцый
            if button_build_road.pressed and event.type == pygame.MOUSEBUTTONDOWN and score >= ROAD_COST:
                what_you_build = 'road'
                page = 'process of build'

            if button_build_castle1.pressed and event.type == pygame.MOUSEBUTTONDOWN and score >= HOUSE_COST:
                what_you_build = 'house'
                type = 1
                page = 'process of build'
                
            if button_build_castle2.pressed and event.type == pygame.MOUSEBUTTONDOWN and score >= HOUSE_COST:
                what_you_build = 'house'
                type = 2
                page = 'process of build'
                
            if button_build_castle3.pressed and event.type == pygame.MOUSEBUTTONDOWN and score >= HOUSE_COST:
                what_you_build = 'house'
                type = 3
                page = 'process of build'

            if button_build_water.pressed and event.type == pygame.MOUSEBUTTONDOWN and score >= WATER_COST:
                what_you_build = 'water'
                page = 'process of build'

            if button_build_electricity.pressed and event.type == pygame.MOUSEBUTTONDOWN and score >= ELECTRICITY_COST:
                what_you_build = 'electricity'
                page = 'process of build'

            if button_build_park.pressed and event.type == pygame.MOUSEBUTTONDOWN and score >= PARK_COST:
                what_you_build = 'park'
                page = 'process of build'

            # если недостаточно счёта для строительства
            if ((button_build_castle1.pressed) or (button_build_castle2.pressed) or (button_build_castle3.pressed) and event.type == pygame.MOUSEBUTTONDOWN and score < HOUSE_COST) or (
                    button_build_water.pressed and event.type == pygame.MOUSEBUTTONDOWN and score < WATER_COST) or (
                    button_build_electricity.pressed and event.type == pygame.MOUSEBUTTONDOWN and score < ELECTRICITY_COST) or (
                    button_build_road.pressed and event.type == pygame.MOUSEBUTTONDOWN and score < ROAD_COST) or (
                    button_build_park.pressed and event.type == pygame.MOUSEBUTTONDOWN and score < PARK_COST):
                texttime = pygame.time.get_ticks()
                text = 'not enough'

            # возвращает на страницу main при нажатии кнопки close
            if button_build_close.pressed and event.type == pygame.MOUSEBUTTONDOWN:
                page = 'main'

            if event.type == pygame.QUIT:
                finished = True
   
    
    time+=1

pygame.quit()
