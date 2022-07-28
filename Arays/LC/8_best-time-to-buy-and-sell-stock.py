# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution(object):

    # brute force
    def maxProfit_bf(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n= len(prices)
        max_profit = 0
        for i in range(n):
            buy = prices[i]
            for j in range(i+1,n):
                sell = prices[j]
                profit = sell-buy
                max_profit = max(profit, max_profit)

        return max_profit

    # optimal solution
    def maxProfit(self, prices):

        n=len(prices)
        min_so_far =float('inf')
        max_profit=0
        for price in prices:
            min_so_far = min(price, min_so_far)
            profit = price - min_so_far
            max_profit = max(profit, max_profit)

        return max_profit




s=Solution()
prices= [7,1,5,3,6,4]
print(s.maxProfit(prices))
