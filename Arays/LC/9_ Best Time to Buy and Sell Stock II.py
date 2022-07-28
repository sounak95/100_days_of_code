# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit =0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]

        return profit

s=Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))
