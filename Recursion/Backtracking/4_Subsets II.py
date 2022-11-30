
# https://leetcode.com/problems/subsets-ii/

# Given an integer array nums that may contain duplicates, return all possible
# subsets
#  (the power set).
class Solution(object):

    def func(self, ind, nums, ds, ans):
        ans.append(ds.copy())

        for i in range(ind, len(nums)):
            if i>ind and nums[i]==nums[i-1]: continue
            ds.append(nums[i])
            self.func(i+1, nums, ds, ans)
            ds.pop()

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        self.func(0,sorted(nums), [], ans)
        return ans

