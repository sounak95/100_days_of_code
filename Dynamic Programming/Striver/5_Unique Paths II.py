
# https://www.codingninjas.com/codestudio/problems/maze-obstacles_977241?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos

def func1(i,j, mat):
    if i>=0 and j>=0 and mat[i][j]==-1:
        return 0
    if i==0 and j==0:
        return 1
    if i<0 or j<0:
        return 0

    left = func1(i-1,j, mat)
    up=func1(i,j-1, mat)
    return left+up


def mazeObstacles(m, n, mat):
    # Write your code here.
    return func1(m-1,n-1, mat)

def func2(i,j, mat, dp):
    if i>=0 and j>=0 and mat[i][j]==-1:
        return 0
    if i==0 and j==0:
        return 1
    if i<0 or j<0:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    left = func2(i-1,j, mat,dp)
    up=func2(i,j-1, mat,dp)
    dp[i][j] = left+up
    return dp[i][j]

import copy
def mazeObstacles2(m, n, mat):
    dp = []
    l1 = [-1] * n
    for i in range(m):
        dp.append(copy.deepcopy(l1))
    return func2(m-1,n-1, mat,dp)

import copy
MOD= pow(10,9)+7
def mazeObstacles3(m, n,mat):
    dp = []
    l1 = [0] * n
    for i in range(m):
        dp.append(copy.deepcopy(l1))
    for i in range(0, m):
        for j in range(0,n):
            if mat[i][j]==-1:
                dp[i][j]=0
            elif i==0 and j==0:
                 dp[i][j] =1
            else:
                up=0
                left=0
                if i>0:
                    up=dp[i-1][j]
                if j>0:
                    left=dp[i][j-1]
                dp[i][j] = (up+left)%MOD

    return dp[m-1][n-1]

def mazeObstacles(m, n, mat):
    prev = [0] * n
    for i in range(0, m):
        temp = [0] * n
        for j in range(0,n):
            if mat[i][j]==-1:
                temp[j]=0
            elif i==0 and j==0:
                 temp[j] =1
            else:
                up=0
                left=0
                if i>0:
                    up=prev[j]
                if j>0:
                    left=temp[j-1]
                temp[j] = (up+left)%MOD
        prev=temp
    return prev[n-1]
