def no_space(x):
    #your code here
    l = x.split()
    result = "".join(l)
    return result
print(no_space("hello world"))