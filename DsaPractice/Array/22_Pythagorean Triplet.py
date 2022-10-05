
# https://practice.geeksforgeeks.org/problems/pythagorean-triplet3018/1


class Solution:

    def checkTriplet(self,arr, n):
        arr.sort()
        for i, ele in enumerate(arr):
            arr[i] = ele*ele

        for i in range(n-1, -1,-1):
            left=0
            right=i-1
            target = arr[i]
            while(left<right):
                sum= arr[left]+ arr[right]
                if sum< target:
                    left+=1
                elif sum> target:
                    right-=1
                else:
                    return True

        return False

s=Solution()
print(s.checkTriplet([3, 8, 5], 3))
