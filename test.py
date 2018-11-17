# from PIL import Image
# bidule = Image.open("corto.jpg")
# trublion = Image.open("lenna.png")
# pommedAmour = bidule + trublion
# pommedAmour.show()
# # trublion.show()

import pygame.display
import pygame.image 
import pygame.event
from pygame.locals import *
pygame.init()

window = pygame.display.set_mode((1000,1000),RESIZABLE)
background = pygame.image.load("lenna.png").convert()
position_background = background.get_rect()

window.blit(background, position_background)

pygame.display.flip()
pygame.key.set_repeat(400, 30)

continuer = 1

while continuer:
    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            continuer = 0    #On arrête la boucle
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                print("Espace")
            if event.key == K_RETURN:
                print("Entrée")
            if event.key == K_DOWN: 
                position_background = position_background.move(0,10)
            if event.key == K_UP: 
                position_background = position_background.move(0,-10)
            if event.key == K_RIGHT: 
                position_background = position_background.move(10,0)
            if event.key == K_LEFT: 
                position_background = position_background.move(-10,0)


    window.blit(background, position_background)
    pygame.display.flip()