WIDTH = 1200
HEIGHT = 750
len_width = int(WIDTH / (16))
len_height = int(HEIGHT / (10))

HOUSE_LEN = len_width * 2
HOUSE_HIGHT = len_height * 1
WATER_LEN = len_width * 1
WATER_HIGHT = len_height * 1
ELECTRICITY_LEN = len_width * 1
ELECTRICITY_HIGHT = len_height * 1
PARK_LEN = len_width * 1
PARK_HIGHT = len_height * 1
ROAD_LEN = len_width * 1
ROAD_HIGHT = len_height * 1


def add_data(what_you_build, building_data, obj):
    '''
    функция записывает в массив данные об ячейках сетки, занятой постройкой
    аргументы: тип постройки(house, water, electricity), массив для записи данных, объект, информация о котором записывается в массив
    возвращает: массив с данными о занятых ячейках сетки
    None - ячейка свободна, объект класса постройки - занят постройкой, для класса Buildings, занимающего 2 ячейки, в левой ячейке записан обьект, в правой - 1
    '''
    if what_you_build == 'house':
        building_data[obj.y // len_height][obj.x // len_width] = obj
        building_data[obj.y // len_height][obj.x // len_width + 1] = 1

    if what_you_build == 'electricity':
        building_data[obj.y // len_height][obj.x // len_width] = obj

    if what_you_build == 'water':
        building_data[obj.y // len_height][obj.x // len_width] = obj

    if what_you_build == 'park':
        building_data[obj.y // len_height][obj.x // len_width] = obj

    if what_you_build == 'road':
        building_data[obj.y // len_height][obj.x // len_width] = obj
    return building_data


def check_the_place(what_you_build, building_data, x, y):
    '''
    функция проверяет возможность постройки объекта в выбранном месте (свободны ли ячейки, не вылезает ли за размеры игрового поля
    аргументы: тип постройки(house, water, electricity), массив для записи данных, x, y - координаты постройки
    возвращает: True - если постройка на этом месте возможна, False - если невозможно построить объект
    '''
    flag = True
    if what_you_build == 'house':
        if y // len_height + HOUSE_HIGHT // len_height > HEIGHT // len_height or x // len_width + HOUSE_LEN // len_width > WIDTH // len_width or y == 0:
            flag = False
        else:
            if building_data[y // len_height][x // len_width] != None or building_data[y // len_height][
                x // len_width + 1] != None:
                flag = False


    elif what_you_build == 'electricity':
        if y // len_height + ELECTRICITY_HIGHT // len_height > HEIGHT // len_height or x // len_width + ELECTRICITY_LEN // len_width > WIDTH // len_width:
            flag = False
        else:
            if building_data[y // len_height][x // len_width] != None:
                flag = False


    elif what_you_build == 'water':
        if y // len_height + WATER_HIGHT // len_height > HEIGHT // len_height or x // len_width + WATER_LEN // len_width > WIDTH // len_width:
            flag = False
        else:
            if building_data[y // len_height][x // len_width] != None:
                flag = False


    elif what_you_build == 'park':
        if y // len_height + PARK_HIGHT // len_height > HEIGHT // len_height or x // len_width + PARK_LEN // len_width > WIDTH // len_width:
            flag = False
        else:
            if building_data[y // len_height][x // len_width] != None:
                flag = False

    elif what_you_build == 'road':
        if y // len_height + ROAD_HIGHT // len_height > HEIGHT // len_height or x // len_width + ROAD_LEN // len_width > WIDTH // len_width:
            flag = False
    return flag

def proverka_of_road(building_data, x, y, obj):

    x=x // len_width
    y=y // len_height
    s=[2,2,2,2]
    if type(building_data[y-1][x]).__name__=="Roads":
        if building_data[y-1][x].type[2]==1:
            s[0]=1
        else:
            s[0]=0

    if type(building_data[y][x+1]).__name__=="Roads":
        if building_data[y][x+1].type[3]==1:
            s[1]=1
        else:
            s[1]=0

    if type(building_data[y+1][x]).__name__=="Roads":
        if building_data[y+1][x].type[0]==1:
            s[2]=1
        else:
            s[2]=0

    if type(building_data[y][x-1]).__name__=="Roads":
        if building_data[y][x-1].type[1]==1:
            s[3]=1
        else:
            s[3]=0

    t=True

    for i in range(4):
        if (obj.type[i]==1 and s[i]==0) or (obj.type[i]==0 and s[i]==1):
           t=False
    return t


def water_road_check(building_data, obj, buildings, resources):
    '''
    функция проверяет, соединил ли водный провод замок и озеро (проверяет для дороги)
    аргументы: массив с данными о постройках, водный провод, массив с постройками, массив с ресурсами
    возвращает: True - если водный провод соединил замок и озеро, False - если нет
    '''
    



    obj_beginning = building_data[obj.beginning_y // len_height][obj.beginning_x // len_width]
    obj_ending = building_data[obj.ending_y // len_height][obj.ending_x // len_width]
    if obj_beginning in buildings:
        if obj_ending in resources and obj_ending.type == 1:
            obj_beginning.level = min(obj_beginning.level + 1, 3)
    elif obj_beginning == 1:
        if obj_ending in resources and obj_ending.type == 1:
            building_data[obj.beginning_y // len_height][obj.beginning_x // len_width - 1] = min(building_data[obj.beginning_y // len_height][obj.beginning_x // len_width - 1].level + 1, 3)
    elif obj_beginning in resources and obj_beginning.type == 1:
        if obj_ending in buildings:
            obj_ending.level = min(obj_ending.level + 1, 3)
        elif obj_ending == 1:
            building_data[obj.ending_y // len_height][obj.ending_x // len_width - 1] = min(building_data[obj.ending_y // len_height][obj.ending_x // len_width - 1].level + 1, 3)
'''
    if  obj_ending in resources:
        if obj_ending.type == 1:
            if obj_beginning in buildings:
                obj_beginning.level = min(obj_beginning.level + 1, 3)
            if obj_beginning == 1:
                building_data[obj.beginning_y // len_height][obj.beginning_x // len_width - 1] = min(building_data[obj.beginning_y // len_height][obj.beginning_x // len_width - 1].level + 1, 3)
    if  obj_beginning in resources:
        if obj_beginning.type == 1:
            if obj_ending in buildings:
                obj_ending.level = min(obj_ending.level + 1, 3)
            if obj_ending == 1:
                building_data[obj.ending_y // len_height][obj.ending_x // len_width - 1] = min(building_data[obj.ending_y // len_height][obj.ending_x // len_width - 1].level + 1, 3)
 '''   





'''
def check_for_the_object(building_data, obj, buildings, resources, resource_roads):
    for wr in resource_roads:
        if wr.beginning_x // len_width == obj.x and wr.beginning_y // len_height == obj.y:
            if obj in buildings and building_data[wr.ending_y // len_height][wr.ending_x // len_width] in resources:
                if building_data[wr.ending_y // len_height][wr.ending_x // len_width].type == 1:
                    obj.level = min(obj.level + 1, 3)
            elif obj in resources and building_data[wr.beginning_y // len_height][wr.beginning_x // len_width] in buildings:
                if building_data[wr.beginning_y // len_height][wr.beginning_x // len_width].type == 1:
                    building_data[wr.beginning_y // len_height][wr.beginning_x // len_width].level = min(building_data[wr.beginning_y // len_height][wr.beginning_x // len_width].level + 1, 3)
        
'''           

























        
