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

# Les differentes classes utilisé sont dans classes la structure du niveau est dans 
# lab.txt

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

    #plateau.seringue()

    plateau.afficher(window)

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
                    #position_hero = position_hero.move(0,10)
                    hero.mouvement("bas")
                if event.key == K_UP:
                    hero.mouvement("haut")
                    #position_hero = position_hero.move(0,-10)
                if event.key == K_RIGHT:
                    hero.mouvement("droite")
                    #position_hero = position_hero.move(10,0)
                if event.key == K_LEFT:
                    hero.mouvement("gauche")
                    #position_hero = position_hero.move(-10,0)
        plateau.afficher(window)
        pygame.display.flip()


# Jeu en ligne de commande


    # whileI!= 'quit':
    #     #print(plateau.MATRICE)
    #     print(plateau)
    #     #plateau.display()
    #     print('')
    #     print('***')
    #     print(hero)
    #     print('Utilisez QZDS pour bouger le hero. Rentrez quit pour quitter')
    #    I= input('Tapez encore qeqchose svp.')
    #     print('***')
    #     print('')
    #     if(i=='z'):
    #        I= hero.mouvement(3)  
    #     if(i=='s'):
    #        I= hero.mouvement(2)
    #     if(i=='d'):
    #        I= hero.mouvement(0)
    #     if(i=='q'):
    #        I= hero.mouvement(1)
    #     #i = hero.isWin();



main()