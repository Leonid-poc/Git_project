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

    def proof_pos(self):
        for i in map_coords_spisok:
            if self.rect.x + self.rect.width > i[0] and self.rect.y + self.rect.height > i[1]:
                return False
            if i[0] + i[2] > self.rect.x and i[1] + i[3] > self.rect.y:
                return False
            return True

    def update(self, image):
        if self.image != image:
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = 0, 745
            print(self.rect.y)
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
                    self.rect.y += (self.count_jump ** 2) / 10
                else:
                    self.rect.y -= (self.count_jump ** 2) / 10
                self.count_jump -= 1
            else:
                self.jumping = False
                self.count_jump = 20


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
    if just_comfort.return_now_skin() != vremenaya.return_skin():
        player_group.update(vremenaya.return_skin())
    player_group.update(just_comfort.return_now_skin())

    ren_fon = fon.render(f'{int(clock.get_fps())}', True, (255, 255, 255))
    screen.blit(ren_fon, (0, 0))

    all_sprites.draw(screen)
    map_group.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)
