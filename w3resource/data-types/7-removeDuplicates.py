"""
    7. Write a Python program to remove duplicates from a list. 
"""

my_list = [1, 2, 2, 3, 4, 4, 5]

def removeDuplicate(the_list):
    new_list = []

    [new_list.append(x) for x in the_list if x not in new_list]

    return new_list


print(removeDuplicate(my_list))


"""
    SOLUTION:
"""

# a = [10,20,30,20,10,50,60,40,80,50,40]

# dup_items = set()
# uniq_items = []
# for x in a:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)

# print(dup_items)