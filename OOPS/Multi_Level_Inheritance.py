class classA:
    def methodA(self):
        print("Method A from class A")

    def Hello(self):
        print("Hello from class A")

class classB(classA):  # Inheriting from classA
    def methodB(self):
        print("Method B from class B")

    def Hello(self):
        print("Hello from class B")

class classC(classB):  # Inheriting from classB
    def methodC(self):
        print("Method C from class C")

c = classC()  # Creating object of classC
c.methodC()  # Calling method of classC
c.methodB()  # Calling method of classB
c.methodA()  # Calling method of classA
c.Hello()    # Calling overridden method, should call from classB