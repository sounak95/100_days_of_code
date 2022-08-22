
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    # optimal solution
    def maxProfit(self, prices):
        n=len(prices)
        l,r = 0, 1
        max_profit = 0
        for r in range(1,n):
            if prices[l]<prices[r]:
                max_profit= max(max_profit, prices[r]-prices[l])
            else:
                l=r

        return max_profit

s=Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))
