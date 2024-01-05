import turtle
import random

t = turtle.Turtle()

def r():
    return random.randint(1, 3)

def op_art(depth, dist):
    if depth < 0:
        #t.forward(dist)
        t.forward(dist / 2)
        t.pendown()
        t.circle(dist / 2, steps=50)
        t.penup()
        t.forward(dist / 2)
    elif depth == 0:
        t.forward(dist / 2)
        t.pendown()
        t.begin_fill()
        t.circle(dist / 2, steps=50)
        t.end_fill()
        t.penup()
        t.forward(dist / 2)
    else:
        op_art(depth - r(), dist / 2)
        op_art(depth - r(), dist / 2)

        t.backward(dist)
        t.left(90)
        t.forward(dist / 2)
        t.right(90)

        op_art(depth - r(), dist / 2)
        op_art(depth - r(), dist / 2)

        t.right(90)
        t.forward(dist / 2)
        t.left(90)

t.reset()
t.penup()
t.goto(-400, -400)
t.penup()
t.speed("fastest")
t.pencolor("black")
t.fillcolor("#FF8000")
op_art(8, 800)
