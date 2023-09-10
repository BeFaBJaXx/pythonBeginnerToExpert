import os
from random import choice  
from art import logo 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def replay():
    playAgain = input("\nDo you want to play again? (y/N)").lower()
    if playAgain == 'y':
        clear()
        game()
    else:
        global check_flag
        check_flag = False
def attempts(difficulty):
    if difficulty == 'easy':
        return EASY
    elif difficulty == 'hard':
        return HARD
    
def check(number,numberOfAttempts):
    global check_flag
    check_flag = True
    while check_flag == True and numberOfAttempts >= 0:
        if numberOfAttempts>0: 
            makeAguess = int(input("make a guess : "))
        if makeAguess == number:
            print(f"You guessed it right ! The number was {number}")
            check_flag = False
            replay()
        elif numberOfAttempts >0:
             numberOfAttempts -= 1
             if makeAguess < number:
                 print("Too low.\nGuess again!")
             else:
                 print ("too high\nGuess Again!")
             print(f"You have left {numberOfAttempts} to guess the right number!!")
        else: 
            print(f"The correct answer was {number}")        
            check_flag = False
            replay()


def game():
    print(logo)
    global check_flag
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 to 100.")
    difficulty = input("Choose difficuly! Tyep 'easy' or 'hard': ").lower()
    number_range = range(1,101)
    # randint function could have been used here too!! randint(1,100).
    number  = choice(number_range)
    numberOfAttempts = attempts(difficulty)
    print(f"You have {numberOfAttempts} to guess the right number!!")
    check(number=number,numberOfAttempts=numberOfAttempts)
EASY = 10
HARD = 5
check_flag = True
clear()    
game()

