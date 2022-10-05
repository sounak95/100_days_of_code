
 #https://leetcode.com/problems/sort-an-array/

import sys

sys.setrecursionlimit(10 ** 6)


class Solution(object):

    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m + 1 - 1

        arr1 = [None] * n1
        arr2 = [None] * n2

        for i in range(n1):
            arr1[i] = arr[l + i]

        for i in range(n2):
            arr2[i] = arr[m + 1 + i]

        i = 0
        j = 0
        k = l

        while (i < n1 and j < n2):
            if arr1[i] < arr2[j]:
                arr[k] = arr1[i]
                i += 1
            else:
                arr[k] = arr2[j]
                j += 1
            k += 1

        while (i < n1):
            arr[k] = arr1[i]
            k += 1
            i += 1

        while (j < n2):
            arr[k] = arr2[j]
            j += 1
            k += 1

    def helper(self, arr, l, r):
        if l>=r:
            return

        m = (l + r)//2
        self.helper(arr, l, m)
        self.helper(arr, m+1, r)
        self.merge(arr, l, m, r)

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.helper(nums, 0, len(nums) - 1)
        return nums