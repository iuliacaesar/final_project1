import pygame
pygame.init()

def draw_setka(screen, width, height):
    for i in range(0, width, int(width/13)):
        for j in range (0, height, int(height/7)):
            pygame.draw.line(screen, (0, 0, 0), [i, 0], [i, height], 4)
            pygame.draw.line(screen, (0, 0, 0), [0, j], [width, j], 4)

def draw_fon(screen, x, y):
    image = pygame.image.load('поле.jpg').convert_alpha()
    scaled_image = pygame.transform.scale(image, (1300, 700))
    screen.blit(scaled_image, (x, y))

def draw_building(screen, x, y):
    image = pygame.image.load('дом.png').convert_alpha()
    scaled_image = pygame.transform.scale(image, (100, 100))
    screen.blit(scaled_image, (x, y))


def draw_road(x, y):
    k=0


if __name__ == "__main__":
    print("This module is not for direct call!")