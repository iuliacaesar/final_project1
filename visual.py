import pygame
from button import *

# В визуализации те же параметры экрана, что и в main
# И len_width и len_height - параметры разбиения экрана на сетку, растояние между соседними линиями

WIDTH = 1200
HEIGHT = 750
len_width = int(WIDTH / (16))
len_height = int(HEIGHT / (10))

pygame.init()


# Фон загружается лишь один раз в глабальную переменную, а потом лишь рисуется
def load_fon():
    global FON, FON1, road0, road1, road2, road3, road4, road5, road6, road7, road8, road9, road10, castle1, castle2, castle3, \
        mile1, mile2, lake, star1, star2, star3, clouds, fonstarta, button_castle1, button_castle2, button_castle3, \
        button_lake, button_mile, button_road, button_park, button_water, but_h1, but_h2, but_h3, but_h4, but_h5, but_h6, but_h7,\
        but_h8, but_h9, but_h10, but_m1, but_m2, but_m3, but_m4, but_m5, but_m6, but_m7, but_m8, but_m9, but_m10, but_m11, \
        but_m12, but_m13, but_m14,  but_m15, but_m16, but_m17, but_m18, but_m19, but_m20, but_m21, park, moster_smile, \
        button_destroy, turtle, final1, final2, final3, final4, final5, final6, final7, final8, final9, final10, final11, \
        final12, final13, final14, final15, final16, final17, final18, final19, final20, FINAL

    FON = pygame.image.load('.\images\image.psd.png').convert_alpha()
    FON1 = pygame.image.load('.\images\image1.psd.png').convert_alpha()

    road0 = pygame.image.load('.\images\дорога0.png').convert_alpha()
    road1 = pygame.image.load('.\images\дорога1.png').convert_alpha()
    road2 = pygame.image.load('.\images\дорога2.png').convert_alpha()
    road3 = pygame.image.load('.\images\дорога3.png').convert_alpha()
    road4 = pygame.image.load('.\images\дорога4.png').convert_alpha()
    road5 = pygame.image.load('.\images\дорога5.png').convert_alpha()
    road6 = pygame.image.load('.\images\дорога6.png').convert_alpha()
    road7 = pygame.image.load('.\images\дорога7.png').convert_alpha()
    road8 = pygame.image.load('.\images\дорога8.png').convert_alpha()
    road9 = pygame.image.load('.\images\дорога9.png').convert_alpha()
    road10 = pygame.image.load('.\images\дорога10.png').convert_alpha()

    castle1 = pygame.image.load('.\images\замок1.png').convert_alpha()
    castle2 = pygame.image.load('.\images\замок2.png').convert_alpha()
    castle3 = pygame.image.load('.\images\замок3.png').convert_alpha()

    mile1 = pygame.image.load('.\images\ресурс2.png').convert_alpha()
    mile2 = pygame.image.load('.\images\мельница1.png').convert_alpha()

    lake = pygame.image.load('.\images\ресурс1.png').convert_alpha()

    star1 = pygame.image.load('.\images\звезда1.png').convert_alpha()
    star2 = pygame.image.load('.\images\звезда2.png').convert_alpha()
    star3 = pygame.image.load('.\images\звезда3.png').convert_alpha()
    moster_smile = pygame.image.load('.\images\monstr_smile.png').convert_alpha()

    clouds = pygame.image.load(".\images\\CloudsBG.jpg").convert_alpha()
    fonstarta = pygame.image.load(".\images\\фонстарта.jpg").convert_alpha()

    button_castle1 = pygame.image.load(".\images\\button_castle1.png").convert_alpha()
    button_castle2 = pygame.image.load(".\images\\button_castle2.png").convert_alpha()
    button_castle3 = pygame.image.load(".\images\\button_castle3.png").convert_alpha()
    button_lake = pygame.image.load(".\images\\button_lake.png").convert_alpha()
    button_mile = pygame.image.load(".\images\\button_mile.png").convert_alpha()
    button_road = pygame.image.load(".\images\\button_road.png").convert_alpha()
    button_park = pygame.image.load(".\images\\button_park.png").convert_alpha()
    button_water = pygame.image.load(".\images\\button_water.png").convert_alpha()
    button_destroy = pygame.image.load(".\images\\destroy.png").convert_alpha()

    but_h1=pygame.image.load(".\images\\11zon_1.png").convert_alpha()
    but_h2 = pygame.image.load(".\images\\11zon_2.png").convert_alpha()
    but_h3 = pygame.image.load(".\images\\11zon_3.png").convert_alpha()
    but_h4 = pygame.image.load(".\images\\11zon_4.png").convert_alpha()
    but_h5 = pygame.image.load(".\images\\11zon_5.png").convert_alpha()
    but_h6 = pygame.image.load(".\images\\11zon_6.png").convert_alpha()
    but_h7 = pygame.image.load(".\images\\11zon_7.png").convert_alpha()
    but_h8 = pygame.image.load(".\images\\11zon_8.png").convert_alpha()
    but_h9 = pygame.image.load(".\images\\11zon_9.png").convert_alpha()
    but_h10 = pygame.image.load(".\images\\11zon_10.png").convert_alpha()

    but_m1 = pygame.image.load(".\images\\1.png").convert_alpha()
    but_m2 = pygame.image.load(".\images\\2.png").convert_alpha()
    but_m3 = pygame.image.load(".\images\\3.png").convert_alpha()
    but_m4 = pygame.image.load(".\images\\4.png").convert_alpha()
    but_m5 = pygame.image.load(".\images\\5.png").convert_alpha()
    but_m6 = pygame.image.load(".\images\\6.png").convert_alpha()
    but_m7 = pygame.image.load(".\images\\7.png").convert_alpha()
    but_m8 = pygame.image.load(".\images\\8.png").convert_alpha()
    but_m9 = pygame.image.load(".\images\\9.png").convert_alpha()
    but_m10 = pygame.image.load(".\images\\10.png").convert_alpha()
    but_m11= pygame.image.load(".\images\\11.png").convert_alpha()
    but_m12= pygame.image.load(".\images\\12.png").convert_alpha()
    but_m13= pygame.image.load(".\images\\13.png").convert_alpha()
    but_m14= pygame.image.load(".\images\\14.png").convert_alpha()
    but_m15= pygame.image.load(".\images\\15.png").convert_alpha()
    but_m16= pygame.image.load(".\images\\16.png").convert_alpha()
    but_m17= pygame.image.load(".\images\\17.png").convert_alpha()
    but_m18= pygame.image.load(".\images\\18.png").convert_alpha()
    but_m19= pygame.image.load(".\images\\19.png").convert_alpha()
    but_m20= pygame.image.load(".\images\\20.png").convert_alpha()
    but_m21= pygame.image.load(".\images\\21.png").convert_alpha()

    park = pygame.image.load(".\images\\парк.png").convert_alpha()
    # turtle = pygame.image.load(".\images\\черепах.png").convert_alpha()

    final1 = pygame.image.load(".\images\\1=.png").convert_alpha()
    final2 = pygame.image.load(".\images\\2=.png").convert_alpha()
    final3 = pygame.image.load(".\images\\3=.png").convert_alpha()
    final4 = pygame.image.load(".\images\\4=.png").convert_alpha()
    final5 = pygame.image.load(".\images\\5=.png").convert_alpha()
    final6 = pygame.image.load(".\images\\6=.png").convert_alpha()
    final7 = pygame.image.load(".\images\\7=.png").convert_alpha()
    final8 = pygame.image.load(".\images\\8=.png").convert_alpha()
    final9 = pygame.image.load(".\images\\9=.png").convert_alpha()
    final10 = pygame.image.load(".\images\\10=.png").convert_alpha()
    final11 = pygame.image.load(".\images\\11=.png").convert_alpha()
    final12 = pygame.image.load(".\images\\12=.png").convert_alpha()
    final13 = pygame.image.load(".\images\\13=.png").convert_alpha()
    final14 = pygame.image.load(".\images\\14=.png").convert_alpha()
    final15 = pygame.image.load(".\images\\15=.png").convert_alpha()
    final16 = pygame.image.load(".\images\\16=.png").convert_alpha()
    final17 = pygame.image.load(".\images\\17=.png").convert_alpha()
    final18 = pygame.image.load(".\images\\18=.png").convert_alpha()
    final19 = pygame.image.load(".\images\\19=.png").convert_alpha()
    final20 = pygame.image.load(".\images\\20=.png").convert_alpha()
    FINAL=[final1, final2, final3, final4, final5, final6, final7, final8, final9, final10, final11,
        final12, final13, final14, final15, final16, final17, final18, final19, final20]

