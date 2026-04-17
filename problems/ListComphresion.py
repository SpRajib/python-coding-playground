def ListComphresion(l1):
    even = []
    for x in l1:
        if x%2 == 0:
            even.append(x)
    return even

     # OR   
        
    evens = [x for x in l1 if x%2 == 0]
    return evens

l1 = [1,2,3,4,5,6,7,8,9]
print(ListComphresion(l1))