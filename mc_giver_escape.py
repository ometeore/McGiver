""" Ce module contient le main, ici est gere certaines reaction de l'utilisateur ainsi
        que certaines parties de l'affichage"""
import pygame.display
import pygame.event
import pygame.image
import pygame.font
from pygame.locals import RESIZABLE, QUIT, KEYDOWN, K_ESCAPE, K_DOWN, K_UP, K_RIGHT, K_LEFT, K_SPACE
from classes.plateau import Plateau
from classes.hero import Hero
from classes.seringue import Seringue

#####################################################################################
############################LA GRANDE ECHAPPE DE MC GIVER############################
#####################################################################################



def main():
    """ Ceci est le main"""
    pygame.init()
    window = pygame.display.set_mode((1000, 600), RESIZABLE)

    continuer_acceuil = True
    while continuer_acceuil:

        acceuil = pygame.image.load("ressource/MacAcceuil.jpeg").convert()
        acceuil = pygame.transform.scale(acceuil, (1000, 600))

        window.blit(acceuil, (0, 0))
        font_titre = pygame.font.SysFont("comicsansms", 55)
        font_texte = pygame.font.SysFont("comicsansms", 35)
        titre = font_titre.render("Mac Giver Escape", True, (255, 255, 255))
        but = font_texte.render("Ramassez vos armes et récupérez votre or.", True, (255, 255, 255))
        space = font_texte.render("Appuyez sur espace pour commencer.", True, (255, 255, 255))
        window.blit(titre, (250, 50))
        window.blit(but, (180, 250))
        window.blit(space, (230, 450))
        pygame.display.flip()

        pygame.time.Clock().tick(30)
        continuer_jeu = False
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                print("fini propre")
                continuer_acceuil = False
                continuer_jeu = False
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:

                    plateau = Plateau(window)
                    print("le plateau a été crée")
                    hero = Hero(plateau)
                    print("le hero a été crée")
                    Seringue(plateau)
                    print("la seringue a été crée")
                    plateau.afficher(hero)
                    print("premier affichage plateau")
                    pygame.display.flip()
                    pygame.key.set_repeat(400, 30)

                    continuer_jeu = True


        while continuer_jeu:
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer_jeu = False
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        continuer_jeu = hero.mouvement("bas")
                    if event.key == K_UP:
                        continuer_jeu = hero.mouvement("haut")
                    if event.key == K_RIGHT:
                        continuer_jeu = hero.mouvement("droite")
                    if event.key == K_LEFT:
                        continuer_jeu = hero.mouvement("gauche")
                    if event.key == K_ESCAPE:
                        continuer_jeu = False
            plateau.afficher(hero)
            pygame.display.flip()

main()
