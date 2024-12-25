"""
Given an array of integers, return indices of
the two numbers such that they add up to a
specific target.
"""

def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == target - arr[j] and j != i:
                return i, j 

print(two_sum([3,2,4], 6))
