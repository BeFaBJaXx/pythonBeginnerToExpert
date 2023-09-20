from color_extraction import rgb_list
from random import choice
import turtle as t

t.speed("fastest")
t.screensize(450,450)
t.setworldcoordinates(0.0,0.0,450.0,450.0)
t.setpos(0.0,0.0)
t.colormode(255)
t.hideturtle()

while t.pos() != (450.0,450.0):
    t.pd()
    t.dot(20,choice(rgb_list))
    t.pu()
    if t.xcor() != (450.0):
        t.fd(50)
    else:
        y = t.ycor()+50.0       
        t.setpos((0.0,y))
    
t.dot(20,choice(rgb_list))

t.exitonclick()
