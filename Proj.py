from Settings import *


# класс отрисовки пуль
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
            self.image = pygame.transform.scale(self.IMAGE_X, (int(screen.get_width() / 10.666),
                                                               int(screen.get_height() / 10)))
        else:
            self.image = pygame.transform.scale(self.IMAGE_X, (int(screen.get_width() / 19.2),
                                                               int(screen.get_height() / 21.6)))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pers_pos_x, self.pers_pos_y

    # пули летят смотря какой персонаж и куда он смотрит и включен ли ГОД мод
    def update(self):
        if not (pygame.sprite.spritecollide(self, map_group, False) or self.rect.topright[0] >= screen.get_width() or
                self.rect.topright[0] < 0):
            if self.mode:
                self.rect.x += 100 * self.VX
            else:
                self.rect.x += 40 * self.VX
        else:
            self.kill()


# класс отрисовки монеток
class Monetki_from_mob(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super(Monetki_from_mob, self).__init__(all_sprites, mod_group)
        self.image = pygame.transform.scale(load_image(r'Other\gold.png'), (int(W_proc * 2.5),
                                                                                   int(W_proc * 2.5)))
        self.rect = self.image.get_rect()
        self.step = 100
        self.rect.x = x + (w / 2) - (self.rect.w / 2)
        self.rect.y = y + (h / 2) - (self.rect.h / 2)
        self.way_x = (screen.get_width() - 25 - (self.rect.x + self.rect.w / 2)) / self.step
        self.way_y = -(self.rect.y + self.rect.h / 2) / self.step

    # по теореме пифагора я расчитываю путь монетки которая долетает до стопки примерно за 2 секунды где бы она не была
    def update(self):
        if pygame.sprite.spritecollideany(self, money_group):
            self.kill()
        else:
            self.rect.x += self.way_x
            self.rect.y += self.way_y


# класс отричовки стопки монеток
class Money(pygame.sprite.Sprite):
    def __init__(self):
        super(Money, self).__init__(all_sprites, money_group)
        self.image = pygame.transform.scale(load_image(r'Other\poket_money.png'), (int(W_proc * 2.5),
                                                                                   int(W_proc * 2.5)))
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() - W_proc * 7.5
        self.rect.y = 0


# класс отрисовки индикаторов у различных оъектов которые имеют характеристики
class Indicator:
    def __init__(self, stat, start_stat, color, x, y, f, r):
        self.stat = stat
        self.start_stat = start_stat
        self.hp_procent = int((self.stat / self.start_stat) * 100) / 100
        self.COLOR_TEXT = (255, 255, 255)
        self.COLOR_PAN = color
        self.x, self.y = x, y
        self.FOOT, self.ROS = f, r

    # показывает характеристики на экране игры
    def obn(self):
        pygame.draw.rect(screen, (self.COLOR_PAN), (self.x, self.y, int(self.FOOT * self.hp_procent), self.ROS))
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.FOOT, self.ROS), 5)

    # главный метод котрый показывает всё сразу
    def show(self):
        self.obn()
        screen.blit(FONT.render(f'{self.stat}', True, self.COLOR_TEXT), (self.x + 15, 5))
