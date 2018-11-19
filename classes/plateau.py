from random import *
import pygame.display
import pygame.image 
import pygame.event
from classes.case import Case


class Plateau:
    LIGNE_MAX = 15
    HAUTEUR_MAX = 15
    WIDTH_CASE = 1
    HEIGHT_CASE = 1
    LARGEUR_SPRITE = 45



    def __init__(self):
        fp = open("lab.txt","r")
        self.MATRICE = []
        for numLigne, ligne in enumerate(fp):
            LIGNE = []
            for numColonne, element in enumerate(ligne):
                coin_bas_gauche = Case(element)
                LIGNE.append(coin_bas_gauche)

            self.MATRICE.append(LIGNE)

        # for morceau in ["1","2","3"]:
        #     IsObjectPosition= False
        #     while not IsObjectPosition:
        #         INtX= randint(0,14)
        #         INtY= randint(0,14)

        #         case1 = Case(morceau)
        #         if self.MATRICE[INtX][INtY].attribut == "o":
        #             self.MATRICE[INtX][INtY] = case1
        #             IsObjectPosition = True
        #         else:
        #             print(self.MATRICE[INtX][INtY])




    def __repr__(self):
        I= 0
        tab = ""
        for LIGNE in self.MATRICE:
            for element in LIGNE:
                tab = tab + element.attribut
            tab = tab + "\n"
        return tab







    def afficher(self, fenetre):

        mur = pygame.image.load("ressource/caseRouge.png").convert()
        mur = pygame.transform.scale(mur, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))

        sol = pygame.image.load("ressource/sol.png").convert()
        sol = pygame.transform.scale(sol, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))
       
        aiguille = pygame.image.load("ressource/aiguille.png").convert_alpha()
        aiguille = pygame.transform.scale(aiguille, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))

        ether = pygame.image.load("ressource/ether.png").convert_alpha()
        ether = pygame.transform.scale(ether, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))

        tube = pygame.image.load("ressource/tube_plastique.png").convert_alpha()
        tube = pygame.transform.scale(tube, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))

        MG = pygame.image.load("ressource/MacGyver.png").convert_alpha()
        MG = pygame.transform.scale(MG, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))

        TinyTina = pygame.image.load("ressource/Gardien.png").convert_alpha()
        TinyTina = pygame.transform.scale(TinyTina, (self.LARGEUR_SPRITE, self.LARGEUR_SPRITE))

        
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
                    fenetre.blit(sol, (x,y))
                if sprite.attribut == 'I':          #m = Mur
                    fenetre.blit(mur, (x,y))
                if sprite.attribut == '1':        #d = Départ
                    fenetre.blit(sol, (x,y))
                    fenetre.blit(aiguille, (x,y))
                if sprite.attribut == '2':        #a = Arrivée
                    fenetre.blit(sol, (x,y))
                    fenetre.blit(ether, (x,y))
                if sprite.attribut == '3':
                    fenetre.blit(sol, (x,y))
                    fenetre.blit(tube, (x,y))
                if sprite.attribut == 'H':
                    fenetre.blit(sol, (x,y))
                    fenetre.blit(MG, (x,y))
                if sprite.attribut == 'M':
                    fenetre.blit(sol, (x,y))
                    fenetre.blit(TinyTina, (x,y))


                num_case += 1
            num_ligne += 1


    def write_case(self, posX, posY, newAttribut):
        self.MATRICE[posX][posY].attribut = newAttribut 


# retourne 0 si la case est vide1si c'est un objet2si c'est tinaTurner
    def returnContains(self, x, y):
        element = self.MATRICE[x][y]
        if element.attribut == "o":
            return 0
        if element.attribut == "1" or element.attribut == "2" or element.attribut =="3":
            return 1
        if element.attribut == "M":
            return 2
        if element.attribut == "I":
            return 3
        else:
            print("?????????????????????????????????????????????????")

    def isAllowed(self, x, y):
        if x<15 and x>=0 and y<15 and y>=0 and self.returnContains(x,y)!=3:
            return 1
        else:
            return 0 