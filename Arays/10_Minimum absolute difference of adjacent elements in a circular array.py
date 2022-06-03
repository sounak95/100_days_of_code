"""

Minimum absolute difference of adjacent elements in a circular array
Given n integers, which form a circle. Find the minimal absolute value of any adjacent pair. If there are many optimum solutions, output any of them.
Note: they are in circle

Examples:

Input : arr[] = {10, 12, 13, 15, 10}
Output : 0
Explanation: |10 - 10| = 0 which is the
minimum possible.

Input : arr[] = {10, 20, 30, 40}
Output : 10
Explanation: |10 - 20| = 10 which is the
minimum, 2 3 or 3 4 can be the answers also.

input:
10 12 13 15 10
output:
0

input:
10 20 30 40 50
output:
10

"""

arr = list(map(int,input().split()))
n= len(arr)

res= abs(arr[1]- arr[0])

for i in range(2,n):
    res= min(res, abs(arr[i]-arr[i-1]))
res= min(res, abs(arr[n-1]- arr[0]))
print(res)