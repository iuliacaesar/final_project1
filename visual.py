import pygame

# В визуализации те же параметры экрана, что и в main
# И len_width и len_height - параметры разбиения экрана на сетку, растояние между соседними линиями

WIDTH = 1200
HEIGHT = 750
len_width = int(WIDTH/(16))
len_height = int(HEIGHT/(10))

pygame.init()

# Фон загружается лишь один раз в глабальную переменную, а потом лишь рисуется
def load_fon():
    global FON
    FON = pygame.image.load('.\images\image.psd.png').convert_alpha()

def get_xy(x, y):
    new_x = int(x/len_width)*len_width
    new_y = int(y/len_height)*len_height
    return [new_x, new_y]

def draw_setka(screen):
    for i in range(0, WIDTH, len_width):
        for j in range (0, HEIGHT, len_height):
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
    x=b.x
    y=b.y
    if type(b).__name__=="Buildings":
        name_of_image=".\images\\" + "замок"+"4"+".png"
        size_of_image=150
        position_y=-60
    if type(b).__name__ == "Resources":
        name_of_image = ".\images\\" + "ресурс" + str(b.type) + ".png"
        size_of_image=75
        position_y=-0


    if type(b).__name__ == "Roads":
        name_of_image = ".\images\\" + "дорога" + str(b.type) + ".png"
        size_of_image=75
        position_y=0

    image = pygame.image.load(name_of_image).convert_alpha()
    temp_surface = pygame.Surface([image.get_width(), image.get_height()], pygame.SRCALPHA)
    temp_surface.blit(image, [0, 0])
    scaled_image = pygame.transform.scale(image, (size_of_image, size_of_image))
    screen.blit(scaled_image, (x, y+position_y))

    if type(b).__name__ == "Buildings":
        name_of_zvezda=".\images\\" + "звезда"+str(b.level)+".png"
        image1 = pygame.image.load(name_of_zvezda).convert_alpha()
        temp_surface.blit(image1, [0, 0])
        scaled_image1 = pygame.transform.scale(image1, (150, 150))
        screen.blit(scaled_image1, (x, y + position_y / 2))
    if type(b).__name__ == "Resources":
        name_of_image = ".\images\\" + "ресурс" + str(b.type) + ".png"
        size_of_image=75
        position_y=-0
        if b.type==2:
            image = pygame.image.load(".\images\мельница1.png").convert_alpha()
            scaled_image = pygame.transform.scale(image, (size_of_image, size_of_image))
            image = pygame.transform.rotate(scaled_image, b.angle)
            b.angle+=2
            screen.blit(image, (x+(-image.get_width()+size_of_image)/2, y + position_y+(-image.get_height()+size_of_image)/2))


    temp_surface = pygame.Surface([size_of_image, 75], pygame.SRCALPHA)
    pygame.draw.polygon(temp_surface, (255, 0, 0, 0), [[0, 0], [size_of_image, 0], [size_of_image, size_of_image], [0, size_of_image]])
    screen.blit(temp_surface, [x, y])




def draw_road(x, y):
    k=0

def process_building(screen, x, y, len_x, len_y):
    x, y = get_xy(x, y)
    temp_surface = pygame.Surface([len_x, len_y], pygame.SRCALPHA)
    pygame.draw.polygon(temp_surface, (255, 0, 0, 100), [[0, 0], [len_x, 0], [len_x, len_y], [0, len_y]])
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

if __name__ == "__main__":
    print("This module is not for direct call!")