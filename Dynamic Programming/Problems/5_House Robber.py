
# https://www.codingninjas.com/codestudio/problems/house-robber_839733

# https://leetcode.com/problems/house-robber/submissions/

class SolutionSpace:

    def solve(self, arr):
        n= len(arr)
        prev2=0
        prev1 = arr[0]
        for i in range(1, n):
            incl =prev2 + arr[i]
            excl = prev1 + 0
            ans = max(incl, excl)
            prev2=prev1
            prev1= ans

        return prev1


    def rob(self, nums):
        n= len(nums)
        # return self.solve(nums)
        return max(self.solve(nums[0:n-1]), self.solve(nums[1:n]))