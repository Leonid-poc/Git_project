from build import *
from Proj import *


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
Text1 = load_image(r"Jungle\jungle.png")
while True:
    screen.blit(Text1, (0, 0))

    KEYS = pygame.key.get_pressed()
    for i in pygame.event.get():
        if i.type == pygame.MOUSEBUTTONDOWN:
            sprites_dop.update(i.pos)
        if i.type == pygame.QUIT or KEYS[pygame.K_F10] or KEYS[pygame.K_ESCAPE]:
            sys.exit()

    pygame.display.flip()
