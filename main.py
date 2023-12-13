import math
import random
import random as rd
"""import numpy as np
"""
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

BUTTON_WIDTH = WIDTH / 3
BUTTON_HIGHT = HEIGHT / 15
BUTTON_LEN = 200

HOUSE_LEN = len_width * 2
HOUSE_HIGHT = len_height * 1
WATER_LEN = len_width * 1
WATER_HIGHT = len_height * 1
ELECTRICITY_LEN = len_width * 1
ELECTRICITY_HIGHT = len_height * 1
PARK_LEN = len_width * 1
PARK_HIGHT = len_height * 1


HOUSE_COST =100
HOUSE_POFIT = 1
ROAD_COST = 0
PARK_COST = 70
WATER_ROAD_COST = 10
ELECTRICITY_ROAD_COST = 10
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
resource_roads = []
monstrs=[]
water = 0
electricity = 0
score = 300

finished = False
page = 'start'
what_you_build = 'nothing'
text = ''
texttime = 0

# Юле: А тут после подгрузки данные из файла предыдущей игры нужно изменить и building_data
# ниже, после нажатия кнопки continue
connection_in(buildings, resources, water, electricity, screen, score)
buildings, resources, water, electricity, screen, score = connection_out()

clock = pygame.time.Clock()
load_fon()
time = 0

