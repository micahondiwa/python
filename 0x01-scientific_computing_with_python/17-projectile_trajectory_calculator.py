"""
Implenting encapsulation by building a program that calculates and draws the trajectory of a projectile 
given the angle, speed and height of the throw
Encapsulation is a core OOP principle based on writing code that limits direct access to data.
"""
import math

GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"

class Projectile:

    def __init__(self, speed, height, angle):
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)
    
    __slots__ = ("__speed", "__height", "__angle")
