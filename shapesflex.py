from turtle import *


def circlery(x):
#    width(20)
    circle(x)

def octagon(x):
    for i in range(8):
        forward(x)
        left(45)

def hexagon(x):
    for i in range(5):
        forward(x)
        left(72)

def square(x):
    for i in range(4):
        forward(x)
        right(90)

def star(x):
    for i in range(5):
        forward(x)
        left(144)

def triangle(x):
    for i in range(3):
        forward(x)
        right(120)
