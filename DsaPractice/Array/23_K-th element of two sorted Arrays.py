
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-arrays/problem/k-th-element-of-two-sorted-array1317

class Solution:
    def kthElement(self, arr1, arr2, n, m, k1):

        i=0
        j=0
        k=0
        arr3=[None] * (m+n)
        while(i<n and j<m):
            if arr1[i]<arr2[j]:
                arr3[k] = arr1[i]
                i+=1
                k+=1
            elif arr1[i]>arr2[j]:
                arr3[k]= arr2[j]
                j+=1
                k+=1

        while(i<n):
            arr3[k] = arr1[i]
            k+=1
            i+=1

        while(j<m):
            arr3[k] = arr2[j]
            k+=1
            j+=1

        # print(arr3)
        return arr3[k1-1]

s=Solution()
print(s.kthElement([2, 3, 6, 7, 9], [1, 4, 8, 10], 5, 4, 5))
