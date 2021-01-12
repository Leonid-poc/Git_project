from build import *
from map import *
import pygame

pygame.init()
clock = pygame.time.Clock()


player = load_image(pers)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__(all_sprites, player_group)
        self.image = player
        self.rect = self.image.get_rect()

    def update(self):
        if not pygame.sprite.spritecollideany(self, map_group):
            self.rect.y += 1
        if KEYS[pygame.K_d]:
            self.rect.x += 5
        if KEYS[pygame.K_a]:
            self.rect.x -= 5


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
vremenaya = Shop()
Settings()
Player()
draw_map()

while True:
    # Основной цикл, куда уж без него, если ты читал комментарии до этого, ты должен всё понять
    # Есть баг с нажатием пробела (110, 112 строчки), помоги исправить, плез, перс улетает в потолок
    KEYS = pygame.key.get_pressed()
    screen.blit(vremenaya.return_background(), (0, 0))
    for i in pygame.event.get():
        if i.type == pygame.MOUSEBUTTONDOWN:
            sprites_dop.update(i.pos)
    player_group.update()
    if KEYS[pygame.K_F10]:
        sys.exit()

    all_sprites.draw(screen)
    map_group.draw(screen)

    pygame.display.flip()
    clock.tick(100)
