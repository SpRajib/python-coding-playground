def invert(lst):
    a = []

    for num in lst:
        a.append(-num)

    return a
print(invert([1, 2, 3, 4, 5]))