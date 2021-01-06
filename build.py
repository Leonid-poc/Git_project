import sys, os, pygame
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from shop import Ui_MainWindow
from settings import Ui_MainWindow_1

pygame.init()
all_sprites = pygame.sprite.Group()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


class MyShop(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Магазин')


class MySettings(QMainWindow, Ui_MainWindow_1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Настройки')
        self.horizontalSlider.sliderMoved.connect(self.run)
        self.horizontalSlider_2.sliderMoved.connect(self.run)
        self.horizontalSlider.sliderReleased.connect(self.run)
        self.horizontalSlider_2.sliderReleased.connect(self.run)
        self.pixmap = [QPixmap(r'data\none_vol.png'), QPixmap(r'data\low_vol.png'),
                       QPixmap(r'data\middle_vol.png'), QPixmap(r'data\hight_vol.png')]
        self.label.setPixmap(self.pixmap[1])
        self.label_2.setPixmap(self.pixmap[1])

    def run(self):
        if self.sender().objectName()[-1] == '2':
            self.lcdNumber_2.display(self.horizontalSlider_2.value())
            if self.horizontalSlider_2.value() == 0:
                self.label_2.setPixmap(self.pixmap[0])
            else:
                if self.horizontalSlider_2.value() >= 99:
                    self.label_2.setPixmap(self.pixmap[3])
                else:
                    self.label_2.setPixmap(self.pixmap[int(self.horizontalSlider_2.value() // 33 + 1)])
        else:
            self.lcdNumber.display(self.horizontalSlider.value())
            if self.horizontalSlider.value() == 0:
                self.label.setPixmap(self.pixmap[0])
            else:
                if self.horizontalSlider.value() >= 99:
                    self.label.setPixmap(self.pixmap[3])
                else:
                    self.label.setPixmap(self.pixmap[int(self.horizontalSlider.value() // 33 + 1)])

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

def qt_start_shop():
    app = QApplication(sys.argv)
    ex = MyShop()
    ex.show()
    sys.excepthook = except_hook
    app.exec()


def qt_start_settings():
    app = QApplication(sys.argv)
    ex = MySettings()
    ex.show()
    sys.excepthook = except_hook
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
        self.image = pygame.transform.scale(load_image('shop.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() - 100
        self.rect.y = 0

    def update(self, pos):
        if self.rect.collidepoint(pos):
            qt_start_shop()
        if pygame.display.get_active():
            self.image = pygame.transform.scale(load_image('shop.png'), (50, 50))
            self.rect.x = screen.get_width() - 100
            self.rect.y = 0


class Settings(pygame.sprite.Sprite):
    def __init__(self):
        super(Settings, self).__init__(all_sprites)
        self.image = pygame.transform.scale(load_image('settings.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() - 50
        self.rect.y = 0

    def update(self, pos):
        if self.rect.collidepoint(pos):
            qt_start_settings()
        if pygame.display.get_active():
            self.rect.x = screen.get_width() - 50
            self.rect.y = 0


Shop()
Settings()

while True:
    screen.fill('black')
    KEYS = pygame.key.get_pressed()
    for i in pygame.event.get():
        if KEYS[pygame.K_q] + KEYS[pygame.K_LCTRL] == 2 or i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(i.pos)
    all_sprites.draw(screen)
    pygame.display.flip()
