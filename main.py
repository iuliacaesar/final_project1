import math
import random as rd
import numpy as np
from button import *
from objects import *
from visual import*
from field_data import*
import pygame

FPS = 60

# FIXME-Лера настройка значений всех параметров ниже, для адекватного расположенияэ всех элементов
# Такое редактировнаие нужно будет сделать не только здесь, а во всех частях где рисуются объекты, места подобных редактирований отмечаю "FIXME-Лера-настройка"

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLOR = (95, 189, 51)
WIDTH = 800
HEIGHT = 600
len_width = int(WIDTH/(8*5))
len_height = int(HEIGHT/(6*5))

BUTTON_WIDTH = 200
BUTTON_HIGHT = 60

HOUSE_LEN = len_width*3
HOUSE_HIGHT = len_height*2
WATER_LEN = len_width*3
WATER_HIGHT = len_height*3
ELECTRICITY_LEN = len_width*3
ELECTRICITY_HIGHT = len_height*3

HOUSE_COST = 10
HOUSE_POFIT = 1
ROAD_COST = 1
WATER_ROAD_COST = 1
ELECTRICITY_ROAD_COST = 1
WATER_COST = 50
ELECTRICITY_COST = 50
building_data = []
for i in range(30):
    building_data.append([0]*40)
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
    3e значение - данные для buildings вида "type,level,x,y\n"
    4ое значение - данные resousces вида "type,x,y\n"
    5ое значение - score
    '''
    global buildings, resources, water, electricity, screen, score
    with open("previous_game.txt", "r") as f:
        data = f.read()
    data = data.split('\n\n')
    water = int(data[0])
    electricity = int(data[1])
    score = int(data[4])
    data_ = data[2].split('\n')
    data_ = [i.split(',') for i in data_]
    data_ = [[float(j) for j in i] for i in data_]
    for i in data_:
        new_bilding = Buildings(i[2], i[3], i[0], i[1], screen)
        buildings.append(new_bilding)
    data = data[3].split('\n')
    data = [i.split(',') for i in data]
    data = [[float(j) for j in i] for i in data]
    for i in data:
        new_resourse = Resources(i[1], i[2], i[0], screen)
        resources.append(new_resourse)

def save_to_file():
    global buildings, resources, water, electricity, screen, score
    data_building =''
    data_resources =''
    for b in buildings:
        data_building += str(b.type)+','+str(b.level)+','+str(b.x)+','+str(b.y)+'\n'
    for b in resources:
        data_resources += str(b.type)+','+str(b.x)+','+str(b.y)+'\n'
    data = str(water)+'\n\n'+str(electricity)+'\n\n'+data_building+'\n'+data_resources+'\n'+str(score)
    with open("previous_game.txt", "w") as f:
        f.write(data)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
buildings = []
resources = []
water = 0
electricity = 0
score = 310

finished = False
page = 'start'
what_you_build = 'nothing'
text = ''
texttime = 0

clock = pygame.time.Clock()

while not finished:
    real_fps = int(clock.get_fps())
    clock.tick(FPS)

    if page == 'start':
        screen.fill(WHITE)

        # FIXME-Лера-настройка
        button_start_new = Button(x = 300, y=200, width=BUTTON_WIDTH, height=BUTTON_HIGHT, text='start_new')
        button_continue = Button(x = 300, y=100, width=BUTTON_WIDTH, height=BUTTON_HIGHT, text='continue')
        
        # Вывод реального fps
        font = pygame.font.SysFont(None, 20)
        fps_label = font.render(f"FPS: {real_fps}", True, "RED")
        screen.blit(fps_label, (20, HEIGHT-20))

        # FIXME-Лера-настройка и тексты
        font0 = pygame.font.SysFont(None, 64)
        img0 = font0.render('Страница - start', True, BLACK)
        screen.blit(img0, (200, 20))
        beginningtext = 'Правила игры: \n прописывай Лера'
        font = pygame.font.SysFont("Calibri", 18)
        blit_text(screen, beginningtext, (WIDTH*0.02, HEIGHT*0.2), font)

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

        # FIXME-Лера-настройка
        button_save = Button(x = WIDTH*0.8, y=HEIGHT*0.9, width=BUTTON_WIDTH/2, height=BUTTON_HIGHT/2, color_text=WHITE, text='Сохранить', size_text=20)

        '''Эти функции рисования написаны по приколу, в дальнейшем функции 
        рисования объектов будут принимать только объект'''
        draw_fon(screen, 0, 0)
        # draw_setka(screen)
        # draw_building(screen, 100, 200)

        # Вывод реального fps
        font = pygame.font.SysFont(None, 20)
        fps_label = font.render(f"FPS: {real_fps}", True, "RED")
        screen.blit(fps_label, (20, HEIGHT-20))

        for b in buildings:
            draw_building(screen, b.x, b.y)
            b.draw()
        for r in resources:
            r.draw()
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

        pygame.display.update()

        for event in pygame.event.get(): 
            button_save.get_pressed(event)    
            if button_start_new.pressed and event.type == pygame.MOUSEBUTTONDOWN:
                save_to_file()                  
            if event.type == pygame.QUIT:
                finished = True
            #если на странице main нажать правую кнопку мыши, открывается окно build
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                page = 'build'

    if page == 'process of build':

        '''Эти функции рисования написаны по приколу, в дальнейшем функции 
        рисования объектов будут принимать только объект'''
        draw_fon(screen, 0, 0)
        draw_setka(screen)
        # draw_setka(screen)
        # draw_building(screen, 100, 200)

        # Вывод реального fps
        font = pygame.font.SysFont(None, 20)
        fps_label = font.render(f"FPS: {real_fps}", True, "RED")
        screen.blit(fps_label, (20, HEIGHT-20))

        for b in buildings:
            draw_building(screen, b.x, b.y)
            b.draw()
        for r in resources:
            r.draw()

        if what_you_build == 'house':
            mouse_x, mouse_y = pygame.mouse.get_pos()
            process_building(screen, mouse_x, mouse_y, HOUSE_LEN, HOUSE_HIGHT)
        if what_you_build == 'water':
            mouse_x, mouse_y = pygame.mouse.get_pos()
            process_building(screen, mouse_x, mouse_y, WATER_LEN, WATER_HIGHT)
        if what_you_build == 'electricity':
            mouse_x, mouse_y = pygame.mouse.get_pos()
            process_building(screen, mouse_x, mouse_y, ELECTRICITY_LEN, ELECTRICITY_HIGHT)

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
                    print(building_data)
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
                    print(building_data)
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
                    print(building_data)
                    what_you_build = 'nothing'
                    score -= ELECTRICITY_COST
                    page = 'main'
                else:
                    print('error')
                    page = 'main'

    if page == 'build':
        screen.fill(WHITE)

        # Вывод реального fps
        font = pygame.font.SysFont(None, 20)
        fps_label = font.render(f"FPS: {real_fps}", True, "RED")
        screen.blit(fps_label, (20, HEIGHT-20))

        # FIXME-Лера-настройка       
        button_build_house = Button(x = 200, y=200, width=BUTTON_WIDTH, height=BUTTON_HIGHT, text='build_house')
        button_build_road = Button(x = 200, y=100, width=BUTTON_WIDTH, height=BUTTON_HIGHT, text='build_road')
        button_build_water = Button(x = 400, y=200, width=BUTTON_WIDTH, height=BUTTON_HIGHT, text='build_water')
        button_build_electricity = Button(x =400, y=100, width=BUTTON_WIDTH, height=BUTTON_HIGHT, text='build_electricity')
        button_build_close = Button(x = 300, y=500, width=BUTTON_WIDTH, height=BUTTON_HIGHT, text='close')
        
        button_build_house.draw(window=screen)
        button_build_road.draw(window=screen)
        button_build_close.draw(window=screen)
        button_build_water.draw(window=screen)
        button_build_electricity.draw(window=screen)

        # FIXME-Лера-настройка
        if pygame.time.get_ticks() - texttime < 500 and text == 'not enough':
            font_ = pygame.font.SysFont(None, 40)
            img_ = font_.render('Недостаточно счёта для строительства', True, BLACK)
            screen.blit(img_, (WIDTH*0.4, 10))

        pygame.display.update()

        for event in pygame.event.get():
            button_build_house.get_pressed(event)
            button_build_road.get_pressed(event)
            button_build_close.get_pressed(event)
            button_build_water.get_pressed(event)
            button_build_electricity.get_pressed(event)

            # строительсто дорог, домов, водяных вышек, электростанцый
            if button_build_road.pressed and event.type == pygame.MOUSEBUTTONDOWN and score >= ROAD_COST:
                what_you_build = 'road'
                page = 'process of build'

            if button_build_house.pressed and event.type ==pygame.MOUSEBUTTONDOWN and score >= HOUSE_COST:
                what_you_build = 'house'
                page = 'process of build'

            if button_build_water.pressed and event.type ==pygame.MOUSEBUTTONDOWN and score >= WATER_COST:
                what_you_build = 'water'
                page = 'process of build'

            if button_build_electricity.pressed and event.type ==pygame.MOUSEBUTTONDOWN and score >= ELECTRICITY_COST:
                what_you_build = 'electricity'
                page = 'process of build'

            # если недостаточно счёта для строительства
            if (button_build_house.pressed and event.type ==pygame.MOUSEBUTTONDOWN and score < HOUSE_COST) or (button_build_water.pressed and event.type ==pygame.MOUSEBUTTONDOWN and score < WATER_COST) or (button_build_electricity.pressed and event.type ==pygame.MOUSEBUTTONDOWN and score < ELECTRICITY_COST) or (button_build_road.pressed and event.type == pygame.MOUSEBUTTONDOWN and score < ROAD_COST):
                texttime = pygame.time.get_ticks()
                text = 'not enough'

            #возвращает на страницу main при нажатии кнопки close
            if button_build_close.pressed and event.type ==pygame.MOUSEBUTTONDOWN:
                page = 'main'

            if event.type == pygame.QUIT:
                finished = True


pygame.quit()

