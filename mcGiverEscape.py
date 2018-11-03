from random import *
import json
import os
os.chdir("/home/pilt/Documents/entrainement/nawak")
#####################################################################################
############################LA GRANDE ECHAPPE DE MC GIVER############################
#####################################################################################

class Case:
    def __init__(self, ligne, hauteur, attribut ):
        # assert : Lève une exception si renvoie False
        assert -0 <= ligne <= 15
        self.ligne = ligne
        assert -0 <= hauteur <= 15
        self.hauteur = hauteur
        self.attribut = attribut

    def __repr__(self):
        return "<x: {},y: {}, {}>".format(self.ligne, self.hauteur, self.attribut)




class Plateau:
    LIGNE_MAX = 15
    HAUTEUR_MAX = 15
    WIDTH_CASE = 1
    HEIGHT_CASE = 1


# for LIGNE in fp:
#     for element in LIGNE:
#         print (element)




    def __init__(self):
        fp = open("lab.txt","r")
        self.MATRICE = []
        for ligne in fp:
            LIGNE = []
            for hauteur in ligne:
                coin_bas_gauche = Case(ligne, hauteur, "o")
                LIGNE.append(coin_bas_gauche)

            self.MATRICE.append(LIGNE)


        self.write_case(randint(0,self.LIGNE_MAX - 1),randint(0,HAUTEUR_MAX),"1")
        self.write_case(randint(0,self.LIGNE_MAX - 1),randint(0,HAUTEUR_MAX),"2")
        self.write_case(randint(0,self.LIGNE_MAX - 1),randint(0,HAUTEUR_MAX),"3")

    def __repr__(self):
        i = 0
        tab = ""
        for LIGNE in self.MATRICE:
            for element in LIGNE:
                tab = tab + element.attribut
            tab = tab + "\n"
        return tab

    def write_case(self, posX, posY, newAttribut):
        self.MATRICE[posX][posY].attribut = newAttribut 


# retourne 0 si la case est vide 1 si c'est un objet 2 si c'est tinaTurner
    def returnContains(self, x, y):
        element = self.MATRICE[x][y]
        if element.attribut == "o":
            return 0
        if element.attribut == "1" or element.attribut == "2" or element.attribut =="3":
            return 1
        if element.attribut == "M":
            return 2
        else:
            print("?????????????????????????????????????????????????")

    def isAllowed(self, x, y):
        if x<15 and x>=0 and y<15 and y>=0:
            return 1
        else:
            return 0 



class Hero:
    def __init__(self, plateau):
        self.y = randint(0,14)
        self.x = randint(0,14)
        self.plato = plateau
        self.armes = 0
        self.plato.write_case(self.x,self.y,"H")

    def __repr__(self):
        return "votre hero se trouve:ligne-> {},hauteur-> {} et il possède {} morceaux de la seringues".format(self.x, self.y, self.armes)

    def isWin(self):
        if self.armes == 3:
            print("WIN >(O.O)<")
            return "quit"
        else:
            print("LOOSER T.T")
            return "quit"


    def mouvement(self, direction): #direction est entre 0 et 3 
        posXOrigine = self.x
        posYOrigine = self.y
        self.plato.write_case(posXOrigine, posYOrigine, 'o')
#       plateau.testCase(posXY)
        if direction == 0:
            self.y = self.y + 1
        if direction == 1:
            self.y = self.y -1
        if direction == 2:
            self.x = self.x + 1
        if direction == 3:
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




class tinaTurner:
    def __init__(self, plateau):
        self.y = 0
        self.x = 0
        plateau.write_case(self.x, self.y, "M")



def main ():


    plateau = Plateau()
    hero = Hero(plateau)
    tinyTina = tinaTurner(plateau)
    i = 0
    while i != 'quit':
        #print(plateau.MATRICE)
        print(plateau)
        print('')
        print('***')
        print(hero)
        print('Utilisez QZDS pour bouger le hero. Rentrez quit pour quitter')
        i = input('Tapez encore qeqchose svp.')
        print('***')
        print('')
        if(i=='z'):
            i = hero.mouvement(0)  
        if(i=='s'):
            i = hero.mouvement(1)
        if(i=='d'):
            i = hero.mouvement(2)
        if(i=='q'):
            i = hero.mouvement(3)
        #i = hero.isWin();



main()