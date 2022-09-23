"""

A simple solution will be first sort the array in descending order and then return the second element from the sorted array. The time complexity of this solution is O(nlogn).

A Better Solution is to traverse the array twice. In the first traversal find the maximum element. In the second traversal find the greatest element less than the element obtained in first traversal. The time complexity of this solution is O(n).

A more Efficient Solution can be to find the second largest element in a single traversal.
Below is the complete algorithm for doing this:

1) Initialize two variables first and second to INT_MIN as,
   first = second = INT_MIN
2) Start traversing the array,
   a) If the current element in array say arr[i] is greater
      than first. Then update first and second as,
      second = first
      first = arr[i]
   b) If the current element is in between first and second,
      then update second to store the value of current variable as
      second = arr[i]
3) Return the value stored in second.

input:
-3 4 -1 -2 1 5
output:
5 4
"""

arr = list(map(int,input().split()))
n= len(arr)
first=second= float('-inf')
for i in range(n):
    if arr[i]>first:
        second= first
        first=arr[i]
    elif(arr[i]>second and arr[i]!=first):
        second= arr[i]
print(first, second)
