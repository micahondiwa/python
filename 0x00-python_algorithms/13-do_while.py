'''
A guessing game: Asks user to guess a number between 1 and 10
'''
secret_number = 7

while True:
    guess = int(input("Guess a number bteween 1 and 10: "))

    if guess == secret_number:
        print("You guessed it!")
        break