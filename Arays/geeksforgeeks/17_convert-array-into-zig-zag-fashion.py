# https://www.geeksforgeeks.org/convert-array-into-zig-zag-fashion/

def zigZag(arr, n):
    for i in range(n-1):
        if i%2==0:
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1]= arr[i+1], arr[i]
        else:
            if arr[i]<arr[i+1]:
                arr[i], arr[i+1]= arr[i+1], arr[i]
    return arr

    # for i in range(1,n-1, 2):
    #
    #     if i>0 and arr[i]<arr[i-1]:
    #         arr[i], arr[i-1]= arr[i-1], arr[i]
    #
    #     if i<n-1 and arr[i]<arr[i+1]:
    #         arr[i], arr[i+1]= arr[i+1], arr[i]
    #
    # return arr





# Driver program
arr = [6202, 4625, 5469, 2038, 5916, 3405, 5533]
n = len(arr)
print(zigZag(arr, n))