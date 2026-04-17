class person: # class

    def Hello_class(self):  # method
        print("Hello from class person")

    def sum(self, a, b):  # method with parameters
        print(a + b)

def hello_function(): # function
    print("Hello from function hello_function")

p=person() # creating object of class person
p.Hello_class() # calling method of class person
hello_function()

print(hello_function) # prints the memory address of the function
print(p.Hello_class) # prints the memory address of the method

p.sum(10,20) # calling method with parameters
person.sum(p,30,40) # calling method with parameters by passing object as first argument

p.name = "Rajib" # adding property to object
p.phone = "1234567890" # adding property to object
p.city  = "New York" # adding property to object

q=person()
q.name = "Alice" # adding property to another object
q.phone = "0987654321" # adding property to another object
q.city  = "Los Angeles" # adding property to another object

print(p.name, p.phone, p.city) # accessing properties of object p
print(q.name, q.phone, q.city) # accessing properties of object q