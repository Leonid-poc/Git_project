from random import randrange
import os
from Proj import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
Text1 = pygame.transform.scale(load_image(r"Screen\main_screen.png"), screen.get_size())

background_music = pygame.mixer.music
background_music.load(r'data\Music\Screen_music.mp3')
background_music.play(-1)
with open('volume.txt', encoding='utf-8', mode='r') as text:
    txt = text.read().split()
    background_music.set_volume(int(txt[0]) / 100)


# эта фун-ия вызывается когда ты проиграл на окно пайгейм инструкция что делать дальше
def lose():
    render = FONT.render('YOU DIED', 50, (randrange(100, 255), 0, 0))
    render1 = FONT.render('Play - F9', 50, (randrange(100, 255), 0, 0))
    render2 = FONT.render('Exit - F10', 50, (randrange(100, 255), 0, 0))
    screen.blit(render, (W_proc * 41.66, H_proc * 50))
    screen.blit(render1, (W_proc * 41.66, H_proc * 59.25))
    screen.blit(render2, (W_proc * 41.66, H_proc * 62.96))
    pygame.display.flip()
    clock.tick(15)

# эта фун-ия вызывается когда игра окончена
def end_game():
    pygame.mixer.music.stop()
    b = pygame.mixer.music
    b.load(r'data\Music\Screen_music.mp3')
    b.play(-1)
    while True:
        lose()
        KEYS = pygame.key.get_pressed()
        for i in pygame.event.get():
            if i.type == pygame.QUIT or KEYS[pygame.K_F10] or KEYS[pygame.K_ESCAPE]:
                exit()
            if KEYS[pygame.K_F9]:
                pygame.quit()
                if 'new_phis.exe' in os.listdir(path='.'):
                    os.system('new_phis.exe')
                else:
                    os.system('new_phis.py')

            pygame.display.flip()

