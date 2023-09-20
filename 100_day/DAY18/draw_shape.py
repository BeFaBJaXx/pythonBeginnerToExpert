import turtle as t

colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown"]

t.pu()
t.setpos(x=-10,y=100)
t.pd()
for i in range(3,11):
    for _ in range(i):
        t.pensize(i)
        t.color(colors[i-3  ])
        angle = 360/i
        t.forward(100)
        t.right(angle)


t.exitonclick()