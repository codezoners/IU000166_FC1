import turtle
import os

t = turtle.Turtle()

def teleport(x, y):
    t.penup(); t.goto(x, y); t.pendown()

def save_to(stem):
    psfile = os.path.join(os.getcwd(), "Assignment", stem + ".ps")
    jpgfile = os.path.join(os.getcwd(), "Assignment", stem + ".jpg")
    t.getscreen().getcanvas().postscript(file=psfile)
    os.system(" ".join(["convert", psfile, jpgfile]))

def tree(depth, dist):
    # We assume we're at the base of the trunk, pointing up:
    t.forward(dist)

    if depth > 0:
        t.left(20)
        tree(depth - 1, dist / 1.5)
        t.right(40)
        tree(depth - 1, dist / 1.5)
        t.left(20)

    t.backward(dist)

t.reset()
t.screen.setup(400, 400)
teleport(0, -150)
t.width(3)
t.left(90)
t.speed("fastest")
tree(1, 100)
t.hideturtle()
save_to("tree")
