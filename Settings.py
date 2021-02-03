from map import *
# инициализируем пайгем и звук из пайгейма
import pygame
from pprint import pprint
import random as rg
from Load_image import load_image, load_image_t
pygame.init()
pygame.mixer.init()
# ссоздаю группу спрайтов котораая нам понадобится в будущем
sprites_dop = pygame.sprite.Group()
player_group = pygame.sprite.Group()
map_group = pygame.sprite.Group()
projectales = pygame.sprite.Group()
mod_group = pygame.sprite.Group()
money_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# задаю кол-во кадровв в секунду и размер экрана в данном случае на весь экран
FPS = 60
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
FONT = pygame.font.SysFont('rockwell', 50)

with open("MONEY.txt", encoding="utf-8", mode="r") as mn:
    COUNT_MONEY = int(mn.read())

# музыка заднего фона
background_music = pygame.mixer.music
background_music.load(r'data\Music\background_1.mp3')
background_music.play(-1)

KEYS = pygame.key.get_pressed()


player_shoot_mus = pygame.mixer.Sound(r'data\Music\posoh_shoot_green.mp3')

# придаю ей начальные настройки при запуске игры
with open('volume.txt', encoding='utf-8', mode='r') as text:
    txt = text.read().split()
    background_music.set_volume(int(txt[0]) / 100)
    player_shoot_mus.set_volume(int(txt[1]) / 100)

# загружаю стартовую локацию при запуске игры
location = [r'Jungle\jungle.png', r'Jungle\floor.png', r'Jungle\wall.png', range(3, 6)]

mob_animation = [load_image_t(r'Jungle\jungle_mob.png'),
                 [load_image_t(r'Jungle\jungle_mob1.png'), load_image_t(r'Jungle\jungle_mob2.png'),
                  load_image_t(r'Jungle\jungle_mob3.png')], {'damage': 30, 'health': 180, 'mana': None}]
# загружаю задний фон по дефолту
background = [load_image(location[0]), location[3]]
# задаю карту из списка по дефолту
location_code = JUNGLE
# задаю скин игрока по дефолту
pers = pygame.transform.scale(load_image(r'Jungle\jungle_mainhero.png'), (120, 180))
pers = [pers, pygame.transform.flip(pers, True, False), load_image('Other\\fireball2.png'),
        pygame.transform.flip(load_image('Other\\fireball2.png'), True, False),
        player_shoot_mus, {'damage': 90, 'health': 180, 'mana': 200}]
# список координат всех квадратов земли на холсте
map_coords_spisok = []

