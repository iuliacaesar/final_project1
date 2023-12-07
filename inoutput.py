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

def connection_in(b, r, w, e, scr, sco):
    global buildings, resources, water, electricity, screen, score
    buildings = b
    resources = r
    water = w
    electricity = e
    screen = scr
    score = sco

def connection_out():
    global buildings, resources, water, electricity, screen, score
    return buildings, resources, water, electricity, screen, score


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
    data_ = [[int(j) for j in i] for i in data_]
    for i in data_:
        new_bilding = Buildings(int(i[2]), int(i[3]), i[0], i[1], screen)
        buildings.append(new_bilding)
    data = data[3].split('\n')
    data = [i.split(',') for i in data]
    data = [[int(j) for j in i] for i in data]
    for i in data:
        new_resourse = Resources(int(i[1]), i[2], i[0], screen)
        resources.append(new_resourse)


def save_to_file():
    global buildings, resources, water, electricity, screen, score
    data_building = ''
    data_resources = ''
    for b in buildings:
        data_building += str(int(b.type)) + ',' + str(int(b.level)) + ',' + str(b.x) + ',' + str(b.y) + '\n'
    for b in resources:
        data_resources += str(int(b.type)) + ',' + str(b.x) + ',' + str(b.y) + '\n'
    data = str(water) + '\n\n' + str(electricity) + '\n\n' + data_building + '\n' + data_resources + '\n' + str(score)
    with open("previous_game.txt", "w") as f:
        f.write(data)