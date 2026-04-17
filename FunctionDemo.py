def helloworld():
    print("Hello, World!")
    c=10+90
    print(c)
    print("bye")

def sum(num1,num2):
    c=num1+num2
    print("Sum is:",c)
    return c

# print(sum(10,20))
# helloworld()

def sum(num1, num2=10):
    c = num1 + num2
    return c

result = sum(50)
print("Result is:", result)

def sum(a,b,c=0,d=0):
    total = a + b + c + d
    return total

result = sum(10,20,30) # c takes 30, d takes default 0
print("Result is:", result)

def greetings(fname, lname):
    print("Hello,", fname, lname)

greetings("Rajib", "Sahoo")
greetings(lname="Sahoo", fname="Rajib")