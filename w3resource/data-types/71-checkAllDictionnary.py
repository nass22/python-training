"""
    71. Write a Python program to check whether all dictionaries in a list are empty or not.
"""

list1 = [{},{},{}]
list2 = [{1,2},{},{}]

def checkIfListEmpty(dictionnary):
    print(all(not item for item in dictionnary))


checkIfListEmpty(list1)
checkIfListEmpty(list2)

