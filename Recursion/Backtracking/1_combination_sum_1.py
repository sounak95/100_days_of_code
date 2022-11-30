
# https://leetcode.com/problems/combination-sum/

# Given an array of distinct integers candidates
# The same number may be chosen from candidates an unlimited number of times.
class Solution(object):

    def findCombination(self, index, target, arr, ans, ds):
        if index==len(arr):
            if target==0:
                ans.append(ds.copy())
            return

        if arr[index]<=target:
            ds.append(arr[index])
            self.findCombination(index, target-arr[index], arr,ans, ds)
            ds.pop()

        self.findCombination(index+1, target, arr, ans, ds)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        ds=[]
        self.findCombination(0, target, candidates, ans, ds)
        return ans