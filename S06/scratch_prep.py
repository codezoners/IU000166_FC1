import turtle
import numpy

# We need to tell Python where to find the files that it
# needs to import.
import site
site.addsitedir("/Users/nick/GITHUB/codezoners/IU000166_FC1/S06/")

# First import of our library (and all we need if it doesn't change):
import S06.shapes_prep as shapes_prep

# This is how to force a reload of a library after the file has changed:
import importlib
importlib.reload(shapes_prep)

t = turtle.Turtle()

# Default state: pen up.
t.reset()
t.up()
t.speed(0)


t.forward(-4.5 * 50)
t.right(90)
t.forward(-4.5 * 50)
t.left(90)

# And more generally: mapping across X/Y (e.g. size).
# brew install numpy
# e.g. numpy.interp(3, [0, 10], [0, 100])

for down in range(10):
    for across in range(10):
        size = numpy.interp(down, [0, 10], [20, 40])
        # size = 40
        shapes_prep.square(t, size, fill=(across == down), red=(across == 3))
        t.forward(50)

    # Prepare for next row. Pitch is 50, 10 squares.

    t.forward(-10 * 50)
    t.right(90)
    t.forward(50)
    t.left(90)
