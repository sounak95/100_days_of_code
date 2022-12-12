
# https://www.codingninjas.com/codestudio/problems/maximum-path-sum-in-the-matrix_797998?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos

def getMaxPathSumUtil1(i,j,m, matrix):
    if j<0 or j>=m:
        return float('-inf')

    if i==0:
        return matrix[i][j]

    up = matrix[i][j] + getMaxPathSumUtil1(i-1,j,m, matrix)
    ld = matrix[i][j] + getMaxPathSumUtil1(i-1,j-1,m, matrix)
    rd = matrix[i][j] + getMaxPathSumUtil1(i-1,j+1,m, matrix)

    return max(up,ld,rd)

def getMaxPathSum1(matrix):

    #   Write your code here
    n= len(matrix)
    m= len(matrix[0])

    maxi = float('-inf')
    for j in range(m):
        ans = getMaxPathSumUtil1(n-1,j,m,matrix)
        maxi = max(maxi, ans)

    return maxi

def getMaxPathSumUtil2(i,j,m, matrix, dp):
    if j<0 or j>=m:
        return float('-inf')

    if i==0:
        return matrix[i][j]

    if dp[i][j]!=-1:
        return dp[i][j]

    up = matrix[i][j] + getMaxPathSumUtil2(i-1,j,m, matrix,dp)
    ld = matrix[i][j] + getMaxPathSumUtil2(i-1,j-1,m, matrix, dp)
    rd = matrix[i][j] + getMaxPathSumUtil2(i-1,j+1,m, matrix, dp)

    dp[i][j] = max(up,ld,rd)
    return dp[i][j]

import copy
def getMaxPathSum2(matrix):

    #   Write your code here
    n= len(matrix)
    m= len(matrix[0])

    dp = []
    l1 = [-1] * m

    for i in range(n):
        dp.append(copy.deepcopy(l1))

    maxi = float('-inf')
    for j in range(m):
        ans = getMaxPathSumUtil2(n-1,j,m,matrix, dp)
        maxi = max(maxi, ans)

    return maxi


import copy
def getMaxPathSum(matrix):

    #   Write your code here
    n= len(matrix)
    m= len(matrix[0])

    dp = []
    l1 = [0] * m

    for i in range(n):
        dp.append(copy.deepcopy(l1))

    for j in range(m):
        dp[0][j] = matrix[0][j]

    for i in range(1,n):
        for j in range(m):
            up = matrix[i][j] + dp[i-1][j]
            ld = matrix[i][j]
            if j-1>=0:
                ld += dp[i-1][j-1]
            else:
                ld+=float('-inf')
            rd = matrix[i][j]
            if j+1<m:
                rd += dp[i-1][j+1]
            else:
                rd+=float('-inf')
            dp[i][j] = max(up, ld, rd)

    maxi = float('-inf')
    for j in range(m):
        ans = dp[n-1][j]
        maxi = max(maxi, ans)

    return maxi