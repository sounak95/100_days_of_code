1# https://leetcode.com/problems/two-sum/

# use hashing to store number and corresponding index

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m={}
        for i, num in enumerate(nums):
            goal = target-num
            if goal in m:
                return m[goal], i
            m[num]=i
        return -1

nums = [3,2,4]
target = 6
s=Solution()
print(s.twoSum(nums,target))