def draw_monstr(but, window):
    if int(but.time) == 1:
        image = but_m1
    elif int(but.time) == 2:
        image = but_m2
    elif int(but.time) == 3:
        image = but_m3
    elif int(but.time) == 4:
        image = but_m4
    elif int(but.time) == 5:
        image = but_m5
    elif int(but.time) == 6:
        image = but_m6
    elif int(but.time) == 7:
        image = but_m7
    elif int(but.time) == 8:
        image = but_m8
    elif int(but.time) ==9:
        image = but_m9
    elif int(but.time) ==10:
        image = but_m10
    elif int(but.time) ==11:
        image = but_m11
    elif int(but.time) ==12:
        image = but_m12
    elif int(but.time) == 13:
        image = but_m13
    elif int(but.time) ==14:
        image = but_m14
    elif int(but.time) ==15:
        image = but_m15
    elif int(but.time) ==16:
        image = but_m16
    elif int(but.time) ==17:
        image = but_m17
    elif int(but.time) ==18:
        image = but_m18
    elif int(but.time) ==19:
        image = but_m19
    elif int(but.time) ==20:
        image = but_m20
    elif int(but.time) ==21:
        image = but_m21


        but.time=1
    but.time+=0.25
    temp_surface = pygame.Surface([100, 100], pygame.SRCALPHA)
    temp_surface.blit(image, [0, 0])
    scaled_image = pygame.transform.scale(image, (but.width, but.height))
    window.blit(scaled_image, (but.x, but.y))
