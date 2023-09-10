import os
import art
from gamedata import data
from random import randint

game_flag = True
i =49
current_score = 0

def clear():
    os.system('cls')

def pick():
    global i
    a = randint(0,i)
    sample = data.pop(a)
    name = sample['name']
    description = sample['description']
    country = sample['country']
    follower_count = sample['follower_count']
    i -= 1
    return name , description , country , follower_count

def game():
        clear()
        print(art.logo)
        A = pick()
        print(f"Compare A: {A[0]},a {A[1]},from {A[2]}")
        print(art.vs)    
        B = pick()
        print(f"Compare B: {B[0]},a {B[1]},from {B[2]}")
        check(A,B)
        
def check(A,B):    
    global current_score
    guess = input("Who as more followers? 'A' or 'B': ").lower()
    global game_flag
    while game_flag == True:
        if guess == 'a':
            if A[3] >= B [3]:
                current_score += 1
            else:
                print("that's wrong🥲,final score is: ",current_score)
                game_flag = False
                break
        elif guess == 'b':
            if A[3] <= B [3]:
                current_score += 1
            else:
                game_flag = False        
                print("that's wrong🥲,final score is: ",current_score)
                break
        else:
            game_flag = False
            print("that's wrong🥲,final score is: ",current_score)
            break
        A = B
        clear()
        print(f"Thats right!,Your current score is: {current_score}")
        print(art.logo)
        print(f"Compare A: {A[0]},a {A[1]},from {A[2]}")
        B = pick()
        print(art.vs)
        print(f"Compare B: {B[0]},a {B[1]},from {B[2]}")
        check(A,B)
        
game()    