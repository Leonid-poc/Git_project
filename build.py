import sys, os, pygame
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from shop import Ui_MainWindow
from settings import Ui_MainWindow_1
from map import *

pygame.init()


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


sprites_dop = pygame.sprite.Group()
player_group = pygame.sprite.Group()
map_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

FPS = 60
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
RES = WIDTH, HEIGHT = pygame.display.get_window_size()
prop_pers_x, prop_pers_y = int(WIDTH * 0.1324), int(HEIGHT * 0.459)


location = [r'Jungle\jungle.png', r'Jungle\floor.png', r'Jungle\wall.png']
background = load_image(location[0])
font = pygame.font.Font(None, 100)
location_code = JUNGLE
pers = load_image(r'Jungle\jungle_mainhero.png')


class MyShop(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Магазин')
        self.pixmap_loc = [QPixmap(r'data\Jungle\jungle.png').scaled(267, 150),
                           QPixmap(r'data\Winter\Winter.png').scaled(267, 150),
                           QPixmap(r'data\Desert\desert.png').scaled(267, 150)]
        self.pixmap_pers = [QPixmap(r'data\Jungle\jungle_mainhero.png').scaled(prop_pers_x, prop_pers_y),
                            QPixmap(r'data\Winter\winter_mainhero.png').scaled(prop_pers_x, prop_pers_y),
                            QPixmap(r'data\Desert\desert_mainhero.png').scaled(prop_pers_x, prop_pers_y)]
        self.label_4.setPixmap(self.pixmap_loc[0])
        self.label_5.setPixmap(self.pixmap_loc[1])
        self.label_6.setPixmap(self.pixmap_loc[2])
        self.label.setPixmap(self.pixmap_pers[0])
        self.label_2.setPixmap(self.pixmap_pers[1])
        self.label_3.setPixmap(self.pixmap_pers[2])
        self.pushButton.clicked.connect(self.run_pers)
        self.pushButton_2.clicked.connect(self.run_pers)
        self.pushButton_3.clicked.connect(self.run_pers)
        self.pushButton_4.clicked.connect(self.run_loc)
        self.pushButton_5.clicked.connect(self.run_loc)
        self.pushButton_6.clicked.connect(self.run_loc)

    def run_loc(self):
        global background, location_code, location
        map_group.empty()
        if self.sender().objectName()[-1] == '4':
            location = [r'Jungle\jungle.png', r'Jungle\floor.png', r'Jungle\wall.png']
            location_code = JUNGLE
        if self.sender().objectName()[-1] == '5':
            location = [r'Winter\Winter.png', r'Winter\floor.png', r'Winter\wall.png']
            location_code = WINTER
        if self.sender().objectName()[-1] == '6':
            location = [r'Desert\desert.png', r'Desert\floor.png', r'Desert\wall.png']
            location_code = DESERT
        background = load_image(location[0])
        draw_map()


    def run_pers(self):
        global player, pers
        if self.sender().objectName()[-1] == 'n':
            pers = pygame.transform.scale(load_image(r'Jungle\jungle_mainhero.png'), (prop_pers_x, prop_pers_y))
        if self.sender().objectName()[-1] == '2':
            pers = pygame.transform.scale(load_image(r'Winter\winter_mainhero.png'), (prop_pers_x, prop_pers_y))
        if self.sender().objectName()[-1] == '3':
            pers = pygame.transform.scale(load_image(r'Desert\desert_mainhero.png'), (prop_pers_x, prop_pers_y))



class MySettings(QMainWindow, Ui_MainWindow_1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Настройки')
        self.horizontalSlider.sliderMoved.connect(self.run)
        self.horizontalSlider_2.sliderMoved.connect(self.run)
        self.horizontalSlider.sliderReleased.connect(self.run)
        self.horizontalSlider_2.sliderReleased.connect(self.run)
        self.pixmap = [QPixmap(r'data\Other\none_vol.png'), QPixmap(r'data\Other\low_vol.png'),
                       QPixmap(r'data\Other\middle_vol.png'), QPixmap(r'data\Other\hight_vol.png')]
        self.label.setPixmap(self.pixmap[1])
        self.label_2.setPixmap(self.pixmap[1])

    def run(self):
        with open('volume.txt', mode='w', encoding='utf-8') as txt:
            self.num_vol_music, self.num_vol_effects = 1, 1
            if self.sender().objectName()[-1] == '2':
                self.lcdNumber_2.display(self.horizontalSlider_2.value())
                if self.horizontalSlider_2.value() == 0:
                    self.num_vol_music = 0
                    self.label_2.setPixmap(self.pixmap[self.num_vol_music])
                else:
                    if self.horizontalSlider_2.value() >= 99:
                        self.num_vol_music = 3
                        self.label_2.setPixmap(self.pixmap[self.num_vol_music])
                    else:
                        self.num_vol_music = int(self.horizontalSlider_2.value() // 33 + 1)
                        self.label_2.setPixmap(self.pixmap[self.num_vol_music])
            else:
                self.lcdNumber.display(self.horizontalSlider.value())
                if self.horizontalSlider.value() == 0:
                    self.num_vol_effects = 0
                    self.label.setPixmap(self.pixmap[self.num_vol_effects])
                else:
                    if self.horizontalSlider.value() >= 99:
                        self.num_vol_effects = 3
                        self.label.setPixmap(self.pixmap[self.num_vol_effects])
                    else:
                        self.num_vol_effects = int(self.horizontalSlider.value() // 33 + 1)
                        self.label.setPixmap(self.pixmap[self.num_vol_effects])
            txt.write(f'{self.horizontalSlider.value()} {self.horizontalSlider_2.value()}'
                      f' {self.num_vol_effects} {self.num_vol_music}')

    def save_vol(self):
        with open('volume.txt', mode='r', encoding='utf-8') as text:
            text = text.read().split()
            if len(text) <= 2:
                text = ['25', '25', '1', '1']
            self.horizontalSlider.setValue(int(text[0]))
            self.label.setPixmap(self.pixmap[int(text[3])])
            self.label_2.setPixmap(self.pixmap[int(text[2])])
            self.lcdNumber.display(int(text[0]))
            self.horizontalSlider_2.setValue(int(text[1]))
            self.lcdNumber_2.display(int(text[1]))


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
    ex.save_vol()
    ex.show()
    sys.excepthook = except_hook
    app.exec()


def draw_map():
    for i in enumerate(location_code):
        for j in enumerate(i[1]):
            if j[1] == 'q':
                Map(location[1], location_code, screen.get_width() // len(location_code[0]) * j[0],
                    screen.get_height() // len(location_code) * i[0])
            if j[1] == 'w':
                Map(location[2], location_code, screen.get_width() // len(location_code[0]) * j[0],
                    screen.get_height() // len(location_code) * i[0])


class Shop(pygame.sprite.Sprite):
    def __init__(self):
        super(Shop, self).__init__(sprites_dop, all_sprites)
        self.image = pygame.transform.scale(load_image(r'Other\shop.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() - 100
        self.rect.y = 0

    def return_background(self):
        return background

    def update(self, pos):
        if self.rect.collidepoint(pos):
            qt_start_shop()

    def return_skin(self):
        return pers

class Settings(pygame.sprite.Sprite):
    def __init__(self):
        super(Settings, self).__init__(sprites_dop, all_sprites)
        self.image = pygame.transform.scale(load_image(r'Other\settings.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() - 50
        self.rect.y = 0

    def update(self, pos):
        if self.rect.collidepoint(pos):
            qt_start_settings()


class Map(pygame.sprite.Sprite):
    def __init__(self, image, loc, x, y):
        super(Map, self).__init__(map_group)
        self.image = pygame.transform.scale(load_image(image), (screen.get_width() // len(loc[0]),
                                                                screen.get_height() // len(loc)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
