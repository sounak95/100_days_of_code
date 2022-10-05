
# https://practice.geeksforgeeks.org/problems/zero-sum-subarrays1825/1

class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        prefix_sum=0
        map={}
        map[prefix_sum]=1
        count=0
        for i, ele in enumerate(arr):
            prefix_sum+=ele
            if prefix_sum in map:
                count+=map.get(prefix_sum,0)
            map[prefix_sum] = map.get(prefix_sum,0)+1
        return count
