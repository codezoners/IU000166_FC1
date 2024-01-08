import turtle
import os
import random

t = turtle.Turtle()

def teleport(x, y):
    t.penup(); t.goto(x, y); t.pendown()

def save_to(stem):
    psfile = os.path.join(os.getcwd(), "Assignment", stem + ".ps")
    jpgfile = os.path.join(os.getcwd(), "Assignment", stem + ".jpg")
    t.getscreen().getcanvas().postscript(file=psfile)
    os.system(" ".join(["convert", psfile, jpgfile]))

def randomise(rand_pc):
    if rand_pc > 0:
        return random.randrange(100 - rand_pc, 100 + rand_pc) / 100
    else:
        return 1

def tree(depth, dist, angle=20, scale=0.6, rand_pc=0):
    # We assume we're at the base of the trunk, pointing up:
    t.forward(dist)

    if depth > 0:
        t.left(angle * randomise(rand_pc))
        tree(depth - 1, dist * scale * randomise(rand_pc))
        t.right(angle * 2 * randomise(rand_pc))
        tree(depth - 1, dist * scale * randomise(rand_pc))
        t.left(angle * randomise(rand_pc))

    t.backward(dist)

# Simple example in docs:
t.reset()
t.screen.setup(400, 400)
teleport(0, -150)
t.width(3)
t.left(90)
t.speed("fastest")
tree(1, 100)
t.hideturtle()
save_to("tree")

# More like a forest:
t.reset()
t.screen.setup(800, 400)

teleport(-200, -150)
t.width(3)
t.left(90)
t.speed("fastest")
tree(3, 100)
save_to("tree_3")

teleport(0, -150)
t.width(2)
t.speed("fastest")
tree(5, 100, angle=40, scale=0.4)
t.hideturtle()

teleport(200, -150)
t.width(1)
t.speed("fastest")
tree(9, 50, angle=35, scale=0.95, rand_pc=30)
t.hideturtle()

save_to("tree_3")
