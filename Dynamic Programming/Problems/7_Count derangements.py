# https://www.codingninjas.com/codestudio/problems/count-derangements_873861

def countDerangementsRec(n):
    # Write your code here.
    if n==1:
        return 0

    if n==2:
        return 1

    ans = (((n-1)%(pow(10,9)+7)) *((countDerangementsRec(n-1)% (pow(10,9)+7)) + countDerangementsRec(n-2)% (pow(10,9)+7))% (pow(10,9)+7))
    return ans


def solveMem(n, dp):
    # Write your code here.
    if n == 1:
        return 0
    if n == 2:
        return 1

    if dp[n]!=-1:
        return dp[n]

    dp[n] = (((n - 1) % (pow(10, 9) + 7)) * (
                (solveMem(n - 1, dp) % (pow(10, 9) + 7)) + solveMem(n - 2, dp) % (pow(10, 9) + 7)) % (
                       pow(10, 9) + 7))
    return dp[n]


def solveTab(n):
    dp=[0] * (n+1)
    dp[1] =0
    dp[2]=1

    for i in range(3,n+1):
        first = dp[i-1] % (pow(10,9)+7)
        second = dp[i-2] % (pow(10,9)+7)
        sum = (first+ second) % (pow(10,9)+7)
        ans = (((i-1)* sum)% (pow(10,9)+7))
        dp[i]= ans

    return dp[n]

def solveSpace(n):

    prev2=0
    prev1=1

    for i in range(3,n+1):
        first = prev1 % (pow(10,9)+7)
        second = prev2 % (pow(10,9)+7)
        sum = (first+ second) % (pow(10,9)+7)
        ans = (((i-1)* sum)% (pow(10,9)+7))
        prev2=prev1
        prev1=ans

    return prev1



def countDerangements(n):
    # dp =[-1] * (n+1)
    # return solveMem(n,dp)

    return solveTab(n)

# Main.
t = int(input())
while t:
    n = int(input())
    print(countDerangements(n))
    t = t-1