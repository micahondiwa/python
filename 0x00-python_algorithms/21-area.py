'''
A function to claculate the area of different shapes
'''

import math

def get_area(shape):
    shape = shape.lower

    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please enter rectangle or circle")

    def rectangle_area():
        length = float(input("Enter length: "))
        width= float(input("Enter width: "))

        area = length * width
        print("The area of the rectangle is: ", area)

    def circle_area():
        radius = float(input("Enter radius: "))

        area = math.pi * (math.pow(radius, 2))
        print("The area of the circle is {:.2f".format(area))
