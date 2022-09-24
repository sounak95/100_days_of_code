
# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum=0
        res=0
        map={}
        map[prefix_sum] =1
        for i, num in enumerate(nums):
            prefix_sum +=num
            goal = prefix_sum-k
            res+=map.get(goal,0)
            map[prefix_sum] = map.get(prefix_sum,0)+1
        return res