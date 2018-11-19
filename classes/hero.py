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

        IsObjectPosition= False
        while not IsObjectPosition:
            case1 = Case("H")
            if self.plato.MATRICE[self.x][self.y].attribut == "o":
                self.plato.MATRICE[self.x][self.y] = case1
                IsObjectPosition = True
            else:
                print(self.plato.MATRICE[self.x][self.y])        # IsObjectPosition= False





    def __repr__(self):
        return "votre hero se trouve:ligne-> {},colonne-> {} et il possède {} morceaux de la seringues".format(self.x, self.y, self.armes)
    

    def isWin(self):
        if self.armes == 3:
            print("WIN >(O.O)<")
            return "quit"
        else:
            print("LOOSER T.T")
            return "quit"


    def mouvement(self, direction): #direction est entre 0 et3

    # changer direction 0 1 2 3  par haut bas....

        posXOrigine = self.x
        posYOrigine = self.y

        self.plato.write_case(posXOrigine, posYOrigine, 'o')
#       plateau.testCase(posXY)
        if direction == "droite":
            self.y = self.y + 1
        if direction == "gauche":
            self.y = self.y -1
        if direction == "bas":
            self.x = self.x + 1
        if direction == "haut":
            self.x = self.x - 1

        if self.plato.isAllowed(self.x,self.y):
            if self.plato.returnContains(self.x,self.y) == 0:
                pass
            if self.plato.returnContains(self.x,self.y) == 1:
                self.armes = self.armes + 1
            if self.plato.returnContains(self.x,self.y) == 2:
                return self.isWin()
        else:
            self.x = posXOrigine
            self.y = posYOrigine

        self.plato.write_case(self.x,self.y,"H")