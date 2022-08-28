# https://leetcode.com/problems/contains-duplicate/

# use hasing to check duplicates

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        m={}

        for i,num in enumerate(nums):
            if num in m:
                return True
            m[num]=1
        return False

s=Solution()
nums = [1,2,3,1]
nums = [1,2,3,4]
print(s.containsDuplicate(nums))