from turtle import Turtle,Screen
from random import choice,randint

game_flag = False

screen = Screen()
screen.setup(width=500,height=400)
screen.setworldcoordinates(llx=0.0,lly=0.0,urx=500,ury=400)
colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown"]
guess = screen.textinput(title= "Pick a Turtle", prompt= "Enter the turtle's number who would win the race")
if guess:
    game_flag = True

def pick_color():
    return choice(colors)

def create_turtles(name,k):
    name = Turtle(shape="turtle")
    name.pu()
    name.color(colors[k])
    y = 20 + k*50 
    name.setpos(x=10,y=y)
    return name

turtles = []

for i in range(8):
    turtles.append(create_turtles(name=colors[i],k=i))

while game_flag:
    for i in range(0,8):
        if turtles[i].xcor() <= (480.0):
            turtles[i].fd(randint(1,10))
            if turtles[i].xcor() >=(480.0):
                winner = turtles[i]
                game_flag = False
        else:
            winner = turtles[i]
            game_flag = False

pick_winner = turtles.index(winner)
name = colors[pick_winner]

if guess == name:
    print("You won the bet!")
else:
    print ("Sorry! You lost your money.Winner was {}".format(name))
screen.exitonclick()