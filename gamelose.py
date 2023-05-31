import pygame
import player
import txtpng
import pipevar
import pipe

#afficher si mord
def gameover(screen,bool):
    if bool:
        screen.blit(pygame.image.load("gameover.png"),(155,50))
        txtpng.png(155,50,"retry.png",True,screen)
def retry():
    player.py = 0
    pipevar.pipex = 664
    pipe.isgameover = False
