# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
# Kadane’s Algorithm


def maxSubArraySum(a,size):
    max_so_far= float('-inf')
    max_enfding_here = 0

    for ele in a :
        max_enfding_here+=ele

        max_so_far = max(max_so_far, max_enfding_here)

        if max_enfding_here<0:
            max_enfding_here=0

    return max_so_far

a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSubArraySum(a,len(a)))