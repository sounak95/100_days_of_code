
# https://www.codingninjas.com/codestudio/problems/frog-jump_3621012


def func(ind, heights):
    if ind==0:
        return 0
    left = func(ind-1, heights) + abs(heights[ind]-heights[ind-1])
    right= float('inf')
    if ind>1:
        right= func(ind-2, heights) + abs(heights[ind]-heights[ind-2])
    return min(left, right)


def func1(ind, heights, dp):
    if ind == 0:
        return 0
    if dp[ind] != -1:
        return dp[ind]

    left = func1(ind - 1, heights, dp) + abs(heights[ind] - heights[ind - 1])
    right = float('inf')
    if ind > 1:
        right = func1(ind - 2, heights, dp) + abs(heights[ind] - heights[ind - 2])
    dp[ind] = min(left, right)
    return dp[ind]


def frogJump1(n, heights):
    # return func(n-1, heights)
    dp = [-1] * n
    return func1(n-1, heights, dp)

def frogJump2(n, heights):
    # return func(n-1, heights)
    dp = [0] * n
    dp[0] =0
    for i in range(1,n):
        left = dp[i-1] + abs(heights[i] - heights[i-1])
        right = float('inf')
        if i>1:
            right = dp[i-2] + abs(heights[i] - heights[i-2])
        dp[i] = min(left, right)
    return dp[n-1]

def frogJump(n, heights):
    # return func(n-1, heights)
    prev=0
    prev2=0
    for i in range(1,n):
        left = prev + abs(heights[i] - heights[i-1])
        right = float('inf')
        if i>1:
            right =prev2 + abs(heights[i] - heights[i-2])
        curr = min(left, right)
        prev2=prev
        prev=curr
    return prev



