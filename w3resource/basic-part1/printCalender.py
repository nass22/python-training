"""
    12. Write a Python program that prints the calendar for a given month and year.
    Note : Use 'calendar' module.
"""

import calendar

year = int(input("Year: "))
month = int(input("Month: "))

calendar = calendar.month(year, month)

print(calendar)