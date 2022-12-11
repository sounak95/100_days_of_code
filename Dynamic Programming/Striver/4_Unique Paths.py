
# https://www.codingninjas.com/codestudio/problems/total-unique-paths_1081470?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos

def func1(i,j):
    if i==0 and j==0:
        return 1
    if i<0 or j<0:
        return 0

    left = func1(i-1,j)
    up=func1(i,j-1)
    return left+up


def uniquePaths1(m, n):
	# Write your code here.
    return func1(m-1,n-1)

def func2(i,j, dp):
    if i==0 and j==0:
        return 1
    if i<0 or j<0:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    left = func2(i-1,j, dp)
    up=func2(i,j-1, dp)
    dp[i][j] = left+up
    return dp[i][j]

import copy
def uniquePaths2(m, n):
    dp = []
    l1 = [-1] * n
    for i in range(m):
        dp.append(copy.deepcopy(l1))
    return func2(m-1,n-1, dp)

import copy
def uniquePaths3(m, n):
    dp = []
    l1 = [0] * n
    for i in range(m):
        dp.append(copy.deepcopy(l1))
    for i in range(0, m):
        for j in range(0,n):
            if i==0 and j==0:
                 dp[i][j] =1
            else:
                up=0
                left=0
                if i>0:
                    up=dp[i-1][j]
                if j>0:
                    left=dp[i][j-1]
                dp[i][j] = up+left

    return dp[m-1][n-1]

import copy
def uniquePaths3(m, n):
    prev = [0] * n
    for i in range(0, m):
        temp = [0] * n
        for j in range(0,n):
            if i==0 and j==0:
                 temp[j] =1
            else:
                up=0
                left=0
                if i>0:
                    up=prev[j]
                if j>0:
                    left=temp[j-1]
                temp[j] = up+left
        prev=temp
    return prev[n-1]



