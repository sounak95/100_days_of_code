"""

Rearrange an array in maximum minimum form
Given a sorted array of positive integers, rearrange the array alternately i.e first element should be maximum value, second minimum value, third second max, fourth second min and so on.

Examples:

Input: arr[] = {1, 2, 3, 4, 5, 6, 7}
Output: arr[] = {7, 1, 6, 2, 5, 3, 4}


Input:
1 2 3 4 5 6 7
Output:
7 1 6 2 5 3 4


"""

arr = list(map(int,input().split()))
n= len(arr)

s=0
l=n-1

temp=[None]*n

for i in range(n):
    if i%2!=0:
        temp[i]= arr[s]
        s+=1
    else:
        temp[i]=arr[l]
        l-=1

for item in temp:
    print(item, end=' ')