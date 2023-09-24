from turtle import Turtle , Screen

'''Requirenments:-When pressed..
W:-Move forward, S:-Backwards,
A:-keep moving head into left side , D:-keep moving head into right side,
UP+RIGHT arrow:- circle on right from given point,
UP+left arrow:- circle on left from given point
C:-Clear'''

jimmy = Turtle()
screen = Screen()

jimmy.speed("fastest")

def W():
    jimmy.fd(1) 
def S():
    jimmy.backward(1)
def A():
    jimmy.lt(1)
def D():
    jimmy.rt(1)
def C():
    jimmy.clear()
    jimmy.pu()
    jimmy.seth(0)
    jimmy.setpos(0.0,0.0)
    jimmy.pd()
def call():
    screen.onkeypress(key="Left",fun = left_circle)
    screen.onkeypress(key="Right",fun=right_circle)

def left_circle():
    jimmy.lt(1)
    jimmy.fd(1)

def right_circle():
    jimmy.rt(1)
    jimmy.fd(1)    

screen.listen()
screen.onkeypress(key ="w",fun=W)
screen.onkeypress(key="s",fun=S)
screen.onkeypress(key="a", fun=A)
screen.onkeypress(key="d",fun=D)
screen.onkey(key="c", fun=C)
screen.onkeypress(key="Up",fun=call)

screen.exitonclick()