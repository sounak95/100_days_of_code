'''

WAP to inset an element in an arry at index post

1 2 3 4 5
3
11
'''

#take array input

arr = list(map(int,input().split()))
arr.append(None)
pos = int(input())
ele = int(input())
n= len(arr)

for i in range(n-2, pos-1, -1):
    arr[i+1]= arr[i]
arr[pos] = ele

for item in arr:
    print(item, end=' ')
print()