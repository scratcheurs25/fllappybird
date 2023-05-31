import pygame

def bg(screen,bg,bgb,bool):
    if bool:
        screen.blit(pygame.image.load(bgb),(0,0))
    else:
          screen.blit(pygame.image.load(bg),(0,0))