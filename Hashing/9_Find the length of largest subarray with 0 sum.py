
# https://www.geeksforgeeks.org/find-the-largest-subarray-with-0-sum/

# use hasing to store first prefix sum
class Solution:
    def maxLen(self, n, arr):
        #Code
        map={}

        prefix_sum=0
        max_len=0
        for i,ele in enumerate(arr):

            prefix_sum+=ele

            if ele==0 and max_len==0:
                max_len=1

            if prefix_sum==0:
                max_len=max(max_len, i+1)

            if prefix_sum in map:
                max_len = max(max_len, i-map[prefix_sum])

            else:
                map[prefix_sum] = i

        return max_len

s=Solution()
arr=[6,-1,-3,4,-2,2,4,6,-12,-7]
# arr=[1,-2,2]
arr=[6, 3, -1, -3, 4, -2, 2,
             4, 6, -12, -7]
s.maxLen(len(arr), arr)
