import pygame
from setting import *
from Player import Player
from math import *
from functions import *

display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
player = Player()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    player.delta = delta_time()
    player.move()
    display.fill((0, 0, 0))

    pygame.draw.circle(display, pygame.Color("green"), (player.x, player.y), 10)

    ray_size = width
    toX, toY = ray_size * cos(player.angle) + player.x, ray_size * sin(player.angle) + player.y
    pygame.draw.line(display, pygame.Color("green"), (player.x, player.y), (toX, toY))
    clock.tick(0)
    pygame.display.flip()