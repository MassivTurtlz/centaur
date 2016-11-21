import pygame, sys
from pygame.locals import *
import tile_config as t


tilemap = [[t.GRASS for w in range(t.MAPWIDTH)] for h in range(t.MAPHEIGHT)]

colours = {t.GRASS: t.GREEN}

pygame.init()
CENTAUR = pygame.display.set_mode((t.MAPWIDTH*t.TILESIZE, t.MAPHEIGHT*t.TILESIZE +50))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
                sys.exit()
    for row in range(t.MAPHEIGHT):
        for column in range(t.MAPWIDTH):
            pygame.draw.rect(CENTAUR, colours[tilemap[row][column]], (column*t.TILESIZE, row*t.TILESIZE,t.TILESIZE,t.TILESIZE))
    pygame.display.update()