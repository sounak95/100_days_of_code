
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices):
        l=0
        max_profit = float('-inf')
        for r in range(1, len(prices)):
            if prices[l]<prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l=r
        return max_profit
