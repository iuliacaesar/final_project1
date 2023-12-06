WIDTH = 1200
HEIGHT = 750
len_width = int(WIDTH/(16))
len_height = int(HEIGHT/(10))

HOUSE_LEN = len_width*2
HOUSE_HIGHT = len_height*1
WATER_LEN = len_width*1
WATER_HIGHT = len_height*1
ELECTRICITY_LEN = len_width*1
ELECTRICITY_HIGHT = len_height*1
PARK_LEN = len_width*1
PARK_HIGHT = len_height*1
def add_data(what_you_build, building_data, obj):
    '''
    функция записывает в массив данные об ячейках сетки, занятой постройкой
    аргументы: тип постройки(house, water, electricity), массив для записи данных, объект, информация о котором записывается в массив
    возвращает: массив с данными о занятых ячейках сетки
    None - ячейка свободна, объект класса постройки - занят постройкой, для класса Buildings, занимающего 2 ячейки, в левой ячейке записан обьект, в правой - 1
    '''
    if what_you_build == 'house':
        building_data[obj.y//len_height][obj.x//len_width] = obj
        building_data[obj.y//len_height][obj.x//len_width + 1] = 1
        
    if what_you_build == 'electricity':
        building_data[obj.y//len_height][obj.x//len_width] = obj
        
    if what_you_build == 'water':
        building_data[obj.y//len_height][obj.x//len_width] = obj

    if what_you_build == 'park':
        building_data[obj.y//len_height][obj.x//len_width] = obj
    return building_data
def check_the_place(what_you_build, building_data, x, y):
    '''
    функция проверяет возможность постройки объекта в выбранном месте (свободны ли ячейки, не вылезает ли за размеры игрового поля
    аргументы: тип постройки(house, water, electricity), массив для записи данных, x, y - координаты постройки
    возвращает: True - если постройка на этом месте возможна, False - если невозможно построить объект
    '''
    flag = True
    if what_you_build == 'house':
        if y//len_height + HOUSE_HIGHT//len_height > HEIGHT//len_height or x//len_width + HOUSE_LEN//len_width > WIDTH//len_width:
            flag = False
        else:
            if building_data[y//len_height][x//len_width] != None or building_data[y//len_height][x//len_width+1] != None:
                flag = False

                
    elif what_you_build == 'electricity':
        if y//len_height + ELECTRICITY_HIGHT//len_height > HEIGHT//len_height or x//len_width + ELECTRICITY_LEN//len_width > WIDTH//len_width:
            flag = False
        else:
            if building_data[y//len_height][x//len_width] != None:
                flag = False

                
    elif what_you_build == 'water':
        if y//len_height + WATER_HIGHT//len_height > HEIGHT//len_height or x//len_width + WATER_LEN//len_width > WIDTH//len_width:
            flag = False
        else:
            if building_data[y//len_height][x//len_width] != None:
                flag = False

                
    elif what_you_build == 'park':
        if y//len_height + PARK_HIGHT//len_height > HEIGHT//len_height or x//len_width + PARK_LEN//len_width > WIDTH//len_width:
            flag = False
        else:
            if building_data[y//len_height][x//len_width] != None:
                flag = False
    return flag
                   
    
                    
    
