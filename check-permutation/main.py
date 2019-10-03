def checkPermutation(per1 , per2):

    if len(per1) != len(per2):
        return False
    
    per1 = ' '.join(sorted(per1))
    per2 = ' '.join(sorted(per2))
    print(per1)
    print(per2)

    n = len(per1)

    for i in range(n):
        if per1[i] != per2[i]:
            return False
    return True

print(checkPermutation("god", "dog"))