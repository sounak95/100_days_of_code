"""

The time complexity of the above solution is O(nLogn) if a O(nLogn) sorting algorithm like Merge Sort, Heap Sort, .. etc is used.

This can be done in O(n) time by doing a single traversal of given array. The idea is based on the fact that if we make sure that all even positioned (at index 0, 2, 4, ..) elements are greater than their adjacent odd elements, we don’t need to worry about odd positioned element. Following are simple steps.
1) Traverse all even positioned elements of input array, and do following.
….a) If current element is smaller than previous odd element, swap previous and current.
….b) If current element is smaller than next odd element, swap next and current.

Below are implementations of above simple algorithm.

"""

arr = list(map(int,input().split()))
n= len(arr)
for i in range(0, n, 2):
    if(i>0 and arr[i]< arr[i-1]):
        arr[i], arr[i-1]= arr[i-1], arr[i]
    if (i<n-1 and arr[i]< arr[i+1]):
        arr[i], arr[i+1]=arr[i+1], arr[i]

for item in arr:
    print(item, end=' ')
print()