def findDuplicate(l):
    duplicate = []
    for ele in l:
        if ele not in duplicate:
            duplicate.append(ele)
    return duplicate

ls = [1, 2, 3, 4, 5, 2, 3, 6]
print(findDuplicate(ls))