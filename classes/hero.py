""" Ce module gere ce qui est relatif au hero et a ses deplacements sur le plateau """
from random import randint
from classes.case import Case



class Hero:
    """ classe du hero """
    def __init__(self, plateau):
        self.plato = plateau
        self.armes = 0

        objet_en_place = False
        while not objet_en_place:
            case1 = Case("H")
            self.position_y = randint(0, 14)
            self.position_x = randint(0, 14)
            if plateau.matrice[self.position_x][self.position_y].attribut == "o":
                plateau.matrice[self.position_x][self.position_y] = case1
                objet_en_place = True

    def __repr__(self):
        """ affichage du hero (position armes) dans le terminal use for debug"""
        return "votre hero se trouve:ligne-> {},colonne-> {} et il possède {} morceaux de la seringues".format(self.position_x, self.position_y, self.armes)


    def mouvement(self, direction):
        """fait appel a des fonctions du plateau pour savoir si le mvment est possible """
        position_x_origine = self.position_x
        position_y_origine = self.position_y

        self.plato.write_case(position_x_origine, position_y_origine, 'o')

        if direction == "droite":
            self.position_y = self.position_y + 1
        if direction == "gauche":
            self.position_y = self.position_y -1
        if direction == "bas":
            self.position_x = self.position_x + 1
        if direction == "haut":
            self.position_x = self.position_x - 1

        if self.plato.is_allowed(self.position_x, self.position_y):
            if self.plato.return_contains(self.position_x, self.position_y) == "vide":
                pass
            if self.plato.return_contains(self.position_x, self.position_y) == "seringue":
                self.armes = self.armes + 1
            if self.plato.return_contains(self.position_x, self.position_y) == "Tina":
                if self.armes != 3:
                    self.plato.victory(False)
                    return False
            if self.plato.return_contains(self.position_x, self.position_y) == "butin":
                self.plato.victory(True)
                return False

        else:
            self.position_x = position_x_origine
            self.position_y = position_y_origine

        self.plato.write_case(self.position_x, self.position_y, "H")
        return True
