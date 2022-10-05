class Solution(object):
    def partition(self, arr, s, e):
        pivot = arr[s]
        cnt = 0
        for i in range(s + 1, e + 1):
            if arr[i] <= pivot:
                cnt += 1

        pivot_index = s + cnt
        arr[s], arr[pivot_index] = arr[pivot_index], arr[s]

        i = s
        j = e

        while (i < pivot_index and j > pivot_index):
            while arr[i] <= pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1

            if i < pivot_index and j > pivot_index:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        return pivot_index

    def helper(self, arr, s, e):
        if s >= e:
            return
        p = self.partition(arr, s, e)
        self.helper(arr, s, p - 1)
        self.helper(arr, p + 1, e)

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.helper(nums, 0, len(nums) - 1)
        return nums