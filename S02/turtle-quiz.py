import turtle

t = turtle.Turtle()

t.reset()
t.pensize(5)

# Position
t.up()
t.forward(200)
t.down()
t.left(90)

# Draw square
t.color("black", "#A0A0A0")
t.forward(200)
# t.begin_fill()
t.left(90); t.forward(400)
t.left(90); t.forward(400)
t.left(90); t.forward(400)
t.left(90); t.forward(200)
# t.end_fill()

# EXERCISE: Back to centre:
t.left(90)
t.up()
t.forward(200)
t.down()
t.left(180)

# EXERCISE: Reorient and repeat
t.left(45)


# c.getscreen().getcanvas().destroy()
# c.getscreen().mainloop()

t.pos()


t.reset()
