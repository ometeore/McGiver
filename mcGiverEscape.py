import pygame.display
import pygame.event
import pygame.image 
import pygame.font
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


    pygame.init()
    window = pygame.display.set_mode((1000,600),RESIZABLE)

    continuerAcceuil = True
    while continuerAcceuil:

        acceuil = pygame.image.load("ressource/MacAcceuil.jpeg").convert()
        acceuil = pygame.transform.scale(acceuil, (1000, 600))

        window.blit(acceuil, (0,0))
        font_titre = pygame.font.SysFont("comicsansms", 55)
        font_texte = pygame.font.SysFont("comicsansms",35)
        titre = font_titre.render("Mac Giver Escape", True, (255, 255, 255))
        but = font_texte.render("Ramassez vos armes et récupérez votre or.", True, (255,255,255))
        space = font_texte.render("Appuyez sur espace pour commencer.", True, (255, 255, 255))
        window.blit(titre,(250,50))
        window.blit(but,(180,250))
        window.blit(space,(230,450))
        pygame.display.flip()

        pygame.time.Clock().tick(30)
        continuerJeu = False
        for event in pygame.event.get():   
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:     
                continuerAcceuil = False
                continuerJeu = False  
            elif event.type == KEYDOWN:   
                if event.key == K_SPACE:

                    window.fill((255, 255, 255))
                    
                    plateau = Plateau(window)
                    print("le plateau a été crée")
                    hero = Hero(plateau)
                    print("le hero a été crée")
                    Seringue(plateau)
                    print("la seringue a été crée")
                    plateau.afficher()
                    print("premier affichage plateau")
                    pygame.display.flip()
                    pygame.key.set_repeat(400, 30)
                    
                    continuerJeu = True


        while continuerJeu:
            for event in pygame.event.get():  
                if event.type == QUIT:  
                    continuerJeu = False   
                if event.type == KEYDOWN:
                    if event.key == K_DOWN: 
                        continuerJeu = hero.mouvement("bas")
                    if event.key == K_UP:
                        continuerJeu = hero.mouvement("haut")
                    if event.key == K_RIGHT:
                        continuerJeu = hero.mouvement("droite")
                    if event.key == K_LEFT:
                        continuerJeu = hero.mouvement("gauche")
                    if event.key == K_ESCAPE:
                        continuerJeu = False
            plateau.afficher()
            pygame.display.flip()

main()