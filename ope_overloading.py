class Student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return  self.marks + other.marks 
    def __sub__(self,other):
        return self.marks - other.marks
    def __mul__(self,other):
        return self.marks*other.marks
    def __truediv__(self,other):
        return self.marks/other.marks
s1 = Student(85)
s2 = Student(90)
print(s1+s2)
# print(s1-s2)
# print(s1*s2)
# print(s1/s2)
