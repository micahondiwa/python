#!/usr/bin/python3

def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

    # Write your logic here

    return leap


year = int(input())
print(is_leap(year))
