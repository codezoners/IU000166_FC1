import turtle
import os
import math

t = turtle.Turtle()
DIST = 400
SIZE = 600
t.screen.setup(SIZE, SIZE)

# First form only:
t.forward(DIST / 3)
t.left(60)
t.forward(DIST / 3)
t.right(120)
t.forward(DIST / 3)
t.left(60)
t.forward(DIST / 3)

def snowflake(depth, dist):
    if depth == 0:
        t.forward(dist)
    else:
        snowflake(depth - 1, dist / 3)
        t.left(60)
        snowflake(depth - 1, dist / 3)
        t.right(120)
        snowflake(depth - 1, dist / 3)
        t.left(60)
        snowflake(depth - 1, dist / 3)

def teleport(x, y):
    t.penup(); t.goto(x, y); t.pendown()

def reset(size=(SIZE, SIZE), pensize=1):
    t.reset()
    t.screen.setup(*size)
    t.screen.bgcolor("white")
    t.speed("fastest")
    t.pencolor("black")
    t.fillcolor("#D0D0D0")
    t.pensize(pensize)

def save_to(stem):
    psfile = os.path.join(os.getcwd(), "Assignment", stem + ".ps")
    jpgfile = os.path.join(os.getcwd(), "Assignment", stem + ".jpg")
    t.getscreen().getcanvas().postscript(file=psfile)
    os.system(" ".join(["convert", psfile, jpgfile]))

# First form:
reset(pensize=3, size=(SIZE, SIZE / 3))
teleport(-DIST / 2, 0)
snowflake(0, DIST)
t.hideturtle()
save_to("form_0")

# Second form only:
reset(pensize=3, size=(SIZE, SIZE / 3))
teleport(-DIST / 2, -40)
snowflake(1, DIST)
t.hideturtle()
save_to("form_1")


# Three forms:
reset(pensize=3, size=(SIZE, SIZE))
teleport(-DIST / 2, 200)
snowflake(0, DIST)
teleport(-DIST / 2, 0)
snowflake(1, DIST)
teleport(-DIST / 2, -200)
snowflake(2, DIST)
t.hideturtle()
save_to("form_012")

reset(pensize=2)
teleport(-DIST / 2, DIST / 3)
t.begin_fill()
for i in range(3):
    snowflake(4, DIST)
    t.right(120)
t.end_fill()
t.hideturtle()
save_to("snowflake_4")
