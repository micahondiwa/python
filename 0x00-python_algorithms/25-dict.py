'''
An array of customer dictionary
'''
customers = []

while True:
    createEntry = input("Enter Customer (Yes/No): ")
    createEntry = createEntry[0].lower()

    if createEntry == 'n':
        break

    else:
        fname, lname = input("Enter customer Name: ").split()

        customers.append({"fname: ", fname, "lname: ", lname})