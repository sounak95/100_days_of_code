
# https://www.codingninjas.com/codestudio/problems/cut-into-segments_1214651

def solveRec(n, x, y, z):
    if n==0:
        return 0
    if n<0:
        return float('-inf')
    a = solveRec(n-x, x, y, z) + 1
    b = solveRec(n-y, x, y, z) + 1
    c = solveRec(n-z, x, y, z) + 1

    return max(a,b,c)

def solveMem(n, x, y, z, dp):
    if n==0:
        return 0

    if n<0:
        return float('-inf')

    if dp[n]!=-1:
        return dp[n]

    a = solveMem(n - x, x, y, z, dp) + 1
    b = solveMem(n - y, x, y, z, dp) + 1
    c = solveMem(n - z, x, y, z, dp) + 1

    dp[n] = max(a,b,c)

    return dp[n]

def solveTab(n, x, y, z, dp):
    if n==0:
        return 0

    if n<0:
        return float('-inf')

    if dp[n]!=-1:
        return dp[n]

    a = solveMem(n - x, x, y, z, dp) + 1
    b = solveMem(n - y, x, y, z, dp) + 1
    c = solveMem(n - z, x, y, z, dp) + 1

    dp[n] = max(a,b,c)

    return dp[n]

def solveTab(n,x,y,z):
    dp = [float('-inf')] * (n+1)
    dp[0] = 0

    for i in range(1, n+1):
        if (i-x)>=0:
            dp[i] = max(dp[i], dp[i-x] + 1)
        if (i-y)>=0:
            dp[i] = max(dp[i], dp[i-y] + 1)
        if (i-z)>=0:
            dp[i] = max(dp[i], dp[i-z] + 1)

    if dp[n]<0:
        return 0
    else:
        return dp[n]



def cutSegments(n, x, y, z):
    # Write your code here.
    # ans = solveRec(n,x,y,z)
    # if ans<0:
    #     return 0
    # else:
    #     return ans

    # dp= [-1] * (n+1)
    # ans = solveMem(n,x,y,z,dp)
    # if ans<0:
    #     return 0
    # else:
    #     return ans

    return solveTab(n,x,y,z)



