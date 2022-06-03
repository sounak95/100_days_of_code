"""
Method 2 (Scan from right)
Scan all the elements from right to left in an array and keep track of maximum till now. When maximum changes its value, print it.
"""

arr = list(map(int,input().split()))
n= len(arr)
max_form_right=arr[n-1]
print(max_form_right, end=' ')

for i in range(n-2,-1,-1):
    if arr[i]>max_form_right:
        max_form_right=arr[i]
        print(max_form_right, end=' ')
