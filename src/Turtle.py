import turtle
from turtle import *
import time
def izris_polja(sirina, visina):
    screen = Screen()
    screen.screensize(600, 600)
    hideturtle()
    for i in range(-1, visina):
        speed(0)
        x = -250
        y = i*-50 + 150
        penup()
        goto(x, y)
        pendown()
        turtle.width(4)
        forward(visina*50)

    for i in range(-1, sirina):
        speed(0)
        x = i * 50 - 200
        y = 200
        penup()
        goto(x, y)
        pendown()
        turtle.width(4)
        setheading(270)
        forward(sirina*50)

    for i in range(sirina + 1):
        speed(0)
        x = i*50 - 275
        y = 200
        penup()
        goto(x, y)
        pendown()
        write(i, align= "center", font= ["arial", 20])

    for i in range(sirina + 1):
        speed(0)
        x = - 275
        y = i * -50 + 200
        penup()
        goto(x, y)
        pendown()
        write(i, align= "center", font= ["arial", 20])


    turtle.done()

izris_polja(10,10)