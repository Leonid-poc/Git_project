import pygame
from setting import *
from math import cos, sin, ceil
from map import *

pygame.init()
screen = pygame.display.set_mode((WIDTH_SCREEN, HIGHT_SCREEN))
run = True
clock = pygame.time.Clock()
angle = 0
player = pygame.draw.circle(screen, 'green', (250, 250), 20)

while run:
    screen.fill('black')
    KEYS = pygame.key.get_pressed()

    for x1, y1 in world_map:
        pygame.draw.rect(screen, 'gray', (x1, y1, TILE_X, TILE_Y), 3)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    cos_a = cos(angle)
    sin_a = sin(angle)
    if KEYS[pygame.K_w]:
        player.x += PLAYER_STEP * cos_a
        player.y += PLAYER_STEP * sin_a
    if KEYS[pygame.K_a]:
        player.y += -PLAYER_STEP * cos_a
        player.x += PLAYER_STEP * sin_a
    if KEYS[pygame.K_d]:
        player.y += PLAYER_STEP * cos_a
        player.x += -PLAYER_STEP * sin_a
    if KEYS[pygame.K_s]:
        player.x += -PLAYER_STEP * cos_a
        player.y += -PLAYER_STEP * sin_a
    if KEYS[pygame.K_LEFT]:
        angle -= ANGLE_SPEED
    if KEYS[pygame.K_RIGHT]:
        angle += ANGLE_SPEED
    if KEYS[pygame.K_SPACE]:
        print(angle, cos_a, sin_a)
    pygame.draw.circle(screen, 'tomato', (player.x, player.y), 20)
    for i in range(-ANGLE, ANGLE + 1):
        i /= 100
        pygame.draw.line(screen, 'gold', (player.x, player.y),
                         (player.x + OBZOR * cos(angle + i), player.y + OBZOR * sin(angle + i)), 1)

    pygame.display.flip()
    clock.tick(FPS)