import os
print(os.getcwd())
print("TWO")

def square(t):
    size = 400
    t.up()
    t.forward(size / 2)
    t.left(90)
    t.down()

    t.forward(size / 2); t.left(90)
    t.forward(size); t.left(90)
    t.forward(size); t.left(90)
    t.forward(size); t.left(90)
    t.forward(size / 2); t.right(90)
    t.end_fill()

    t.up()
    t.forward(-size / 2)
    t.down()

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
