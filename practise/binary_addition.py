def add_binary(a,b):
    #your code here
    r = a+b
    return bin(r)[2:] # 2: removes the '0b' prefix from the binary representation

print(add_binary(1,1))
print(add_binary(5,9))