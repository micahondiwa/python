'''
List comprehension
'''

# Example 1
import random
import math

even_list = [i*2 for i in range(10)]

for i in even_list:
    print(i)

# Example 2
number_list = [2, 4, 5, 6, 67]
list_of_values = [[math.pow(m, 2), math.pow(3, 3), math.pow(m, 4)]
                  for m in number_list]

for i in list_of_values:
    print(i)
print()

# Example 3
multi_D_list = [[0] * 10 for i in range(10)]
multi_D_list[0][1] = 1000
print(multi_D_list[0][1])

# Example 4
list_table = [[0] * 4 for i in range(4)]

for i in range(4):
    for j in range(4):
        list_table[i][j] = "{} : {}".format(i, j)

for i in range(4):
    for j in range(4):
        print(list_table[i][j], end= " |")
    print()

