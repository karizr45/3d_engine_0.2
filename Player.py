from math import *
import pygame

from setting import *
##-------------------------------------PLayer-------------------------------------##
class Player:
    def __init__(self):
        self.x = half_width
        self.y = half_height
        self.angle = 0
        self.delta = 0
    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.angle -= 0.3 * self.delta * 8
        if key[pygame.K_RIGHT]:
            self.angle += 0.3 * self.delta * 8