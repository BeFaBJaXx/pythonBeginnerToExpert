from sys import exit
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
operation = ['encode','decode']
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

def check(direction):
   if direction not in operation:
      print("Wrong operation")
      run_again()
      

def run_again():
    restart = input("Type 'yes' to go again\n 'No' to stop : ").lower()    
    if restart == "yes":
      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
      check(direction)
      text = input("Type your message:\n").lower()
      shift = int(input("Type the shift number:\n")) 
      ceaser(direction,text,shift)
      run_again()
    else:
       exit()

def ceaser(direction, text, shift):
      message = ""
      if direction == "decode":
         shift *= -1
      for char in text:
         if char in alphabet:
            position = alphabet.index(char) + shift
            message += alphabet[position%26]
         else:
            message += char
      print(f"The {direction}d message is : {message}")


check(direction)
   
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n")) 
ceaser(direction , text, shift)
run_again()  
