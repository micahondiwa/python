'''
The program creates a class named Robot.
The class have multiple methods and 2 objects to implement the methods.
'''
class Robot:
    """Represents a robot class, with a name."""
    population = 0

    def __init__(self, name):
        """Initilaizes the data"""
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """I am dying"""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))
    def say_hi(self):
        """Greeting by robbot.

        yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod

    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))

    @classmethod
    def how_manay(cls):
        pass


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_manay()