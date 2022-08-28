# https://www.geeksforgeeks.org/first-element-occurring-k-times-array/

# use hasing to track the frequency of the characters

class Solution:
    def firstElementKTime(self,  a, n, k):
        # code here
        map={}
        for ele in a:
            map[ele]= map.get(ele,0)+1
            if map[ele] == k:
                return ele

        # for ele in a:
        #     if map[ele]==k:
        #         return ele

        return -1