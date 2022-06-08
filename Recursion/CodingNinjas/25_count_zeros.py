'''
Count Zeros
Send Feedback
Given an integer N, count and return the number of zeros that are present in the given integer using recursion.
Input Format :
Integer N
Output Format :
Number of zeros in N
Constraints :
0 <= N <= 10^9
Sample Input 1 :
0
Sample Output 1 :
1
Sample Input 2 :
00010204
Sample Output 2 :
2
Explanation for Sample Output 2 :
Even though "00010204" has 5 zeros, the output would still be 2 because when you convert it to an integer, it becomes 10204.
Sample Input 3 :
708000
Sample Output 3 :
4
'''


def count_zeros(n,s):
    if n==0:
        return s
    rem = n % 10
    if rem==0:
        return count_zeros(n // 10, s+1)
    else:
        return count_zeros(n // 10, s)

def solve(n, s=0):
    # print(n)
    if n == "":
        return s

    if n[0] == "0":
        return solve(n[1:], s + 1)
    else:
        return solve(n[1:], s)

print(solve("02345600"))

# print(count_zeros(abs(int(input())),0))
