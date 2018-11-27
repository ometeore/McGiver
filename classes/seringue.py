from random import randint
import pygame.image 
from classes.case import Case


class Seringue:
    def __init__(self, plateau):
        self.plato = plateau
        for morceau in ["1","2","3"]:
            IsObjectPosition= False
            while not IsObjectPosition:
                INtX= randint(0,14)
                INtY= randint(0,14)

                case1 = Case(morceau)
                if self.plato.MATRICE[INtX][INtY].attribut == "o":
                    self.plato.MATRICE[INtX][INtY] = case1
                    IsObjectPosition = True