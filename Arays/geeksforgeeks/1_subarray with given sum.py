# https://www.geeksforgeeks.org/find-subarray-with-given-sum/

# siding window
def subArraySum(self, nums, n, k):
    n = len(nums)
    curr_sum = nums[0]
    start = 0
    i = 0
    for i in range(1, n):
        while (curr_sum > k and start < i - 1):
            curr_sum -= nums[start]
            start += 1

        if curr_sum == k:
            return (start + 1, i)

        curr_sum += nums[i]

    while (curr_sum > k and start < i):
        curr_sum -= nums[start]
        start += 1

    if curr_sum == k:
        return (start + 1, i + 1)

    return [-1]


arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum = 23

subArraySum(arr,sum)
