
# https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        max_subarray_sum = arr[0]
        max_ending_here =0
        for ele in arr:
            max_ending_here+=ele
            max_subarray_sum = max(max_ending_here, max_subarray_sum)
            if max_ending_here<0:
                max_ending_here=0

        return max_subarray_sum

s=Solution()
print(s.maxSubArraySum([1,2,3,-2,5], 5))

