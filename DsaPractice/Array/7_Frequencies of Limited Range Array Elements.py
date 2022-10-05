
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-arrays/problem/frequency-of-array-elements-1587115620


class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        map={}
        for ele in arr:
            map[ele] = map.get(ele,0)+1

        for i in range(1,N+1):
            arr[i-1] = map.get(i,0)




