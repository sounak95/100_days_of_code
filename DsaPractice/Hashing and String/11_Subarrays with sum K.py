
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-hashing/problem/subarrays-with-sum-k

class Solution:
    def findSubArraySum(self, Arr, N, k):
        # code here
        prefix_sum=0
        map={}
        map[0]=1
        res=0
        for i, ele in enumerate(Arr):
            prefix_sum+=ele
            goal = prefix_sum-k
            res += map.get(goal,0)
            map[prefix_sum] = map.get(prefix_sum,0)+1
        return res


