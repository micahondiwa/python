'''
string operation
'''

sample_string = "This is a very important string"

print(sample_string[0])
print(sample_string[-1])
print(sample_string[3 + 5])
print("String length:", len(sample_string))
print(sample_string[0:4])
print(sample_string[8:])
print("Hello" * 5)
num_string = str(6)

for char in sample_string:
    print(char)

for i in range(0, len(sample_string)-1,2):
    print(sample_string[i] + sample_string[i+1])

#Uppercase: A-Z -> 65 - 90
#Lowercase: a-z -> 97 - 122

print("A = ", ord("A"))
print("65 = ", chr(65))

'''
Enter a string in uppercase: HIDE
secrete message: 35647890
original message: HIDE
cycle through each character in the string
store each character code in a string
prnt a secrete message
'''
norm_string = input("Enter a string to hide in uppercase: ")

secret_string = ""
for  char in norm_string:
    secret_string += str(ord(char))

print("Secret Message: ", secret_string)

norm_string = ""
for i in range(0, len(secret_string)-1, 2):
    char_code = secret_string[i] + secret_string[i + 1]
    norm_string += chr(int(char_code))

print("Original Message: ", norm_string)

