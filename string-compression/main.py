def stringCompression(stringInput):
    compString = "" 
    count = 1
    for i in range(len(stringInput)-1):
        if stringInput[i] == stringInput[i+1]:
            count += 1
        else:
            compString += stringInput[i] + str(count)
            count = 1
        
        compString += stringInput[i] + str(count)

    if len(compString) >= len(stringInput):
        return stringInput
    else:
        return compString

print(stringCompression("aabcccccaaa"))