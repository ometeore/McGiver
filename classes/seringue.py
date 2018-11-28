""" Dispositionne sur le plateau les 3 morceaux de seringues """
from random import randint
from classes.case import Case


class Seringue:
    """ positionne les morceaux de seringues """
    def __init__(self, plateau):
        self.plato = plateau
        for morceau in ["1", "2", "3"]:
            objet_en_position = False
            while not objet_en_position:
                position_x = randint(0, 14)
                position_y = randint(0, 14)

                case1 = Case(morceau)
                if self.plato.matrice[position_x][position_y].attribut == "o":
                    self.plato.matrice[position_x][position_y] = case1
                    objet_en_position = True
