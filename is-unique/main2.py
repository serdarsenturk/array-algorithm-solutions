name = "hydaa"

name = name.lower()
name = name.replace(" ", "")
name = "".join(sorted(name))


def isUnique(inputString):
    for i in range(len(inputString)-1):
        for k in range(i+1, len(inputString)):
            if inputString[i] == inputString[k]:
                return False
            else:
                return True

print(isUnique(name))                   #Daha fazla düzenlenebilir
        

