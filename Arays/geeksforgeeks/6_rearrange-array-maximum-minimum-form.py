# https://www.geeksforgeeks.org/rearrange-array-maximum-minimum-form/

# two pointer
def rearrange(arr, n):
    temp= [None]*n
    small=0
    large=n-1

    for i in range(n):
        if i%2!=0:
            temp[i]=arr[small]
            small+=1
        else:
            temp[i]= arr[large]
            large-=1
    for ele in temp:
        print(ele, end=' ')


# Driver code
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
print("Original Array")
print(arr)
print("Modified Array")
rearrange(arr, n)