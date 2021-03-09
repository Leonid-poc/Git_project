import os
import sys
import pygame

import ctypes
user32 = ctypes.windll.user32
size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# функция для адекватной загрузки картинок
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


# фун-ия которая возвращает две картикни флипнутая и нет
def load_image_t(name, colorkey=None):
    return pygame.transform.scale(pygame.transform.flip(load_image(name, colorkey), True, False),
                                  (size[0] // 16, size[1] // 6)), \
           pygame.transform.scale(load_image(name, colorkey), (size[0] // 16, size[1] // 6))
