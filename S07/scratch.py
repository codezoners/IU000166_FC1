import turtle

t = turtle.Turtle()

import site
site.addsitedir("/Users/nick/GITHUB/codezoners/IU000166_FC1/S07/")

# First import
import shapes

# Import again after any changes:
import importlib
importlib.reload(shapes)

def clear():
    t.reset()
    t.up()
    t.speed(0)
    # By default, we want the pen to be up.

    t.backward(300)
    t.right(90)
    t.backward(300)
    t.left(90)

clear()

for y in range(10):
    for x in range(10):

        c = "blue" if x < 3 else "white" if x < 7 else "red"

        shapes.square(t, 50, True, c)
        t.forward(60)

    t.backward(600)
    t.right(90)
    t.forward(60)
    t.left(90)
