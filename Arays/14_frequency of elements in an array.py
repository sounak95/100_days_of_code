'''
Input:
1 2 1 3 2 5 6 1

Output:
Frequency of 1 is 3
Frequency of 2 is 2
Frequency of 3 is 1
Frequency of 5 is 1
Frequency of 6 is 1
'''

arr = list(map(int,input().split()))
n= len(arr)
visited=[False]*n
for i in range(n):
    count=1
    if visited[i]:
        continue
    for j in range(i+1, n):
        if arr[i]==arr[j]:
            count+=1
            visited[j]=True
    print(f"Frequency of {arr[i]} is {count}")
