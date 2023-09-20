import turtle as t

for i in range(0,20):
    if i%2 == 0:
        t.penup()
        t.forward(10)
    else:
        t.pendown()
        t.forward(10)

t.exitonclick()