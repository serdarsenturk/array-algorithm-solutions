def hasOnlyUniqueChars(stringInput):
    emptyDict = {}
    index = 0
    for i in stringInput:
        if i in emptyDict:
            return False
        else:
            emptyDict[i] = index
            print(emptyDict)
            index += 1
    return True

givenString = "marrie"
givenString = givenString.replace(" ", "")
givenString = givenString.lower()


print(hasOnlyUniqueChars(givenString))