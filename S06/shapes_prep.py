import os
#print(os.getcwd())

def square(t, size, fill=False, red=False):
    t.forward(size / 2)
    t.left(90)
    t.down()

    if red:
        t.color("red")
    else:
        t.color("black")

    if fill: t.begin_fill()
    t.forward(size / 2); t.left(90)
    t.forward(size); t.left(90)
    t.forward(size); t.left(90)
    t.forward(size); t.left(90)
    t.forward(size / 2); t.right(90)
    if fill: t.end_fill()

    t.up()
    t.forward(-size / 2)

def circle(t):
    size = 400
    t.up()
    t.forward(size / 2)
    t.left(90)
    t.down()
    t.circle(size / 2)
    t.right(90)
    t.penup()
    t.backward(size / 2)
