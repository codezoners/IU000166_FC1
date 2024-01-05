import turtle

t = turtle.Turtle()

def tree(depth, dist):
    width = dist / 10
    # We assume we're at the base of the trunk, pointing up:
    t.left(90); t.forward(width / 2); t.right(90)
    t.forward(dist); t.right(90); t.forward(width); t.right(90)
    t.forward(dist); t.right(90); t.forward(width / 2); t.right(90)

    # If we're branching, move to top and branch left and right:
    if depth > 0:
        t.penup()
        t.forward(dist)
        t.pendown()

        t.left(40)
        tree(depth - 1, dist / 1.5)
        t.right(80)
        tree(depth - 1, dist / 1.5)
        t.left(40)

        t.penup()
        t.backward(dist)
        t.pendown()

t.reset()
t.left(90)
t.speed("fastest")
tree(6, 100)
