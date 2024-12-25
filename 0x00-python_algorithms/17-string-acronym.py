'''
Ask for a string
convert the string to uppercase
convert the string to a list
cycle through the list
get the first letter of the word and eliminate the newline
add a new line
'''
original_string = input("Convert to Acronym: ")

original_string = original_string.upper()

list_of_words = original_string.split()

for word in list_of_words:
    print(word[0], end = "")
print()