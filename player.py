#import game
import pygame
import gamelose
import pipe
#var
py = 0
px = 150 + 32
img = pygame.image.load("player.png")
#désiiner le joueur
def wirte(screen,bool):
    global py
    if not bool :
        screen.blit(img,(px,py))
#si le joueur est mord
def lose():
    if pipe.isgameover:
        gamelose.retry()