'''
factorial
example: 3! = 3 * 2 * 1
'''
def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return  result

print(factorial(10))
