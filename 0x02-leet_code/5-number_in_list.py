"""
Given a list of umbers of unknown length,
return True if number 2 is in the list and False 
otherwise.
"""

def number_in_list(arr):
    for i in range(len(arr)):
        if i == 2:
            return True
        else:
            return False

arr1 = [3, 10, 7]
print(number_in_list(arr1))