import turtle

# We need to tell Python where to find the files that it
# needs to import.
import site
site.addsitedir("/Users/nick/GITHUB/codezoners/IU000166_FC1/S04/")

# First import of our library (and all we need if it doesn't change):
import shapes

# This is how to force a reload of a library after the file has changed:
import importlib
importlib.reload(shapes)

t = turtle.Turtle()

shapes.circle(t)
shapes.square(t)
