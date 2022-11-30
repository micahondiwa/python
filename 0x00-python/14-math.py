'''
Basic mathemtical operations using the math library
'''
import math
from decimal import Decimal as D


print("ceil(4.4) = ", math.ceil(4.4))
print("floor(4.4 = ", math.floor(4.4))
print("fabs(-4.4 = ", math.fabs(-4.4))
print("factorial(4) = ", math.factorial(4))
print("fmod(5,4 = ", math.fmod(5,4))
print("trunc(4.2 =", math.trunc(4.2))
print("pow(2,2) = ", math.pow(2,2))

sum = D(0)
sum += D("0.1")
sum += D("0.1")
sum += D("0.1")
sum -= D("0.3")

print("sum = ", sum)

print(".1 + .1 + .1 -.3 = ", .1 + .1 + .1 -.3)

