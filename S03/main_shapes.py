import site
site.addsitedir("/Users/nick/OneDrive - University of the Arts London/S03/")

import turtle

t = turtle.Turtle()

import simple_shapes
simple_shapes.square(t)

import importlib
importlib.reload(simple_shapes)
