from datetime import date
from datetime import time
from datetime import datetime

def main():
    ## Date Objects
    # #Get today's date from the simple today() method from the date class
    # today = date.today()
    # print("Today's date is ",today)

    # #print out the date's individual components
    # print("Date components: ",today.year,today.month,today.day)
    
    # #retrieve today's weekday 
    # print("Today's weekday# is: ",today.weekday())

    # day = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

    # print("Today is: ",day[today.weekday()])

    # Datetime Objects
    # Get today's date from the datetime class

    # today = datetime.today()
    # today1 = datetime.now()

    # print("Today's date is: ", today,today1)
    # #Get the current time
    # t = datetime.time(today)
    # print("Current time is ",t)

    ## Formating time and date output
    # now = datetime.now()

    # print(now.strftime("%I:%M:%S %p"))

    x = 123
    y = 123
    print(id(x))
    print(id(y))
    print(x==y)


if __name__ == "__main__":
    main()