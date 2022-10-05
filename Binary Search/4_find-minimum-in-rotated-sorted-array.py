

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution(object):
    def findMin(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        e=len(arr ) -1
        mid = s+(e-s)// 2

        if arr[s] < arr[e]:
            return arr[s]

        while(s<e):
            if arr[mid]>=arr[0] :
                s=mid+1
            else:
                e=mid
            mid = s+ (e-s)//2

        return arr[s]
