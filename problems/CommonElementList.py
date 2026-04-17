def CommonElement(l1,l2):
    newList = [set(l1) & set(l2)]

    return newList
l1 = [1,2,3,4]
l2 = [2,4,5,6,7]
print(CommonElement(l1,l2))