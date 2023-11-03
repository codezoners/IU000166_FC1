import turtle

t = turtle.Turtle()

import site
site.addsitedir("/Users/nick/GITHUB/codezoners/IU000166_FC1/S06/")

# First import
import shapes

# Import again after any changes:
import importlib
importlib.reload(shapes)

t.reset()
t.up()
t.speed(0)
# By default, we want the pen to be up.

t.backward(300)
t.right(90)
t.backward(300)
t.left(90)


for y in range(10):
    for x in range(10):
        shapes.square(t, 50)
        t.forward(60)

    t.backward(600)
    t.right(90)
    t.forward(60)
    t.left(90)
