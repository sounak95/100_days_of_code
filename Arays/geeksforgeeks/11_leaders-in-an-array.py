
# https://www.geeksforgeeks.org/leaders-in-an-array/

def printLeaders(arr, size):

    max_from_right = arr[size-1]
    print(max_from_right, end=' ')

    for i in range(size-2, -1, -1):
        if arr[i] > max_from_right:
            max_from_right = arr[i]
            print(max_from_right, end=' ')

# Driver function
arr = [16, 17, 4, 3, 5, 2]
printLeaders(arr, len(arr))
