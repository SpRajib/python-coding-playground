class person:
    # def __init__(self,fname, lname):
    #     print("Hello,", fname, lname)

    def __init__(self,f, l): # constructor with parameters
        self.fname = f # instance variable
        self.lname = l # instance variable
        print("Hello,", self.fname, self.lname) # constructor body


    def sum(self, a, b):
        self.v1=a
        self.v2=b
        return self.v1 + self.v2

x = person("Rajib", "Sahoo") # creating object of class person with parameters
# When an object of class person is created, the __init__ method is automatically called, printing "Hello Python". 
print(x.sum(10,20))

