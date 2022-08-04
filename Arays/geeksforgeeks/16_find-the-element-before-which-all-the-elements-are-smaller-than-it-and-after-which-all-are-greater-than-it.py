

# https://www.geeksforgeeks.org/find-the-element-before-which-all-the-elements-are-smaller-than-it-and-after-which-all-are-greater-than-it/
# left array, right array

def findElement(arr, n):

    leftMax= [None]*n
    leftMax[0] = arr[0]

    for i in range(1,n):
        leftMax[i] = max(leftMax[i-1], arr[i-1])

    rightMin = [None]*n
    rightMin[n-1] = arr[n-1]

    for i in range(n-2,-1,-1):
        rightMin[i]= min(rightMin[i+1], arr[i+1])

    for i in range(1,n-1):
        ele = arr[i]
        if ele>= leftMax[i] and ele<=rightMin[i]:
            return i

    return -1





# Driver program
if __name__ == "__main__":
    arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]
    n = len(arr)
    print("Index of the element is", findElement(arr, n))