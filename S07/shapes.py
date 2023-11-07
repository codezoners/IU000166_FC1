def square(t, size, filled, colour):
    t.fillcolor(colour)
    t.pencolor( [0, 0, 0] )
    # Draw a square:
    t.forward(size / 2)
    t.left(90)
    t.down()
    if filled:
        t.begin_fill()
    t.forward(size / 2)

    for i in range(3):
        t.left(90)
        t.forward(size)

    t.left(90)
    t.forward(size / 2)
    if filled:
        t.end_fill()
    t.right(90)
    t.up()
    t.forward(-size / 2)
