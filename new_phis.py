from build import *
import pygame

# инициализирую пайтон и добавляю переменные часы для того чтобы выставить значение фпс
pygame.init()
clock = pygame.time.Clock()


# класс игрока который отвечает за любые события и изменения персонажа
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__(all_sprites, player_group)
        self.image = pers
        self.mask = pygame.mask.from_surface(self.image)
        self.count_jump = 20
        self.jumping = False
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 735
        self.START_HP = 180
        self.NOW_HP = 180
        self.START_MANA = 200
        self.NOW_MANA = 200
        self.god_mode = False
        self.time_to_restart_mana = 0

    def return_now_skin(self):
        return self.image

    def give_mod(self):
        if not self.god_mode:
            self.god_mode = True
        else:
            self.god_mode = False

    def proof_pos(self):
        for i in map_coords_spisok:
            if self.rect.x + self.rect.width > i[0] and self.rect.y + self.rect.height > i[1]:
                return False
            if i[0] + i[2] > self.rect.x and i[1] + i[3] > self.rect.y:
                return False
            return True

    def proof_font_fall_out_map(self):
        for i in map_coords_spisok:
            if self.rect.topright[0] >= i[0] and self.rect.x <= i[0] + i[2] and i[1] - 180 <= self.rect.y <= i[1]:
                print(self.rect.bottom, i[1])
                while self.rect.bottom > i[1]:
                    self.rect.y -= 1

    def send_hp(self):
        if self.god_mode:
            pass
        return self.START_HP


    def up_mana(self):
        if self.NOW_MANA != self.START_MANA:
            self.time_to_restart_mana += 1
            if self.time_to_restart_mana == 100:
                self.time_to_restart_mana = 0
                self.NOW_MANA += 20

    def update(self, image):
        if self.image != image:
            x, y = self.rect.x, self.rect.y
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = x, y
            print(self.rect.y)
        if not pygame.sprite.spritecollide(self, map_group, False, pygame.sprite.collide_mask) and not self.jumping:
            self.rect.y += 5

        if KEYS[pygame.K_SPACE] and not self.jumping and pygame.sprite.spritecollideany(self, map_group):
            self.jumping = True

        if KEYS[pygame.K_d] and self.rect.x + self.rect.width <= screen.get_width():
            self.right_pers, self.left_pers = True, False
            self.rect.x += 5

        if KEYS[pygame.K_a] and self.rect.x >= 0:
            self.right_pers, self.left_pers = False, True
            self.rect.x -= 5

        if KEYS[pygame.K_q]:
            if self.NOW_MANA >= 20:
                self.NOW_MANA -= 20
                if not self.god_mode:
                    Projectale(self, self.rect, True)
                else:
                    Projectale(self, self.rect)

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


class Projectale(pygame.sprite.Sprite):
    def __init__(self, person, person_rect, god_mode=False):
        super().__init__(projectales)
        self.mode = god_mode
        self.person_rect = person_rect
        self.person = person
        self.pers_pos_x, self.pers_pos_y = person_rect.x, person_rect.y


        if self.mode:
            self.image = pygame.transform.scale(load_image(r'Other\qt.png'), (100, 60))
        else:
            self.image = pygame.transform.scale(load_image(r'Other\qt.png'), (200, 120))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pers_pos_x, self.pers_pos_y

    def update(self):

            if not (pygame.sprite.spritecollide(self, map_group, True) or self.rect.topright[0] >= screen.get_width()):
                if not self.mode:
                    self.rect.x += 100
                else:
                    self.rect.x += 40
            else:
                self.kill()


class Indicator:
    def __init__(self, stat, start_stat, color, x, y):
        self.stat = stat
        self.start_stat = start_stat
        self.hp_procent = int((self.stat / self.start_stat) * 100) / 100
        self.COLOR_TEXT= (255, 255, 255)
        self.COLOR_PAN = color
        self.x, self.y = x, y
        self.FOOT, self.ROS = 140, 65
    def show(self):
        pygame.draw.rect(screen, (self.COLOR_PAN), (self.x, self.y, int(self.FOOT * self.hp_procent), self.ROS))
        pygame.draw.rect(screen, (0,0,0), (self.x, self.y, self.FOOT, self.ROS), 5)
        screen.blit(FONT.render(f'{self.stat}', True, self.COLOR_TEXT), (self.x+15, 5))

# вызываю определённые классы которые автоматически отрисовывваются
Shop()
Settings()
Player1 = Player()
draw_map()

while True:
    # Основной цикл, куда уж без него, если ты читал комментарии до этого, ты должен всё понять
    # Есть баг с нажатием пробела (110, 112 строчки), помоги исправить, плез, перс улетает в потолок

    screen.blit(return_background(), (0, 0))
    KEYS = pygame.key.get_pressed()
    for i in pygame.event.get():
        if i.type == pygame.MOUSEBUTTONDOWN:
            sprites_dop.update(i.pos)
        if i.type == pygame.QUIT or KEYS[pygame.K_F10]:
            sys.exit()
        if KEYS[pygame.K_t] + KEYS[pygame.K_i] + KEYS[pygame.K_o]:
            Player1.give_mod()
        # if i.type ==
    # if Player.return_now_skin() not in (return_skin()):
    player_group.update(return_skin())
    # player_group.update(Player.return_now_skin())
    Player1.up_mana()
    ren_fon = FONT.render(f"{int(clock.get_fps())}", True, (255, 255, 255))
    screen.blit(ren_fon, (0, 0))
    # Отрисовка спрайтов
    all_sprites.draw(screen)
    projectales.update()
    projectales.draw(screen)
    map_group.draw(screen)
    # Отрисовка кол-ва хп

    ind_hp = Indicator(Player1.NOW_HP, Player1.START_HP, (255, 0, 0), 100, 0)
    ind_hp.show()
    ind_mana = Indicator(Player1.NOW_MANA, Player1.START_MANA, (0, 0, 255), 260, 0)
    ind_mana.show()
    # Смена кадра
    pygame.display.flip()
    clock.tick(FPS)
