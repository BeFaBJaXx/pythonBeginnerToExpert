from turtle import Turtle,Screen

jimmy = Turtle()
jimmy.shape("turtle")
jimmy.color("red")
jimmy.fillcolor("yellow")
jimmy.begin_fill()
while True:
    jimmy.forward(200)
    jimmy.left(170)
    if abs(jimmy.pos()) <1:
        break

jimmy.end_fill()




screen = Screen()
screen.exitonclick()