def swapTwoNumber(a, b):
    a,b = b,a
    return a,b

a = 5
b = 10
print(f"a={a}, b={b}")
print(f"a={swapTwoNumber(a, b)[0]}, b={swapTwoNumber(a, b)[1]}")