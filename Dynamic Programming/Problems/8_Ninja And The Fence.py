
# https://www.codingninjas.com/codestudio/problems/ninja-and-the-fence_3210208

MOD = pow(10,9)+7
def add (a,b):
    return ((a%MOD) + (b%MOD))% MOD

def mul (a,b):
    return ((a%MOD) * (b%MOD))% MOD

def solveRec(n, k):
    # write your code here
    if n==1:
        return k
    if n==2:
        return add(k, mul(k,k-1))

    ans = add(mul(solveRec(n-2,k), k-1), mul(solveRec(n-1,k),k-1))
    return ans

def solveMem(n, k, dp):
    # write your code here
    if n==1:
        return k
    if n==2:
        return add(k, mul(k,k-1))
    if dp[n]!=-1:
        return dp[n]
    dp[n] = add(mul(solveMem(n-2,k, dp), k-1), mul(solveMem(n-1,k, dp),k-1))
    return dp[n]

def solveTab(n,k):
    dp= [0] * (n+1)
    dp[1] =k
    if n>1:
        dp[2] =add(k, mul(k,k-1))

    for i in range(3, n+1):
        dp[i] = add(mul(dp[i-2], k-1), mul(dp[i-1],k-1))

    return dp[n]

def solveSpace(n,k):
    prev2 =k
    if n==1:
        return prev2
    if n>1:
        prev1 =add(k, mul(k,k-1))

    for i in range(3, n+1):
        ans = add(mul(prev2, k-1), mul(prev1,k-1))
        prev2= prev1
        prev1= ans

    return prev1


def numberOfWays(n, k):
    # return solveRec(n,k)

    # dp =[-1] * (n+1)
    # return solveMem(n,k,dp)

    # return solveTab(n,k)
    return solveSpace(n,k)

print(numberOfWays(1,1))