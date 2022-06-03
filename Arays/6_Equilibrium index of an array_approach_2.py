"""

Description - Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. We are given an Array of integers, We have to find out the first index i from left such that -
A[0] + A[1] + ... A[i-1] = A[i+1] + A[i+2] ... A[n-1]
Input
[-7, 1, 5, 2, -4, 3, 0]
Output
3
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

Tricky Solution : The idea is to get total sum of array first. Then Iterate through the array and keep updating the left sum which is initialized as zero. In the loop, we can get right sum by subtracting the elements one by one. Then check whether Leftsum and Rightsum are equal.
Pseudo Code
// n : size of array
int eqindex(arr, n)
{
    sum = 0
    leftsum = 0
    for (i=0 to n-1)
        sum += arr[i]

    for (i=0 to n-1)
    {
        // now sum will be righsum for index i
        sum -= a[i]
        if (sum == leftsum )
            return i
        leftsum += a[i]
    }
}
Time Complexity : O(n)
Auxiliary Space : O(1)

input:
-7 1 5 2 -4 3 0

output:
2
"""

arr = list(map(int,input().split()))
n= len(arr)
flag=True
sum=0
for item in arr:
    sum+=item

left_sum=0
for i in range(n):
    sum-=arr[i]
    if sum==left_sum:
        flag=False
        print(i)
        break
    left_sum+=arr[i]
if flag:
    print(-1)
