
# https://practice.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1

class SolutionRec:

    def solve(self, arr, index):
        if index<0:
            return 0
        if index ==0:
            return arr[0]

        incl = self.solve(arr, index-2) + arr[index]
        excl = self.solve(arr, index-1) + 0

        return max(incl , excl)

    def findMaxSum(self, arr, n):
        return self.solve(arr, n-1)

class SolutionMem:

    def solve(self, arr, index, dp):
        if index<0:
            return 0
        if index ==0:
            return arr[0]

        if dp[index]!=-1:
            return dp[index]

        incl = self.solve(arr, index-2, dp) + arr[index]
        excl = self.solve(arr, index-1, dp) + 0

        dp[index] = max(incl , excl)
        return dp[index]

    def findMaxSum(self, arr, n):
        dp=[-1] * n
        return self.solve(arr, n-1, dp)

class SolutionTab:

    def solve(self, arr, n, dp):
        dp[0] = arr[0]
        for i in range(1, n):
            # if (i-2)>=0:
            incl = dp[i-2] + arr[i]
            excl = dp[i-1] + 0
            dp[i] = max(incl, excl)

        return dp[n-1]


    def findMaxSum(self, arr, n):
        dp=[0] * n
        return self.solve(arr, n, dp)


class SolutionSpace:

    def solve(self, arr, n, dp):
        prev2=0
        prev1 = arr[0]
        for i in range(1, n):
            incl =prev2 + arr[i]
            excl = prev1 + 0
            ans = max(incl, excl)
            prev2=prev1
            prev1= ans

        return prev1


    def findMaxSum(self, arr, n):
        dp=[0] * n
        return self.solve(arr, n, dp)

# code here