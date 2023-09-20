import turtle as t
from random import randint

t.speed("fastest")
t.colormode(255)

def pick_colors():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

for _ in range(72):
    t.color(pick_colors())
    t.circle(100)
    t.left(5)



t.exitonclick()