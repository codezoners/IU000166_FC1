import site
site.addsitedir("/Users/nick/GITHUB/codezoners/IU000166_FC1/S03/")

import turtle

t = turtle.Turtle()

import simple_shapes
simple_shapes.square(t)

import importlib
importlib.reload(simple_shapes)
