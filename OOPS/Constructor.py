class A:
    def __init__(self):
        print("Constructor of class A")

class B(A):  # Inheriting from class A
    def __init__(self):
        super().__init__()  # Calling the constructor of class A
        print("Constructor of class B")

class C(B):  # Inheriting from class B
    def __init__(self):
        super().__init__()  # Calling the constructor of class B
        print("Constructor of class C")

obj = C()  # Creating object of class C, which will call the constructors in order
