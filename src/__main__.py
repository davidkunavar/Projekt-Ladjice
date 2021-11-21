import random

from src.app import ConsolApp, TurtleApp
import turtle
from turtle import *
import time

from src.domain import Ladjica

app = TurtleApp(10, 10)


app.izris_polja(300)
app.narisi(1)
app.izris_polja(- 300)
app.narisi(0)

while True:
    zadetek0 = 0
    zadetek1 = 0

    print("Kam boš vrgel bombo - 0")
    y = int(textinput("Pozor", "Vnesi y"))+1
    x = int(textinput("Pozor", "vnesi x"))+1

    app.morje.vrzi_bombo(y, x)
    if app.zadetek(y, x):
        app.izris_znaka(x, y, "red", -300)

        zadetek0 += 1
        penup()
        goto(50, 350)
        pendown()
        write(f"Zadetki rdečega: {zadetek0}", font=["arial", 40, "bold"])


    else:
        app.izris_znaka(x, y, "red", -300)

    print(app.st_potopljenih())

    if zadetek0 == 4:
        print("Zmagal si, rdeci")
        break

    print("Kam boš vrgel bombo - 1")
    y = int(textinput("Pozor", "Vnesi y:"))+1
    x = int(textinput("Pozor", "Vnesi x:"))+1

    app.morje.vrzi_bombo(y, x)
    if app.zadetek(y, x):
        app.izris_znaka(x, y, "blue", 300)
        zadetek1 += 1
        penup()
        goto(-550, 350)
        pendown()
        write(f"Zadetki modrega {zadetek1}", font=["arial", 40, "bold"])
    else:
        app.izris_znaka(x, y, "blue", 300)
    print(app.st_potopljenih())

    if zadetek1 == 4:
        print("Zmagal si, modri")
        break


