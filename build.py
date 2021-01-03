import sys, os, pygame
from PyQt5.QtWidgets import QApplication, QMainWindow
from shop import Ui_MainWindow

pygame.init()
all_sprites = pygame.sprite.Group()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Магазин')

def shop_start():
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    app.exec()

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

class Shop(pygame.sprite.Sprite):
    def __init__(self):
        super(Shop, self).__init__(all_sprites)
        self.image = pygame.transform.scale(load_image('pol.png'), (50, 70))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50

    def update(self, pos):
        if self.rect.collidepoint(pos):
            shop_start()


Shop()
while True:
    screen.fill('black')
    KEYS = pygame.key.get_pressed()
    for i in pygame.event.get():
        if KEYS[pygame.K_q] + KEYS[pygame.K_LCTRL] == 2:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(i.pos)
    all_sprites.draw(screen)
    pygame.display.flip()