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


class Money(pygame.sprite.Sprite):
    def __init__(self):
        super(Money, self).__init__(all_sprites, money_group)
        self.image = pygame.transform.scale(load_image(r'Other\poket_money.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() - 150
        self.rect.y = 0
        self.count_money = 0
        self.vivod_money = FONT.render(f'{self.count_money}', True, (123, 104, 238))
        self.rect_money = self.vivod_money.get_rect()
        screen.blit(self.vivod_money, (screen.get_width() - 150 - self.rect_money.w, 0))

    def update(self):
        self.vivod_money = FONT.render(f'{self.count_money}', True, (123, 104, 238))
        screen.blit(self.vivod_money, (screen.get_width() - 150 - self.rect_money.w, 10))


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
