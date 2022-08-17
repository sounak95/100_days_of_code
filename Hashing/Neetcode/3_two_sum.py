
# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        m={}
        for i,num in enumerate(nums):
            goal = target-num
            if goal in m:
                return m[goal], i
            else:
                m[num] =i


s=Solution()
print(s.twoSum([3,2,4], 6))


