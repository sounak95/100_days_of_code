
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

    def indexes(self, v, x):
        return self.firstOcc(v,x), self.lastOcc(v,x)

# Your code goes here
