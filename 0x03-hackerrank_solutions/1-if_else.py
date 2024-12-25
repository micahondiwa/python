#!/usr/bin/python3
"""Using if else statement to print weird and Not Weird"""


def weird(n):
    """A function to print based on conditions"""
    if n < 1:
        pass
    elif n % 2 != 0:
        print("Weird")
    elif n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
    elif n > 100:
        pass
    else:
        print("Not Weird")
        
"""generating random values and storing as n"""
n = int(input())
weird(n)
