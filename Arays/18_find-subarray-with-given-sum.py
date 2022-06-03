"""
Find subarray with given sum
Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number.
Examples :

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4

Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
Ouptut: Sum found between indexes 1 and 4

Input: arr[] = {1, 4}, sum = 0
Output: No subarray found

Input:
1 4 0 0 3 10 5
7
Output
Sum found between 1 and 4

1 4 20 3 10 5
33
Sum found between 2 and 4

1 4 20 3 10 5
4
Sum found between 1 and 1
"""

arr = list(map(int,input().split()))
n= len(arr)
sum=int(input())

flag=False
for i in range(n):
    current_sum=arr[i]
    for j in range(i+1,n):
        if current_sum==sum:
            flag=True
            print(f"Sum found between {i} and {j-1}")
            break
        current_sum+=arr[j]
        if current_sum>sum:
            break
    if flag:
        break

if not flag:
    print("No subarray found")