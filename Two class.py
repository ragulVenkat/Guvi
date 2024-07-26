"""
3. From the given List create two class Methods Area and perimeter which will be going to calculate the Area and Perimeter

"""

# Class 1 - Rectangle

class Rectangle:
    def __init__(self, breadth, lenght):
        self.breadth = breadth
        self.lenght = lenght

    def area(self):
        area = self.breadth * self.lenght
        return area
    
    def perimeter(self):
        perimeter = 2 * (self.lenght + self.breadth)
        return perimeter
    
# Class 2 - Circle
    
class Circle:

    _pi = 3.141

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = Circle._pi * (self.radius **2)
        return area
    
    def perimeter(self):
        perimeter = 2 * Circle._pi * self.radius
        return perimeter
    
Venkat_1 = Rectangle(10, 20)
Venkat_2 = Circle(7)

print("Rectangle Area:", Venkat_1.area())          
print("Rectangle Perimeter:", Venkat_1.perimeter()) 

print("Circle Area:", Venkat_2.area())           
print("Circle Perimeter:", Venkat_2.perimeter()) 

