"""
    70. Write a Python program to find items starting with a specific character from a list.
"""

my_list = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']

# def findItems(list_string):
#     result = []
#     userInput = input("Choose your letter: ")

#     for item in list_string:
#         if userInput == item[0]:
#             result.append(item)

#     print(result)

# findItems(my_list)

def findItemsWithStartsWith(list_string):
    result = []
    userInput = input("Choose your letter: ")

    for item in list_string:
        if item.startswith(userInput):
            result.append(item)
    
    print(result)

findItemsWithStartsWith(my_list)


"""
    SOLUTION
"""

# def test(lst, char):
#     result = [i for i in lst if i.startswith(char)]
#     return result


# text = ["abcd", "abc", "bcd", "bkie", "cder", "cdsw", "sdfsd", "dagfa", "acjd"]


# print("\nOriginal list:")
# print(text)
# char = "a"
# print("\nItems start with",char,"from the said list:")
# print(test(text, char))
# char = "d"
# print("\nItems start with",char,"from the said list:")
# print(test(text, char))
# char = "w"
# print("\nItems start with",char,"from the said list:")
# print(test(text, char))