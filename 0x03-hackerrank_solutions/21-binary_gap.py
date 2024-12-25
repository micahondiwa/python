#!/bin/user/python3
"""
    Takes a number N, convers to binary, determines the length of
    binary gap (the number of consecutive zeros), and returns the 
    maximum binary length. 
    """


def solution(N):
    binaryN = bin(N)[2:]
    maxGap = 0
    minGap = 0
    for i in binaryN:
        if i == '1':
            if minGap > maxGap:
                maxGap = minGap
            minGap = 0
        else:
            minGap += 1
    return maxGap


'''An example'''
print("Binary gap of {}: ".format(8), solution(8))
print("Binary gap of {}: ".format(9), solution(9))
print("Binary gap of {}: ".format(529), solution(529))
