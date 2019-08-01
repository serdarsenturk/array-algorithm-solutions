givenString = "marrie"
givenString = givenString.replace(" ", "")
givenString = givenString.lower()

emptyDict = dict()



def isUnique(stringInput):
    index = 0
    for i in givenString:
        if i in emptyDict:
            return False
        else:
            emptyDict[i] = index
            print(emptyDict)
            index += 1
    return True

print(isUnique(givenString))