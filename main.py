#pygame
import pygame
import player
import gamelose
import palyerjump
import bg
import pipe
import pipevar

#créer pygame
pygame.init()



#screen set
screen = pygame.display.set_mode((600,300))
pygame.display.set_caption(("flappy bird"))

#game loop
game = True
while game:
    pipe.birdpipe()
    pipevar.pipe()
    player.py += 0.5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        #jump
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               palyerjump.jump()
               #retry if dead
               player.lose()
    #screen refrech
    screen.fill((0,0,0))
    bg.bg(screen,"bg.png","black.png",pipe.isgameover)
    #player whrite
    player.wirte(screen,pipe.isgameover)
    #gamelose if player no in the screen
    gamelose.gameover(screen,pipe.isgameover)
    pipe.pipe(pipevar.pipex,pipevar.pipey,pipe.isgameover,screen)
    pygame.display.update()
