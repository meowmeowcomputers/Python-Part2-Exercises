
def circlery():
    width(20)
    circle(180)
    mainloop()

def octagon():
    for i in range(8):
        forward(20)
        left(45)
    mainloop()

def hexagon():
    for i in range(5):
        forward(200)
        left(72)
    mainloop()

def square():
    for i in range(4):
        forward(100)
        right(90)
    mainloop()

def star():
    for i in range(5):
        forward(200)
        left(144)
    mainloop()

def triangle():
    for i in range(3):
        forward(100)
        right(90)
    mainloop()
