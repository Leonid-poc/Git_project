from map import *
# инициализируем пайгем и звук из пайгейма
import pygame
import random as rg
from Load_image import load_image
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
FONT = pygame.font.Font(None, 50)
COUNT_MONEY = 0

# музыка заднего фона
background_music = pygame.mixer.music
background_music.load(r'data\Music\background_1.mp3')
background_music.play(-1)

player_shoot_mus = pygame.mixer.music
player_shoot_mus.load(r'data\Music\posoh_shoot_green.mp3')

# придаю ей начальные настройки при запуске игры
with open('volume.txt', encoding='utf-8', mode='r') as text:
    txt = text.read().split()
    background_music.set_volume(int(txt[0]) / 100)
    player_shoot_mus.set_volume(int(txt[1]) / 100)

# загружаю стартовую локацию при запуске игры
location = [r'Jungle\jungle.png', r'Jungle\floor.png', r'Jungle\wall.png']
# загружаю задний фон по дефолту
background = load_image(location[0])
# задаю карту из списка по дефолту
location_code = JUNGLE
# задаю скин игрока по дефолту
pers = pygame.transform.scale(load_image(r'Jungle\jungle_mainhero.png'), (120, 180))
pers = [pers, pygame.transform.flip(pers, True, False), load_image('Other\\fireball2.png'),
        pygame.transform.flip(load_image('Other\\fireball2.png'), True, False),
        player_shoot_mus]
# список координат всех квадратов земли на холсте
map_coords_spisok = []

