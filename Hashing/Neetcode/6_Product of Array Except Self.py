
# https://leetcode.com/problems/product-of-array-except-self/


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        prefix=1

        for i,num in enumerate(nums):
            res[i] = prefix
            prefix = prefix * num

        postfix=1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix = postfix*nums[i]

        return res

s=Solution()
nums = [-1,1,0,-3,3]
print(s.productExceptSelf(nums))