'''
* Receive age input
* eval automatically converts input to integer
* Provide different output based on age in put and logical operator
* i - 18 -> important
* 21, 50, > 60 -> important
* All others -> Not imporatnt
'''

age = eval(input('Enter age: '))
if (age >= 1) and (age <= 18):
    print("Important Birthday")
elif (age == 21) or (age == 50):
    print("Important Birthday")
elif not(age < 65):
    print("Important Birthday")
else:
    print("Sorry, not important Birthday")
