# https://www.geeksforgeeks.org/check-if-two-arrays-are-equal-or-not/

# use hasing to track the frequency of the characters

class Solution:
    # Function to check if two arrays are equal or not.
    def check(self, A, B, N):
        if len(A) !=len(B):
            return 0

        map={}
        for ele in A:
            map[ele]= map.get(ele,0)+1

        for ele in B:
            if ele not in map:
                return 0
            map[ele]-=1

        for key in map.keys():
            if map[key]!=0:
                return 0
        return 1

# return: True or False

# code here
