# This Module will create Modern Art
from turtle import *
from random import *


# Random RGB
def randomColor():
    red = randint(0, 254)
    green = randint(0, 254)
    blue = randint(0, 254)
    color(red, green, blue)  # Changes turtle color


def randomPlace():
    x = randint(-100, 100)
    y = randint(-100, 100)
    goto(x, y)


def Draw():
    colormode(255)
    shape("turtle")
    randomColor()
    randomPlace()
    stamp()
    randomColor()
    randomPlace()
    stamp()
    input("Press Enter to continue...")