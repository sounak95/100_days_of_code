# https://www.geeksforgeeks.org/sort-array-according-order-defined-another-array/


def counter(arr):
    d={}
    for ele in arr:
        d[ele] = d.get(ele, 0)+1

    return d


def relativeSort(arr1, arr2):
    arr1=A1
    arr2 = A2
    f= counter(arr1)

    res=[]

    for ele in arr2:
        if ele in f:
            res.extend([ele]*f[ele])
            f[ele] = 0

    # print(f)
    # print(res)

    rem = list(sorted(filter(lambda x:f[x]!=0, f)))

    # print(rem)
    for ele in rem:
        res.extend([ele]*f[ele])

    return res





# Driver Code
if __name__ == "__main__":
    arr1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
    arr2 = [2, 1, 8, 3]
    print(relativeSort(arr1, arr2))