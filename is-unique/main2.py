def hasOnlyUniqueChars(inputString):
    for i in range(len(inputString)-1):
        for k in range(i+1, len(inputString)):
            if inputString[i] == inputString[k]:
                return False

    return True
             

name = "ydaa"

print(hasOnlyUniqueChars(name))

