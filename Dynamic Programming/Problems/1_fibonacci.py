

# https://www.codingninjas.com/codestudio/problems/nth-fibonacci-number_74156


# recursion + memoization, Top down approach
# TC: o(n) SC: o(n) for dp array + o(n) for recursion
def fibo(n, dp):
    if n<=1:
        return n

    # step 3
    if dp[n]!=-1:
        return dp[n]
    # step 2
    dp[n] = fibo(n-1, dp) + fibo(n-2, dp)
    return dp[n]

# tabulation
# TC: o(n) SC: o(n) for dp array
def fibo1(n, dp):
    dp[1] =1
    dp[0] = 0

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# space optimization
# TC: o(n) SC: o(1)
def fibo2(n):
    prev1 = 1
    prev2 = 0

    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2=prev1
        prev1= curr

    return prev1

if __name__ == '__main__':
    n = int(input())
    # step 1
    dp=[-1] * (n+1)
    print(fibo2(n))