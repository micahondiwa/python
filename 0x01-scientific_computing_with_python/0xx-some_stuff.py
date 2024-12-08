class Calculator:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Object dimensions: length = {self.x}, Width = {self.y}'
    
    def area(self):
        return f'Area: {self.x * self.y}'
    
    def perimeter(self):
        return f'Perimeter: {self.x + self.y}'

object1 = Calculator(82, 69)

print(object1)
print(object1.area())
print(object1.perimeter())
    