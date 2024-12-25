#!/usr/bin/env python3
"""maxProfit Module"""


def maxProfit(price):
    """ Given a list of stock prices say [6, 7, 8, 2, 9],
    the max profit will be 7 i.e. buy on day 4 (price = 2)
    and sell on day 5 (price = 9). I want to find the maximum profit.
    Max profit is when you buy when the price is low and sell
    when the price is highest. If prices all prices of subsequent
    days are decreasing or lower than prices of previous days, then return 0.

    Args:
        price: An array containing the prices for subsequent trading days.
    """
    n = len(price)
    if n <= 1:
        return 0

    maxprofit = 0
    minprice = price[0]
    for i in range(1, n):
        if price[i] < minprice:
            minprice = price[i]
        else:
            maxprofit = max(maxprofit, price[i] - minprice)
    return maxprofit


prices = [6, 7, 8, 2, 9]
print(maxProfit(prices))
prices2 = [9, 8, 7, 6, 2]
print(maxProfit(prices2))

# string = 'somestuff'
# print(string[::-1])