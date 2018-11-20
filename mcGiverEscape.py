from random import *
import pygame.display
import pygame.image 
import pygame.event
from classes.case import Case
from classes.plateau import Plateau
from classes.hero import Hero
from classes.seringue import Seringue
from pygame.locals import *


#####################################################################################
############################LA GRANDE ECHAPPE DE MC GIVER############################
#####################################################################################


#####################################################################################
############################           LE MAIN           ############################
#####################################################################################


def main ():
    plateau = Plateau()
    hero = Hero(plateau)
    seringue = Seringue(plateau)
    # tinyTina = tinaTurner(plateau)

    pygame.init()
    window = pygame.display.set_mode((1000,1000),RESIZABLE)

    plateau.afficher(window)

    pygame.display.flip()
    pygame.key.set_repeat(400, 30)

    continuer = True

    while continuer:
        for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
            if event.type == QUIT:     #Si un de ces événements est de type QUIT
                continuer = False    #On arrête la boucle
            if event.type == KEYDOWN:
                if event.key == K_DOWN: 
                    hero.mouvement("bas")
                if event.key == K_UP:
                    hero.mouvement("haut")
                if event.key == K_RIGHT:
                    hero.mouvement("droite")
                if event.key == K_LEFT:
                    hero.mouvement("gauche")
        plateau.afficher(window)
        pygame.display.flip()

main()