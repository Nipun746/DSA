class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        max_profit = 0

        minimum = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]

            profit = prices[i] - minimum

            if profit > max_profit:
                max_profit = profit

        return max_profit