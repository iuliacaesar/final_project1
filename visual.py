import pygame

# В визуализации те же параметры экрана, что и в main
# И len_width и len_height - параметры разбиения экрана на сетку, растояние между соседними линиями

WIDTH = 800
HEIGHT = 600
len_width = int(WIDTH/(8*5))
len_height = int(HEIGHT/(6*5))

pygame.init()

def get_xy(x, y):
    new_x = int(x/len_width)*len_width
    new_y = int(y/len_height)*len_height
    return [new_x, new_y]

def draw_setka(screen):
    for i in range(0, WIDTH, len_width):
        for j in range (0, HEIGHT, len_height):
            pygame.draw.line(screen, (0, 0, 0), [i, 0], [i, HEIGHT], 1)
            pygame.draw.line(screen, (0, 0, 0), [0, j], [WIDTH, j], 1)

# В temp_surface можно запихнуть несколько объектов и они будут в итоге как одна картинка, например дом с надписью его уровня

def draw_fon(screen, x, y):
    image = pygame.image.load('поле.jpg').convert_alpha()
    temp_surface = pygame.Surface([image.get_width(), image.get_height()], pygame.SRCALPHA)
    temp_surface.blit(image, [0, 0])
    scaled_image = pygame.transform.scale(temp_surface, (WIDTH, HEIGHT))
    screen.blit(scaled_image, (x, y))

# И картинки поменьше!!! FPS из-за них падает до 7 из 60 нужных
# И стадантизируй для всех домов их разрешения, чтобы для всех одинаковые

def draw_building(screen, x, y):
    image = pygame.image.load('дом.png').convert_alpha()
    temp_surface = pygame.Surface([image.get_width(), image.get_height()], pygame.SRCALPHA)
    temp_surface.blit(image, [0, 0])
    scaled_image = pygame.transform.scale(temp_surface, (100, 100))
    screen.blit(scaled_image, (x, y))

def draw_road(x, y):
    k=0

def process_building(screen, x, y, len_x, len_y):
    x, y = get_xy(x, y)
    temp_surface = pygame.Surface([len_x, len_y], pygame.SRCALPHA)
    pygame.draw.polygon(temp_surface, (255, 0, 0, 100), [[0, 0], [len_x, 0], [len_x, len_y], [0, len_y]])   
    screen.blit(temp_surface, [x, y])                     

if __name__ == "__main__":
    print("This module is not for direct call!")