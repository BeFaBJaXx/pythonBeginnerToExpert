import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game = [rock,paper,scissors]
choise = [1,2,3]
a = int(input("Choose 1 for rock , 2 for paper and 3 for  scissors\n"))
if choise.count(a) == 0:
    print("You loose!")
else:
    print("You've choose:\n")
    print(game[a-1])
    print("The computer has choose:\n")
    b = random.randint(1,3)
    print(game[b-1])
    if a == b-1 :
        print("you loose")
    elif a == b:
        print("draw")
    else:
        print("You Win")