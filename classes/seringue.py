from random import *
import pygame.display
import pygame.image 
import pygame.event
from classes.case import Case


class Seringue:
    def __init__(self, plateau):
        for morceau in ["1","2","3"]:
            IsObjectPosition= False
            while not IsObjectPosition:
                INtX= randint(0,14)
                INtY= randint(0,14)

                case1 = Case(morceau)
                if self.plateau.MATRICE[INtX][INtY].attribut == "o":
                    self.plateau.MATRICE[INtX][INtY] = case1
                    IsObjectPosition = True
                else:
                    print(self.plateau.MATRICE[INtX][INtY])
