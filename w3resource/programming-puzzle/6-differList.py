"""
    6. Write a Python program to test a list of one hundred integers between 0 and 999, which all differ by ten from one another. Return True otherwise False.
"""

def exercice6(my_list: list):
    y=0
    while y < len(my_list)-1:
        firstPos = my_list[y]
        z = y+1
        secondPos = my_list[z]

        if secondPos-firstPos == 10:
            y += 1
        else:
            return False
        
    
    return True
                

x = list(range(0, 1000, 10))
print(exercice6(x))
print()
y = list(range(0, 1000, 20))
print(exercice6(y))

"""
    SOLUTION
"""

"""
    Explanation:
    
    all() = Check if all items in a list are True
    abs() = return the absolute value and remove the negative sign of a number
"""

# def test(li):
#     return all(i in range(1000) and abs(i - j) >= 10 for i in li for j in li if i != j) and len(set(li)) == 100
# nums = list(range(0, 1000, 10))
# print("Original list:")
# print(nums)
# print("Check whether the said list contains one hundred integers between 0 and 999 which all differ by ten from one another:")
# print(test(nums))
# nums = list(range(0, 1000, 20))
# print("Original list:")
# print(nums)
# print("Check whether the said list contains one hundred integers between 0 and 999 which all differ by ten from one another:")
# print(test(nums))

