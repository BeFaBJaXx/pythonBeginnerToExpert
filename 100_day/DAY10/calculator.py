import art
def addition(n1,n2):
   return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2
art.cal()
n1 = float(input("Enter the first number: "))
operations = {
  '+' : addition,
  '-' : subtract,
  '*' : multiply,
  '/' : divide,
}

print("\nEnter an operation Symbol")
for operation in operations:
  print(operation)

opertaion_symbol = input("\nPick an operation from above :")
n2 = float(input("Enter the Second number: "))
function = operations[opertaion_symbol]
answer = function(n1,n2)

if opertaion_symbol not in operations:
    print("Enter a valid operator symbol")

print(f"\n{n1} {opertaion_symbol} {n2} = {answer}")

flag = input(f"Type 'y' to continue calculating with {answer} , type 'n' to exit: ").lower()
while(flag=='y'):
    opertaion_symbol = input("\nPick an operation from above :")
    function = operations[opertaion_symbol]
    n2 = float(input("\nEnter the number: "))
    n1 = answer
    answer = function(n1,n2)
    print(f"\n{n1} {opertaion_symbol} {n2} = {answer}")
    flag =input(f"Type 'y' to continue calculating with {answer} , type 'n' to exit: ").lower()