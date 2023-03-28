"""
142. Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of same length in a given string. Return True/False.
Original sequence: 01010101
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
True
Original sequence: 00
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
False
Original sequence: 000111000111
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
True
Original sequence: 00011100011
Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
False
"""


"""
WARNING: here I don't look if the sequences are 0 or 1, but just if the sequences are the same!
"""
def checkSequence(sequence):
    listSequence = []
    lengthSequence = []
    
    for num in sequence:
        listSequence.append(num)

    current_number = listSequence[0]
    count = 0
    lengthList = len(listSequence)
    cursor = 0 

    for number in listSequence:
        cursor += 1
        if number == str(current_number):
            if cursor != lengthList:
                count += 1
            else:
                count += 1
                lengthSequence.append(count)
        elif number != str(current_number):
            if cursor != lengthList:
                lengthSequence.append(count)
                count = 0
                current_number = number
                count += 1
            else:
                lengthSequence.append(count)
                count = 0
                current_number = number
                count += 1
                lengthSequence.append(count)

    firstSeq = lengthSequence[0]
    boolSeq = True

    for seq in lengthSequence:
        if seq != firstSeq:
            boolSeq = False
            break

    return boolSeq


testSequence="01010101"
x = checkSequence(testSequence)

print(x)