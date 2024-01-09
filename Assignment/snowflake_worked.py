import turtle

t = turtle.Turtle()

DIST = 400

def snowflake(depth, dist):
    if depth == 0:
        t.forward(dist)
    else:
        snowflake(depth - 1, dist / 3)
        t.right(90)
        snowflake(depth - 1, dist / 3)
        t.left(90)
        snowflake(depth - 1, dist / 3)
        t.left(90)
        snowflake(depth - 1, dist / 3)
        t.right(90)
        snowflake(depth - 1, dist / 3)

t.reset()
t.speed("fastest")

# (square form!)
#t.begin_fill()
for i in range(4):
    snowflake(4, DIST)
    t.right(90)
#t.end_fill()
