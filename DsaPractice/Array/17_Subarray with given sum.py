

# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1


class Solution:

    # def subArraySum(self, arr, n, s):
    #     for i in range(n):
    #         curr_sum = 0
    #         for j in range(i, n):
    #             curr_sum += arr[j]
    #             if curr_sum == s:
    #                 return (i + 1, j + 1)
    #             elif curr_sum > s:
    #                 break
    #
    #     return [-1]

    def subArraySum(self, nums, n, k):
        n = len(nums)
        curr_sum = nums[0]
        start = 0
        for i in range(1, n):
            while (curr_sum > k and start<i-1):
                curr_sum -= nums[start]
                start += 1

            if curr_sum == k:
                return (start+1, i)

            curr_sum += nums[i]


        while (curr_sum > k and start<i-1):
            curr_sum -= nums[start]
            start += 1

        if curr_sum == k:
            return (start + 1, i+1)




        return [-1]

s=Solution()
input ="135 101 170 125 79 159 163 65 106 146 82 28 162 92 196 143 28 37 192 5 103 154 93 183 22 117 119 96 48 127 172 139 70 113 68 100 36 95 104 12 123 134"
l1= list(map(int,input.split(" ")))
# print(l1)
# print(s.subArraySum(l1, 42,468))
print(s.subArraySum([1,2,3,4], 4, 0))

