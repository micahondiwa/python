'''
* Store user input of 2 numbers and the operator of choice
* Convert the numbers int ints
* if  + then we need to provide output based on addition
* print the result
'''
num1, operator, num2 = input("Enter calculation: ").split()
num1 = int(num1)
num2 = int(num2)

if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "%":
    print("{} % {} = {}".format(num1, num2, num1 % num2))
else:
    print("Use either +, -, *, / or % next time")

