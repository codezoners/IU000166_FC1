import turtle

t = turtle.Turtle()
t.reset()
t.pensize(5)
t.speed(1)

# Draw me a square, *centered around the turtle*
# - and put the turtle back when finished.

def draw_square(size, line_colour, fill_colour):
    t.pencolor(line_colour)
    t.up()
    t.forward(size / 2)
    t.left(90)
    t.down()

    if fill_colour is not None:
        t.fillcolor(fill_colour)
        t.begin_fill()

    t.forward(size / 2); t.left(90)
    t.forward(size); t.left(90)
    t.forward(size); t.left(90)
    t.forward(size); t.left(90)
    t.forward(size / 2); t.right(90)
    t.end_fill()

    t.up()
    t.forward(-size / 2)
    t.down()

draw_square(400, "black", "#606060")
t.left(30)
draw_square(200, "white", "orange")
draw_square(30, "white", "black")

t.reset()
for i in range(50):
    draw_square(i * 5, "#FF8000", None)
    t.left(1)
