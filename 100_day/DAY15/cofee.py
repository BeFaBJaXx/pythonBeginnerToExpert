from data import MENU,resources,remain

is_off = True
tresure = 0

def cost(choice):
    global tresure
    money = MENU[choice]["cost"]
    print("Please enter coins below!!")
    q=int(input("How many Quaters? : "))
    d=int(input("How many Dimes? : "))
    n=int(input("How many Nickles? : "))
    p=int(input("How many Pennys? : "))
    amount  = q*0.25 +d*0.1 +n*0.05 + p*0.01 
    if amount<money:
        print("Sorry! Not enough Money!😣")
    else:
        tresure += money 
        change = amount - money
        change = round(change,2)
        print("Here is {} in change.".format(change))
        print("Here is your {}☕ Enjoy!!.".format(choice))
        

def coffee(choice):
    for resource in resources:
        need = MENU[choice]["ingredients"][resource]
        have = remain[resource]
        if need>have:
            print( "Sorry! We don't have enough {}".format(resource))
            return
        else:
            remain[resource] = have-need
    cost(choice)

def response(choice):
    if choice == "report":
        print('Water: {}ml'.format(remain["water"]))
        print('Milk : {}ml'.format(remain["milk"]))
        print('Coffee : {}g'.format(remain["coffee"]))
        print("Money : ${}".format(tresure))
        
    else:
        coffee(choice)


while(is_off):
    choice = input("What would you like? (espresso/latte/cappuccino) : ").lower()
    if choice == 'off':
        is_off = False
        break
    else:
        response(choice)