from build import *
import pygame

# инициализирую пайтон и добавляю переменные часы для того чтобы выставить значение фпс
pygame.init()
clock = pygame.time.Clock()


# класс игрока который отвечает за любые события и изменения персонажа
class Player(pygame.sprite.Sprite):
    left_pers = False
    right_pers = True

    def __init__(self):
        super(Player, self).__init__(all_sprites, player_group)
        self.image = pers
        self.mask = pygame.mask.from_surface(self.image)
        self.count_jump = 20
        self.jumping = False
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 735

    def return_now_skin(self):
        return self.image

    def proof_pos(self):
        for i in map_coords_spisok:
            if self.rect.x + self.rect.width > i[0] and self.rect.y + self.rect.height > i[1]:
                return False
            if i[0] + i[2] > self.rect.x and i[1] + i[3] > self.rect.y:
                return False
            return True

    def povorot_pers(self):
        return (self.left_pers, self.right_pers)

    def proof_font_fall_out_map(self):
        for i in map_coords_spisok:
            if self.rect.topright[0] >= i[0] and self.rect.x <= i[0] + i[2] and i[1] - 180 <= self.rect.y <= i[1]:
                print(self.rect.bottom, i[1])
                while self.rect.bottom > i[1]:
                    self.rect.y -= 1

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
        if KEYS[pygame.K_q] and len(projectales.sprites()) <= 10:
            Projectale(self.rect)
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
    def __init__(self, person):
        super(Projectale, self).__init__(all_sprites, projectales)
        self.pers_pos_x, self.pers_pos_y = person.topright[0], person.bottom - 110
        self.image = pygame.transform.scale(load_image(r'Other\fireball1.png'), (60, 40))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pers_pos_x, self.pers_pos_y

    def update(self):
        if not (pygame.sprite.spritecollideany(self, map_group) or self.rect.topright[0] >= screen.get_width()):
            self.rect.x += 10
        else:
            self.kill()


# вызываю определённые классы которые автоматически отрисовывваются
vremenaya = Shop()
Settings()
just_comfort = Player()
draw_map()

while True:
    # Основной цикл, куда уж без него, если ты читал комментарии до этого, ты должен всё понять
    # Есть баг с нажатием пробела (110, 112 строчки), помоги исправить, плез, перс улетает в потолок
    KEYS = pygame.key.get_pressed()
    screen.blit(vremenaya.return_background(), (0, 0))
    for i in pygame.event.get():
        if i.type == pygame.MOUSEBUTTONDOWN:
            sprites_dop.update(i.pos)
        if i.type == pygame.QUIT or KEYS[pygame.K_F10]:
            sys.exit()

    if just_comfort.return_now_skin() not in (vremenaya.return_skin(), vremenaya.return_mirror_skin()):
        player_group.update(vremenaya.return_skin())
    player_group.update(just_comfort.return_now_skin())

    ren_fon = fon.render(f'{int(clock.get_fps())}', True, (255, 255, 255))
    screen.blit(ren_fon, (0, 0))

    all_sprites.draw(screen)
    projectales.update()
    map_group.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)
