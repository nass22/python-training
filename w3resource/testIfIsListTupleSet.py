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


"""
RESPONSE
"""

# # x = ['a', 'b', 'c', 'd']
# # x = {'a', 'b', 'c', 'd'}

# x = ('tuple', False, 3.2, 1)
# if type(x) is list:
#     print('x is a list')
# elif type(x) is set:
#     print('x is a set')
# elif type(x) is tuple:
#     print('x is a tuple')    
# else:
#     print('Neither a list or a set or a tuple.')