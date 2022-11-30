'''
* Takes age input and classify the grade
* if age is 5 -> kindergarten
* ages 6 through 17 -> grades 1 through 12
* ages >17 -> college
'''
age = eval(input("Enter age:"))
if age < 5:
    print("Too young for school!")
elif age == 5:
    print("Go to kindergarten.")
elif (age > 5) and (age <= 17):
    print("Go to garde {}.".format(age-5))
elif age > 17:
    print("Go to college.")