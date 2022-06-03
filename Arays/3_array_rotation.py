'''

Rotation in a 1D array by 'k'

Say, arr[] = [1, 2, 3, 4, 5, 6, 7], K = 2
1) Store first K elements in a temp array
   temp[] = [1, 2]
2) Shift rest of the arr[]
   arr[] = [3, 4, 5, 6, 7, 6, 7]
3) Store back the K elements from temp
   arr[] = [3, 4, 5, 6, 7, 1, 2]

1 2 3 4 5 6 7
2

'''

arr = list(map(int,input().split()))
n= len(arr)
index = int(input())

temp=[]
for i in range(index):
    temp.append(arr[i])

j=0
for i in range(index,n ):
    arr[j] = arr[i]
    j+=1

j=0
for i in range(n-index, n):
    arr[i] = temp[j]
    j+=1

for item in arr:
    print(item, end=' ')
print()

