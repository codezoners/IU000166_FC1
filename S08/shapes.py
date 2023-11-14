def square(t, size_x, size_y, filled, colour, rotate):
    t.fillcolor(colour)
    t.pencolor( [1, 1, 1] )
    if rotate:
        t.left(45)
    # Draw a square:
    t.forward(size_x / 2)
    t.left(90)
    t.down()
    if filled:
        t.begin_fill()
        t.width(1)
    else:
        t.width(5)
        
    t.forward(size_y / 2)

    t.left(90); t.forward(size_x)
    t.left(90); t.forward(size_y)
    t.left(90); t.forward(size_x)

    t.left(90)
    t.forward(size_y / 2)
    if filled:
        t.end_fill()
    t.right(90)
    t.up()
    t.forward(-size_x / 2)
    if rotate:
        t.right(45)
