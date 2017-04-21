from turtle import *
speed(0)

def triangle(x):
    for i in range(3):
        forward(x/2)
        right(120)

def hexagon(x):
    for i in range(5):
        forward(x)
        left(72)

for i in range(0, 800, 10):
    if i < 255:
        c = i
        pensize(4)
        left(5)
        triangle(i)
        colormode(255)
        color(c, 100, 50)
    else:
        c = (i%255)
        pensize(4)
        left(10)
        triangle(i)
        colormode(255)
        color(c, 100, 50)
    print('rgb'+str(c))
    print('i'+str(i))


mainloop()
