import pygame
import player
import pipevar
isgameover=False

def pipe(x,y,bool,screen):
    if not bool:
        screen.blit(pygame.image.load("pipe.png"),(x,y))
        screen.blit(pygame.image.load("piper.png"),(x,y - y))
    else:
        pipevar.pipex = 0
def birdpipe():
    global isgameover
    if player.py >= 300:
        isgameover=True
    if pipevar.pipex <= player.px + 32 and player.px <= pipevar.pipex + 64 and pipevar.pipey <= player.py + 32 and player.py <= pipevar.pipey + 100:
        isgameover=True
    if pipevar.pipex <= player.px + 32 and player.px <= pipevar.pipex + 64 and 0 <= player.py + 32 and player.py <= 0 + 100:
        isgameover=True
  
