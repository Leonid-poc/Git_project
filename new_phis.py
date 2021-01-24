from build import *
from Proj import *

# инициализирую пайтон и добавляю переменные часы для того чтобы выставить значение фпс
pygame.init()
clock = pygame.time.Clock()


# класс игрока который отвечает за любые события и изменения персонажа
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, pers):
        super(Player, self).__init__(all_sprites, player_group)
        # задаю главные переменные
        self.spisok_animation = pers
        self.image = self.spisok_animation[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.count_jump = 20
        self.jumping = False
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.START_HP = 180
        self.NOW_HP = 180
        self.START_MANA = 200
        self.NOW_MANA = 200
        self.god_mode = False
        self.time_to_restart_mana = 0
        self.time_to_shoot = 0
        self.count_shoot = 0
        self.shield = 100
        self.right_pers, self.left_pers = True, False

    # метод возвращения настоящей картинки
    def return_now_skin(self):
        return self.image

    # метод выдачи режима бога
    def give_mod(self):
        if not self.god_mode:
            self.god_mode = True
        else:
            self.god_mode = False

    # проверка не провалился ли слегка игрок под карту
    def proof_font_fall_out_map(self):
        while self.rect.bottom > map_coords_spisok[0]:
            self.rect.y -= 1

    # отправка в определённое место кол-во ХП
    def send_hp(self):
        if self.god_mode:
            pass
        return self.START_HP

    # восстановление маны
    def up_mana(self):
        if self.NOW_HP >0:
            if self.NOW_MANA != self.START_MANA:
                self.time_to_restart_mana += 1
                if self.time_to_restart_mana == 100:
                    self.time_to_restart_mana = 0
                    self.NOW_MANA += 20
        else:
            self.NOW_MANA = 0


    def update(self, image):
        # проверка что скин не меняли через QT
        if self.spisok_animation != image:
            x, y = self.rect.x, self.rect.y
            self.spisok_animation = image
            self.image = self.spisok_animation[0]
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = x, y
        # если персонаж в воздухе он плавно спускается как будто на парашуте)))
        if not pygame.sprite.spritecollide(self, map_group, False, pygame.sprite.collide_mask) and not self.jumping:
            self.rect.y += 5

        if pygame.sprite.spritecollideany(self, mod_group) and self.shield >= 100:
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

        # прыжок
        if self.jumping:
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

        # задержка выстрелов из орудия\посоха
        self.count_shoot += 1
        self.shield += 1


class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Mob, self).__init__(mod_group, all_sprites)
        self.spisok_animation = [pygame.transform.scale(load_image(r'Jungle\jungle_mob.png'), (120, 180)),
                                 pygame.transform.flip(
                                     pygame.transform.scale(load_image(r'Jungle\jungle_mob.png'), (120, 180)), True,
                                     False)]
        self.image = self.spisok_animation[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.START_HP = 180
        self.NOW_HP = 180
        self.START_MANA = 200
        self.NOW_MANA = 200
        self.jumping = False
        self.god_mode = False
        self.time_to_restart_mana = 0
        self.time_to_shoot = 0
        self.count_jump = 20
        self.vx = rg.choice(range(5, 10))


    def proof_font_fall_out_map(self):
        while self.rect.bottom > map_coords_spisok[0]:
            self.rect.y -= 1

    def update(self):
        global COUNT_MONEY
        if not pygame.sprite.spritecollide(self, map_group, False, pygame.sprite.collide_mask) and not self.jumping:
            self.rect.y += 5
        if self.rect.x + self.rect.w >= screen.get_width() or self.rect.x <= 0:
            self.vx = -self.vx
            self.image = self.spisok_animation[abs(self.spisok_animation.index(self.image) - 1)]
        if pygame.sprite.spritecollide(self, projectales, True):
            self.NOW_HP -= 60
            if self.NOW_HP == 0:
                COUNT_MONEY += rg.choice(range(3, 6))
                self.kill()
                Monetki_from_mob(self.rect.x, self.rect.y, self.rect.w, self.rect.h)

        if not self.jumping and pygame.sprite.spritecollide(self, map_group, False, pygame.sprite.collide_mask):
            self.jumping = rg.choice(range(100))
        if self.jumping == 10:
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
        self.rect.x += self.vx


# вызываю определённые классы которые автоматически отрисовывваются
shop_for_circle = Shop()
Settings()
Money()
Player1 = Player(0, 500, pers)
draw_map()
moobs = []
for i in range(5):
    moobs.append(Mob(1700, 0))


while True:
    screen.blit(shop_for_circle.return_background(), (0, 0))
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
    ind_hp = Indicator(Player1.NOW_HP, Player1.START_HP, (255, 0, 0), 100, 0, 140, 65)
    ind_hp.show()
    ind_mana = Indicator(Player1.NOW_MANA, Player1.START_MANA, (0, 0, 255), 260, 0, 140, 65)
    ind_mana.show()

    # Восполнение маны
    Player1.up_mana()
    for mob in moobs:
        if mob.NOW_HP != 0:
            Indicator(mob.NOW_HP, mob.START_HP, (255, 0, 0), mob.rect.x, mob.rect.y, 100, 10).obn()

    # Отрисовка спрайтов
    player_group.update(shop_for_circle.return_skin())
    projectales.update()
    mod_group.update()

    all_sprites.draw(screen)
    ren_fon = FONT.render(f"{int(clock.get_fps())}", True, (255, 255, 255))
    money_fon = FONT.render(str(COUNT_MONEY), True, (195, 176, 165))
    rect_money = money_fon.get_rect()
    screen.blit(ren_fon, (0, 0))
    screen.blit(money_fon, (screen.get_width() - 150 - rect_money.w, 0))
    with open("MONEY.txt", encoding="utf-8", mode="w") as mn:
        mn.write(str(COUNT_MONEY))
    # Смена кадра
    pygame.display.flip()
    clock.tick(FPS)
