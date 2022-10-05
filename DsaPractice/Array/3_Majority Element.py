
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-arrays/problem/majority-element-1587115620

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        freq={}
        for ele in A:
            freq[ele] = freq.get(ele,0)+1
            if freq[ele]>N/2:
                return ele

        return -1




