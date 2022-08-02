# https://www.geeksforgeeks.org/first-element-occurring-k-times-array/

class Solution:
    def firstElementKTime(self,  a, n, k):
        # code here
        map={}
        for ele in a:
            map[ele]= map.get(ele,0)+1

        for ele in a:
            if map[ele]==k:
                return ele

        return -1