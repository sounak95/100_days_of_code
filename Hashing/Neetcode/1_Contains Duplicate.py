
# https://leetcode.com/problems/contains-duplicate/

# use hasing to check duplicates

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        m=set()

        for num in nums:
            if num in m:
                return True
            else:
                m.add(num)

        return False
