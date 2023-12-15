import math
import random
import random as rd
import numpy as np
from button import *
from objects import *
from visual import *
from field_data_functions import *
import pygame

# buildings = [] 
# resources = [] 
# water = 0
# electricity = 0
# screen = 0
# score = 0

def connection_in(b, r, w, e, a, m, scr, sco):
    global buildings, resources, roads, parks, resource_roads, monstrs, screen, score
    buildings = b
    resources = r
    roads = w
    parks = e
    resource_roads = a
    monstrs = m
    screen = scr
    score = sco

def connection_out():
    global buildings, resources, roads, parks, resource_roads, monstrs, screen, score
    return buildings, resources, roads, parks, resource_roads, monstrs, screen, score


def upload_data_from_file():
    """
    Считываем:
    score
    resources, roads, parks, resource_roads
    buildings
    """

    global buildings, resources, roads, parks, resource_roads, monstrs, screen, score

    with open("previous_game.txt", "r") as f:
        data = f.read()

    data = data.split("\n===\n")

    score = int(data[0])

    data_ = data[1].split('\n')
    for i in data_:
        if i != '': 
            j = list(map(int, i.split(',')))
            new_resourse = Resources(j[0], j[1], j[2], screen)
            resources.append(new_resourse)

    data_ = data[2].split('\n')
    for i in data_:
        if i != '':
            j = list(i.split(','))
            type = [int(j[2][0]), int(j[2][1]), int(j[2][2]), int(j[2][3])]
            new_resourse = Roads(int(j[0]), int(j[1]), type, screen)
            roads.append(new_resourse)

    data_ = data[3].split('\n')
    for i in data_:
        if i != '':
            j = list(map(int, i.split(',')))
            new_resourse = Parks(j[0], j[1], j[2], j[3], screen)
            parks.append(new_resourse)

    data_ = data[4].split('\n')
    for i in data_:
        if i != '':
            j = list(map(int, i.split(',')))
            new_resourse = Resource_roads(0, 0, 1, screen, j[0], j[1], j[2], j[3])
            resource_roads.append(new_resourse)

    data_ = data[5].split('\n')
    for i in data_:
        if i != '':
            j = list(map(int, i.split(',')))
            if j[0] == 0:
                new_building = Buildings(j[1], j[2], j[3], j[4], screen)
                new_buttom_1 = Button(j[5], j[6], width=40, height=40, color_text=(0, 0, 0), text='block', size_text=20)
                new_buttom_2 = Button(j[7], j[8], width=75, height=75, color_text=(0, 0, 0), text='MONSTR', size_text=20)
                buildings.append([new_building, new_buttom_1, new_buttom_2])
            if j[0] == 1:
                new_building = Buildings(j[1], j[2], j[3], j[4], screen)
                new_buttom_1 = Button(j[5], j[6], width=40, height=40, color_text=(0, 0, 0), text='block', size_text=20)
                buildings.append([new_building, new_buttom_1, None])
            if j[0] == 2:
                new_building = Buildings(j[1], j[2], j[3], j[4], screen)
                new_buttom_1 = Button(j[5], j[6], width=40, height=40, color_text=(0, 0, 0), text='block', size_text=20)
                buildings.append([new_building, None, new_buttom_1])
            if j[0] == 3:
                new_building = Buildings(j[1], j[2], j[3], j[4], screen)
                buildings.append([new_building, None, None])


def save_to_file():
    """
    Сохраняем:
    score
    resources, roads, parks, resource_roads
    buildings
    """

    global buildings, resources, roads, parks, resource_roads, monstrs, screen, score

    data_resources = ''
    data_roads = ''
    data_parks = ''
    data_resource_roads = ''
    data_buildings = ''

    for b in resources:
        data_resources += str(b.x) + ',' + str(b.y) + ',' + str(b.get_type()) + '\n'
    for b in parks:
        data_parks += str(b.x) + ',' + str(b.y) + ',' + str(int(b.type)) + ',' + str(int(b.level))+ '\n'
    for b in roads:
        data_roads += str(b.x) + ',' + str(b.y) + ',' + str(b.type[0])+ str(b.type[1])+ str(b.type[2])+ str(b.type[3]) + '\n'
    for b in resource_roads:
        data_resource_roads += str(b.beginning_x) + ',' + str(b.beginning_y) + ',' + str(int(b.ending_x)) + ',' + str(int(b.ending_y)) + '\n'

    for b in buildings:
        if b[1] != None and b[2] != None:
            data_buildings += '0,' + str(b[0].x) + ',' + str(b[0].y) + ',' + str(b[0].get_type()) + ',' + str(b[0].level) + ',' + str(b[1].x) + ',' + str(b[1].y) + ',' + str(b[2].x) + ',' + str(b[2].y) + '\n'
        elif b[1] != None:
            data_buildings += '1,' + str(b[0].x) + ',' + str(b[0].y) + ',' + str(b[0].get_type()) + ',' + str(b[0].level) + ',' + str(b[1].x) + ',' + str(b[1].y)  + '\n'
        elif b[2] != None:
            data_buildings += '2,' + str(b[0].x) + ',' + str(b[0].y) + ',' + str(b[0].get_type()) + ',' + str(b[0].level) + ',' + str(b[2].x) + ',' + str(b[2].y) + '\n'
        else:
            data_buildings += '3,' + str(b[0].x) + ',' + str(b[0].y) + ',' + str(b[0].get_type()) + ',' + str(b[0].level) + '\n'
    data = str(score) + "\n===\n" + data_resources + "\n===\n" + data_roads + "\n===\n" + data_parks + "\n===\n" + data_resource_roads + "\n===\n" + data_buildings
   
    with open("previous_game.txt", "w") as f:
        f.write(data)