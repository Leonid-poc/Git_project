# import pygame, sys
#
# pygame.init()
# screen = pygame.display.set_mode((500, 500))
# s = pygame.mixer.Sound(r'data\Music\bullet_shoot.mp3')
# b = pygame.mixer.music
# b.load(r'data\Music\background_1.mp3')
# b.play(-1)
# b.set_volume(0.2)
#
#
# while True:
#     screen.fill('red')
#     KEYS = pygame.key.get_pressed()
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             sys.exit()
#         if i.type == pygame.MOUSEBUTTONDOWN:
#             s.play(1)
#         if i.type == pygame.MOUSEBUTTONUP:
#             pass
#     pygame.display.update()