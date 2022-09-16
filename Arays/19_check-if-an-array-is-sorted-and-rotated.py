"""
Check if an array is sorted and rotated
Given an array of N distinct integers. The task is to write a program to check if this array is sorted and rotated counter-clockwise. A sorted array is not considered as sorted and rotated, i.e., there should at least one rotation.

Examples:

Input : arr[] = { 3, 4, 5, 1, 2 }
Output : YES
The above array is sorted and rotated.
Sorted array: {1, 2, 3, 4, 5}.
Rotating this sorted array clockwise
by 3 positions, we get: { 3, 4, 5, 1, 2}

Input: arr[] = {7, 9, 11, 12, 5}
Output: YES

Input: arr[] = {1, 2, 3}
Output: NO

3 4 5 1 2
Yes

"""

"""
Find the minimum element in the array.
Now, if the array is sorted and then rotated then all the elements before minimum element will be in increasing order and all elements after the minimum element will also be in increasing order.
Check if all elements before minimum element are in increasing order.
Check if all elements after minimum element are in increasing order.
Check if the last element of the array is smaller than the element just before the minimum element.
If all of the above three condition satisfies then print YES otherwise print NO.

"""

arr = list(map(int,input().split()))
n= len(arr)

flag1=flag2=flag3=True

min_index= arr.index(min(arr))

if min_index==0:
    print("No")
else:
    for i in range(1, min_index):
        if arr[i]<arr[i-1]:
            flag1=False

    for i in range(min_index+1, n):
        if arr[i]<arr[i-1]:
            flag2=False

    if arr[n-1]>arr[min_index-1]:
        flag3=False

    if flag2 and flag1 and flag3:
        print("Yes")
    else:
        print("No")
