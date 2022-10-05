

# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        s=0
        e=len(arr)-1
        mid = s+(e-s)//2
        while(s<e):
            if arr[mid]<arr[mid+1]:
                s=mid+1
            else:
                e=mid
            mid = s+(e-s)//2

        return s