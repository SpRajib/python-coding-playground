class classA:
    def methodA(self):
        print("Method A from class A")

    def hello(self):
        print("Hello from class A")

class classB:
    def methodB(self):
        print("Method B from class B")
    
    def hello(self):
        print("Hello from class B")

class classC(classA, classB):  # Inheriting from classA and classB
    def methodC(self):
        print("Method C from class C")

c = classC()  # Creating object of classC
c.methodA()  # Calling method of classA
c.methodB()  # Calling method of classB
c.methodC()  # Calling method of classC
c.hello()    # Calling method, should call from classA due to MRO - Method Resolution Order - first parent listed - classA
print(classC.__mro__)  # Print the Method Resolution Order