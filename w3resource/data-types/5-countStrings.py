"""
    5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
"""

my_list = ['abc', 'xyz', 'aba', '1221']

def countString(list_string):
    count = 0

    for string in list_string:
        len_string = len(string)

        first_caract = string[0]
        last_caract = string[-1]

        if len_string >= 2 and first_caract == last_caract:
            count += 1
        
    
    return count


print(countString(my_list))


"""
    SOLUTION: SAME
"""