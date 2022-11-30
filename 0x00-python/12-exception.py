'''
Exception handling: Asks user to enter a number and throws an error if the user does not enter a number
'''
while True:

    try:
        number = int(input("Please enter a number: "))
        break

    except ValueError:
        print("You didn't enter a number")
    except:
        print("An unknown error occured")

print("Thank you for entering {}".format(number))