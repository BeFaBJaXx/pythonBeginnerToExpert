# We'll learn to use even listner on space key!

import turtle as t


def move_fd(): 
    '''Note that function we are passing inside event listener is without any argument!!'''
    t.fd(20)

# first we need to get our screen to listen using following line
t.listen()
t.onkey(key="space",fun=move_fd)

t.exitonclick()