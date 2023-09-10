print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# above print startement is an ASCII ART Search on google to know more JaXx

print("Welcome to Dragon Ball.")
print("Your mission is to find The Dragon Balls.")
c1 = input("Where do you wanna find it? On Earth or On Nemek\n")
choise1 = c1.lower()
if choise1 == 'earth':
  print("Your enemy ; who is stronger than you, find the DragonBalls before you and you loose. ")
else:
  c2 = input("Will you ask your friends to help you? yes or no ?\n")
  choise2 = c2.lower()
  if choise2 == 'no':
    print("Your enemy has more resoursces than you. He find those before you do!! You loose.")
  else:
    c3 = input("You want to use a ship (all friends are together) or you want to fly separately or you want to use Instant Transmission? ")
    choise3 = c3.lower()
    if choise3 =='ship' :
      print("You ran out of time")
    elif choise3 == 'instant transmission':
      print("You loose due to Lack of information")
    else:
      print("great choices! You win.")