import random

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
        else:
            if building_data[y // len_height][x // len_width] != None and building_data[y // len_height][
                x // len_width] != 1:
                if type(building_data[y // len_height][x // len_width]).__name__ == "Roads":
                    flag = False
    return flag


def proverka_of_road(building_data, x, y, obj):
    x = x // len_width
    y = y // len_height
    s = [2, 2, 2, 2]
    if type(building_data[y - 1][x]).__name__ == "Roads":
        if building_data[y - 1][x].type[2] == 1:
            s[0] = 1
        else:
            s[0] = 0

    if type(building_data[y][x + 1]).__name__ == "Roads":
        if building_data[y][x + 1].type[3] == 1:
            s[1] = 1
        else:
            s[1] = 0

    if type(building_data[y + 1][x]).__name__ == "Roads":
        if building_data[y + 1][x].type[0] == 1:
            s[2] = 1
        else:
            s[2] = 0

    if type(building_data[y][x - 1]).__name__ == "Roads":
        if building_data[y][x - 1].type[1] == 1:
            s[3] = 1
        else:
            s[3] = 0

    t = True

    for i in range(4):
        if (obj.type[i] == 1 and s[i] == 0) or (obj.type[i] == 0 and s[i] == 1):
            t = False
    return t


def which_road(x, y, building_data):
    '''
    Используется при строительстве новой дороги:
    автоматически определяет тип дороги по тому, рядом с какими дорогами ставится новая
    получает x, y, building_data
    возвращает type_
    '''
    x = int(x // len_width)
    y = int(y // len_height)
    field_end = x - 1 < 0 or y - 1 < 0 or x + 1 > len(building_data[0]) - 1 or y + 1 > len(building_data) - 1
    type_ = [0, 0, 0, 0]
    # type(building_data[x][y-1].__name__=="Buildings" or type(building_data[x][y+1]).__name__=="Roads"
    if not (field_end):
        if building_data[y - 1][x] != None:
            if type(building_data[y - 1][x]).__name__ == "Roads":
                type_[0] = 1
                privios_road = building_data[y - 1][x]
                privios_road.type[2] = 1
        if building_data[y + 1][x] != None:
            if type(building_data[y + 1][x]).__name__ == "Roads":
                type_[2] = 1
                privios_road = building_data[y + 1][x]
                privios_road.type[0] = 1
        if building_data[y][x + 1] != None:
            if type(building_data[y][x + 1]).__name__ == "Roads":
                type_[1] = 1
                privios_road = building_data[y][x + 1]
                privios_road.type[3] = 1
        if building_data[y][x - 1] != None:
            if type(building_data[y][x - 1]).__name__ == "Roads":
                type_[3] = 1
                privios_road = building_data[y][x - 1]
                privios_road.type[1] = 1

    elif x - 1 < 0:
        if y - 1 < 0:
            if building_data[y + 1][x] != None:
                if type(building_data[y + 1][x]).__name__ == "Roads":
                    type_[2] = 1
                    privios_road = building_data[y + 1][x]
                    privios_road.type[0] = 1
            if building_data[y][x + 1] != None:
                if type(building_data[y][x + 1]).__name__ == "Roads":
                    type_[1] = 1
                    privios_road = building_data[y][x + 1]
                    privios_road.type[3] = 1
        elif y + 1 > len(building_data) - 1:
            if building_data[y - 1][x] != None:
                if type(building_data[y - 1][x]).__name__ == "Roads":
                    type_[0] = 1
                    privios_road = building_data[y - 1][x]
                    privios_road.type[2] = 1
            if building_data[y][x + 1] != None:
                if type(building_data[y][x + 1]).__name__ == "Roads":
                    type_[1] = 1
                    privios_road = building_data[y][x + 1]
                    privios_road.type[3] = 1
        else:
            if building_data[y - 1][x] != None:
                if type(building_data[y - 1][x]).__name__ == "Roads":
                    type_[0] = 1
                    privios_road = building_data[y - 1][x]
                    privios_road.type[2] = 1
            if building_data[y + 1][x] != None:
                if type(building_data[y + 1][x]).__name__ == "Roads":
                    type_[2] = 1
                    privios_road = building_data[y + 1][x]
                    privios_road.type[0] = 1
            if building_data[y][x + 1] != None:
                if type(building_data[y][x + 1]).__name__ == "Roads":
                    type_[1] = 1
                    privios_road = building_data[y][x + 1]
                    privios_road.type[3] = 1
    elif x + 1 > len(building_data[0]) - 1:
        if y - 1 < 0:
            if building_data[y + 1][x] != None:
                if type(building_data[y + 1][x]).__name__ == "Roads":
                    type_[2] = 1
                    privios_road = building_data[y + 1][x]
                    privios_road.type[0] = 1
            if building_data[y][x - 1] != None:
                if type(building_data[y][x - 1]).__name__ == "Roads":
                    type_[3] = 1
                    privios_road = building_data[y][x - 1]
                    privios_road.type[1] = 1
        elif y + 1 > len(building_data) - 1:
            if building_data[y - 1][x] != None:
                if type(building_data[y - 1][x]).__name__ == "Roads":
                    type_[0] = 1
                    privios_road = building_data[y - 1][x]
                    privios_road.type[2] = 1
            if building_data[y][x - 1] != None:
                if type(building_data[y][x - 1]).__name__ == "Roads":
                    type_[3] = 1
                    privios_road = building_data[y][x - 1]
                    privios_road.type[1] = 1
        else:
            if building_data[y - 1][x] != None:
                if type(building_data[y - 1][x]).__name__ == "Roads":
                    type_[0] = 1
                    privios_road = building_data[y - 1][x]
                    privios_road.type[2] = 1
            if building_data[y + 1][x] != None:
                if type(building_data[y + 1][x]).__name__ == "Roads":
                    type_[2] = 1
                    privios_road = building_data[y + 1][x]
                    privios_road.type[0] = 1
            if building_data[y][x - 1] != None:
                if type(building_data[y][x - 1]).__name__ == "Roads":
                    type_[3] = 1
                    privios_road = building_data[y][x - 1]
                    privios_road.type[1] = 1
    elif y - 1 < 0:
        if x - 1 < 0:
            if building_data[y + 1][x] != None:
                if type(building_data[y + 1][x]).__name__ == "Roads":
                    type_[2] = 1
                    privios_road = building_data[y + 1][x]
                    privios_road.type[0] = 1
            if building_data[y][x + 1] != None:
                if type(building_data[y][x + 1]).__name__ == "Roads":
                    type_[1] = 1
                    privios_road = building_data[y][x + 1]
                    privios_road.type[3] = 1
        elif x + 1 > len(building_data[0]) - 1:
            if building_data[y + 1][x] != None:
                if type(building_data[y + 1][x]).__name__ == "Roads":
                    type_[2] = 1
                    privios_road = building_data[y + 1][x]
                    privios_road.type[0] = 1
            if building_data[y][x - 1] != None:
                if type(building_data[y][x - 1]).__name__ == "Roads":
                    type_[3] = 1
                    privios_road = building_data[y][x - 1]
                    privios_road.type[1] = 1
        else:
            if building_data[y][x + 1] != None:
                if type(building_data[y][x + 1]).__name__ == "Roads":
                    type_[1] = 1
                    privios_road = building_data[y][x + 1]
                    privios_road.type[3] = 1
            if building_data[y + 1][x] != None:
                if type(building_data[y + 1][x]).__name__ == "Roads":
                    type_[2] = 1
                    privios_road = building_data[y + 1][x]
                    privios_road.type[0] = 1
            if building_data[y][x - 1] != None:
                if type(building_data[y][x - 1]).__name__ == "Roads":
                    type_[3] = 1
                    privios_road = building_data[y][x - 1]
                    privios_road.type[1] = 1
    elif y + 1 > len(building_data) - 1:
        if x - 1 < 0:
            if building_data[y - 1][x] != None:
                if type(building_data[y - 1][x]).__name__ == "Roads":
                    type_[0] = 1
                    privios_road = building_data[y - 1][x]
                    privios_road.type[2] = 1
            if building_data[y][x + 1] != None:
                if type(building_data[y][x + 1]).__name__ == "Roads":
                    type_[1] = 1
                    privios_road = building_data[y][x + 1]
                    privios_road.type[3] = 1
        elif x + 1 > len(building_data[0]) - 1:
            if building_data[y - 1][x] != None:
                if type(building_data[y - 1][x]).__name__ == "Roads":
                    type_[0] = 1
                    privios_road = building_data[y - 1][x]
                    privios_road.type[2] = 1
            if building_data[y][x - 1] != None:
                if type(building_data[y][x - 1]).__name__ == "Roads":
                    type_[3] = 1
                    privios_road = building_data[y][x - 1]
                    privios_road.type[1] = 1
        else:
            if building_data[y - 1][x] != None:
                if type(building_data[y - 1][x]).__name__ == "Roads":
                    type_[0] = 1
                    privios_road = building_data[y - 1][x]
                    privios_road.type[2] = 1
            if building_data[y][x + 1] != None:
                if type(building_data[y][x + 1]).__name__ == "Roads":
                    type_[1] = 1
                    privios_road = building_data[y][x + 1]
                    privios_road.type[3] = 1
            if building_data[y][x - 1] != None:
                if type(building_data[y][x - 1]).__name__ == "Roads":
                    type_[3] = 1
                    privios_road = building_data[y][x - 1]
                    privios_road.type[1] = 1

    # if type_ == [0, 0, 0, 0] or type_ == [0, 1, 0, 0] or type_ == [0, 0, 0, 1] :
    #     type_ = [0, 1, 0, 1]

    # if type_ == [1, 0, 0, 0] or type_ == [0, 0, 1, 0]:
    #     type_ =[1, 0, 1, 0]

    # if building_data[y+1][x] == None and building_data[y-1][x] == None and building_data[x][y+1] == None and building_data[x][y+1] == None:
    #     return [0, 1, 0, 1]

    return type_

def check_resource_road_type(building_data, obj, resources):
    '''
    определяет тип провода в зависимости от того, какие обьекты он соединяет
    '''
    if (building_data[obj.beginning_y // len_height][obj.beginning_x // len_width] in resources) and (building_data[obj.ending_y // len_height][obj.ending_x // len_width] in resources):
        obj.type = 3
    elif building_data[obj.beginning_y // len_height][obj.beginning_x // len_width] in resources:
        obj.type = building_data[obj.beginning_y // len_height][obj.beginning_x // len_width].type
    elif building_data[obj.ending_y // len_height][obj.ending_x // len_width] in resources:
        obj.type = building_data[obj.ending_y // len_height][obj.ending_x // len_width].type
    else:
        obj.type = 3
def water_road_check(building_data, obj, buildings, resources):
    '''
    функция проверяет, соединил ли водный провод замок и озеро (проверяет для дороги)
    аргументы: массив с данными о постройках, водный провод, массив с постройками, массив с ресурсами
    возвращает: True - если водный провод соединил замок и озеро, False - если нет
    '''

    obj_beginning = building_data[obj.beginning_y // len_height][obj.beginning_x // len_width]
    obj_ending = building_data[obj.ending_y // len_height][obj.ending_x // len_width]
    castles = []
    for b in buildings:
        castles.append(b[0])
    if obj_beginning in castles:
        if obj_ending in resources and obj_ending.castles < 3:
            obj_ending.castles += 1
            if obj_ending.type == 1:
                obj_beginning.water = 1
            if obj_begining.type == 2:
                obj_beginning.electricity = 1
            obj_beginning.level = min(3, obj_beginning.m + obj_beginning.park + obj_beginning.electricity + obj_beginning.water)
    
    elif obj_beginning == 1:
        
        if obj_ending in resources and obj_ending.castles < 3:
            x = building_data[obj.beginning_y // len_height][obj.beginning_x // len_width - 1]
            if obj_ending.type == 1:
                x.water = 1
            if obj_ending.type == 2:
                x.electricity = 1
            x.level = min(3, x.water + x.electricity + x.park + x.m)
    elif obj_beginning in resources and obj_beginning.castles < 3:
        obj_beginning.castles += 1
        if obj_ending in castles:
            if obj_beginning.type == 1:
                obj_ending.water =1
            if obj_beginning.type == 2:
                obj_ending.electricity =1
            
            obj_ending.level = min(3,obj_ending.m + obj_ending.park + obj_ending.electricity + obj_ending.water) 
        elif obj_ending == 1:
            x = building_data[obj.ending_y // len_height][obj.ending_x // len_width - 1]
            if obj_beginning.type == 1:
                x.water = 1
            if obj_beginning.type == 2:
                x.electricity = 1


                
def park_check(building_data, obj, buildings, parks):
    '''
    проверяет, находится ли рядом с обьектом парк(если обьект-замок), находится ли рядом с обьектом замок(если обьект - парк)
    '''
    x = obj.x // len_width
    y = obj.y // len_height
    castles = []
    for b in buildings:
        castles.append(b[0])
    

    if obj in castles:
        for i in range(3):
            for j in range(4):
                
                if y -1 + i <= 9 and x - 1 + j <= 15:
                    if building_data[y-1+i][x-1+j] in parks:
                        obj.park = 1
                    
                        obj.level = min(3, 1 + obj.water + obj.electricity+obj.m + obj.park)
                        print(obj.level)
                   
        
    
    if obj in parks:
        
        for i in range(3):
            for j in range(4):
                #print(building_data[y-1+i][x-1+j] in castles)
                if y-2+i <= 9 and x-2+j <= 15:
                    if building_data[y-1+i][x-2+j] in castles:
                        building_data[y-1+i][x-2+j].park = 1
                    
                        x1 = x-2+j
                        y1 = y-1+i
                    
                        building_data[y1][x1].level = min(3, 1 + building_data[y1][x1].water +building_data[y1][x1].electricity+ building_data[y1][x1].m + building_data[y1][x1].park)
        
    
                
def place_for_monstr(building, building_data):
    '''Функция находит свободное место рядом с замком, чтобы впихнуть монстра и возвращает координаты пустой клетки'''
    i=random.randint(building.x//len_width-1, building.x//len_width+1)
    j = random.randint(building.y // len_height - 1,  building.y // len_height + 1)
    if building_data[j][i]==None:
        return (i*len_width, j*len_height)
    return(0, 0)






























