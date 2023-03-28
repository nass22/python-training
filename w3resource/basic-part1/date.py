"""
    3. Write a Python program to display the current date and time.
    Sample Output :
    Current date and time :
    2014-07-05 14:34:14
"""

# from datetime import datetime

# now = datetime.now()

# datetime = now.strftime("%Y-%m-%d %H:%M:%S")

# print(datetime)

# CORRECTION:

import datetime

now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))