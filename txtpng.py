import pygame

#afficher une image
def png(x,y,img,bool,screen):
    if bool:
        screen.blit(pygame.image.load(img),(x,y))
