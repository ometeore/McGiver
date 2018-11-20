from random import *
import pygame.display
import pygame.image 
import pygame.event
from classes.case import Case
from classes.plateau import Plateau



class Hero:

    def __init__(self, plateau):
        self.y = randint(0,14)
        self.x = randint(0,14)
        self.plato = plateau
        self.armes = 0

        colision = 0 

        IsObjectPosition= False
        while not IsObjectPosition:
            case1 = Case("H")
            if self.plato.MATRICE[self.x][self.y].attribut == "o":
                self.plato.MATRICE[self.x][self.y] = case1
                IsObjectPosition = True
                print("Le hero a eu {} collisions.".format(colision))
            else:
                colision = colision + 1  
                print(colision)       # IsObjectPosition= False





    def __repr__(self):
        return "votre hero se trouve:ligne-> {},colonne-> {} et il possède {} morceaux de la seringues".format(self.x, self.y, self.armes)
    

    def mouvement(self, direction): 

        posXOrigine = self.x
        posYOrigine = self.y

        self.plato.write_case(posXOrigine, posYOrigine, 'o')

        if direction == "droite":
            self.y = self.y + 1
        if direction == "gauche":
            self.y = self.y -1
        if direction == "bas":
            self.x = self.x + 1
        if direction == "haut":
            self.x = self.x - 1

        if self.plato.isAllowed(self.x,self.y):
            if self.plato.returnContains(self.x,self.y) == "vide":
                pass
            if self.plato.returnContains(self.x,self.y) == "seringue":
                self.armes = self.armes + 1
            if self.plato.returnContains(self.x,self.y) == "Tina":
                if self.armes == 3:
                    pass
                else:
                    #Signaler la defaite
                    # return False
                    self.plato.victory(False)
            if self.plato.returnContains(self.x,self.y) == "butin":
                #condition de victoire
                # return False
                self.plato.victory(True)
                pass

        else:
            self.x = posXOrigine
            self.y = posYOrigine

        self.plato.write_case(self.x,self.y,"H")
        # return True