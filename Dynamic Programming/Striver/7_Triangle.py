
# https://www.codingninjas.com/codestudio/problems/triangle_1229398?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos

def func1(i, j, triangle, n):
    if i == n - 1:
        return triangle[i][j]

    d = triangle[i][j] + func1(i + 1, j, triangle, n)
    dg = triangle[i][j] + func1(i + 1, j + 1, triangle, n)

    return min(d, dg)


def minimumPathSum1(triangle, n):
    # Write your code here.
    return func1(0, 0, triangle, n)

def func2(i, j, triangle, n, dp):
    if i == n - 1:
        return triangle[i][j]

    if dp[i][j]!=-1:
        return dp[i][j]

    d = triangle[i][j] + func2(i + 1, j, triangle, n,dp)
    dg = triangle[i][j] + func2(i + 1, j + 1, triangle, n,dp)

    dp[i][j]= min(d, dg)
    return dp[i][j]


import copy
def minimumPathSum2(triangle, n):
    # Write your code here.
    dp = []
    l1 = [-1] * n
    for i in range(n):
        dp.append(copy.deepcopy(l1))

    return func2(0, 0, triangle, n, dp)

def minimumPathSum3(triangle, n):
    # Write your code here.
    dp = []
    l1 = [0] * n

    for i in range(n):
        dp.append(copy.deepcopy(l1))

    for j in range(n):
        dp[n-1][j] = triangle[n-1][j]

    for i in range(n-2, -1, -1):
        for j in range(i,-1,-1):
            d = triangle[i][j] + dp[i+1][j]
            dg= triangle[i][j] + dp[i+1][j+1]
            dp[i][j]= min(d,dg)

    return dp[0][0]

def minimumPathSum(triangle, n):
    # Write your code here.
    front = [0] * n
    curr = [0] * n

    for j in range(n):
        front[j] = triangle[n-1][j]

    for i in range(n-2, -1, -1):
        for j in range(i,-1,-1):
            d = triangle[i][j] + front[j]
            dg= triangle[i][j] + front[j+1]
            curr[j]= min(d,dg)

        front=curr

    return front[0]
