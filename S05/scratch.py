import turtle

# We need to tell Python where to find the files that it
# needs to import.
import site
site.addsitedir("/Users/nick/GITHUB/codezoners/IU000166_FC1/S05/")

# First import of our library (and all we need if it doesn't change):
import shapes

# This is how to force a reload of a library after the file has changed:
import importlib
importlib.reload(shapes)

t = turtle.Turtle()

shapes.circle(t)

shapes.square(t, 200)
shapes.square(t, 220)
shapes.square(t, 240)

t.reset()

for i in range(10):
    shapes.square(t)

t.reset()
t.up()
t.forward(-200)


for i in range(10):
    t.down()
    shapes.square(t, 40)
    t.up()
    t.forward(50)

t.right(90)
t.forward(50)
t.right(90)
t.forward(50)

# ----------

t.reset()

# Import my file and Iya's file:
import nick, iya

t.reset()

importlib.reload(nick)


# "N" "I"
nick.N(t)
iya.I(t)
