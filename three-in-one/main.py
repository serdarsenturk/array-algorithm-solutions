def pushTheStackOne(stackOne):
    if len(stackOne) == 0:
        return "Empty"
    else:
        for i in range(len(stackOne)):
            arr.append(stackOne[i])
        return arr

def pushTheStackTwo(stackTwo):
    if len(stackTwo) == 0:
        return "Empty"
    else:
        for i in range(len(stackTwo)):
            arr.append(stackTwo[i])
        return arr

arr = []

print(pushTheStackOne([1, 2, 5, 6]))
print(pushTheStackTwo([10, 15, 25, 36]))

# Muhtemelen Yanlış anladım
