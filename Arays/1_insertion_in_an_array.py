'''

Insertion in a 1D array

Now, before inserting the element at the index idx, shift all elements from the index idx till end of the array to the right by 1 place. This can be done as:
for(i = len-1; i >= idx; i--)
{
    arr[i+1] = arr[i];
}
After shifting the elements, place the element K at index idx.
arr[idx] = K;

Time Complexity in worst case of this insertion operation can be linear i.e. O(N) as we might have to shift all of the elements by one place to the right.


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
