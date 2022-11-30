'''
Receive a message to encrypt and the number of characters to shift
cycle through each character in the message
get the character code and the shift amount
a - z : 97 - 122
ord(your_letter)
chr(your_code
'''
message = input("Enter your message: ")
key = int(input("How many characters should we shift (1-26): "))

#Prepare the secrete message
secret_message = ""


#Encrypting
for char in message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key

        if char.upper():
            if char_code > ord('Z'):
                char_code -= 26
            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26

        secret_message += chr(char_code)
    else:
        secret_message += char

print("Encrypted: ", secret_message)

#Decrypting
key = -key
original_message = ""

for char in message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key

        if char.upper():
            if char_code > ord('Z'):
                char_code -= 26

            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26

        original_message  += chr(char_code)
    else:
        original_message  += char

print("Decrypted: ", secret_message )