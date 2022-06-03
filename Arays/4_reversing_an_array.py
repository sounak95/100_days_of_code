'''

Method 1 (Using Temporary Array): The idea is to first copy all of the elements of the given array in a temporary array. Then traverse the temporary array from end and replace elements in original array by elements of temp array.

This method will take extra space in order of O(N).
Method 2 (Efficient): This method is efficient then the above method and avoids using extra spaces. The idea is to traverse the array from both ends and keep swapping elements from both ends until middle of the array is reached.
1) Initialize start and end indexes as
   start = 0, end = N-1
2) In a loop, swap arr[start] with arr[end]
   and change start and end as follows :
       start = start + 1,
       end = end – 1

'''


arr = list(map(int,input().split()))
n= len(arr)
s=0
e=n-1

while(s<e):
    arr[s], arr[e] = arr[e], arr[s]
    s+=1
    e-=1

for item in arr:
    print(item, end=' ')
print()