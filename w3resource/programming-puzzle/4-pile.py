"""
    4. 4. We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile.
"""

count = 0
stack = 0

def exercice4(number: int):
    return [number+2 * i for i in range(number)]
    

print(exercice4(2))
print()
print(exercice4(10))
print()
print(exercice4(3))
print()
print(exercice4(17))
