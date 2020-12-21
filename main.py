import pygame
from setting import *
from player import *
import os, sys
import math
from map import world_map
from ray_casting import ray_casting

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

pygame.init()
all_sprites = pygame.sprite.Group()
sc = pygame.display.set_mode((WIDTH, HEIGHT))

class Pol(pygame.sprite.Sprite):
    image_pol = load_image('pol_2.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = self.image_pol
        self.rect = self.image.get_rect()
        self.rect.y = HEIGHT // 2
        self.perem = 10

    def update(self):
        pass
        # pygame.time.delay(200)
        # self.perem = -self.perem
        # self.rect.y -= self.perem

sprite = Pol()
sprite.image = pygame.transform.scale(load_image('pol_2.png'), (WIDTH, HEIGHT // 2))
sprite.rect = sprite.image.get_rect()
sprite.rect.y = HEIGHT // 2

clock = pygame.time.Clock()
player = Player(sprite)
s = 0
all_sprites.add(sprite)


while True:
    KEYS = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    all_sprites.update()
    sc.fill(WHITE)

    pygame.draw.rect(sc, BLACK, (0, 0, WIDTH, HALF_HEIGHT))
    all_sprites.draw(sc)

    ray_casting(sc, player.pos, player.angle)

    # pygame.draw.circle(sc, GREEN, (int(player.x), int(player.y)), 12)
    # pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
    #                                          player.y + WIDTH * math. sin(player.angle)), 2)
    # for x,y in world_map:
    #     pygame.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE), 2)

    pygame.display.flip()
    clock.tick(FPS)
    # print(clock.get_fps())