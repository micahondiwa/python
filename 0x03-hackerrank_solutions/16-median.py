#!/user/bin/env python 3

'''
A function that returns the median value of an array.
'''

def medianValue(arr):
    arr = sorted(arr)
    n = len(arr)
    
    return (arr[n / 2 + 1] + arr[n / 2]) / 2 if n % 2 == 0 else arr[n // 2]
