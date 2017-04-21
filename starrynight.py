from turtle import *
import random

o = random.randint(100, 200)
bgcolor('black')
speed(0)
# o = random.randint(10, 20)

def star(x, y, z):
    left(x)
    begin_fill()
    color('yellow')
    fillcolor('yellow')
    pu()
    setpos(x, y)
    pd()
    for i in range(10):
        if i % 2 == 0:
            forward(z)
            left(108)
        if i % 2 == 1:
            forward(z)
            right(36)

    end_fill()

for i in range(o):
    a = random.randint(-350, 350)
    b = random.randint(-350, 350)
    z = random.randint(1, 20)
    # # x = 3
    # # y = 3
    # z = 10
    star(a, b, z)
    print(a, b)

mainloop()
