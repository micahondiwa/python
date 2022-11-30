'''
The Buble sort algorith:

An outer loop decreases in size each time
The goal is to have the largest number at the end of
the list when the outer loop completes 1 cycle
The inner loop starts comparing indexes at the beginning of the loop
check if list[index] > list[index + 1]
if so swap the index values
when the inner loop completes the largest number is at the end of
the list.
Decrement the outer loop by 1
'''
import random
import math

number_list = []
for i in range(5):
    number_list.append(random.randrange(1, 10))

i = len(number_list) - 1

while i > 1:
    j = 0

    while j < i:
        print("\nIs {} > {}".format(number_list[j], number_list[j + 1]))
        if number_list[j] > number_list[j + 1]:
            print("Switch")
            temp = number_list[j]
            number_list[j] = number_list[j + 1]
            number_list[j + 1] = temp

        else:
            print("Dont switch")

            j += 1

            for k in number_list:
                print(k, end= ", ")

    print("END OF ROUND!")
    i -= 1

for k in number_list:
    print(k, end= ", ")
print()