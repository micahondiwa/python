"""
A function that will return the count of distinct case-insensitive
alphabetic characters and numeric characters that occur more tha
once in the input string. The inputs can be assumed to contain only
alphabets (both upercase and lowercase) and numeric digits.
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"""

def duplicate_count(text):
    counts = {}

    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1

    duplicates = 0
    
    for 
