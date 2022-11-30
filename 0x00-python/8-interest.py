'''
* Enter the investment amount and the expected interest
* Enter year the investment will increase + investment * interest aret
* Print the earnings
'''

investment_amt = input("How much to input: ")
interest_rate = input("Enter interest rate: ")

investment_amt = float(investment_amt)
interest_rate = float(interest_rate) * 0.01

for i in range(10):
    earnings = investment_amt + (i * interest_rate)
    print("Earnings after {} years = {:.2f} ".format(i, earnings))