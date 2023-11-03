import turtle

# We need to tell Python where to find the files that it
# needs to import.
import site
site.addsitedir("/Users/nick/GITHUB/codezoners/IU000166_FC1/S06/")

# First import of our library (and all we need if it doesn't change):
import shapes

# This is how to force a reload of a library after the file has changed:
import importlib
importlib.reload(shapes)

t = turtle.Turtle()

# Default state: pen up.
t.reset()
t.up()


t.forward(-4.5 * 50)
t.right(90)
t.forward(-4.5 * 50)
t.left(90)

for down in range(10):
    for across in range(10):
        shapes.square(t, 40)
        t.forward(50)

    # Prepare for next row. Pitch is 50, 10 squares.

    t.forward(-10 * 50)
    t.right(90)
    t.forward(50)
    t.left(90)
