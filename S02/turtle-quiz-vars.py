import turtle

t = turtle.Turtle()

turtle.Screen().title("Three Squares")
#turtle.Screen().title("Vars for Nested Squares")

t.reset()
t.pensize(5)

length = 400
length = 380
length = 360

# Position
t.up()
t.forward(length / 2)
t.down()
t.left(90)

# Draw square
t.color("black", "#A0A0A0")
t.forward(length / 2)
# t.begin_fill()
t.left(90); t.forward(length)
t.left(90); t.forward(length)
t.left(90); t.forward(length)
t.left(90); t.forward(length / 2)
# t.end_fill()

# EXERCISE: Back to centre:
t.left(90)
t.up()
t.forward(length / 2)
t.down()
t.left(180)

# EXERCISE: Reorient and repeat
t.left(45)
t.left(30)


# c.getscreen().getcanvas().destroy()
# c.getscreen().mainloop()

t.pos()


t.reset()
