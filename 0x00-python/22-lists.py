'''
Implementing lists in python
'''
import random
import math

radom_list = ["string", 1.234, 25, True]
oneToTen = list(range(10))
randlist = random_list + oneToTen
print(randlist[0])
print("List length: ", len(randlist))

first3 = randlist[3]
for i in first3:
    print("{} : {}".format(first3.index(i), i))

