
# https://leetcode.com/problems/find-the-duplicate-number/

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow==fast:
                break

        slow2=0
        while(True):
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow==slow2:
                break

        return slow