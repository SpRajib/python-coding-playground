class A:
    def hello(self):
        print("Hello from class A")

class B(A): # Inheriting from class A
    def hello(self): # Method overriding
        print("Hello from class B")

class C(B): # Inheriting from class B
    def hello(self): # Method overriding
        print("Hello from class C")

obj1 = B()
obj1.hello()  # Output: Hello from class B

obj2 = A()
obj2.hello()  # Output: Hello from class A