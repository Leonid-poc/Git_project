import sys, os, pygame
from PyQt5.QtWidgets import QApplication, QMainWindow
from shop import Ui_MainWindow

pygame.init()

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
    sys.exit(app.exec_())

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

while True:
    screen.fill('black')
    KEYS = pygame.key.get_pressed()
    for i in pygame.event.get():
        if i.type == pygame.QUIT or KEYS[pygame.K_c]:
            sys.exit()

    pygame.display.flip()