""" 
A function that takes as argument a sequence and returns 
a list of items without any elements with the same value
next to each other and preserving the original order of elements.
Examples:
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
"""
def unique_in_order(sequence):
    unique = []

    for char in sequence:
        if not unique or char != unique[-1]:
            unique.append(char)
    return unique

sequence = unique_in_order('AAAABBBCCDAABBB')
print(unique_in_order(sequence=sequence))