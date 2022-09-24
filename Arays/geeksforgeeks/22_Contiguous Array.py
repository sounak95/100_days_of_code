
# https://leetcode.com/problems/contiguous-array/


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum=0
        map={}
        max_len = 0
        for i,num in enumerate(nums):
            if num==0:
                prefix_sum=prefix_sum+(-1)
            else:
                prefix_sum+=1

            if prefix_sum==0:
                max_len=max(max_len, i+1)
            elif prefix_sum in map:
                max_len=max(max_len, i-map[prefix_sum])
            else:
                map[prefix_sum]=i
        return max_len