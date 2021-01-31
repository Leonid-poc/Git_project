from timeit import time

from build import *
from Proj import *

# инициализирую пайтон и добавляю переменные часы для того чтобы выставить значение фпс
pygame.init()
clock = pygame.time.Clock()
KILL_COUNT = 0


class Game_Object(pygame.sprite.Sprite):
    def __init__(self, x, y, pers, group):
        super(Game_Object, self).__init__(all_sprites, group)
        self.image = pers[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.count_jump = 20
        self.jumping = False
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.god_mode = False
        self.time_to_restart_mana = 0
        self.time_to_shoot = 0
        self.count_shoot = 0
        self.shield = 100
        self.right_pers, self.left_pers = True, False

    # проверка не провалился ли слегка игрок под карту
    def proof_font_fall_out_map(self):
        while self.rect.bottom > map_coords_spisok[0] + 1:
            self.rect.y -= 1

    def jump(self, proof):
        if proof:
            if self.count_jump >= -20:
                if self.count_jump < 0:
                    if not pygame.sprite.spritecollide(self, map_group, False, pygame.sprite.collide_mask):
                        self.rect.y += (self.count_jump ** 2) / 10
                    else:
                        self.jumping = False
                        self.count_jump = 20
                        self.proof_font_fall_out_map()
                else:
                    self.rect.y -= (self.count_jump ** 2) / 10
                self.count_jump -= 1
            else:
                if not pygame.sprite.spritecollide(self, map_group, False, pygame.sprite.collide_mask):
                    self.rect.y += (self.count_jump ** 2) / 10
                    self.count_jump -= 1
                else:
                    self.jumping = False
                    self.count_jump = 20
                    self.proof_font_fall_out_map()
        else:
            self.jumping = False


class Mob(Game_Object):
    def __init__(self, x, y, pers):
        super(Mob, self).__init__(x, y, pers, mod_group)
        self.spisok_animation = [pygame.transform.scale(load_image(r'Jungle\jungle_mob.png'), (120, 180)),
                                 pygame.transform.flip(
                                     pygame.transform.scale(load_image(r'Jungle\jungle_mob.png'), (120, 180)), True,
                                     False)]
        self.image = self.spisok_animation[1]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.START_HP = 180
        self.NOW_HP = 180
        self.START_MANA = 200
        self.NOW_MANA = 200
        self.jumping = False
        self.count_jump = 20
        self.vx = 6

    def update(self):
        global COUNT_MONEY, KILL_COUNT
        # Падение
        if not pygame.sprite.spritecollide(self, map_group, False, pygame.sprite.collide_mask) and not self.jumping:
            self.rect.y += 5
            self.proof_font_fall_out_map()
        # if self.rect.x + self.rect.w >= screen.get_width() and self.rect.x >= 100:
        #     self.vx = -self.vx
        #     self.image = self.spisok_animation[abs(self.spisok_animation.index(self.image) - 1)]
        #     self.rect.x += self.vx
        if self.rect.x + self.rect.w >= screen.get_width() and self.rect.x > 100:
            #     self.vx = -self.vx
            self.rect.x -= self.vx
        if self.rect.x <= 100:
            # self.vx = abs(self.vx)
            self.vx = 0

        if pygame.sprite.spritecollide(self, projectales, True):
            self.NOW_HP -= Player1.return_damage()
            if self.NOW_HP <= 0:
                with open('MONEY.txt', mode='w', encoding='utf-8') as txt:
                    COUNT_MONEY = return_money(rg.choice(range(3, 6)))
                    txt.write(str(COUNT_MONEY))
                self.kill()
                mobs.pop()
                KILL_COUNT += 1
                Monetki_from_mob(self.rect.x, self.rect.y, self.rect.w, self.rect.h)

        if not self.jumping and pygame.sprite.spritecollide(self, map_group, False, pygame.sprite.collide_mask):
            self.jumping = rg.choice(range(100))
        self.jump(self.jumping == 10)

        self.rect.x -= self.vx

        if self.NOW_HP > 0:
            Indicator(self.NOW_HP, self.START_HP, (255, 0, 0), self.rect.x, self.rect.y, 100, 10).obn()


# класс игрока который отвечает за любые события и изменения персонажа
class Player(Game_Object):
    def __init__(self, x, y, pers):
        super(Player, self).__init__(x, y, pers, player_group)
        self.spisok_animation = pers
        self.update_static_pers()

    # метод выдачи режима бога
    def give_mod(self):
        if not self.god_mode:
            self.god_mode = True
        else:
            self.god_mode = False

    def update_static_pers(self):
        self.START_HP = self.spisok_animation[5]['health']
        self.NOW_HP = self.spisok_animation[5]['health']
        self.START_MANA = self.spisok_animation[5]['mana']
        self.NOW_MANA = self.spisok_animation[5]['mana']

    # метод возвращения настоящей картинки
    def return_now_skin(self):
        return self.image

    # восстановление маны
    def up_mana(self):
        if self.NOW_HP > 0:
            if self.NOW_MANA != self.START_MANA:
                self.time_to_restart_mana += 1
                if self.time_to_restart_mana == 100:
                    self.time_to_restart_mana = 0
                    self.NOW_MANA += 20
        else:
            self.NOW_MANA = 0

    def return_mana(self):
        return self.NOW_MANA, self.START_MANA

    def return_hp(self):
        return self.NOW_HP, self.START_HP

    def return_damage(self):
        return self.spisok_animation[5]['damage']

    def update(self, image):
        # # проверка что скин не меняли через QT
        if self.spisok_animation != image:
            x, y = self.rect.x, self.rect.y
            self.spisok_animation = image
            self.image = self.spisok_animation[0]
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = x, y
            self.update_static_pers()
        # если персонаж в воздухе он плавно спускается как будто на парашуте)))
        if not pygame.sprite.spritecollide(self, map_group, False, pygame.sprite.collide_mask) and not self.jumping:
            self.rect.y += 5

        if pygame.sprite.spritecollideany(self, mod_group) and self.shield >= 150:
            self.shield = 0
            self.NOW_HP -= 30
            if self.NOW_HP == 0:
                self.kill()

        # делаем прыжок
        if KEYS[pygame.K_SPACE] and not self.jumping and pygame.sprite.spritecollideany(self, map_group):
            self.jumping = True

        # когда персонаж идёт направо выполняется смена опаределённой картинки
        if KEYS[pygame.K_d] and self.rect.x + self.rect.width <= screen.get_width():
            self.right_pers, self.left_pers = True, False
            self.image = self.spisok_animation[0]
            self.rect.x += 5

        # когда персонаж идёт налево выполняется смена опаределённой картинки
        if KEYS[pygame.K_a] and self.rect.x >= 0:
            self.right_pers, self.left_pers = False, True
            self.image = self.spisok_animation[1]
            self.rect.x -= 5

        # выстрел
        if KEYS[pygame.K_q]:
            left_or_right_x = False if self.left_pers else True
            if self.god_mode:
                Projectale(self, self.rect, True, left_or_right_x, self.spisok_animation)
            else:
                if self.count_shoot >= 20:
                    self.count_shoot = 0
                    left_or_right_x = False if self.left_pers else True
                    if self.time_to_shoot <= 0:
                        self.time_to_shoot += 300
                        if self.NOW_MANA >= 20:
                            self.NOW_MANA -= 20
                            self.spisok_animation[4].play()
                            Projectale(self, self.rect, False, left_or_right_x, self.spisok_animation)

        if KEYS[pygame.K_F12] + KEYS[pygame.K_F9]:
            with open('shop_pers_loc.json') as FAQ:
                data = json.load(FAQ)
                for i in data:
                    data[i]['hero'] = False
                    data[i]['location'] = False
            with open('shop_pers_loc.json', 'w') as FAQ:
                json.dump(data, FAQ)

        # прыжок
        self.jump(self.jumping)

        # задержка выстрелов из орудия\посоха
        self.count_shoot += 1
        self.shield += 1


mobs = []
count_mobs = 3
wave_number = 0


def wave_print():
    if len(mobs) == 0:
        pygame.draw.rect(screen, (72, 61, 139), (700, 400, 500, 150))
        pygame.draw.rect(screen, (0, 0, 0), (700, 400, 500, 150), 20)

        screen.blit(FONT.render(f'Wave {wave_number}', True, (255, 204, 0)), (850, 420))


def wave():
    global count_mobs, wave_number, mobs
    if len(mobs) == 0:
        Player1.NOW_MANA = Player1.START_MANA
        # pygame.draw.rect(screen, (72, 61, 139), (700, 400, 500, 150))
        # pygame.draw.rect(screen, (0, 0, 0), (700, 400, 500, 150), 20)
        # screen.blit(FONT.render(f'Wave {wave_number}', True, (255, 204, 0)), (850, 420))
        for i in range(count_mobs):
            mobs.append(Mob(2700 + (250 * i), 750, pers))

        count_mobs += 2
        wave_number += 1


# вызываю определённые классы которые автоматически отрисовывваются

shop = Shop()
Settings()
Money()
Player1 = Player(0, 500, pers)
draw_map()

# Mob(1700, 700)
while True:
    screen.blit(return_background(), (0, 0))
    KEYS = pygame.key.get_pressed()
    for i in pygame.event.get():
        if i.type == pygame.MOUSEBUTTONDOWN:
            sprites_dop.update(i.pos)
        if i.type == pygame.QUIT or KEYS[pygame.K_F10] or KEYS[pygame.K_ESCAPE]:
            sys.exit()
        if KEYS[pygame.K_t] + KEYS[pygame.K_i] + KEYS[pygame.K_o]:
            Player1.give_mod()

    # Если у игрока не включен год мод, от появляется кул даун - воот он проходит
    if not Player1.god_mode:
        Player1.time_to_shoot -= 10
    # Отрисовка кол-ва хп и маны
    Indicator(Player1.return_hp()[0], Player1.return_hp()[1], (255, 0, 0), 100, 0, 140, 65).show()
    Indicator(Player1.return_mana()[0], Player1.return_mana()[1], (0, 0, 255), 260, 0, 140, 65).show()

    # Восполнение маны
    Player1.up_mana()
    # Отрисовка хп мобов
    for mob in mobs:
        if mob.NOW_HP != 0:
            Indicator(mob.NOW_HP, mob.START_HP, (255, 0, 0), mob.rect.x, mob.rect.y, 100, 10).obn()

    # Отрисовка спрайтов

    player_group.update(return_skin())
    projectales.update()
    mod_group.update()

    all_sprites.draw(screen)
    # Отрисовка всех доп.статов на экране
    ren_fon = FONT.render(f"{int(clock.get_fps())}", True, (255, 255, 255))
    money_fon = FONT.render(str(COUNT_MONEY), True, (195, 176, 165))
    rect_money = money_fon.get_rect()
    screen.blit(ren_fon, (0, 0))
    screen.blit(money_fon, (screen.get_width() - 150 - rect_money.w, 0))
    # Сохранение кол-ва монеток и максимального кол-ва килов
    with open('KILL_COUNT.txt', encoding='utf-8', mode='r') as mn1:
        BEST_KILL_COUNT = int(mn1.read())
        if BEST_KILL_COUNT < KILL_COUNT:
            BEST_KILL_COUNT = KILL_COUNT
    with open("KILL_COUNT.txt", encoding="utf-8", mode="w") as mn1:
        mn1.write(str(BEST_KILL_COUNT))

    # pygame.draw.rect(screen, (0, 0, 0), (0, 70, 350, 100))
    kills = FONT.render(f"Kills: {KILL_COUNT}", True, (255, 255, 255))
    screen.blit(kills, (0, 70))
    best_kills = FONT.render(f"Best Kills: {BEST_KILL_COUNT}", True, (255, 255, 255))
    w = FONT.render(f"Wave: {wave_number}", True, (255, 255, 255))
    screen.blit(w, (410, 0))
    screen.blit(best_kills, (0, 110))
    # Вызов волн мобов

    wave()

    # Смена кадра
    pygame.display.flip()
    clock.tick(FPS)
