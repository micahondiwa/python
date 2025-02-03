""" 
A function that adds two numbers and returns the sum in binary.
The conversion can be done before or after the addition.
The binary returned should be a string.
Examples:
1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
"""

def add_binary(a,b):
    sum = a + b

    if sum == 0:
        return 0
    
    binary = ""
    while sum > 0:
        remainder = sum % 2
        binary = str(remainder) + binary
        sum = sum // 2
    return binary

print(add_binary(5, 9))
