import pygame.display
import pygame.image 
import pygame.event
import pygame.font

from classes.case import Case
from pygame.locals import *

class Plateau:
    LIGNE_MAX = 15
    HAUTEUR_MAX = 15
    WIDTH_CASE = 1
    HEIGHT_CASE = 1
    LARGEUR_SPRITE = 40



    def __init__(self, fenetre):
        self.fenetre = fenetre
        fp = open("lab.txt","r")
        self.MATRICE = []
        for numLigne, ligne in enumerate(fp):
            LIGNE = []
            for numColonne, element in enumerate(ligne):
                coin_bas_gauche = Case(element)
                LIGNE.append(coin_bas_gauche)

            self.MATRICE.append(LIGNE)


    def __repr__(self):
        I= 0
        tab = ""
        for LIGNE in self.MATRICE:
            for element in LIGNE:
                tab = tab + element.attribut
            tab = tab + "\n"
        return tab







    def afficher(self):

        mur = pygame.image.load("ressource/caseRouge.png").convert()
        mur = pygame.transform.scale(mur, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))

        sol = pygame.image.load("ressource/sol.png").convert()
        sol = pygame.transform.scale(sol, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))
       
        aiguille = pygame.image.load("ressource/aiguille.png").convert_alpha()
        aiguille = pygame.transform.scale(aiguille, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))

        ether = pygame.image.load("ressource/ether.png").convert()
        ether = pygame.transform.scale(ether, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))
        ether.set_colorkey((0, 0, 0))

        tube = pygame.image.load("ressource/tube_plastique.png").convert()
        tube = pygame.transform.scale(tube, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))
        tube.set_colorkey((255, 255, 255))

        MG = pygame.image.load("ressource/MacGyver.png").convert_alpha()
        MG = pygame.transform.scale(MG, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))

        TinyTina = pygame.image.load("ressource/Gardien.png").convert_alpha()
        TinyTina = pygame.transform.scale(TinyTina, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))

        butin = pygame.image.load("ressource/butin.png").convert_alpha()
        butin = pygame.transform.scale(butin, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))

        diable = pygame.image.load("ressource/diable.png").convert_alpha()
        diable = pygame.transform.scale(diable, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))
        
        #On parcourt la liste du niveau
        num_ligne = 0
        for ligne in self.MATRICE:
            #On parcourt les listes de lignes
            num_case = 0
            for sprite in ligne:
                #On calcule la position réelle en pixels
                x = num_case * self.LARGEUR_SPRITE
                y = num_ligne * self.LARGEUR_SPRITE
                


# debugage


                #print("X"+sprite.attribut+"X")
          
                if sprite.attribut == 'o':          #m = Mur
                    self.fenetre.blit(sol, (x,y))
                if sprite.attribut == 'I':          #m = Mur
                    self.fenetre.blit(mur, (x,y))
                if sprite.attribut == '1':        #d = Départ
                    self.fenetre.blit(sol, (x,y))
                    self.fenetre.blit(aiguille, (x,y))
                if sprite.attribut == '2':        #a = Arrivée
                    self.fenetre.blit(sol, (x,y))
                    self.fenetre.blit(ether, (x,y))
                if sprite.attribut == '3':
                    self.fenetre.blit(sol, (x,y))
                    self.fenetre.blit(tube, (x,y))
                if sprite.attribut == 'H':
                    self.fenetre.blit(sol, (x,y))
                    self.fenetre.blit(MG, (x,y))
                if sprite.attribut == 'M':
                    self.fenetre.blit(sol, (x,y))
                    self.fenetre.blit(TinyTina, (x,y))
                if sprite.attribut == 'B':
                    self.fenetre.blit(sol, (x,y))
                    self.fenetre.blit(butin, (x,y))
                if sprite.attribut == 'd':
                    self.fenetre.blit(sol, (x,y))
                    self.fenetre.blit(diable, (x,y))

                num_case += 1
            num_ligne += 1


    def write_case(self, posX, posY, newAttribut):
        self.MATRICE[posX][posY].attribut = newAttribut 


# retourne 0 si la case est vide1si c'est un objet2si c'est tinaTurner
    def returnContains(self, x, y):
        element = self.MATRICE[x][y]
        if element.attribut == "o":
            return "vide"
        if element.attribut == "1" or element.attribut == "2" or element.attribut =="3":
            return "seringue"
        if element.attribut == "M":
            return "Tina"
        if element.attribut == "I":
            return "mur"
        if element.attribut == "B":
            return "butin"
        if element.attribut == "d":
            return "diable"
        else:
            print("?????????????????????????????????????????????????")

    def isAllowed(self, x, y):
        if x<15 and x>=0 and y<15 and y>=0 and self.returnContains(x,y)!="mur" and self.returnContains(x,y)!="diable":
            return 1
        else:
            return 0 

    def victory (self, victoire):
        font = pygame.font.SysFont("comicsansms",35)
        font_espace = pygame.font.SysFont("comicsansms",18)
        font_victoire = font.render("victoire", True, (0, 255, 0))
        font_defaite = font.render("defaite", True, (255, 0, 0))
        space = font_espace.render("Appuyez sur espace pour revenir au menu.", True, (0, 0, 255))
        if victoire == True:
            self.fenetre.blit(font_victoire,(630,250))
            self.fenetre.blit(space,(610,350))
            pygame.display.flip()
            num_ligne = 0
            for ligne in self.MATRICE:
                #On parcourt les listes de lignes
                num_case = 0
                for sprite in ligne:
                    #On calcule la position réelle en pixels
                    x = num_case * self.LARGEUR_SPRITE
                    y = num_ligne * self.LARGEUR_SPRITE
                    if sprite.attribut == 'o':          #m = Mur
                        sprite.attribut = 'B'
        if victoire == False:
            self.fenetre.blit(font_defaite,(640,250))
            self.fenetre.blit(space,(610,350))
            pygame.display.flip()
            num_ligne = 0
            for ligne in self.MATRICE:
                #On parcourt les listes de lignes
                num_case = 0
                for sprite in ligne:
                    #On calcule la position réelle en pixels
                    x = num_case * self.LARGEUR_SPRITE
                    y = num_ligne * self.LARGEUR_SPRITE
                    if sprite.attribut == 'o':          #m = Mur
                        sprite.attribut = 'd'
        continuerVictoire = True

        while continuerVictoire:
            for event in pygame.event.get():
                if event.type == KEYDOWN:   
                    if event.key == K_SPACE:
                        continuerVictoire = False
