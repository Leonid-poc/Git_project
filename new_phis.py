from build import *
import pygame

pygame.init()
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__(all_sprites, player_group)
        self.image = pers
        self.count_jump = 10
        self.jumping = False
        self.rect = self.image.get_rect()

    def return_now_skin(self):
        return self.image

    def update(self, image):
        if self.image != image:
            x, y = self.rect.x, self.rect.y
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = x, y
        if not pygame.sprite.spritecollideany(self, map_group) and not self.jumping:
            self.rect.y += 5
        if KEYS[pygame.K_SPACE] and not self.jumping and pygame.sprite.spritecollideany(self, map_group):
            self.jumping = True
        if KEYS[pygame.K_d] and self.rect.x + self.rect.width <= screen.get_width():
            self.rect.x += 5
        if KEYS[pygame.K_a] and self.rect.x >= 0:
            self.rect.x -= 5
        if self.jumping:
            if self.count_jump >= -10:
                if self.count_jump < 0:
                    self.rect.y += (self.count_jump ** 2)
                else:
                    self.rect.y -= (self.count_jump ** 2)
                self.count_jump -= 1
            else:
                self.jumping = False
                self.count_jump = 10


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

    all_sprites.draw(screen)
    map_group.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)
