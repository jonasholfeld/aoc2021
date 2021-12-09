def solveCode(inputString):
    mapping = {
        0: "",
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
        8: "",
        9: "",
    }
    input = sorted(inputString.split(), key=len)
    solvedmappings = 0
    while solvedmappings < 10:
        valuesToRemove = []
        for digit in input:
            if len(digit) == 2:
                mapping[1] = digit
                solvedmappings +=1
                valuesToRemove.append(digit)
                ##print('solved 1')
            elif len(digit) == 3:
                mapping[7] = digit
                solvedmappings +=1
                valuesToRemove.append(digit)
                #print('solved 3')
            elif len(digit) == 4:
                mapping[4] = digit
                solvedmappings +=1
                valuesToRemove.append(digit)
                #print('solved 4')
            elif len(digit) == 7:
                mapping[8] = digit
                solvedmappings +=1
                valuesToRemove.append(digit)
                #print('solved 8')
            elif(mapping[1] != "") and mapping[6] != "" and (len(digit) == 5):
                if all(letter in split(digit) for letter in split(mapping[1])):
                    mapping[3] = digit
                    solvedmappings +=1
                    valuesToRemove.append(digit)
                    #print('solved 3')
                elif all(letter in split(mapping[6]) for letter in split(digit)):
                    mapping[5] = digit
                    solvedmappings +=1
                    valuesToRemove.append(digit)
                    #print('solved 5')
                else:
                    mapping[2] = digit
                    solvedmappings +=1
                    valuesToRemove.append(digit)
                    #print('solved 2')
            elif(mapping[1] != "") and (len(digit) == 6):
                if all(letter in split(digit) for letter in split(mapping[4])):
                    mapping[9] = digit
                    solvedmappings +=1
                    valuesToRemove.append(digit)
                    #print('solved 9')
                elif all(letter in split(digit) for letter in split(mapping[1])):
                    mapping[0] = digit
                    solvedmappings +=1
                    valuesToRemove.append(digit)
                    #print('solved 0')
                else:
                    mapping[6] = digit
                    solvedmappings +=1
                    valuesToRemove.append(digit)
                    #print('solved 6')
        for value in valuesToRemove:
            input.pop(input.index(value))
    return mapping

def split(word):
    return [char for char in word]

def decode(letters, mapping):
    if all(letter in mapping[1] for letter in split(letters)):
        return 1
    if all(letter in mapping[7] for letter in split(letters)):
        return 7
    if all(letter in mapping[4] for letter in split(letters)):
        return 4
    if all(letter in mapping[2] for letter in split(letters)):
        return 2
    if all(letter in mapping[3] for letter in split(letters)):
        return 3
    if all(letter in mapping[5] for letter in split(letters)):
        return 5
    if all(letter in mapping[0] for letter in split(letters)):
        return 0
    if all(letter in mapping[6] for letter in split(letters)):
        return 6
    if all(letter in mapping[9] for letter in split(letters)):
        return 9
    if all(letter in mapping[8] for letter in split(letters)):
        return 8