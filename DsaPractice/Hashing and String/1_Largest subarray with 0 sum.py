

# https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1


class Solution:
    def maxLen(self, n, arr):
        #Code here
        prefix_sum=0
        map={}
        max_len=0
        for i, ele in enumerate(arr):
            prefix_sum += ele

            if ele==0 and max_len==0:
                max_len=1
            elif prefix_sum==0:
                max_len= max(max_len, i+1)
            elif prefix_sum in map:
                max_len= max(max_len, i-map[prefix_sum])
            else:
                map[prefix_sum] = i
        return max_len

s=Solution()
print(s.maxLen(5,[15,-2,2,-8,1,7,10,23]))