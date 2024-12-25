"""Reverse string module"""

def reverse_string(string):
    reversed_string = ""
    for i in range(len(string) -1, -1, -1):
        reversed_string += string[i]
    return reversed_string

print(reverse_string('HotChips'))
print(reverse_string("Hello world!"))