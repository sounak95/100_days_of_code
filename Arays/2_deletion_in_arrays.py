'''

Deletion in a 1D array

for(i = idx+1; i < len; i++)
{
    arr[i-1] = arr[i];
}

len = len-1;

Time Complexity in worst case of this insertion operation can be linear i.e. O(N) as we might have to shift all of the elements by one place to the left.


WAP to delete an element in an array

1 2 3 4 5
2


'''

arr = list(map(int,input().split()))
index = int(input())
n = len(arr)
for i in range(index+1,n):
    arr[i-1] = arr[i]
n=n-1
arr.pop()
for item in arr:
    print(item, end=' ')
print()