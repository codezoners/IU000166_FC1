import turtle
import random
import numpy

t = turtle.Turtle()

import site
site.addsitedir("/Users/nick/GITHUB/codezoners/IU000166_FC1/S08/")

# First import
import shapes

# Import again after any changes:
import importlib
importlib.reload(shapes)

def clear():
    t.reset()
    t.screen.bgcolor([0.1, 0.1, 0.1])
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
        rand = random.random()
        r = numpy.interp(rand, [0, 1], [0, 1])
        g = r / 2                                    # r # random.random() # 1 if x == y else 0
        b = 0      
        filled = True if rand > 0.5 else False                         # random.random() # y / 9
        rotate = True if rand > 0.5 else False
        shapes.square(t, 50, 100, filled, [r, g, b], rotate)
        t.forward(60)

    t.backward(600)
    t.right(90)
    t.forward(60)
    t.left(90)

