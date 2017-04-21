from turtle import *


def circlery():
#    width(20)
    circle(180)

def octagon():
    for i in range(8):
        forward(20)
        left(45)

def hexagon():
    for i in range(5):
        size(100)
        forward(200)
        left(72)

def square():
    for i in range(4):
        forward(100)
        right(90)

def star(x, y, z):
    for i in range(10):
        if i % 2 == 0:
            color('yellow')
            begin_fill()
            forward(z)
            left(144)
            end_fill()

def triangle():
    for i in range(3):
        forward(100)
        right(90)
