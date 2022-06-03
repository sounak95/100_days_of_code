'''
Input:
1 2 3 4 5 6
8
Output:
6 5 4 3 2 1

'''
arr = list(map(int,input().split()))
n= len(arr)
k = int(input())

for i in range(0, n,k):
    left=i
    right=min(i+k-1, n-1)
    while(left<right):
        arr[left], arr[right]= arr[right], arr[left]
        left+=1
        right-=1

for item in arr:
    print(item, end=' ')
print()