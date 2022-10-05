
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-hashing/problem/largest-subarray-of-0s-and-1s

class Solution:
    def maxLen(self,arr, N):
        # code here
        map={}
        prefix_sum=0
        max_len = 0
        for i, ele in enumerate(arr):
            if arr[i]==0:
                prefix_sum-=1
            elif arr[i]==1:
                prefix_sum+=1

            if prefix_sum==0:
                max_len= max(max_len, i+1)
            elif prefix_sum in map:
                max_len= max(max_len, i-map[prefix_sum])
            else:
                map[prefix_sum] = i

        return max_len

s=Solution()
print(s.maxLen([0,1,0,1],4))

