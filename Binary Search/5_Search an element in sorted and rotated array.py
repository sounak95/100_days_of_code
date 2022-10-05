# User function Template for python3

def findPivot(arr):
    """
    :type nums: List[int]
    :rtype: int
    """
    s = 0
    e = len(arr) - 1
    mid = s + (e - s) // 2

    if arr[s] < arr[e]:
        return arr[s]

    while (s < e):
        if arr[mid] >= arr[0]:
            s = mid + 1
        else:
            e = mid
        mid = s + (e - s) // 2

    return s


def bs(arr, s, e, key):
    start = s
    end = e
    mid = start + (end - start) // 2

    while (start <= mid):
        if arr[mid] == key:
            return mid
        if key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

        mid = start + (end - start) // 2

    return -1


def Search(arr, n, k):
    # code here
    pivot_index = findPivot(arr)

    if arr[pivot_index] <= k <= arr[n - 1]:
        return bs(arr, pivot_index, n - 1, k)
    else:
        return bs(arr, 0, pivot_index - 1, k)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tcs = int(input())
    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]
        k = int(input())

        print(Search(arr, n, k))

# } Driver Code Ends