import sys

import pygame, os
import pymunk.pygame_util
from PyQt5.QtWidgets import QApplication


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


class Player():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        # Основные переменные
        self.RES = self.WIDTH, self.HEIGHT = 1920, 1080
        self.FPS = 60
        self.STEP = 50
        self.JUMP = 250
        # Инициализация Pymunk, создание основынх переменных (поверхность, переопределение координат для Pymunk)
        pymunk.pygame_util.positive_y_is_up = False
        self.surface = pygame.display.set_mode(self.RES)
        self.draw_options = pymunk.pygame_util.DrawOptions(self.surface)
        self.space = pymunk.Space()
        self.space.gravity = 0, 2000

        # Инициализация основных игровых объектов
        self.ball_mass, self.ball_radius = 10, 70

        self.down_segment_shape = pymunk.Segment(self.space.static_body, (-100, self.HEIGHT),
                                                 (self.WIDTH + 100, self.HEIGHT), 35)
        self.down_segment_shape.elasticity = 0.2
        self.space.add(self.down_segment_shape)

        # Инициализация персонажа
        self.pers_mass, self.pers_size = 5, (43, 63)
        self.pers_moment = pymunk.moment_for_box(self.pers_mass, self.pers_size)
        self.pers_body = pymunk.Body(self.pers_mass, self.pers_moment)
        self.pers_body.position = 100, 935
        self.pers_shape = pymunk.Poly.create_box(self.pers_body, self.pers_size)
        self.pers_shape.elasticity, self.pers_shape.friction = 0.1, 1.0
        self.space.add(self.pers_body, self.pers_shape)

    def create_ball(self, space, pos):
        self.ball_moment = pymunk.moment_for_circle(self.ball_mass, 0, self.ball_radius)
        self.ball_body = pymunk.Body(self.ball_mass, self.ball_moment)
        self.ball_body.position = pos
        self.ball_shape = pymunk.Circle(self.ball_body, self.ball_radius)
        self.ball_shape.elasticity = 0.8
        self.ball_shape.friction = 0.5
        space.add(self.ball_body, self.ball_shape)
        return self.ball_body
        # Функция для создания шаров

    def check_position(self, pers_body, symbol):
        # Функция для проверки выхода за пределы мира и передвижения
        x, y = pers_body.position

        if symbol == "+":
            if x + self.STEP <= self.WIDTH:
                return (x + self.STEP, y)
            else:
                return (self.WIDTH, y)
        if symbol == "J":
            if y - self.JUMP >= 0:
                return (x, y - self.JUMP)
            else:
                return (x, 0)
        if symbol == "-":
            if x - self.STEP >= 0:
                return (x - self.STEP, y)
            else:
                return (0, y)

    def for_start(self):
        # Функция для старта программы, определение управления персонажем и миром
        background = load_image('dshungl.png')
        while True:
            KEYS = pygame.key.get_pressed()
            self.surface.blit(pygame.transform.scale(background,
                                                     (self.surface.get_width(), self.surface.get_height())), (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        Player.create_ball(self, self.space, event.pos)

            if KEYS[pygame.K_F10]:
                exit()
            if KEYS[pygame.K_a]:
                self.pers_body.position = Player.check_position(self, self.pers_body, "-")
            if KEYS[pygame.K_d]:
                self.pers_body.position = Player.check_position(self, self.pers_body, "+")
            if KEYS[pygame.K_SPACE]:
                self.pers_body.position = Player.check_position(self, self.pers_body, "J")

            self.space.step(1 / self.FPS)
            self.space.debug_draw(self.draw_options)

            pygame.display.flip()
            self.clock.tick(self.FPS)

    def main(self):
        app = QApplication(sys.argv)
        ex = Player()
        ex.for_start()
        sys.excepthook = except_hook
        app.exec()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    Player.main(Player)
