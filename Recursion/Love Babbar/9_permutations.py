# https://leetcode.com/problems/permutations/

class Solution(object):
    def solve(self,nums, ans, index):
        if index>= len(nums):
            ans.append(nums.copy())
            return

        for j in range(index, len(nums)):
            nums[index], nums[j] = nums[j], nums[index]
            self.solve(nums, ans, index+1)
            # backtrack
            nums[index], nums[j] = nums[j], nums[index]

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        index =0
        self.solve(nums, ans, index)
        return ans