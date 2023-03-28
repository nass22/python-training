"""
    11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
    Sample function : abs()
    Expected Result :
    abs(number) -> number
    Return the absolute value of the argument.
"""

def sumOfInteger(x:int, y:int):
    """This function return the sum of 2 integers"""

    result = x+y

    return result

print(sumOfInteger.__doc__)