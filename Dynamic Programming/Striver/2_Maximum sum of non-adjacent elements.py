
# https://www.codingninjas.com/codestudio/problems/maximum-sum-of-non-adjacent-elements_843261?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0


def func1(ind, nums):
    if ind==0:
        return nums[ind]
    if ind<0:
        return 0
    pick = nums[ind] + func1(ind-2, nums)
    not_pick = 0+ func1(ind-1, nums)
    return max(pick, not_pick)

def maximumNonAdjacentSum1(nums):
    # Write your code here.
    n= len(nums)
    return func1(n-1, nums)


def func2(ind, nums, dp):
    if ind == 0:
        return nums[ind]
    if ind < 0:
        return 0

    if dp[ind] != -1:
        return dp[ind]

    pick = nums[ind] + func2(ind - 2, nums, dp)
    not_pick = 0 + func2(ind - 1, nums, dp)
    dp[ind] = max(pick, not_pick)

    return dp[ind]


def maximumNonAdjacentSum2(nums):
    # Write your code here.
    n = len(nums)
    dp = [-1] * n
    return func2(n - 1, nums, dp)


def maximumNonAdjacentSum3(nums):
    # Write your code here.
    n = len(nums)
    dp = [0] * n
    dp[0]=nums[0]
    for i in range(1,n):
        pick = nums[i]
        if i>1:
            pick+=dp[i-2]
        not_pick = 0+dp[i-1]
        dp[i] = max(pick, not_pick)
    return dp[n-1]

def maximumNonAdjacentSum(nums):
    # Write your code here.
    n = len(nums)
    prev=nums[0]
    prev_2=0
    for i in range(1,n):
        pick = nums[i]
        if i>1:
            pick+=prev_2
        not_pick = 0+prev
        curr = max(pick, not_pick)
        prev_2=prev
        prev=curr
    return prev