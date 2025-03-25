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
    __slots__ = ('__speed', '__height', '__angle')

    def __init__(self, speed, height, angle):
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)
        
    def __calculate_displacement(self):
        g = GRAVITATIONAL_ACCELERATION
        d = (self.__speed * math.cos(self.__angle) * (self.__speed * math.sin(self.__angle) + math.sqrt(self.__speed ** 2 * math.sin(self.__angle)**2 + 2 * g * self.__height))) / g
        return d 
