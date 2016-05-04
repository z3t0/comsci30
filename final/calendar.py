import datetime

# let's me make up objects
class Foo(object):
    pass

def get_input():
    year = -1
    month = -1
    day = -1

    while(year > 9999 or year < 1):
        year = int(raw_input("Enter the year: "))

    while(month > 12 or month < 1):
        month = int(raw_input("Enter Month(January = 1, February = 2 etc...): "))

# February
    if(month == 2):
        if (year % 4 == 0): # Leap Year
            while(day < 0 or day > 29):
                day = int(raw_input("Enter the day of the month: "))
        else: #Not a leap year
            while(day < 0 or day > 28):
                day = int(raw_input("Enter the day of the month: "))

# 31 Day months
    elif (month == 1 or month == 3 or month == 5 or month ==  7 or month == 8 or month == 10 or month == 12):
        while(day < 0 or day > 31):
            day = int(raw_input("Enter the day of the month: "))

# 30 Day months
    else:
        while(day < 0 or day > 30):
            day = int(raw_input("Enter the day of the month: "))


    input = Foo();

    input.year = year
    input.month = month
    input.day = day

    return input

# Get User Input
input = get_input()

d = datetime.date(input.year, input.month, input.day)

print "-----"

if d.weekday() == 0:
    print str(d) + " is a Monday: \t TRUE"
else:
    print str(d) + " is a Monday: \t FALSE"

if d.weekday() == 1:
    print str(d) + " is a Tuesday: \t TRUE"
else:
    print str(d) + " is a Tuesday: \t FALSE"

if d.weekday() == 2:
    print str(d) + " is a Wednesday: \t TRUE"
else:
    print str(d) + " is a Wednesday: \t FALSE"

if d.weekday() == 3:
    print str(d) + " is a Thursday: \t TRUE"
else:
    print str(d) + " is a Thursday: \t FALSE"

if d.weekday() == 4:
    print str(d) + " is a Friday: \t TRUE"
else:
    print str(d) + " is a Friday: \t FALSE"

if d.weekday() == 5:
    print str(d) + " is a Saturday: \t TRUE"
else:
    print str(d) + " is a Saturday: \t FALSE"
if d.weekday() == 6:
    print str(d) + " is a Sunday: \t TRUE"
else:
    print str(d) + " is a Sunday: \t FALSE"

print "-----"

if d.weekday() > 4:
    print str(d) + " is a weekday: \t FALSE"
    print str(d) + " is on the weekend: \t TRUE"

else:
    print str(d) + " is a weekday: \t TRUE"
    print str(d) + " is on the weekend: \t FALSE"

# print input.__dict__
