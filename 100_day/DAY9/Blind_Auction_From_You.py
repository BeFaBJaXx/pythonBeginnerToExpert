import os
from art import logo

os.system('cls' if os.name == 'nt' else 'clear')
print(logo)
print("Welcome to the secret bidder program!")
flag = True
name =[]
bid = []
while flag == True:
    name_ele = input("What is your name : ")
    bid_ele = int(input("What's your bid : "))
    name += [name_ele]
    bid += [bid_ele]

    f = input("Are there any other bideers? yes or no : ").lower()
    if f == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        continue  
    else:
        flag = False     
        m = max(bid)
        i = bid.index(m)
        winner  = name[i]
        print(f"The winner is {winner} for {m} amount!")