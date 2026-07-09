'''
class Students:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    
    def average(self):
        return (self.sub1 + self.sub2 + self.sub3) / 3
    
s1 = Students("Alice", 85, 90, 95)
print(f"Average marks of {s1.name} = {s1.average()}")

s2 = Students("Bob", 78, 82, 88)
print(f"Average marks of {s2.name} = {s2.average()}")
'''

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)
    
s1 = Student("Alice", [85, 90, 95])
print(f"Average marks of {s1.name} = {s1.average()}")

s2 = Student("Bob", [78, 82, 88])
print(f"Average marks of {s2.name} = {s2.average()}")