def hasOnlyUniqueChars(givenString):

    charSet = [False] * 26
    for k in range(len(st)):
        charIndex = ord(st[k]) - ord('a')
    
        if charSet[charIndex] == True:
            return False
        else:
            charSet[charIndex] = True

    return True
            
st = "sinem"

print(hasOnlyUniqueChars(st))