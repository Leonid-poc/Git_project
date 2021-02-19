import os

import pygame as pg
import sys, requests
from PIL import Image
from io import BytesIO

pg.init()
coords = input()
z = 7
spn = input()
clock = pg.time.Clock()


def get_img():
    params = {
        'll': coords,
        'size': '450,450',
        'l': 'sat',
        'z': z
    }
    w = requests.get(f"https://static-maps.yandex.ru/1.x/?", params)
    map_file = "image.png"
    if os.path.exists(map_file):
        os.remove(map_file)
    with open(map_file, "wb") as file:
        file.write(w.content)

    return pg.image.load(map_file)


pg.display.set_caption('Маша_Редиска№1_Льоньа')
img = get_img()
size = img.get_size()
screen = pg.display.set_mode(size)

while True:
    screen.fill('black')
    screen.blit(img, (0, 0))
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        if i.type == pg.KEYDOWN:
            if i.key == pg.K_PAGEDOWN and z > 0:
                z -= 1
            if i.key == pg.K_PAGEUP and z < 20:
                z += 1
    img = get_img()
    clock.tick(1)
    pg.display.flip()
