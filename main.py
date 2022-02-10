import pygame
from setting import *

display = pygame.display.set_mode(width, height)
clock = pygame.time.clock()

while True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    display.fill((0, 0, 0))

    clock.tick()
    pygame.display.flip()