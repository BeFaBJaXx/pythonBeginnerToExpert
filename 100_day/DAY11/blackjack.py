import os
import random
from art import logo
print(logo)
def pickWinner(user_sum, computer_sum):
    if user_sum<computer_sum:
        return "Dealer (Computer) wins!!"
    elif user_sum == computer_sum:
        return "It's a Draw!!"
    else:
        return "Congratulations!! You Win!!"
    
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

game_flag = input("Do you want to play a game of BlackJack? Type 'y' or 'n': " ).lower()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def pick_card():
    random.shuffle(cards)
    card = random.choice(cards)
    return card

def sum(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum
            
while(game_flag == 'y'):
    clear()
    user = []
    computer = []
    for i in range (0,2):
        playerCard = pick_card()
        user.append(playerCard)
    print(f"your cards are: {user}")
    for i in range (0,2):
        computerCard = pick_card()
        computer.append(computerCard)
    print(f"Dealers cards are: {computer[0],'X'}")
    sum_user = sum(user)
    sum_computer = sum(computer)
    hit_flag = True
    while hit_flag == True:
         if sum_user < 21:
            hit = input("Hit? Type 'yes' to pic another card!!  'No' to pass :").lower()
            if hit == 'yes':
                playerCard = pick_card()
                user.append(playerCard)
                sum_user = sum(user)
            hit_flag = False
    print(f"your cards are: {user}")
    print(f" Your score is : {sum_user}")
    print(f"Dealers cards are: {computer}")
    print(f" Dealer's score is : {sum_computer}")
    if sum_user > 21:
                    print("Busted!!")
                    game_flag = 'n'
    else:
        winner = pickWinner(sum_user,sum_computer)
        print(winner)
        game_flag = input("Would you like to play again? Type 'y' or 'n': " ).lower()
