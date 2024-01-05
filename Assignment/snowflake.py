import turtle

t = turtle.Turtle()

def snowflake(depth, dist):
    if depth == 0:
        t.forward(dist)
    else:
        snowflake(depth - 1, dist / 3)
        t.left(60)
        snowflake(depth - 1, dist / 3)
        t.right(120)
        snowflake(depth - 1, dist / 3)
        t.left(60)
        snowflake(depth - 1, dist / 3)


t.reset()
t.speed("fastest")
t.pencolor("black")
t.fillcolor("#FF8000")

t.begin_fill()
for i in range(3):
    snowflake(4, 400)
    t.right(120)
t.end_fill()
t.hideturtle()
