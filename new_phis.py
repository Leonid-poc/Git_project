from build import *
from Proj import *
from screensaver import *
# инициализирую пайтон и добавляю переменные часы для того чтобы выставить значение фпс
pygame.init()
clock = pygame.time.Clock()
KILL_COUNT = 0


class Game_Object(pygame.sprite.Sprite):
    def __init__(self, x, y, pers, group):
        super(Game_Object, self).__init__(all_sprites, group)
        self.count_jump = 20
        self.jumping = False
        self.killing = False
        self.god_mode = False
        self.time_to_restart_mana = 0
        self.time_to_shoot = 0
        self.count_shoot = 0
        self.shield = 100
        self.shield_count = 0
        self.START_HP = 0
        self.NOW_HP = 0
        self.START_MANA = 0
        self.NOW_MANA = 0
        self.STEP = 20
        self.count_step = 0

    # проверка не провалился ли слегка игрок под карту
    def proof_font_fall_out_map(self):
        while self.rect.bottom > map_coords_spisok[0] + 3:
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

    def return_mana(self):
        return self.NOW_MANA, self.START_MANA

    def return_hp(self):
        return self.NOW_HP, self.START_HP

    def return_pos(self):
        return self.rect.x, self.rect.y


class Mob(Game_Object):
    def __init__(self, x, y, pers, group=mod_group):
        super(Mob, self).__init__(x, y, pers, group)
        self.characteristics_of_character = pers
        self.right_pers, self.left_pers = False, True
        self.image = self.characteristics_of_character[0][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.START_HP = pers[2]['health']
        self.NOW_HP = pers[2]['health']
        self.START_MANA = 200
        self.NOW_MANA = 200
        self.jumping = False
        self.jumping_anim = True
        self.count_jump = 20
        self.agressian = True if Player1.count_agressors < 4 else False
        if self.agressian:
            Player1.append_agressor()
        self.vx = rg.randrange(4, 7)

    def animation(self):
        x, y = self.rect.x, self.rect.y
        if pygame.sprite.spritecollide(self, player_group, False, pygame.sprite.collide_mask):
            self.count_step %= self.STEP * 3
            self.image = self.characteristics_of_character[1][self.count_step // self.STEP][1 if self.right_pers else 0]
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = x, y
            self.count_step += 1
            self.jumping_anim = False
            for i in pygame.sprite.spritecollide(self, player_group, False, pygame.sprite.collide_mask):
                i.damage(self.characteristics_of_character[2]['damage'])
        else:
            self.image = self.characteristics_of_character[0][1 if self.right_pers else 0]
            self.jumping_anim = True
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = x, y

    def update(self):
        if not self.killing:
            global COUNT_MONEY, KILL_COUNT
            # Падение
            if not pygame.sprite.spritecollide(self, map_group, False, pygame.sprite.collide_mask) and not self.jumping:
                self.rect.y += 5
                self.proof_font_fall_out_map()
            if self.rect.x > 110 and not self.agressian:
                self.rect.x -= self.vx
            elif self.agressian and not pygame.sprite.spritecollide(self,
                                                                    player_group, False, pygame.sprite.collide_mask):
                raznica = Player1.return_pos()[0] - self.rect.x
                if raznica == abs(raznica):
                    self.right_pers, self.left_pers = True, False
                    self.rect.x += self.vx
                else:
                    self.right_pers, self.left_pers = False, True
                    self.rect.x -= self.vx

            self.animation()

            if pygame.sprite.spritecollide(self, projectales, True):
                self.NOW_HP -= Player1.return_damage()
                if self.NOW_HP <= 0:
                    with open('MONEY.txt', mode='w', encoding='utf-8') as txt:
                        COUNT_MONEY = return_money(rg.choice(return_background()[1]))
                        txt.write(str(COUNT_MONEY))
                    self.killing = True
                    mobs.pop()
                    KILL_COUNT += 1
                    Monetki_from_mob(self.rect.x, self.rect.y, self.rect.w, self.rect.h)

            if not self.jumping and pygame.sprite.spritecollide(self, map_group, False, pygame.sprite.collide_mask):
                if self.jumping_anim:
                    self.jumping = rg.choice(range(100))
            self.jump(self.jumping == 10)

            if self.NOW_HP > 0:
                Indicator(self.NOW_HP, self.START_HP, (255, 0, 0), self.rect.x, self.rect.y - 10, 100, 10).obn()
        else:
            if self.rect.h >= 10:
                x, y = self.rect.x, self.rect.y
                self.image = pygame.transform.scale(self.image, (self.rect.w, self.rect.h - 2))
                self.rect = self.image.get_rect()
                self.rect.x, self.rect.y = x, y + 2
            else:
                if self.agressian:
                    Player1.kill_agressor()
                self.kill()


# класс игрока, который отвечает за любые события и изменения персонажа
class Player(Game_Object):
    count_agressors = 0

    def __init__(self, x, y, pers, group=player_group):
        super(Player, self).__init__(x, y, pers, group)
        self.characteristics_of_character = pers
        self.image = pers[0]
        self.rect = self.image.get_rect()
        self.rect.y = 755
        self.mask = pygame.mask.from_surface(self.image)
        self.right_pers, self.left_pers = True, False
        self.update_static_pers()

    # метод выдачи режима бога
    def give_mod(self):
        if not self.god_mode:
            self.god_mode = True
        else:
            self.god_mode = False

    def update_static_pers(self):
        self.START_HP = self.characteristics_of_character[5]['health']
        self.NOW_HP = self.characteristics_of_character[5]['health']
        self.START_MANA = self.characteristics_of_character[5]['mana']
        self.NOW_MANA = self.characteristics_of_character[5]['mana']

    # метод возвращения настоящей картинки
    def return_now_skin(self):
        return self.image

    def append_agressor(self):
        self.count_agressors += 1

    def kill_agressor(self):
        self.count_agressors -= 1

    # восстановление маны
    def up_mana(self):
        if self.NOW_HP > 0:
            if self.NOW_MANA != self.START_MANA:
                self.time_to_restart_mana += 1
                if self.time_to_restart_mana == 100:
                    self.time_to_restart_mana = 0
                    self.NOW_MANA += 20
                    # self.NOW_HP += 5
        else:
            self.NOW_MANA = 0

    def damage(self, dam):
        if self.shield_count >= self.shield and not (self.god_mode):
            self.NOW_HP -= dam
            self.shield_count = 0

    def return_damage(self):
        return self.characteristics_of_character[5]['damage']

    def update(self, image):
        if not self.killing:
            self.shield_count += 1
            # # проверка что скин не меняли через QT
            if self.characteristics_of_character != image:
                x, y = self.rect.x, self.rect.y
                self.characteristics_of_character = image
                self.image = self.characteristics_of_character[0]
                self.rect = self.image.get_rect()
                self.right_pers, self.left_pers = True, False
                self.rect.x, self.rect.y = x, y
                self.update_static_pers()
            # если персонаж в воздухе он плавно спускается как будто на парашуте)))
            if not pygame.sprite.spritecollide(self, map_group, False, pygame.sprite.collide_mask) and not self.jumping:
                self.rect.y += 5

            self.NOW_HP = max(self.NOW_HP, 0)
            if self.NOW_HP == 0:
                self.killing = True

            # делаем прыжок
            if KEYS[pygame.K_SPACE] and not self.jumping and pygame.sprite.spritecollideany(self, map_group):
                self.jumping = True

            # когда персонаж идёт направо выполняется смена опаределённой картинки
            if KEYS[pygame.K_d] and self.rect.x + self.rect.width <= screen.get_width():
                self.right_pers, self.left_pers = True, False
                self.image = self.characteristics_of_character[0]
                self.rect.x += 8

            # когда персонаж идёт налево выполняется смена опаределённой картинки
            if KEYS[pygame.K_a] and self.rect.x >= 0:
                self.right_pers, self.left_pers = False, True
                self.image = self.characteristics_of_character[1]
                self.rect.x -= 8

            # выстрел
            if KEYS[pygame.K_q]:
                left_or_right_x = False if self.left_pers else True
                if self.god_mode:
                    Projectale(self, self.rect, True, left_or_right_x, self.characteristics_of_character)
                else:
                    if self.count_shoot >= 20:
                        self.count_shoot = 0
                        left_or_right_x = False if self.left_pers else True
                        if self.time_to_shoot <= 0:
                            self.time_to_shoot += 300
                            if self.NOW_MANA >= 20:
                                self.NOW_MANA -= 20
                                self.characteristics_of_character[4].play()
                                Projectale(self, self.rect, False, left_or_right_x, self.characteristics_of_character)

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
        else:
            if self.rect.h >= 16:
                x, y = self.rect.x, self.rect.y
                self.image = pygame.transform.scale(self.image, (self.rect.w, self.rect.h - 2))
                self.rect = self.image.get_rect()
                self.rect.x, self.rect.y = x, y + 2
            else:
                self.kill()


class Portal(Game_Object):
    def __init__(self, x, y, pers, group=player_group):
        super(Portal, self).__init__(x, y, pers, group)
        self.characteristics_of_character = pers
        self.image = pers[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.killing = False
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.god_mode = False
        self.START_HP = 1000
        self.NOW_HP = 1000

    def damage(self, dam):
        if self.NOW_HP > 0:
            if self.shield_count >= self.shield:
                self.NOW_HP -= dam
                self.shield_count = 0


    def update(self, q=None):
        self.shield_count += 1
        self.count_step %= self.STEP * 4
        self.image = self.characteristics_of_character[self.count_step // self.STEP]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 10, 680
        self.count_step += 1


mobs = []
count_mobs = 3
wave_number = 0

port = []
for i in range(4):
    port.append(pygame.transform.scale(load_image(rf'Other\portal{i}.png'), (130, 254)))
port.append({'damage': 0, 'health': 700, 'mana': 0})




def wave():
    global count_mobs, wave_number, mobs
    if len(mobs) == 0:
        Player1.NOW_MANA = Player1.START_MANA
        Player1.count_agressors = 0
        # pygame.draw.rect(screen, (72, 61, 139), (700, 400, 500, 150))
        # pygame.draw.rect(screen, (0, 0, 0), (700, 400, 500, 150), 20)
        # screen.blit(FONT.render(f'Wave {wave_number}', True, (255, 204, 0)), (850, 420))
        for i in range(count_mobs):
            mobs.append(Mob(2700 + (250 * i), 750, return_mob()))

        count_mobs += 2
        wave_number += 1


# вызываю определённые классы которые автоматически отрисовывваются
portal = Portal(10, 680, port)
shop = Shop()
Settings()
Money()
Player1 = Player(0, 500, pers)
draw_map()
def check_vol():
    background_music.load(r'data\Music\background_1.mp3')
    background_music.play(-1)

def upgrade():
    pass

def mainest_main():
    global KEYS
    while True:
        screen.blit(return_background()[0], (0, 0))
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
        Indicator(portal.return_hp()[0], portal.return_hp()[1], (255, 0, 0), 10, 650, 130, 20).obn()
        # Восполнение маны
        Player1.up_mana()

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


        if portal.NOW_HP <= 0 or Player1.NOW_HP <= 0:
            portal.NOW_HP = 0
            Player1.NOW_HP = 0
            Player1.NOW_MANA = 0
            screen.blit(return_background()[0], (0, 0))
            Indicator(Player1.return_hp()[0], Player1.return_hp()[1], (255, 0, 0), 100, 0, 140, 65).show()
            Indicator(Player1.return_mana()[0], Player1.return_mana()[1], (0, 0, 255), 260, 0, 140, 65).show()
            Indicator(portal.return_hp()[0], portal.return_hp()[1], (255, 0, 0), 10, 650, 130, 20).obn()
            player_group.update(return_skin())
            projectales.update()
            mod_group.update()
            all_sprites.draw(screen)
            screen.blit(ren_fon, (0, 0))
            screen.blit(money_fon, (screen.get_width() - 150 - rect_money.w, 0))
            screen.blit(kills, (0, 70))
            screen.blit(w, (410, 0))
            screen.blit(best_kills, (0, 110))

            pygame.display.flip()
            clock.tick(FPS)

            end_game()



def start():
    while True:
        screen.blit(Text1, (0, 0))

        KEYS = pygame.key.get_pressed()
        for i in pygame.event.get():
            if i.type == pygame.QUIT or KEYS[pygame.K_F10] or KEYS[pygame.K_ESCAPE]:
                exit()
            if KEYS[pygame.K_F9]:
                background_music.load(r'data\Music\background_1.mp3')
                background_music.play(-1)
                mainest_main()
                sys.exit()
        pygame.display.flip()

if __name__ == '__main__':
    try:
        start()
    except Exception:
        pass
