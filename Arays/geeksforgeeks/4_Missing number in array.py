
# https://www.geeksforgeeks.org/find-the-missing-number/

def getMissingNo(arr, n):
    sum=(n+1)*(n+2)//2

    arr_sum=0
    for ele in arr:
        arr_sum+=ele

    return sum-arr_sum


if __name__ == '__main__':
    arr = [1, 2, 3, 5]
    N = len(arr)

    # Function call
    miss = getMissingNo(arr, N)
    print(miss)
