class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        max_profit = 0

        minimum = float('inf')
        for price in prices:
            if  price < minimum:
                minimum = price
            profit = price - minimum

            if max_profit < profit :
                max_profit = profit
        return max_profit