def draw_block(but, window):
    if int(but.time) == 1:
        image = but_h1
    elif int(but.time) == 2:
        image = but_h2
    elif int(but.time) == 3:
        image = but_h3
    elif int(but.time) == 4:
        image = but_h4
    elif int(but.time) == 5:
        image = but_h5
    elif int(but.time) == 6:
        image = but_h6
    elif int(but.time) == 7:
        image = but_h7
    elif int(but.time) == 8:
        image = but_h8
    elif int(but.time) == 9:
        image = but_h9
    elif int(but.time) == 10:
        image = but_h10
        but.time=1
    but.time+=0.33
    temp_surface = pygame.Surface([150, 150], pygame.SRCALPHA)
    temp_surface.blit(image, [0, 0])
    scaled_image = pygame.transform.scale(image, (but.width/2, but.height/2))
    window.blit(scaled_image, (but.x, but.y))

def draw_monets(but, window):
    image=but_h1
    temp_surface = pygame.Surface([150, 150], pygame.SRCALPHA)
    temp_surface.blit(image, [0, 0])
    scaled_image = pygame.transform.scale(image, (50, 50))
    window.blit(scaled_image, (but.x+but.width-35, but.y-15))
    text_money=""
    if but.text=="castle 1" or but.text=="castle 2" or but.text=="castle 3":
        text_money=str(100)
    elif but.text=="lake":
        text_money = str(50)
    elif but.text=="mile":
        text_money = str(50)
    elif but.text=="road":
        text_money = str(0)
    elif but.text=="park":
        text_money = str(70)
    elif but.text=="connect_objects":
        text_money = str(10)
    elif but.text == "demolition":
        text_money = "+40"
    font = pygame.font.SysFont( "cascadiamonoregular", but.size_text-15, italic=True)
    text = font.render( text_money, True, (49, 19, 9))
    text_rect = text.get_rect(center=(but.x + but.width-10, but.y +10))
    window.blit(text, text_rect)
def draw_button(but, window):
    #Лера, пожалуйста добавь кнопки для underground
    if but.text == "castle 1":
        image = button_castle1
    elif but.text == "castle 2":
        image = button_castle2
    elif but.text == "castle 3":
        image = button_castle3
    elif but.text == "lake":
        image = button_lake
    elif but.text == "mile":
        image = button_mile
    elif but.text == "road":
        image = button_road
    elif but.text == "park":
        image = button_park
    elif but.text == "demolition":
        image = button_destroy
    else:
        image = button_water

    temp_surface = pygame.Surface([image.get_width(), image.get_height()], pygame.SRCALPHA)
    temp_surface.blit(image, [0, 0])
    scaled_image = pygame.transform.scale(image, (but.width - 10, but.height - 10))
    window.blit(scaled_image, (but.x + 5, but.y + 5))

