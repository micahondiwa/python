'''
String functions
'''

random_string = "    this is an important string "
print("With white spaces:", random_string)
#Get rid of the white space on the left
random_string = random_string.lstrip()

#Get rid of the white space on the right
random_string = random_string.rstrip()
print("With no white spaces:", random_string)

#Get rid of the white space on the right and left
random_string = random_string.strip()
print("With no white spaces:", random_string)

#capitalize the fisrt letter
random_string = random_string.capitalize()
print(random_string)

#Convert the string to uppercase
print(random_string.upper())


#Convert the string to lowercase
print(random_string.lower())


# Join strings to form a list
a_list = ["Bunch", "of", "random", "words."]
print(" ".join(a_list))

#Forming a list of strings by spling a singl string
a_list_2 = random_string.split()
for i in a_list_2:
    print(i)

#get number of words in a string
print("How many is: ", random_string.count("is"))

#Index of a matching string
print("Where is string: ", random_string.find("is"))

#replacing strings
print(random_string.replace("an ", "a kind of "))

