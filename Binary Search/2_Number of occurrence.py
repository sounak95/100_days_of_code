
# https://practice.geeksforgeeks.org/problems/number-of-occurrence2259/1

class Solution:

    def firstOcc(self, arr, key):
        s=0
        e= len(arr)-1
        mid = s+(e-s)//2
        ans=-1
        while(s<=e):
            if arr[mid] == key:
                ans=mid
                e=mid-1

            elif key> arr[mid]:
                s= mid+1
            else:
                e=mid-1
            mid= s+(e-s)//2

        return ans

    def lastOcc(self, arr, key):
        s = 0
        e = len(arr) - 1
        mid = s + (e - s) // 2
        ans = -1
        while (s <= e):
            if arr[mid] == key:
                ans = mid
                s = mid + 1

            elif key > arr[mid]:
                s = mid + 1
            else:
                e = mid - 1
            mid = s + (e - s) // 2

        return ans

    def count(self,arr, n, x):
        if self.firstOcc(arr,x) !=-1:
            return self.lastOcc(arr,x)-self.firstOcc(arr,x)+1
        else:
            return 0
