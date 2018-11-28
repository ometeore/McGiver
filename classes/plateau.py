""" Ce module gere le plateau, sa structure et l'affichage des elements qu'il contient"""
import pygame.display
import pygame.image
import pygame.event
import pygame.font

from classes.case import Case
from pygame.locals import KEYDOWN, K_SPACE

class Plateau:
    """ la classe plateau """
    LIGNE_MAX = 15
    HAUTEUR_MAX = 15
    LARGEUR_SPRITE = 40



    def __init__(self, fenetre):
        """ init du plateau """
        self.fenetre = fenetre
        fichier_niveau = open("lab.txt", "r")
        self.matrice = []
        for num_ligne, ligne_temp in enumerate(fichier_niveau):
            ligne = []
            for num_colonne, element in enumerate(ligne_temp):
                coin_bas_gauche = Case(element)
                ligne.append(coin_bas_gauche)
            self.matrice.append(ligne)


    def __repr__(self):
        """ repr du plateau """
        tab = ""
        for ligne_temp in self.matrice:
            for element in ligne_temp:
                tab = tab + element.attribut
            tab = tab + "\n"
        return tab

    def afficher(self, hero):
        """ Affichage des éléments par pygame en récupérant les positions dans matrice """
        self.fenetre.fill((255, 255, 255))
        
        mur = pygame.image.load("ressource/caseRouge.png").convert()
        mur = pygame.transform.scale(mur, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))

        sol = pygame.image.load("ressource/sol.png").convert()
        sol = pygame.transform.scale(sol, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))

        aiguille = pygame.image.load("ressource/aiguille.png").convert_alpha()
        aiguille = pygame.transform.scale(aiguille, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))

        ether = pygame.image.load("ressource/ether.png").convert()
        ether = pygame.transform.scale(ether, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))

        tube = pygame.image.load("ressource/tube_plastique.png").convert()
        tube = pygame.transform.scale(tube, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))
        tube.set_colorkey((255, 255, 255))

        mac_giver = pygame.image.load("ressource/MacGyver.png").convert_alpha()
        mac_giver = pygame.transform.scale(mac_giver, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))

        tiny_tina = pygame.image.load("ressource/Gardien.png").convert_alpha()
        tiny_tina = pygame.transform.scale(tiny_tina, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))

        butin = pygame.image.load("ressource/butin.png").convert_alpha()
        butin = pygame.transform.scale(butin, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))

        diable = pygame.image.load("ressource/diable.png").convert_alpha()
        diable = pygame.transform.scale(diable, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))

        font = pygame.font.SysFont("comicsansms", 35)
        #armes = print(hero)
        armes = "le hero a : {} armes.".format(hero.armes)
        nbr_armes_hero = font.render(armes, True, (0, 255, 0))
        self.fenetre.blit(nbr_armes_hero, (610, 150))

        #On parcourt la liste du niveau
        num_ligne = 0
        for ligne in self.matrice:
            #On parcourt les listes de lignes
            num_case = 0
            for sprite in ligne:
                #On calcule la position réelle en pixels
                x = num_case * self.LARGEUR_SPRITE
                y = num_ligne * self.LARGEUR_SPRITE

                #print("X"+sprite.attribut+"X")

                if sprite.attribut == 'o':          #m = Mur
                    self.fenetre.blit(sol, (x, y))
                if sprite.attribut == 'I':          #m = Mur
                    self.fenetre.blit(mur, (x, y))
                if sprite.attribut == '1':        #d = Départ
                    self.fenetre.blit(sol, (x, y))
                    self.fenetre.blit(aiguille, (x, y))
                if sprite.attribut == '2':        #a = Arrivée
                    self.fenetre.blit(sol, (x, y))
                    self.fenetre.blit(ether, (x, y))
                if sprite.attribut == '3':
                    self.fenetre.blit(sol, (x, y))
                    self.fenetre.blit(tube, (x, y))
                if sprite.attribut == 'H':
                    self.fenetre.blit(sol, (x, y))
                    self.fenetre.blit(mac_giver, (x, y))
                if sprite.attribut == 'M':
                    self.fenetre.blit(sol, (x, y))
                    self.fenetre.blit(tiny_tina, (x, y))
                if sprite.attribut == 'B':
                    self.fenetre.blit(sol, (x, y))
                    self.fenetre.blit(butin, (x, y))
                if sprite.attribut == 'd':
                    self.fenetre.blit(sol, (x, y))
                    self.fenetre.blit(diable, (x, y))

                num_case += 1
            num_ligne += 1


    def write_case(self, position_x, position_y, nouvel_atribut):
        """ ecrire l'attribut a position_x position_y """
        self.matrice[position_x][position_y].attribut = nouvel_atribut


    def return_contains(self, x, y):
        """ retourne la catégorie de l'attribut objet a la case x,y """
        element = self.matrice[x][y]
        if element.attribut == "o":
            return "vide"
        if element.attribut == "1" or element.attribut == "2" or element.attribut == "3":
            return "seringue"
        if element.attribut == "M":
            return "Tina"
        if element.attribut == "I":
            return "mur"
        if element.attribut == "B":
            return "butin"
        if element.attribut == "d":
            return "diable"

    def is_allowed(self, x, y):
        """ empeche les mouvements sur les murs et au dela des limites du plateau """
        if x < 15 and x >= 0 and y < 15 and y >= 0 and self.return_contains(x, y) != "mur" and self.return_contains(x, y) != "diable":
            return 1
        return 0

    def victory(self, victoire):
        """ affiche l'écran de victoire ou de defaite """
        font = pygame.font.SysFont("comicsansms", 35)
        font_espace = pygame.font.SysFont("comicsansms", 18)
        font_victoire = font.render("victoire", True, (0, 255, 0))
        font_defaite = font.render("defaite", True, (255, 0, 0))
        space = font_espace.render("Appuyez sur espace pour revenir au menu.", True, (0, 0, 255))
        escape = font_espace.render("Ou sur echap pour quitter", True, (0, 0, 255))
        if victoire:
            self.fenetre.blit(font_victoire, (630, 250))
            self.fenetre.blit(space, (610, 350))
            self.fenetre.blit(escape, (610, 450))
            pygame.display.flip()
            num_ligne = 0
            for ligne in self.matrice:
                #On parcourt les listes de lignes
                num_case = 0
                for sprite in ligne:
                    if sprite.attribut == 'o':          #m = Mur
                        sprite.attribut = 'B'
        if not victoire:
            self.fenetre.blit(font_defaite, (640, 250))
            self.fenetre.blit(space, (610, 350))
            self.fenetre.blit(escape, (610, 450))
            pygame.display.flip()
            num_ligne = 0
            for ligne in self.matrice:
                #On parcourt les listes de lignes
                num_case = 0
                for sprite in ligne:
                    if sprite.attribut == 'o':          #m = Mur
                        sprite.attribut = 'd'
        continuer_victoire = True

        while continuer_victoire:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        continuer_victoire = False
