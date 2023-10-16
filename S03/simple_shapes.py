# Simple shapes library.
def square(t):
    "Square of preset size centred on turtle."
    t.up()
    t.forward(100)
    t.left(90)
    t.down()

    t.forward(100); t.left(90)
    t.forward(200); t.left(90)
    t.forward(200); t.left(90)
    t.forward(200); t.left(90)
    t.forward(100); t.right(90)
    t.up()
    t.forward(-100)
