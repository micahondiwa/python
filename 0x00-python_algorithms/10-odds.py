'''
Prints odd numbers using the while loop
'''
i = 1
while i <= 20:
    if(i % 2) == 0:
        i += 1
        continue

        if i == 15:
            break

        print("odd :", i)
        i += 1