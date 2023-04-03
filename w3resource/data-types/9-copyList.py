"""
    9. Write a Python program to clone or copy a list.
"""

my_list = [5,4,8,14,1]

def copyList(the_list):
    new_list = the_list.copy()

    return new_list


print("Original list:")
print(my_list)
print()
print("Copy list:")
print(copyList(my_list))


"""
    SOLUTION:
"""

# original_list = [10, 22, 44, 23, 4]
# new_list = list(original_list)
# print(original_list)
# print(new_list)