# Options: fill, colour, rotation (discrete), present/absent, discrete shapes
# Mapping via numpy: size, rotation
# Mapping for colours? t.color(f, f, f) - see colormode()

# Keyword parameters!
# Riley style: make the matrix vary in pitch


def square(t, size, filled):
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
    t.right(90)
    if filled:
        t.end_fill()
    t.up()
    t.forward(-size / 2)
