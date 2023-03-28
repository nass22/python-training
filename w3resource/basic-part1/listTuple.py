"""
    4. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers. Go to the editor
    Sample data : 3, 5, 7, 23
    Output :
    List : ['3', ' 5', ' 7', ' 23']
    Tuple : ('3', ' 5', ' 7', ' 23')
"""

def createListTuple():
    user_input = input("Insert your data separated by a comma: ")

    split_in_list = user_input.split(",")
    split_in_tuple = tuple(split_in_list)

    print("List: " + str(split_in_list))
    print("Tuple: " + str(split_in_tuple))


createListTuple()