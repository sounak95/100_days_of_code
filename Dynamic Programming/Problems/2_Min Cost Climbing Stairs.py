

# https://leetcode.com/problems/min-cost-climbing-stairs/

# recursion
class Solution1(object):
    def solve(self, cost, n):
        # base case
        if n==0:
            return cost[0]
        if n==1:
            return cost[1]

        ans = cost[n] + min(self.solve(cost, n-1), self.solve(cost, n-2))
        return ans

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n= len(cost)
        ans = min(self.solve(cost, n-1), self.solve(cost, n-2))
        return ans

# recursion + memoization. top down
class Solution2(object):
    def solve(self, cost, n, dp):
        # base case
        if n == 0:
            return cost[0]
        if n == 1:
            return cost[1]

            # step 3
        if dp[n] != -1:
            return dp[n]

        dp[n] = cost[n] + min(self.solve(cost, n - 1, dp), self.solve(cost, n - 2, dp))
        return dp[n]

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        # step 1
        dp = [-1] * n
        ans = min(self.solve(cost, n - 1, dp), self.solve(cost, n - 2, dp))
        return ans

# tabulation
class Solution3(object):
    def solve(self, cost, n, dp):
        # step 2
        dp[0] = cost[0]
        dp[1] = cost[1]

        # step 3
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[n-1], dp[n-2])


    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        # step 1
        dp = [-1] * n
        return self.solve(cost, n, dp)

# Space optimization
class Solution(object):
    def solve(self, cost, n, dp):
        # step 2
        prev2 = cost[0]
        prev1 = cost[1]

        # step 3
        for i in range(2, n):
            curr = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = curr

        return min(prev1, prev2)


    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        # step 1
        dp = [-1] * n
        return self.solve(cost, n, dp)