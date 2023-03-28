

def printIntegers():
    i = 1

    while i <= 99:
        if(i%3 == 0 and i%7 == 0):
            print(str(i) + "- OpenSource")
        elif(i%3 == 0):
            print(str(i) + "- Open")
        elif(i%7 == 0):
            print(str(i) + "- Source")
        
        i += 1

printIntegers()
