# https://leetcode.com/problems/majority-element/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m={}
        for i, num in enumerate(nums):
            m[num] = m.get(num,0)+1
        print(m)
        for i ,num in enumerate(nums):
            if m[num]>len(nums)//2:
                return num
        return -1

s=Solution()
nums = [2,2,1,1,1,2,2]
print(s.majorityElement(nums))
