from turtle import Turtle , Screen

jimmy = Turtle()
# jimmy.shape("turtle")
print(jimmy.pos())
screen = Screen()

for i in range(0,4):
    jimmy.right(90)
    jimmy.forward(100)
    


screen.exitonclick()