while not finished:
    real_fps = int(clock.get_fps())
    clock.tick(FPS)

    if page == 'start':
        screen.fill(WHITE)
        draw_fon_start(screen, time)

        # FIXME-Лера-настройка
        button_start_new = Button(x=125, y=600, width=BUTTON_WIDTH, height=BUTTON_HIGHT, text='START', )
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

                # Подгрузка данных в массив building_data из данных о предыдущей игре
                for b in buildings:
                    building_data = add_data('house', building_data, b)
                for r in resources:
                    building_data = add_data('water', building_data, r)
                # print(building_data)

            if button_start_new.pressed and event.type == pygame.MOUSEBUTTONDOWN:
                page = 'main'

            if event.type == pygame.QUIT:
                finished = True

    if page == 'main':
        screen.fill(COLOR)

        # FIXME-Лера-настройка
        button_save = Button(x=WIDTH * 0.8, y=HEIGHT * 0.9, width=BUTTON_WIDTH / 2, height=BUTTON_HIGHT/5*3,
                             color_text=BLACK, text='SAVE', size_text=20)
        #!!!!!!!!!!!!!!!новая кнопка
        button_underground = Button(WIDTH * 0.8, HEIGHT * 0.95, BUTTON_WIDTH / 2, BUTTON_HIGHT/5*3, (100, 0, 150, 100),'black','underground', 20)
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
            draw_road(screen, s)
        #for w in resource_roads:
            #draw_water_road(screen, w)
        for r in resources:
            draw_resources(screen, r)
        for p in parks:
            draw_park(screen, p)
        for b in buildings:
            ''' Цикл проверяет есть ли уже монстры и ресурсы у замка, если их нет но пришло их время, то создает и рисует их вместе с замком'''
            if b[0].time%700==0 and b[1]==None:
                b[1]=button_huyna = Button(b[0].x + 75, b[0].y - 75, width=40, height=40,
                                          color_text=(0, 0, 0), text='ХУЙ', size_text=20)
            if b[0].time%b[0].monstr_time==0 and b[2]==None:
                mass=place_for_monstr(b[0], building_data)
                if mass!=[0,0]:
                    b[0].m = 0
                    b[2]=button_monstr = Button(mass[0],
                                           mass[1], width=75, height=75,
                                           color_text=(0, 0, 0), text='MONSTR', size_text=20)
                    building_data=add_data("monster", building_data, b[2])
                    print(building_data)
            if b[2]!=None:
                b[2].draw(window=screen)
            draw_building(screen, b[0])
            if b[1]!=None:
                b[1].draw(window=screen)
            b[0].time+=1
            b[0].level = b[0].m * min( max(1,  b[0].park + b[0].water + b[0].electricity), 3)


        button_save.draw(window=screen)
        button_underground.draw(window=screen)
        # FIXME-Лера-настройка
        font0 = pygame.font.SysFont(None, 64)
        img0 = font0.render('', True, BLACK)
        screen.blit(img0, (200, 20))
        font1 = pygame.font.SysFont(None, 24)
        img1 = font1.render('Вода:  ' + str(water), True, BLACK)
        screen.blit(img1, (20, 20))
        font2 = pygame.font.SysFont(None, 24)
        img2 = font2.render('Электричество:  ' + str(electricity), True, BLACK)
        screen.blit(img2, (20, 50))
        font3 = pygame.font.SysFont(None, 24)
        img3 = font3.render('Счёт:  ' + str(score), True, BLACK)
        screen.blit(img3, (20, 80))

        if pygame.time.get_ticks() - texttime < 500 and text == 'save':
            font_ = pygame.font.SysFont(None, 40)
            img_ = font_.render('Игра сохранена', True, WHITE)
            screen.blit(img_, (WIDTH * 0.4, HEIGHT / 2))

        pygame.display.update()

        for event in pygame.event.get():
            for b in buildings:
                '''проверяеи не нажат ли ресурс/ монстр рядом с каким либо замком'''
                if b[2]!=None:
                    b[2].get_pressed(event)
                    if b[2].pressed and event.type == pygame.MOUSEBUTTONDOWN:
                        varioty = random.randint(0, 1)
                        if varioty == 1:
                            building_data[b[2].y//len_height][b[2].x//len_width]=None
                            b[2] = None
                            b[0].m = 1
                        else:
                            if score>=50:
                                score -= 50

                if b[1]!=None:
                    b[1].get_pressed(event)
                    if b[1].pressed and event.type == pygame.MOUSEBUTTONDOWN:
                        b[1] = None
                        score += 10 * b[0].level
            button_save.get_pressed(event)
            button_underground.get_pressed(event)
            if button_save.pressed and event.type == pygame.MOUSEBUTTONDOWN:
                save_to_file()
                text = 'save'
                texttime = pygame.time.get_ticks()
                
            if button_underground.pressed and event.type == pygame.MOUSEBUTTONDOWN:
                page = 'underground'
                
            if event.type == pygame.QUIT:
                finished = True
            # если на странице main нажать правую кнопку мыши, открывается окно build
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                page = 'build'

    #страница underground
    if page == 'underground':
        draw_fon1(screen)
        for s in roads:
            draw_road(screen, s)
        for p in parks:
            draw_park(screen, p)
        for r in resources:
            draw_resources(screen, r)
        for b in buildings:
            b[0].level = b[0].m * min( max(1,  b[0].park + b[0].water + b[0].electricity), 3)
            draw_building(screen, b[0])
        button_back=Button(WIDTH * 0.8, HEIGHT * 0.95, BUTTON_WIDTH / 2, BUTTON_HIGHT/5*3, (100, 0, 150, 100), 'black', 'underground', 20)
        button_back.draw(window=screen)
        for w in resource_roads:
            draw_water_road(screen, w)
        for event in pygame.event.get():
            button_back.get_pressed(event)
            if button_back.pressed and event.type == pygame.MOUSEBUTTONDOWN:

                page = 'main'
        
        pygame.display.update()

    if page == 'process of build':

        draw_fon(screen, 0, 0)

        # Вывод реального fps
        font = pygame.font.SysFont(None, 20)
        fps_label = font.render(f"FPS: {real_fps}", True, "RED")
        screen.blit(fps_label, (20, HEIGHT - 20))

        for s in roads:
            draw_road(screen, s)
        for p in parks:
            draw_park(screen, p)
        for w in resource_roads:
            draw_water_road(screen, w)
        for r in resources:
            draw_resources(screen, r)
        for b in buildings:
            b[0].level = b[0].m * min( max(1,  b[0].park + b[0].water + b[0].electricity), 3)
            draw_building(screen, b[0])

        mouse_x, mouse_y = pygame.mouse.get_pos()
        able = check_the_place(what_you_build, building_data, mouse_x, mouse_y)

        if what_you_build == 'house':
            process_building(screen, mouse_x, mouse_y, HOUSE_LEN, HOUSE_HIGHT, able)
        if what_you_build == 'water':
            process_building(screen, mouse_x, mouse_y, WATER_LEN, WATER_HIGHT, able)
        if what_you_build == 'electricity':
            process_building(screen, mouse_x, mouse_y, ELECTRICITY_LEN, ELECTRICITY_HIGHT, able)
        if what_you_build == 'road':
            process_building(screen, mouse_x, mouse_y, 75, 75, able)
        if what_you_build == 'park':
            process_building(screen, mouse_x, mouse_y, PARK_LEN, PARK_HIGHT, able)

        draw_setka(screen)

        # FIXME-Лера-настройка
        button_quit_build = Button(x=WIDTH * 0.8, y=HEIGHT * 0.9, width=BUTTON_WIDTH / 2, height=BUTTON_HIGHT/5*3,
                             color_text=BLACK, text='FINISH', size_text=20)
        button_quit_build.draw(window=screen)

        # FIXME-Лера-настройка
        font0 = pygame.font.SysFont(None, 64)
        img0 = font0.render('', True, WHITE)
        img3 = font3.render('Счёт:  ' + str(score), True, WHITE)
        screen.blit(img3, (20, 80))

        img_3 = font3.render(str(score) + ' / ' + str(get_score(what_you_build=what_you_build)), True, WHITE)
        screen.blit(img_3, (mouse_x + 10, mouse_y - 10))

        pygame.display.update()

        enough_score = check_score(score, what_you_build)
        mouse_x, mouse_y = get_xy(mouse_x, mouse_y)

        for event in pygame.event.get():
            button_quit_build.get_pressed(event)

            if (button_quit_build.pressed and event.type == pygame.MOUSEBUTTONDOWN) or not (enough_score):
                what_you_build = 'nothing'
                page = 'main'

            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and what_you_build == 'house':
                if check_the_place(what_you_build, building_data, mouse_x, mouse_y):
                    new_home = Buildings(mouse_x, mouse_y, type, 1, screen=screen)
                    buildings.append([new_home, None, None])
                    building_data = add_data(what_you_build, building_data, new_home)
                    # print(building_data)
                    # print(building_data[new_home.y//len_height][new_home.x//len_width])
                    park_check(building_data, new_home, buildings, parks)
                    
                    score -= HOUSE_COST
                else:
                    print('error')
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and what_you_build == 'water':
                if check_the_place(what_you_build, building_data, mouse_x, mouse_y):
                    new_resource = Resources(mouse_x, mouse_y, 1, screen=screen)
                    resources.append(new_resource)
                    building_data = add_data(what_you_build, building_data, new_resource)
                    # print(building_data)
                    score -= WATER_COST
                else:
                    print('error')
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and what_you_build == 'electricity':
                if check_the_place(what_you_build, building_data, mouse_x, mouse_y):
                    new_resource = Resources(mouse_x, mouse_y, 2, screen=screen)
                    resources.append(new_resource)
                    building_data = add_data(what_you_build, building_data, new_resource)
                    # print(building_data)

                    score -= ELECTRICITY_COST
                else:
                    print('error')
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and what_you_build == 'road':
                if check_the_place(what_you_build, building_data, mouse_x, mouse_y):
                    type_road = which_road(mouse_x, mouse_y, building_data)
                    new_resource = Roads(mouse_x, mouse_y, type_road, screen=screen)
                    # if proverka_of_road(building_data, mouse_x, mouse_y, new_resource):
                    #     roads.append(new_resource)
                    #     building_data = add_data(what_you_build, building_data, new_resource)
                    roads.append(new_resource)
                    building_data = add_data(what_you_build, building_data, new_resource)
                    score -= ROAD_COST
                else:
                    print('error')
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and what_you_build == 'park':
                # print(check_the_place(what_you_build, building_data, mouse_x, mouse_y))
                if check_the_place(what_you_build, building_data, mouse_x, mouse_y):
                    new_park = Parks(mouse_x, mouse_y, 1, 1, screen=screen)
                    parks.append(new_park)
                    # print(new_park.x, new_park.y)
                    building_data = add_data(what_you_build, building_data, new_park)
                    # print(building_data)
                    park_check(building_data, new_park, buildings, parks)
                    score -= PARK_COST
                else:
                    print('error')

            # ==============================================================
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and what_you_build == 'water_road' and coordinates_type == 2:
                mouse_x2, mouse_y2 = pygame.mouse.get_pos()
                mouse_x2, mouse_y2 = get_xy(mouse_x2, mouse_y2)
                new_water_road = Resource_roads(mouse_x1, mouse_y1, mouse_x2, mouse_y2, 1, screen)
                resource_roads.append(new_water_road)
                score -= WATER_ROAD_COST
                water_road_check(building_data, new_water_road, buildings, resources)
                check_resource_road_type(building_data, new_water_road, resources)
                page = 'main'
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and what_you_build == 'water_road' and coordinates_type == 1:
                mouse_x1, mouse_y1 = pygame.mouse.get_pos()
                mouse_x1, mouse_y1 = get_xy(mouse_x1, mouse_y1)
                coordinates_type = 2

    if page == 'build':

        screen.fill(WHITE)
        draw_fon_menu(screen)

        # Вывод реального fps
        font = pygame.font.SysFont(None, 20)
        fps_label = font.render(f"FPS: {real_fps}", True, "RED")
        screen.blit(fps_label, (20, HEIGHT - 20))

        # FIXME-Лера-настройка
        button_build_road = Button(x=160, y=275, width=BUTTON_LEN , height=BUTTON_LEN, text='road')
        button_build_water = Button(x=840, y=40, width=BUTTON_LEN, height=BUTTON_LEN, text='lake')
        button_build_electricity = Button(x=840, y=275, width=BUTTON_LEN, height=BUTTON_LEN, text='mile')
        button_build_close = Button(x=WIDTH * 0.9, y=HEIGHT * 0.9, width=BUTTON_WIDTH / 4, height=BUTTON_HIGHT/5*3,
                             color_text=BLACK, text='CLOSE', size_text=20)
        button_build_park = Button(x=160, y=40, width=BUTTON_LEN, height=BUTTON_LEN, text='park')
        button_build_castle1 = Button(x=500, y=40,  width=BUTTON_LEN, height=BUTTON_LEN, text='castle 1')
        button_build_castle2 = Button(x=500, y=275, width=BUTTON_LEN, height=BUTTON_LEN, text='castle 2')
        button_build_castle3 = Button(x=500, y=510, width=BUTTON_LEN, height=BUTTON_LEN, text='castle 3')
        button_connect_water = Button(x=160, y=510, width=BUTTON_LEN, height=BUTTON_LEN, text='connect_objects')
        button_destroy = Button(x=840, y=510, width=BUTTON_LEN, height=BUTTON_LEN, text='demolition')



        button_build_road.draw(window=screen)
        button_build_close.draw(window=screen)
        button_build_water.draw(window=screen)
        button_build_electricity.draw(window=screen)
        button_build_park.draw(window=screen)
        button_build_castle1.draw(window=screen)
        button_build_castle2.draw(window=screen)
        button_build_castle3.draw(window=screen)
        button_connect_water.draw(window=screen)
        button_destroy.draw(window=screen)

        # FIXME-Лера-настройка
        if pygame.time.get_ticks() - texttime < 500 and text == 'not enough':
            len_x=WIDTH*0.6
            len_y=HEIGHT*0.2
            temp_surface = pygame.Surface([len_x, len_y], pygame.SRCALPHA)
            pygame.draw.rect(temp_surface, (150, 140, 255, 150), (0,0, len_x, len_y ), border_radius=20)
            screen.blit(temp_surface, [WIDTH * 0.2, HEIGHT*0.4])
            font_ = pygame.font.SysFont(None, 40)
            img_ = font_.render('Недостаточно счёта для строительства', True, (0, 0, 0))
            screen.blit(img_, (WIDTH * 0.3, HEIGHT*0.475))
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
            button_connect_water.get_pressed(event)

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

            if button_connect_water.pressed and event.type == pygame.MOUSEBUTTONDOWN and score >= WATER_ROAD_COST:
                what_you_build = 'water_road'
                coordinates_type = 1
                page = 'process of build'

            # если недостаточно счёта для строительства
            if ((button_build_castle1.pressed) or (button_build_castle2.pressed) or (
            button_build_castle3.pressed) and event.type == pygame.MOUSEBUTTONDOWN and score < HOUSE_COST) or (
                    button_build_water.pressed and event.type == pygame.MOUSEBUTTONDOWN and score < WATER_COST) or (
                    button_build_electricity.pressed and event.type == pygame.MOUSEBUTTONDOWN and score < ELECTRICITY_COST) or (
                    button_build_road.pressed and event.type == pygame.MOUSEBUTTONDOWN and score < ROAD_COST) or (
                    button_build_park.pressed and event.type == pygame.MOUSEBUTTONDOWN and score < PARK_COST) or (
                    button_connect_water.pressed and event.type == pygame.MOUSEBUTTONDOWN and score < WATER_ROAD_COST):
                texttime = pygame.time.get_ticks()
                text = 'not enough'

            # возвращает на страницу main при нажатии кнопки close
            if button_build_close.pressed and event.type == pygame.MOUSEBUTTONDOWN:
                page = 'main'

            if event.type == pygame.QUIT:
                finished = True

    time += 1

pygame.quit()
