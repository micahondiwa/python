import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    
    pos = len([i for i in arr if i > 0])
    neg = len([i for i in arr if i < 0])
    zer = len([i for i in arr if i == 0])
       
    print(pos / n)
    print(neg / n)
    print(zer / n)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
