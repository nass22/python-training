"""
145. Write a Python program to test if a variable is a list, tuple, or set. 
"""

thelist = [1, "Test", 4]
thetuple = (1,2,3,4)
theset = {1, "Hello", "Test"}

test_list = isinstance(thelist, list)
test_tuple = isinstance(thetuple, tuple)
test_set = isinstance(theset, set)

print(f"{thelist} is a list: {test_list}")
print(f"{thetuple} is a tuple: {test_tuple}")
print(f"{theset} is a set: {test_set}")