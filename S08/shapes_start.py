def square(t, size):
    # Draw a square:
    t.forward(size / 2)
    t.left(90)
    t.down()
    t.forward(size / 2)

    for i in range(3):
        t.left(90)
        t.forward(size)

    t.left(90)
    t.forward(size / 2)
    t.right(90)
    t.up()
    t.forward(-size / 2)
