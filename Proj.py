from Settings import *



class Projectale(pygame.sprite.Sprite):
    def __init__(self, person, person_rect, god_mode=False, left_or_right_x=None, puli_ru=None):
        super().__init__(all_sprites, projectales)
        self.mode = god_mode
        self.person_rect = person_rect
        self.person = person
        self.VX = 1 if left_or_right_x else -1
        self.IMAGE_X = puli_ru[2] if left_or_right_x else puli_ru[3]
        self.pos_project = -90 if left_or_right_x else person_rect.w
        self.pers_pos_x, self.pers_pos_y = person_rect.x - self.pos_project, \
                                           person_rect.y + person_rect.h / 2 - 25
        if self.mode:
            self.image = pygame.transform.scale(self.IMAGE_X, (180, 108))
        else:
            self.image = pygame.transform.scale(self.IMAGE_X, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pers_pos_x, self.pers_pos_y

    def update(self):
        if not (pygame.sprite.spritecollide(self, map_group, False) or self.rect.topright[0] >= screen.get_width()):
            if self.mode:
                self.rect.x += 100 * self.VX
            else:
                self.rect.x += 40 * self.VX
        else:
            self.kill()


class Monetki_from_mob(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super(Monetki_from_mob, self).__init__(all_sprites, mod_group)
        self.image = pygame.transform.scale(load_image(r'Other\gold.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.step = 100
        self.rect.x = x + (w / 2) - (self.rect.w / 2)
        self.rect.y = y + (h / 2) - (self.rect.h / 2)
        self.way_x = (screen.get_width() - 25 - (self.rect.x + self.rect.w / 2)) / self.step
        self.way_y = -(self.rect.y + self.rect.h / 2) / self.step

    def update(self):
        if pygame.sprite.spritecollideany(self, money_group):
            self.kill()
        else:
            self.rect.x += self.way_x
            self.rect.y += self.way_y


class Money(pygame.sprite.Sprite):
    def __init__(self):
        super(Money, self).__init__(all_sprites, money_group)
        self.image = pygame.transform.scale(load_image(r'Other\poket_money.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() - 150
        self.rect.y = 0


class Indicator:
    def __init__(self, stat, start_stat, color, x, y, f, r):
        self.stat = stat
        self.start_stat = start_stat
        self.hp_procent = int((self.stat / self.start_stat) * 100) / 100
        self.COLOR_TEXT = (255, 255, 255)
        self.COLOR_PAN = color
        self.x, self.y = x, y
        self.FOOT, self.ROS = f, r

    def obn(self):
        pygame.draw.rect(screen, (self.COLOR_PAN), (self.x, self.y, int(self.FOOT * self.hp_procent), self.ROS))
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.FOOT, self.ROS), 5)

    def show(self):
        self.obn()
        screen.blit(FONT.render(f'{self.stat}', True, self.COLOR_TEXT), (self.x + 15, 5))


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
