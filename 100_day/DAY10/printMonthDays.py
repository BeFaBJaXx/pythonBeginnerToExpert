def is_leap(year):
    '''This will return weather a year is leap year or not.'''
    if year % 4 == 0:
        return True
    else:
        return False
    
def month_days(year,month):
    '''This will return the number of days in a month.'''
    if is_leap(year) and month == 2:
        return 29
    if month % 2 == 0:
        if month == 2:
            return 28
        return 30
    else:
        return 31
    
print(month_days(int(input("Enter the year")),int(input("Enter the month"))))
