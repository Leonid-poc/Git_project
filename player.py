from setting import *
import pygame
import math

class Player:
    def __init__(self, sprites):
        self.x, self.y = player_pos
        self.sprites = sprites
        self.angle = player_angle
        self.num = 10
        self.time = 0

    def __proof(self):
        self.time += 1
        if self.time % 20 == 0:
            self.num = -self.num
            self.sprites.rect.y -= self.num
        if self.time == 1000:
            self.time = 0

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
            self.__proof()
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
            self.__proof()
        if keys[pygame.K_a]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
            self.__proof()
        if keys[pygame.K_d]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a
            self.__proof()
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
            self.__proof()
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
            self.__proof()