def draw_fon1(screen):
    image = FON1
    scaled_image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    screen.blit(scaled_image, (0, 0))
def draw_fon_start(screen, time):
    image = fonstarta
    scaled_image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    screen.blit(scaled_image, (0, 0))
    draw_rules(screen, time)


def draw_rules(screen, time):

    if time <= 50:
        beginningtext = 'Правила игры:'
    elif time > 50 and time <= 400:
        beginningtext = 'Правила игры: Только доблестный рыцарь,  победивший полчища монстров и построивший 7 замков, сможет проийти игру ... '
    elif time > 400 and time < 800:
        beginningtext = "Пропишу"
    else:
        beginningtext = "Возможно"
    temp_surface = pygame.Surface([300, 300], pygame.SRCALPHA)
    font = pygame.font.SysFont(None, 30)
    blit_text(temp_surface, beginningtext, (0, 0), font)
    pygame.draw.polygon(temp_surface, (100, 0, 150, 100), [[0, 0], [300, 0], [300, 300], [0, 300]])
    screen.blit(temp_surface, [100, 100])


def draw_fon_menu(screen):
    image = clouds
    scaled_image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    screen.blit(scaled_image, (0, 0))


def get_xy(x, y):
    new_x = int(x / len_width) * len_width
    new_y = int(y / len_height) * len_height
    return [new_x, new_y]


def draw_setka(screen):
    for i in range(0, WIDTH, len_width):
        for j in range(0, HEIGHT, len_height):
            pygame.draw.line(screen, (0, 50, 0), [i, 0], [i, HEIGHT], 1)
            pygame.draw.line(screen, (0, 50, 0), [0, j], [WIDTH, j], 1)


# В temp_surface можно запихнуть несколько объектов и они будут в итоге как одна картинка, например дом с надписью его уровня

def draw_fon(screen, x, y):
    global FON
    # image = pygame.image.load('.\images\image.psd.png').convert_alpha()
    temp_surface = pygame.Surface([FON.get_width(), FON.get_height()], pygame.SRCALPHA)
    temp_surface.blit(FON, [0, 0])
    scaled_image = pygame.transform.scale(temp_surface, (WIDTH, HEIGHT))
    screen.blit(scaled_image, (x, y))


# И картинки поменьше!!! FPS из-за них падает до 7 из 60 нужных
# И стадантизируй для всех домов их разрешения, чтобы для всех одинаковые

def draw_building(screen, b):
    x = b.x
    y = b.y
    if b.get_type() == 1:
        image = castle1
    elif b.get_type() == 2:
        image = castle2
    elif b.get_type() == 3:
        image = castle3
    size_of_image = 150
    position_y = -60

    temp_surface = pygame.Surface([image.get_width(), image.get_height()], pygame.SRCALPHA)
    temp_surface.blit(image, [0, 0])
    scaled_image = pygame.transform.scale(image, (size_of_image, size_of_image))
    screen.blit(scaled_image, (x, y + position_y))

    if b.level == 1:
        image1 = star1
    elif b.level ==0:
        image1=moster_smile
    elif b.level == 2:
        image1 = star2
    elif b.level == 3:
        image1 = star3
    temp_surface.blit(image1, [0, 0])
    scaled_image1 = pygame.transform.scale(image1, (150, 150))
    screen.blit(scaled_image1, (x, y + position_y / 2))

