"""
    1. Write a Python program to sum all the items in a list.
"""

my_list = [1,20,40,489,47,5]

def sumOfArray(list_number):
    sum = 0
    for nb in list_number:
        sum += nb
    
    return sum


print(sumOfArray(my_list))

"""
    SOLUTION: SAME
"""
