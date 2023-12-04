WIDTH = 1200
HEIGHT = 750
len_width = int(WIDTH/(12*4))
len_height = int(HEIGHT/(7.5*4))

HOUSE_LEN = len_width*6
HOUSE_HIGHT = len_height*3
WATER_LEN = len_width*4
WATER_HIGHT = len_height*3
ELECTRICITY_LEN = len_width*3
ELECTRICITY_HIGHT = len_height*3
def add_data(what_you_build, building_data, obj):
    '''
    функция записывает в массив данные об узлах сетки, занятой постройкой
    аргументы: тип постройки(house, water, electricity), массив для записи данных, объект, информация о котором записывается в массив
    возвращает: массив с данными о занятых узлах сетки
    0 - узел свободен, 1 - узел занят
    '''
    if what_you_build == 'house':
        for i in range(HOUSE_HIGHT//len_height+1):
            for j in range(HOUSE_LEN//len_width+1):
                building_data[obj.y//len_height + i][obj.x//len_width + j] = 1
    if what_you_build == 'electricity':
        for i in range(ELECTRICITY_HIGHT//len_height+1):
            for j in range(ELECTRICITY_LEN//len_width + 1):
                building_data[obj.y//len_height + i][obj.x//len_width + j] = 1
    if what_you_build == 'water':
        for i in range(WATER_HIGHT//len_height+1):
            for j in range(WATER_LEN//len_width + 1):
                building_data[obj.y//len_height + i][obj.x//len_width + j] = 1
    
    return building_data
def check_the_place(what_you_build, building_data, x, y):
    '''
    функция проверяет возможность постройки объекта в выбранном месте (свободны ли узлы, не вылезает ли за размеры игрового поля
    аргументы: тип постройки(house, water, electricity), массив для записи данных, x, y - координаты проверяемого узла
    возвращает: True - если постройка на этом месте возможна, False - если невозможно построить объект
    '''
    flag = True
    if what_you_build == 'house':
        if y//len_height + HOUSE_HIGHT//len_height + 1 > HEIGHT//len_height or x//len_width + HOUSE_LEN//len_width + 1> WIDTH//len_width:
            flag = False
        else:
            for i in range(3):
                for j in range(4):
                    if building_data[y//len_height + i][x//len_width + j] == 1:
                        flag = False
    elif what_you_build == 'electricity':
        if y//len_height + ELECTRICITY_HIGHT//len_height+1 > HEIGHT//len_height or x//len_width + ELECTRICITY_LEN//len_width + 1> WIDTH//len_width:
            flag = False
        else:
            for i in range(ELECTRICITY_HIGHT//len_height+1):
                for j in range(ELECTRICITY_LEN//len_width + 1):
                    if building_data[y//len_height + i][x//len_width + j] == 1:
                        flag = False
    elif what_you_build == 'water':
        if y//len_height + WATER_HIGHT//len_height+1 > HEIGHT//len_height or x//len_width + WATER_LEN//len_width + 1> WIDTH//len_width:
            flag = False
        else:
            for i in range(WATER_HIGHT//len_height+1):
                for j in range(WATER_LEN//len_width + 1):
                    if building_data[y//len_height + i][x//len_width + j] == 1:
                        flag = False
    return flag
                   
    
                    
    