def draw_road(screen, b):
    x = b.x
    y = b.y

    if b.type == [1, 0, 1, 0] or b.type == [1, 0, 0, 0] or b.type == [0, 0, 1, 0]:
        image = road0
    elif b.type == [0, 1, 0, 1] or b.type == [0, 0, 0, 0] or b.type == [0, 1, 0, 0] or b.type == [0, 0, 0, 1]:
        image = road1
    elif b.type == [1, 1, 1, 0]:
        image = road2
    elif b.type == [0, 1, 1, 1]:
        image = road3
    elif b.type == [1, 0, 1, 1]:
        image = road4
    elif b.type == [1, 1, 0, 1]:
        image = road5
    elif b.type == [1, 1, 1, 1]:
        image = road6
    elif b.type == [1, 1, 0, 0]:
        image = road7
    elif b.type == [0, 1, 1, 0]:
        image = road8
    elif b.type == [0, 0, 1, 1]:
        image = road9
    elif b.type == [1, 0, 0, 1]:
        image = road10
    size_of_image = 75
    position_y = 0

    temp_surface = pygame.Surface([image.get_width(), image.get_height()], pygame.SRCALPHA)
    temp_surface.blit(image, [0, 0])
    scaled_image = pygame.transform.scale(image, (size_of_image, size_of_image))
    screen.blit(scaled_image, (x, y + position_y))

def draw_resources(screen, b):
    x = b.x
    y = b.y
    if b.get_type() == 1:
        image = lake
    elif b.get_type()== 2:
        image = mile1
    size_of_image = 75
    position_y = -0
    temp_surface = pygame.Surface([image.get_width(), image.get_height()], pygame.SRCALPHA)
    temp_surface.blit(image, [0, 0])
    scaled_image = pygame.transform.scale(image, (size_of_image, size_of_image))
    screen.blit(scaled_image, (x, y + position_y))

    size_of_image = 75
    position_y = -0
    if b.get_type() == 2:
        image = mile2
        scaled_image = pygame.transform.scale(image, (size_of_image, size_of_image))
        image = pygame.transform.rotate(scaled_image, b.angle)
        b.angle += 2
        screen.blit(image, (
            x + (-image.get_width() + size_of_image) / 2, y + position_y + (-image.get_height() + size_of_image) / 2))

def draw_park(screen, p):
    image = park
    size_of_image = 75
    position_y = -0
    temp_surface = pygame.Surface([image.get_width(), image.get_height()], pygame.SRCALPHA)
    temp_surface.blit(image, [0, 0])
    scaled_image = pygame.transform.scale(image, (size_of_image, size_of_image))
    screen.blit(scaled_image, (p.x, p.y + position_y))
def process_building(screen, x, y, len_x, len_y, able):
    if able:
        color = (0, 255, 0, 100)
    else:
        color = (255, 0, 0, 100)
    x, y = get_xy(x, y)
    temp_surface = pygame.Surface([len_x * 2, len_y * 2], pygame.SRCALPHA)
    pygame.draw.polygon(temp_surface, color, [[0, 0], [len_x, 0], [len_x, len_y], [0, len_y]])
    screen.blit(temp_surface, [x, y])


def blit_text(surface, text, pos, font, color='black'):
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
def draw_water_road(screen, b):
    wgh = 2.5
    r = 5
    color = b.color
    pygame.draw.line(screen, color, [int(b.beginning_x + len_width/2), int(b.beginning_y + len_height/2)], [int(b.ending_x+ len_width/2), int(b.ending_y+ len_height/2)], int(wgh))
    pygame.draw.circle(
        screen, color,
        (int(b.beginning_x + len_width/2), int(b.beginning_y + len_height/2)),
        int(r))
    pygame.draw.circle(
        screen, color,
        (int(b.ending_x+ len_width/2), int(b.ending_y+ len_height/2)),
        int(r))

def draw_water_road_process(screen, x_, y_, x, y, type_ =1):
    wgh = 2.5
    r = 5
    if type_ == 1:
        color = (0, 155, 245)
    else:
        color = (212, 152, 0)
    pygame.draw.line(screen, color, [int(x_ + len_width/2), int(y_+ len_height/2)], [int(x), int(y)], int(wgh))
    pygame.draw.circle(
        screen, color,
        [int(x_ + len_width/2), int(y_+ len_height/2)],
        int(r))
    pygame.draw.circle(
        screen, color,
        [int(x), int(y)],
        int(r))

def draw_final_turtles(x, screen):
    text_money = "WIN"
    font = pygame.font.SysFont("cascadiamonoregular", 300)
    text = font.render(text_money, True, (90, 0, 150, 100))
    text_rect = text.get_rect(center=(600, 200))
    screen.blit(text, text_rect)
    image = FINAL[(x*10//58)%20]
    screen.blit(image, (350, 350))


if __name__ == "__main__":
    print("This module is not for direct call!")