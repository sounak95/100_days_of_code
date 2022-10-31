

# https://leetcode.com/problems/coin-change/


class SolutionRec(object):


    def solve_rec(self, coins, amount):
        if amount==0:
            return 0
        if amount<0:
            return float('inf')

        mini = float('inf')

        for coin in coins:
            ans = self.solve_rec(coins, amount-coin)
            if ans != float('inf'):
                mini = min(mini,1+ ans)

        return  mini

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ans  = self.solve_rec(coins, amount)

        if ans  == float('inf'):
            return -1
        return  ans

class SolutionMem(object):


    def solve_mem(self, coins, amount, dp):
        if amount==0:
            return 0
        if amount<0:
            return float('inf')

        mini = float('inf')

        if dp[amount]!=-1:
            return dp[amount]

        for coin in coins:
            ans = self.solve_mem(coins, amount-coin, dp)
            if ans != float('inf'):
                mini = min(mini,1+ ans)

        dp[amount] = mini
        return  dp[amount]

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = [-1] *(amount+1)
        ans  = self.solve_mem(coins, amount, dp)

        if ans  == float('inf'):
            return -1
        return  ans

class SolutionTab(object):

    def solve(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] =0

        for i in range(0, amount+1):
            for coin in coins:
                if (i-coin)>=0 and dp[i-coin] !=float('inf') :
                    dp[i] = min(dp[i], 1+ dp[i-coin] )


        if dp[amount] == float('inf'):
            return -1

        return dp[amount]


    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        return self.solve(coins, amount)
