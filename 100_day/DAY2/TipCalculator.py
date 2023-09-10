print("Welcome to the tip calculator.")
b = input("What was the total bill? $")
total_bill = float(b)
tip = float(input("What percentage tip would you like to give? 10 ,12 ,15 ? "))
bill_person = (total_bill*(100+tip)/100) / 5
bill = round(bill_person , 2)
print(bill)