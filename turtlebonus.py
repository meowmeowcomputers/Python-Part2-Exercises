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
        
def colorloop(x, limit):
    b = x + limit
    iteration = int(x/limit)
    while iteration % 2 == 0: #odd iterations to count, count up
        return(b % limit)
    while iteration % 2 == 1: #even iterations to count, count down
        return(limit - (b % limit))

for i in range(1, 900, 2):
    print('rgb'+str(i))
    print('i'+str(i))
    pensize(4)
    left(5)
    triangle(i)
    colormode(255)
    color(colorloop(i, 255), 168, 25)

mainloop()
# def isotri (s, h, x, y):
# #function incomplete
#     pu()
#     setpos(x, y)
#     pd()
#     if h == True:
#
#     setheading(h)
#     for i in range(3):
#         forward(s)
#         right(120)

# def trap (l, h, x, y):
#     pu()
#     setpos(x, y)
#     pd()
#     setheading(h) #0 is east, 180 is west
#     forward(l*2)
#     left(120)
#     forward(l)
#     left(60)
#     forward(l)
#     left(60)
#     forward(l)
#     left(60)
#
#
#
# mainloop()
