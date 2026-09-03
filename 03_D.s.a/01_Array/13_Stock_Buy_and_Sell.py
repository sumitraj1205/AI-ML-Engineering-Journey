# Stock Buy and Sell
#
# Problem:
# Given an array where prices[i] represents the price of a stock
# on the ith day, find the maximum profit that can be achieved
# by buying on one day and selling on a later day.
#
# Approach:
# Keep track of the minimum price seen so far.
#
# For every price:
# 1. Calculate the profit if we sell today.
# 2. Update the maximum profit.
# 3. Update the minimum price if the current price is smaller.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


def max_profit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:

        min_price = min(min_price, price)

        profit = price - min_price

        max_profit = max(max_profit, profit)

    return max_profit


prices = [7, 1, 5, 3, 6, 4]

print(max_profit(prices))