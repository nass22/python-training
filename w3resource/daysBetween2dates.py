"""
    14. Write a Python program to calculate the number of days between two dates.
    Sample dates : (2014, 7, 2), (2014, 7, 11)
    Expected output : 9 days
"""
from datetime import date

def calculateDays(date1, date2):
    if date2 > date1:
        diff = date2-date1
    else:
        diff = date1-date2
    
    print("The numbers of days between yours dates is: " + str(diff.days))


firstDate = date(2014, 7, 2)
secondDate = date(2014, 7, 11)

calculateDays(firstDate, secondDate)