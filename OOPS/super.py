class BaseClass:
    def hello_world(self):
        print("Hello from BaseClass")

    def bye(self):
        print("Bye from BaseClass")

class childClass(BaseClass):
    def hello_world(self):
        super().hello_world()  # Calling the method from BaseClass
        BaseClass.hello_world(self)  # Another way to call the method from BaseClass
        print("Hello from childClass")
        super().bye()          # Calling another method from BaseClass

obj = childClass() 
obj.hello_world()  # This will call the overridden method in childClass