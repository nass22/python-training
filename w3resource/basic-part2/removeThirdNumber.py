"""
    3. Write a Python program that removes and prints every third number from a list of numbers until the list is empty.
"""

# def removeNumbers(the_list: list):
#     length_list = len(the_list)
    
#     while not length_list == 0:
#         if length_list > 3:
#             print(the_list[2])
#             the_list.pop(2)
#             length_list = len(the_list)
#         elif length_list <= 3:
#             print(the_list[-1])
#             the_list.pop(-1)
#             length_list = len(the_list)


# removeNumbers([2,3,4,5,6,5,4,8,5])


"""
SOLUTION
"""

def remove_nums(int_list):
    position = 3 - 1 
    idx = 0
    len_list = (len(int_list))
    while len_list>0:
        idx = (position+idx)%len_list
        print(position+idx)
        print(int_list.pop(idx))
        
        len_list -= 1


nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)