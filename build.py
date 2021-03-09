import sys, json
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QMovie
from UI_shop import Ui_MainWindow
from UI_settings import Ui_MainWindow_1
from UI_pashalka import Ui_MainWindow_2
from Settings import *
from Load_image import load_image, load_image_t

# инициализируем пайгем и звук из пайгейма
pygame.init()
pygame.mixer.init()


# класс магазина выполняет функцию окошка Магазин
class MyShop(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Магазин')
        self.update_info()
        # создание перменных цвета и градиента и подключение кнопок к функциям
        self.color_no = 'background-color: qlineargradient(spread:pad, x1:0, y1:0.943, x2:1, y2:0.944, ' \
                        'stop:0 rgba(0, 0, 0, 255), stop:1 rgba(176, 0, 255, 255));'
        self.color_yes = 'background-color: qlineargradient(spread:pad, x1:0, y1:0.943, x2:1, y2:0.944, ' \
                         'stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 64, 255, 255));'

        self.color_yes1 = 'color: rgb(255, 255, 255)'
        self.color_no1 = 'color: rgb:(0, 64, 255)'

        self.pushButton.clicked.connect(self.run_pers)
        self.pushButton_4.clicked.connect(self.run_loc)
        # проверка что у нас купленны или достаточно денег для покупки персов или локаций
        self.proof_price()
        self.pushButton_2.clicked.connect(self.run_pers)
        self.pushButton_3.clicked.connect(self.run_pers)
        self.pushButton_5.clicked.connect(self.run_loc)
        self.pushButton_6.clicked.connect(self.run_loc)

    def proof_price(self):
        with open('shop_pers_loc.json') as FAQ:
            data = json.load(FAQ)
        if COUNT_MONEY >= 1000 or data["winter"]["hero"]:
            self.pushButton_2.setEnabled(True)
        else:
            self.pushButton_2.setEnabled(False)
        if COUNT_MONEY >= 2000 or data["winter"]["location"]:
            self.pushButton_5.setEnabled(True)
        else:
            self.pushButton_5.setEnabled(False)
        if COUNT_MONEY >= 5000 or data["desert"]["hero"]:
            self.pushButton_3.setEnabled(True)
        else:
            self.pushButton_3.setEnabled(False)
        if COUNT_MONEY >= 10000 or data["desert"]["location"]:
            self.pushButton_6.setEnabled(True)
        else:
            self.pushButton_6.setEnabled(False)
        # метод сччитывает какую локацию выбрал игрок и ставит её

    # метод который ставит локацию в свою игру если не купленно то покупает не обращайте внимание тут
    # просто очень приторно а так всё интуитивно понятно
    def run_loc(self):
        global background, location_code, location, background_music, COUNT_MONEY, mob_animation
        map_group.empty()
        self.proof_price()
        with open('MONEY.txt', mode='w', encoding='utf-8') as txt:
            if self.sender().objectName()[-1] == '4':
                location = [r'Jungle\jungle.png', r'Jungle\floor.png', r'Jungle\wall.png', range(3, 6)]
                location_code = JUNGLE
                mob_animation = [load_image_t(r'Jungle\jungle_mob.png'),
                                 [load_image_t(r'Jungle\jungle_mob1.png'), load_image_t(r'Jungle\jungle_mob2.png'),
                                  load_image_t(r'Jungle\jungle_mob3.png')],
                                 {'damage': 30, 'health': 180, 'mana': None}]
                background_music.load(r'data\Music\background_1.mp3')
                background_music.play(-1)
                self.pereresovka(['_4', '_5', '_6'], ['yes', 'no', 'no'])
            if self.sender().objectName()[-1] == '5' and self.pushButton_5.isEnabled():
                if self.pushButton_5.text()[0] == 'К':
                    COUNT_MONEY -= 2000
                    txt.write(str(COUNT_MONEY))
                self.update_json('winter', 'location', True)
                self.update_info()
                location = [r'Winter\Winter.png', r'Winter\floor.png', r'Winter\wall.png', range(10, 16)]
                location_code = WINTER
                mob_animation = [load_image_t(r'Winter\winter_mob.png'),
                                 [load_image_t(r'Winter\winter_mob1.png'), load_image_t(r'Winter\winter_mob2.png'),
                                  load_image_t(r'Winter\winter_mob3.png')],
                                 {'damage': 100, 'health': 150, 'mana': None}]
                background_music.load(r'data\Music\background_2.mp3')
                background_music.play(-1)
                self.pereresovka(['_4', '_5', '_6'], ['no', 'yes', 'no'])

            if self.sender().objectName()[-1] == '6' and self.pushButton_6.isEnabled():
                if self.pushButton_6.text()[0] == 'К':
                    COUNT_MONEY -= 10000
                    txt.write(str(COUNT_MONEY))
                self.update_json('desert', 'location', True)
                self.update_info()
                location = [r'Desert\desert.png', r'Desert\floor.png', r'Desert\wall.png', range(50, 81)]
                location_code = DESERT
                mob_animation = [load_image_t(r'Desert\desert_mob.png'),
                                 [load_image_t(r'Desert\desert_mob1.png'), load_image_t(r'Desert\desert_mob2.png'),
                                  load_image_t(r'Desert\desert_mob3.png')], {'damage': 65, 'health': 285, 'mana': None}]
                background_music.load(r'data\Music\background_3.mp3')
                background_music.play(-1)
                self.pereresovka(['_4', '_5', '_6'], ['no', 'no', 'yes'])
        self.test_proof_money()
        background = [pygame.transform.scale(load_image(location[0]), screen.get_size()), location[3]]
        draw_map()

    # метод который берёт информацию из игры и делает нужные парраметры в магазине
    def update_info(self):
        with open('shop_pers_loc.json') as FAQ:
            data = json.load(FAQ)
        # загружаю все локации и скины в магазин как иконки
        self.pixmap_loc = [QPixmap(r'data\Jungle\jungle.png').scaled(267, 150),
                           QPixmap(f'data\Winter\Winter'
                                   f'{"" if data["winter"]["location"] else "1"}.png').scaled(267, 150),
                           QPixmap(f'data\Desert\desert'
                                   f'{"" if data["desert"]["location"] else "1"}.png').scaled(267, 150)]
        self.pixmap_pers = [QPixmap(r'data\Jungle\jungle_mainhero.png'),
                            QPixmap(f'data\Winter\winter_mainhero'
                                    f'{"" if data["winter"]["hero"] else "1"}.png').scaled(145, 235),
                            QPixmap(f'data\Desert\desert_mainhero_for_shop'
                                    f'{"" if data["desert"]["hero"] else "1"}.png').scaled(145, 235)]
        # присваиваю всемю функционал и картинки
        self.label_4.setPixmap(self.pixmap_loc[0])
        self.label_5.setPixmap(self.pixmap_loc[1])
        self.label_6.setPixmap(self.pixmap_loc[2])
        self.label.setPixmap(self.pixmap_pers[0])
        self.label_2.setPixmap(self.pixmap_pers[1])
        self.label_3.setPixmap(self.pixmap_pers[2])
        if data["winter"]["location"]:
            self.pushButton_5.setText('Зима')
        if data["desert"]["location"]:
            self.pushButton_6.setText('Пустыня')
        if data["winter"]["hero"]:
            self.pushButton_2.setText('The white Stripes')
        if data["desert"]["hero"]:
            self.pushButton_3.setText('Guns N Roses')

    # метод который так же обновляет информацию но только в нашей JSON файле
    def update_json(self, loc, obj, boool):
        with open('shop_pers_loc.json') as FAQ:
            data = json.load(FAQ)
        with open('shop_pers_loc.json', 'w') as FAQ:
            data[loc][obj] = boool
            json.dump(data, FAQ)

    # метод который проверяет не пустой ли файл с деньгами
    def test_proof_money(self):
        proof = False
        with open('MONEY.txt', mode='r', encoding='utf-8') as txt:
            if txt.read() == '':
                proof = True
        with open('MONEY.txt', mode='w', encoding='utf-8') as txt:
            if proof:
                txt.write(scrambler(COUNT_MONEY))

    # метод который ставит персонажа который выбрал пользователь
    def run_pers(self):
        global pers, player_shoot_mus, COUNT_MONEY
        with open('MONEY.txt', mode='w', encoding='utf-8') as txt:
            if self.sender().objectName()[-1] == 'n':
                ## начина от сюда
                pers = pygame.transform.scale(load_image(r'Jungle\jungle_mainhero.png'), (int(screen.get_width() / 16),
                                                                                          int(screen.get_height() / 6)))
                player_shoot_mus = pygame.mixer.Sound(r'data\Music\posoh_shoot_green.mp3')
                pers = [pers, pygame.transform.flip(pers, True, False), load_image('Other\\fireball2.png'),
                        pygame.transform.flip(load_image('Other\\fireball2.png'), True, False),
                        player_shoot_mus, {'damage': 90, 'health': 180, 'mana': 200}]
                ##я до сюда можно сделать отдельный метод для всего этого
                self.pereresovka(['', '_2', '_3'], ['yes', 'no', 'no'])

            if self.sender().objectName()[-1] == '2' and self.pushButton_2.isEnabled():
                if self.pushButton_2.text()[0] == 'К':
                    COUNT_MONEY -= 1000
                    txt.write(str(COUNT_MONEY))
                self.update_json('winter', 'hero', True)
                self.update_info()
                pers = pygame.transform.scale(load_image(r'Winter\winter_mainhero.png'), (int(screen.get_width() / 16),
                                                                                          int(screen.get_height() / 6)))
                player_shoot_mus = pygame.mixer.Sound(r'data\Music\posoh_shoot_white.mp3')
                pers = [pers, pygame.transform.flip(pers, True, False), load_image('Other\\fireball1.png'),
                        pygame.transform.flip(load_image('Other\\fireball1.png'), True, False),
                        player_shoot_mus, {'damage': 500, 'health': 45, 'mana': 300}]
                self.pereresovka(['', '_2', '_3'], ['no', 'yes', 'no'])

            if self.sender().objectName()[-1] == '3' and self.pushButton_3.isEnabled():
                if self.pushButton_3.text()[0] == 'К':
                    COUNT_MONEY -= 5000
                    txt.write(str(COUNT_MONEY))
                self.update_json('desert', 'hero', True)
                self.update_info()
                pers = pygame.transform.scale(load_image('Desert\desert_mainhero.png'), (int(screen.get_width() / 10.666),
                                                                                         int(screen.get_height() / 6)))
                player_shoot_mus = pygame.mixer.Sound(r'data\Music\bullet_shoot.mp3')
                pers = [pers, pygame.transform.flip(pers, True, False), load_image('Other\\bullet.png'),
                        pygame.transform.flip(load_image('Other\\bullet.png'), True, False),
                        player_shoot_mus, {'damage': 65, 'health': 500, 'mana': 225}]
                self.pereresovka(['', '_2', '_3'], ['no', 'no', 'yes'])
        music_start_volume(player_shoot_mus)
        self.test_proof_money()

    # метод который перерисовыйвает виджеты в QT
    def pereresovka(self, spisok, spisok_yes_no):
        exec(f'self.label{spisok[0]}.setStyleSheet(self.color_{spisok_yes_no[0]})')
        exec(f'self.label{spisok[1]}.setStyleSheet(self.color_{spisok_yes_no[1]})')
        exec(f'self.label{spisok[2]}.setStyleSheet(self.color_{spisok_yes_no[2]})')
        exec(f'self.pushButton{spisok[0]}.setStyleSheet(self.color_{spisok_yes_no[0]}1)')
        exec(f'self.pushButton{spisok[1]}.setStyleSheet(self.color_{spisok_yes_no[1]}1)')
        exec(f'self.pushButton{spisok[2]}.setStyleSheet(self.color_{spisok_yes_no[2]}1)')


# класс настроек выполняет функцию окошка Настройки
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

    # большой метод проверяет базовые настройки ползовательского решения
    def run(self):
        global background_music, player_shoot_mus
        with open('volume.txt', mode='r', encoding='utf-8') as txt:
            text = txt.read().split()
            self.num_vol_effects, self.num_vol_music = int(text[3]), int(text[2])
        if self.sender().objectName()[-1] == '2':
            self.lcdNumber_2.display(self.horizontalSlider_2.value())
            if self.horizontalSlider_2.value() == 0:
                self.num_vol_effects = 0
                self.label_2.setPixmap(self.pixmap[self.num_vol_effects])
            else:
                if self.horizontalSlider_2.value() >= 99:
                    self.num_vol_effects = 3
                    self.label_2.setPixmap(self.pixmap[self.num_vol_effects])
                else:
                    self.num_vol_effects = int(self.horizontalSlider_2.value() // 33 + 1)
                    self.label_2.setPixmap(self.pixmap[self.num_vol_effects])
        else:
            self.lcdNumber.display(self.horizontalSlider.value())
            if self.horizontalSlider.value() == 0:
                self.num_vol_music = 0
                self.label.setPixmap(self.pixmap[self.num_vol_music])
            else:
                if self.horizontalSlider.value() >= 99:
                    self.num_vol_music = 3
                    self.label.setPixmap(self.pixmap[self.num_vol_music])
                else:
                    self.num_vol_music = int(self.horizontalSlider.value() // 33 + 1)
                    self.label.setPixmap(self.pixmap[self.num_vol_music])

        background_music.set_volume(self.horizontalSlider.value() / 100)
        player_shoot_mus.set_volume(self.horizontalSlider_2.value() / 100)
        with open('volume.txt', mode='w', encoding='utf-8') as txt:
            txt.write(f'{self.horizontalSlider.value()} {self.horizontalSlider_2.value()}'
                      f' {self.num_vol_music} {self.num_vol_effects}')

    # метод загружает эти настройки когда пользователь только запустил игру
    def save_vol(self):
        global background_music, player_shoot_mus
        with open('volume.txt', mode='r', encoding='utf-8') as text:
            text = text.read().split()
            if len(text) <= 2:
                text = ['25', '25', '1', '1']
            self.horizontalSlider.setValue(int(text[0]))
            self.label.setPixmap(self.pixmap[int(text[2])])
            self.label_2.setPixmap(self.pixmap[int(text[3])])
            self.lcdNumber.display(int(text[0]))
            self.horizontalSlider_2.setValue(int(text[1]))
            self.lcdNumber_2.display(int(text[1]))
            background_music.set_volume(self.horizontalSlider.value() / 100)
            player_shoot_mus.set_volume(self.horizontalSlider_2.value() / 100)


# класс нашей пасхалки))) который вызывается на сочетание клавиш AUF
class MyPashalka(QMainWindow, Ui_MainWindow_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Пасхалка')
        self.move = QMovie('data\\Other\\poop.gif')

        self.move.setScaledSize(QSize(800, 440))
        self.label_2.setMovie(self.move)
        self.move.start()


# проверка ошибок
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# фун-ия которая вызывает пасхалку
def qt_start_pashalka():
    app = QApplication(sys.argv)
    ex = MyPashalka()
    ex.show()
    sys.excepthook = except_hook
    app.exec()


# запуск окна Магазина
def qt_start_shop():
    app = QApplication(sys.argv)
    ex = MyShop()
    ex.show()
    sys.excepthook = except_hook
    app.exec()


# запуск окна Настроек
def qt_start_settings():
    app = QApplication(sys.argv)
    ex = MySettings()
    ex.save_vol()
    ex.show()
    sys.excepthook = except_hook
    app.exec()


# отрисовка карты
def draw_map():
    for i in enumerate(location_code):
        map_coords_spisok.clear()
        for j in enumerate(i[1]):
            if j[1] == 'q':
                Map(location[1], location_code, screen.get_width() // len(location_code[0]) * j[0] + 10,
                    screen.get_height() // len(location_code) * i[0] + 10)


# класс отвечающий за отрисовку иконки магазина на холсте
class Shop(pygame.sprite.Sprite):
    def __init__(self):
        super(Shop, self).__init__(sprites_dop, all_sprites)
        self.image = pygame.transform.scale(load_image(r'Other\shop.png'), (int(W_proc * 2.5), int(W_proc * 2.5)))
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() - W_proc * 5
        self.rect.y = 0

    def update(self, pos):
        if self.rect.collidepoint(pos):
            qt_start_shop()


# класс отвечающий за отрисовку иконки настроек на холсте
class Settings(pygame.sprite.Sprite):
    def __init__(self):
        super(Settings, self).__init__(sprites_dop, all_sprites)
        self.image = pygame.transform.scale(load_image(r'Other\settings.png'), (int(W_proc * 2.5), int(W_proc * 2.5)))
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() - W_proc * 2.5
        self.rect.y = 0

    def update(self, pos):
        if self.rect.collidepoint(pos):
            qt_start_settings()


# фун-ия возврата фона из этого файла
def return_background():
    return background


# фун-ия возврата характеристик перса из этого файла
def return_skin():
    return pers


# фун-ия возврата денег из этого файла
def return_money(n):
    global COUNT_MONEY
    COUNT_MONEY += n
    return COUNT_MONEY


# фун-ия возврата хар-ик моба из этого файла
def return_mob():
    return mob_animation


# класс который зависит от метода draw_map
class Map(pygame.sprite.Sprite):
    def __init__(self, image, location_code, x, y):
        global map_coords_spisok
        super(Map, self).__init__(map_group, all_sprites)
        self.image = pygame.transform.scale(load_image(image),
                                            (screen.get_width() // len(location_code[0]),
                                             (screen.get_height() // len(location_code))))
        map_coords_spisok.append(y)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x - 10
        self.rect.y = y
