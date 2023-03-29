"""
    3. Write a Python program that accepts an integer and determines whether it is greater than 4^4 and which is 4 mod 34.
"""

def exercice3(number: int):
    return number > 4**4 and number%34 == 4


print(exercice3(922))
print(exercice3(914))
print(exercice3(854))


"""
    SOLUTION (SAME)
"""
