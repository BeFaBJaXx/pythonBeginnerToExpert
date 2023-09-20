import turtle as t
from random import randint, choice

# colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown"]
# Now instead of taking colors from list we'll generate random colors each time
t.colormode(255)
def colors():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return r, g, b


angle = [0,90,180,270]
t.pensize(10)
t.speed("fastest")
for _ in range(200):
    i = randint(0,7)
    t.color(colors())
    t.forward(20)
    t.right(angle[i%3])


t.exitonclick()