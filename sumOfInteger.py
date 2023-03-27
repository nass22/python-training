list = ["aaaa", "2", "bb", "3"]
new_list = []


def sumOfIntegers(list: list):
    result = 0

    for elem in list:
        try:
            elem = int(elem)
        except:
            continue
        else:
            new_list.append(elem)
    
    for elem in new_list:
        result += elem
    
    print(result)

sumOfIntegers(list)



