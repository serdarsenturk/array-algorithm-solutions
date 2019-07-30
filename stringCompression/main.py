def stringCompression(stringInput):
    compString = "" 
    sayac = 1
    for i in range(len(stringInput)-1):
        if stringInput[i] == stringInput[i+1]:
            sayac += 1
        else:
            compString += stringInput[i] + str(sayac)
            sayac = 1

    compString += stringInput[i] + str(sayac)

    if len(compString) >= len(stringInput):
        return stringInput
    else:
        return compString

print(stringCompression("aabcccccaaa"))
