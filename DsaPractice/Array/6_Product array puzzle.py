
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-arrays/problem/product-array-puzzle4525

class Solution:
    def productExceptSelf(self, nums, n):
        # code here
        left_product = 1
        left_array = [None] * n

        for i, ele in enumerate(nums):
            left_array[i] = left_product
            left_product *= ele

        right_product = 1
        right_array = [None] * n
        for i in reversed(range(n)):
            right_array[i] = right_product
            right_product *= nums[i]

        for i in range(n):
            nums[i] = left_array[i] * right_array[i]

        return nums



s=Solution()
print(s.productExceptSelf([10,3,5,6,2], 5))