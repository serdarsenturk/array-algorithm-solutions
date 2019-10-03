# eğer uzunlukları eşitse sadece bir harf değiştirince aynı olup olmadıklarına bakabiliriz
def editForChar(stringOne, stringTwo):
    if len(stringOne) == len(stringTwo):
        return replaceCharacter(stringOne, stringTwo)
    elif len(stringOne)-1 == len(stringTwo):
        return insertCharacter(stringOne, stringTwo)
    elif len(stringOne)+1 == len(stringTwo):
        return insertCharacter(stringOne, stringTwo)

def replaceCharacter(s1, s2):
    similarCharacterNumber = 0

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            similarCharacterNumber += 1
            if similarCharacterNumber == len(s1)-1:
                return True

    return False

def insertCharacter(s1, s2):
    index1 = 0
    index2 = 0
    while index1 < len(s1) or index2 < len(s2):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
                index2 += 1
            else:
                index1 += 1
                index2 += 1
    return True


print(editForChar("pales", "pkle"))