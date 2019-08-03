
def hasOnlyUniqueChars(givenString):
    givenString = sorted(givenString)
    for i in range(len(givenString)-1):
        
        if givenString[i] == givenString[i+1]:
            return False
        
    return True
        

print(hasOnlyUniqueChars("engi"))