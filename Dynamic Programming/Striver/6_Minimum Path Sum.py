
# https://www.codingninjas.com/codestudio/problems/minimum-path-sum_985349?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos


def func1(i,j, grid):
    if i==0 and j==0:
        return grid[i][j]
    if i<0 or j<0:
        return float('inf')

    up = grid[i][j] + func1(i-1,j, grid)
    left=grid[i][j] + func1(i,j-1, grid)
    return min(left,up)

def minSumPath1(grid):
    # Write your code here.
    n= len(grid)
    m= len(grid[0])
    return func1(n-1,m-1, grid)

def func2(i,j, mat, dp):
    if i==0 and j==0:
        return mat[i][j]
    if i<0 or j<0:
        return float('inf')
    if dp[i][j]!=-1:
        return dp[i][j]
    up = mat[i][j] + func2(i-1,j, mat,dp)
    left= mat[i][j] + func2(i,j-1, mat,dp)
    dp[i][j] = min(left,up)
    return dp[i][j]

import copy
def minSumPath2(grid):
    # Write your code here.
    n = len(grid)
    m = len(grid[0])
    dp = []
    l1 = [-1] * m
    for i in range(n):
        dp.append(copy.deepcopy(l1))
    return func2(n - 1, m - 1, grid, dp)

import copy
def minSumPath(grid):
    # Write your code here.
    n = len(grid)
    m = len(grid[0])
    dp = []
    l1 = [0] * m

    for i in range(n):
        dp.append(copy.deepcopy(l1))

    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                 dp[i][j] =grid[i][j]
            else:
                up=grid[i][j]
                if i>0:
                    up=+ dp[i-1][j]
                else:
                    up+=float('inf')

                left = grid[i][j]
                if j>0:
                    left+= dp[i][j-1]
                else:
                    left+=float('inf')

                dp[i][j] = min(up,left)

    return dp[n-1][m-1]