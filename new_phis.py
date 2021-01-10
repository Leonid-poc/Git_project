from build import *
from map import *
import pygame

pygame.init()
clock = pygame.time.Clock()
RES = WIDTH, HEIGHT = 1920, 1080
FPS = 60
projectiles = []
# Список снарядов на поле
# переменные ширины и роста для "Персонажей" (x, y)
screen = pygame.display.set_mode(RES)
background = load_image(location[0])
player = load_image(pers)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__(all_sprites, player_group)
        self.image = player
        self.rect = self.image.get_rect()

    def update(self):
        if not pygame.sprite.spritecollideany(self, map_group):
            self.rect.x -= 1

class Map(pygame.sprite.Sprite):
    def __init__(self, image, loc, x, y):
        super(Map, self).__init__(all_sprites, map_group)
        self.image = pygame.transform.scale(load_image(image), (1920 // len(loc[0]), 1080 // len(loc)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# class Not_Static_Object():
#     def __init__(self, x, y):
#         # Основные переменные
#         self.x = x
#         self.y = y
#         self.FPS = 60
#         self.STEP = 50
#         self.JUMP = 120
#         self.FOOT, self.ROS = 20, 40
#
#     # Функция, которая берёт координаты объекта
#     def get_coords(self, obj):
#         return (obj.x, obj.y)
#
#     # Функция отрисовки объектов
#     def render(self, obj):
#         x, y = self.get_coords(obj)
#         pygame.draw.rect(screen, (0, 0, 255), (x, y, self.FOOT, self.ROS))
#
#     def check_position(self, obj, ):
#         # Функция для проверки выхода за пределы мира и передвижения
#         x, y = self.get_coords(obj)
#
#         if x > WIDTH:
#             obj.x = WIDTH - 20
#         if x < 0:
#             obj.x = 0
#         if y > HEIGHT:
#             obj.y = HEIGHT
#         if y < 0:
#             obj.y = 0
#
#     def phis(self, obj):
#         # Функция для физики, пока только более-менее плавное падение
#         if obj.y + self.ROS < HEIGHT - 20:
#             obj.y += 10
#
#     def move_coord(self, obj, coords):
#         # Функция для изменения координат х и у
#         obj.x, obj.y = coords
#
#     def bull_shot(self, obj):
#         # Функция для выстрела из огнетрела
#         bull = Bullet(self.get_coords(obj)[0], self.get_coords(obj)[1])
#         projectiles.append(bull)
#
#     def move(self, obj, symbol):
#         # функция для передвежения возможно, немного сложно, может и переделаю, но ты разберешься)
#         x, y = self.get_coords(obj)
#         if symbol == "+":
#             if x + self.STEP <= WIDTH:
#                 return (x + self.STEP, y)
#             else:
#                 return (WIDTH - self.FOOT, y)
#         if symbol == "J":
#             if y - self.JUMP >= 0:
#                 return (x, y - self.JUMP)
#             else:
#                 return (x, 0)
#         if symbol == "-":
#             if x - self.STEP >= 0:
#                 return (x - self.STEP, y)
#             else:
#                 return (0, y)
#
#
# class Projectile(Not_Static_Object):
#     def __init__(self, x, y):
#         super(Projectile, self).__init__(x, y)
#         self.x, self.y = x, y
#         self.FOOT, self.ROS = 20, 10
#         # Длина и ширина пули
#
#
# class Bullet(Projectile):
#     def __init__(self, x, y):
#         super(Bullet, self).__init__(x, y)
#
#     def fly(self):
#         if self.x <= WIDTH and self.x >= 0:
#             self.x += 30
#             self.render(self)


Shop()
Settings()
Player()

for i in enumerate(location_code):
    for j in enumerate(i[1]):
        if j[1] == 'q':
            Map(location[1], location_code, 1920 // len(location_code[0]) * j[0], 1080 // len(location_code) * i[0])
        if j[1] == 'w':
            Map(location[2], location_code, 1920 // len(location_code[0]) * j[0], 1080 // len(location_code) * i[0])


while True:
    # Основной цикл, куда уж без него, если ты читал комментарии до этого, ты должен всё понять
    # Есть баг с нажатием пробела (110, 112 строчки), помоги исправить, плез, перс улетает в потолок
    KEYS = pygame.key.get_pressed()
    screen.blit(background, (0, 0))
    for i in pygame.event.get():
        if i.type == pygame.MOUSEBUTTONDOWN:
            sprites_dop.update(i.pos)

    if KEYS[pygame.K_F10]:
        sys.exit()

    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(100)
