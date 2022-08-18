

# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0

        for num in nums:
            if num-1 not in numSet:
                length=0
                while(num+length) in numSet:
                    length+=1
                longest=max(length, longest)

        return longest


s=Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([0]))
