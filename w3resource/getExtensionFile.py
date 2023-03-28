"""
    7. Write a Python program that accepts a filename from the user and prints the extension of the file. Go to the editor
    Sample filename : abc.java
    Output : java
"""

def getExtension():
    user_input = input("Insert your filename: ")
    new_list = user_input.split(".")

    print("Filename: " + str(user_input))
    print("The extension of your file is: " + str(new_list[-1]))


getExtension()
