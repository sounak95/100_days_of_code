
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-arrays/problem/maximum-value-of-difference-of-a-pair-of-elements-and-their-index

class Solution:
    def maxValue(self, arr, N):
        # code here
        ans = float('-inf')
        for i in range(0,N):
            for j in range(0,N):
                diff = abs(arr[i]-arr[j]) + abs(i-j)
                ans = max(diff, ans)

        return ans

s=Solution()
print(s.maxValue([3,7,1,5,2,4],6))



