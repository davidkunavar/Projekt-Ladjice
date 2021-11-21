import math
import random


class Ladjica:

    def __init__(self, y: int, x: int, velikost: int, vertikalno: bool):
        self.y = y
        self.x = x
        self.velikost = velikost
        self.vertikalno = vertikalno
        self.deli = []

        for i in range(velikost):
            del_ladje = Del_ladje(y, x)
            self.deli.append(del_ladje)
            if vertikalno == True:
                y += 1
            else:
                x += 1

    def se_nahaja(self, y, x):
        for del_ladje in self.deli:
            if del_ladje.y == y and del_ladje.x == x:
                return True

        return False

    def se_prekriva(self, ladja):
        for del_ladje1 in self.deli:
            for del_ladje2 in ladja.deli:
                if del_ladje1.x == del_ladje2.x and del_ladje1.y == del_ladje2.y:
                    return True
                elif del_ladje1.oddaljenost(del_ladje2) <= 2:
                    return True

        return False

    def potopljena(self):

        for deli_ladje in self.deli:
            if deli_ladje.zadet == False:
                return False
        return True


class Del_ladje:

    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x
        self.zadet = False

    def oddaljenost(self, del_ladje):
        dx = self.x - del_ladje.x
        dy = self.y - del_ladje.y

        return math.sqrt(dx * dx + dy * dy)


class Morje:
    def __init__(self, sirina, visina):
        self.sirina = sirina
        self.visina = visina
        self.modreladjice = []
        self.rdeceladjice = []
        self.bombe = []

        for i in range(1, 4):

            while True:
                seprekriva = False
                modraladjica = Ladjica(random.randint(0, sirina - 3 ), random.randint(0, visina), i,
                                       random.randint(0, 1))
                if self.strli_ven(modraladjica):
                    continue
                for ladje in self.rdeceladjice + self.modreladjice:

                    if ladje.se_prekriva(modraladjica):
                        seprekriva = True

                if seprekriva == False:
                    self.modreladjice.append(modraladjica)
                    break
            while True:
                seprekriva = False
                rdecaladjica = Ladjica(random.randint(0, sirina - 3 ), random.randint(0, visina), i,
                                       random.randint(0, 1))
                if self.strli_ven(rdecaladjica):
                    continue
                for ladje in self.rdeceladjice + self.modreladjice:
                    if ladje.se_prekriva(rdecaladjica):
                        seprekriva = True

                if seprekriva == False:
                    self.rdeceladjice.append(rdecaladjica)
                    break

    def strli_ven(self, ladja):
        for del_ladje in ladja.deli:
            if del_ladje.x < 0 or del_ladje.x >= self.sirina:
                return True
            if del_ladje.y < 0 or del_ladje.y >= self.visina:
                return True
        return False

    def vrzi_bombo(self, y, x):
        bomba = Bomba(y, x)
        self.bombe.append(bomba)
        for i in range(len(self.rdeceladjice)):
            for l in range(len(self.rdeceladjice[i].deli)):
                if self.rdeceladjice[i].deli[l].y == y   and self.rdeceladjice[i].deli[l].x == x:
                    self.rdeceladjice[i].deli[l].zadet = True

        for i in range(len(self.modreladjice)):
            for l in range(len(self.modreladjice[i].deli)):
                if self.modreladjice[i].deli[l].y == y and self.modreladjice[i].deli[l].x == x:
                    self.modreladjice[i].deli[l].zadet = True


class Bomba:
    def __init__(self, y, x):
        self.y = y
        self.x = x
