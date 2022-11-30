''''
string functions
'''

letter_z = "z"
num_3 = "3"
a_space = " "

print("Is z a letter or number:", letter_z.isalnum())
print("Is z a letter: ", letter_z.isalpha())
print("Is 3 a number: ", num_3.isalnum())
print("Is z a lowercase:", letter_z.islower())
print("Is z a uppercase: ", letter_z.isupper())
print("Is space a space: ", a_space.isspace())

#A function to check if number is a float

def isfloat(str_val):
    try:
        float(str_val)
        return True

    except ValueError:
        return False

num_3 = 3.145
print("Is pie a float: ", isfloat(num_3))

