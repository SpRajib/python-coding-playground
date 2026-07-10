class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 22/7*self.radius**2

    def perimeter(self):
        return 2*22/7*self.radius

c1 = Circle(7)
print(f"Area of circle with radius {c1.radius} = {c1.area()}")
print(f"Perimeter of circle with radius {c1.radius} = {c1.perimeter()}")
