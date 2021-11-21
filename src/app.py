from src.domain import Morje
import turtle
from turtle import *
import time


class ConsolApp:

    def __init__(self, visina, sirina):
        self.morje = Morje(visina, sirina)
        self.visina = visina
        self.sirina = sirina

    def narisi(self, player):
        print(" ", end= " ")
        for x in range(self.sirina):
            print(x, end= " ")
        print()

        for y in range(self.visina):
            print(y, end= " ")
            for x in range(self.sirina):

                bomba_narisano = False
                for bomba in self.morje.bombe:
                    if bomba.y == y and bomba.x == x:
                        print("*", end= " ")
                        bomba_narisano = True
                if bomba_narisano == True:
                    continue
                if player == 0:
                    narisano = False
                    for ladja in self.morje.rdeceladjice:
                        for del_ladje in ladja.deli:
                            if del_ladje.x == x and del_ladje.y == y:
                                if del_ladje.zadet == True:
                                    print("X", end= " ")
                                else:
                                    print("R", end= " ")
                                narisano = True


                    if narisano == True:
                        continue
                else:
                    narisano = False
                    for ladja in self.morje.modreladjice:
                        for del_ladje in ladja.deli:
                            if del_ladje.x == x and del_ladje.y == y:
                                if del_ladje.zadet == True:
                                    print("x", end=" ")
                                else:
                                    print("M", end=" ")

                                narisano = True

                    if narisano == True:
                        continue
                print(".", end= " ")

            print()

    def konec(self):
        modri_zgubil = True
        for modra_ladjica in self.morje.modreladjice:

            if modra_ladjica.potopljena() == False:
                modri_zgubil = False
        if modri_zgubil == True:
            return 0

        rdeci_zgubil = True
        for rdeca_ladjica in self.morje.rdeceladjice:

            if rdeca_ladjica.potopljena() == False:
                rdeci_zgubil = False
        if rdeci_zgubil == True:
            return 1

        return -1

class TurtleApp:

    def __init__(self, visina, sirina):
        self.morje = Morje(visina, sirina)
        self.visina = visina
        self.sirina = sirina
        self.screen = Screen()
        self.screen.screensize(1000, 1000)
        hideturtle()
        speed(0)
        turtle.bgpic("morje.png")
    def izris_polja(self, odmik ):


        for i in range(-1, self.sirina):

            x = i * 50 - 200 + odmik
            y = 200
            penup()
            goto(x, y)
            pendown()
            turtle.width(4)
            setheading(270)
            forward(self.sirina * 50)
            setheading(0)
        for i in range(-1, self.visina):
            x = -250 + odmik
            y = i * -50 + 150
            penup()
            goto(x, y)
            pendown()
            turtle.width(4)
            forward(self.sirina * 50)


        for i in range(self.sirina):

            x = i * 50 - 225 + odmik
            y = 200
            penup()
            goto(x, y)
            pendown()
            write(i, align="center", font=["arial", 20])

        for i in range(self.sirina):

            x = - 275 + odmik
            y = i * -50 + 150
            penup()
            goto(x, y)
            pendown()
            write(i, align="center", font=["arial", 20])




    def narisi(self, player ):

        if player == 0:
            for ladja in self.morje.rdeceladjice:
                for deli_ladje in ladja.deli:
                    self.izris_ladje_rdece(deli_ladje.x, deli_ladje.y, "R")

        if player == 1:
            for ladja in self.morje.modreladjice:
                for deli_ladje in ladja.deli:
                    self.izris_ladje_modre(deli_ladje.x, deli_ladje.y, "M")

    def zadetek(self, x, y):

        for ladja in self.morje.rdeceladjice + self.morje.modreladjice:
            for deli_ladje in ladja.deli:
                if deli_ladje.x == x and deli_ladje.y == y:
                    return True
    def izris_ladje_modre(self, x, y,znak):
        a = x * 50 - 240 + 300
        b = y * 50 - 190 - 100
        penup()
        goto(a, b)
        pendown()
        write(znak, font=["arial", 20])
    def izris_ladje_rdece(self, x, y,znak):
        a = x * 50 - 240 - 300
        b = y * 50 - 190 - 100
        penup()
        goto(a, b)
        pendown()
        write(znak, font=["arial", 20])
    def izris_znaka(self, x, y, znak, odmik):

        a = x * 50 - 275 + odmik
        b = y * -50 + 225
        penup()
        goto(a, b)
        pendown()
        dot(50, znak)
    def st_potopljenih(self):
        modra_potopljena = 0

        for modra_ladjica in self.morje.modreladjice:

            if modra_ladjica.potopljena():
                modra_potopljena += 1
        rdeca_potopljena = 0
        for rdeca_ladjica in self.morje.rdeceladjice:

            if rdeca_ladjica.potopljena():
                rdeca_potopljena += 1
        return [modra_potopljena, rdeca_potopljena]

    def konec(self):
        modri_zgubil = True
        for modra_ladjica in self.morje.modreladjice:

            if modra_ladjica.potopljena() == False:
                modri_zgubil = False
        if modri_zgubil == True:
            return 0

        rdeci_zgubil = True
        for rdeca_ladjica in self.morje.rdeceladjice:

            if rdeca_ladjica.potopljena() == False:
                rdeci_zgubil = False
        if rdeci_zgubil == True:
            return 1

        return -1





