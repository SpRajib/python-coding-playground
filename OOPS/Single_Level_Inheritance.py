class base:
    name = "Rajib"
    def MotherMethod(self):
        self.name = "Rajib"
        print("I am in Mother class")

class child(base):  # inheritance
    company = "Google"
    def ChildMethod(self):
        self.company = "Google"
        print("I am in Child class")

c = child()  # creating object of child class
c.ChildMethod()  # calling method of child class
c.MotherMethod()  # calling method of mother class using child class object
print(c.name)  # accessing property of base class using child class object
print(c.company)  # accessing property of base class using child class object