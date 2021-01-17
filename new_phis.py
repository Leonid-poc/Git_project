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
        self.count_jump = 20
        self.jumping = False
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 735

    def return_now_skin(self):
        return self.image

    def update(self, image):
        if self.image != image:
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = 0, 745
        if not pygame.sprite.spritecollideany(self, map_group) and not self.jumping:
            self.rect.y += 5
        if KEYS[pygame.K_SPACE] and not self.jumping and pygame.sprite.spritecollideany(self, map_group):
            self.jumping = True
        if KEYS[pygame.K_d] and self.rect.x + self.rect.width <= screen.get_width():
            self.rect.x += 5
        if KEYS[pygame.K_a] and self.rect.x >= 0:
            self.rect.x -= 5
        if self.jumping:
            if self.count_jump >= -20:
                if self.count_jump < 0:
                    if not pygame.sprite.spritecollideany(self, map_group):
                        self.rect.y += (self.count_jump ** 2) / 10
                    else:
                        self.jumping = False
                        self.count_jump = 20
                else:
                    self.rect.y -= (self.count_jump ** 2) / 10
                self.count_jump -= 1
            else:
                if not pygame.sprite.spritecollideany(self, map_group):
                    self.rect.y += (self.count_jump ** 2) / 10
                    self.count_jump -= 1
                else:
                    self.jumping = False
                    self.count_jump = 20


class Projectale(pygame.sprite.Sprite):
    def __init__(self, person):
        super(Projectale, self).__init__(all_sprites, projectales)
        self.pers_pos_x, self.pers_pos_y = person.get_rect()
        self.image = pygame.transform.scale(load_image(r'Other\ball.png'), (60, 40))
        self.rect = self.image.get_rect()


    def shot(self):
        # self.pos = self.image.get_rect()
        self.rect.x += 10

        projectales.update(self.image)



# вызываю определённые классы которые автоматически отрисовывваются
Shop()
Settings()
Player = Player()
draw_map()


while True:
    # Основной цикл, куда уж без него, если ты читал комментарии до этого, ты должен всё понять
    # Есть баг с нажатием пробела (110, 112 строчки), помоги исправить, плез, перс улетает в потолок
    KEYS = pygame.key.get_pressed()
    screen.blit(return_background(), (0, 0))
    for i in pygame.event.get():
        if i.type == pygame.MOUSEBUTTONDOWN:
            sprites_dop.update(i.pos)
        if i.type == pygame.QUIT or KEYS[pygame.K_F10]:
            sys.exit()
    if Player.return_now_skin() != return_skin():
        player_group.update(return_skin())
    player_group.update(Player.return_now_skin())

    ren_font = FONT.render(f'{int(clock.get_fps())}', True, (255, 255, 255))
    screen.blit(ren_font, (0, 0))
    Projectale.shot(Projectale)
    all_sprites.draw(screen)
    map_group.draw(screen)
    projectales.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
