'''
Asks user to enter 2 numbers and store them as num1 and num2
convert the numbers to inters
Calculates the sum, difference, product, quatient, modulus
Print the results
'''
num1, num2 = input("Enter 2 numbers: ").split()

num1 = int(num1)
num2 = int(num2)

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quatient = num1 / num2
remainder = num1 % num2

print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quatient))
print("{} % {} = {}".format(num1, num2, remainder))


