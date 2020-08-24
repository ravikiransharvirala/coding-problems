#-*- coding: utf-8 -*-
"""
Given a list of stock prices over a period of days and a set of
trades performed on various days, calculate the total profit or
loss at the end of the time period.

Each stock trade is expressed as [[{day}, {number of shares}].
The number of shares is positive for a purchase, and negative 
for a sale of purchased price

Notes:

- It is safe to assume that trade requests are valid and are
performed on days correlating to the 0-indexed list of stock
prices.
- Stock trades are performed in the first-in-first-out order.

Example:

Stock prices: [1, 2, 3, 4]

Trades: [[0, 10], [1, -5], [2, 10], [3, -15]]

Result: 30 
"""

def calculate_profit(stock_prices, trades):
    """
    stock_prices : list
    trades: list[list]
    rtype: int
    """
    profit = 0
    stocks_held = []
    for trade in trades:
        purchase_stock = trade[1] > 0
        for stock in range(abs(trade[1])):
            if purchase_stock:
                stocks_held.append(stock)
                profit -= 1 * stock_prices[trade[0]]
            else: 
                stocks_held.pop()
                profit += 1 * stock_prices[trade[0]]
    return profit

stock_prices = [1, 2, 3, 4]
trades = [[0, 10], [1, -5], [2, 10], [3, -15]]
print(calculate_profit(stock_prices, trades))