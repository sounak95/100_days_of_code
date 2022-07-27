# https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/


def sort012(arr, arr_size):
    low=0
    mid=0
    high= arr_size-1

    while(mid<=high):
        if arr[mid]==0:
            arr[mid], arr[low]= arr[low], arr[mid]
            low+=1
            mid += 1
        elif arr[mid]==1:
            mid+=1
        elif arr[mid]==2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high-=1

    return arr





# Function to print array
def printArray( a):
    for k in a:
        print(k ,end=' ')

# Driver Program
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr_size = len(arr)
arr = sort012( arr, arr_size)
printArray(arr)