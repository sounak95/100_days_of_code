
def rbs(arr, target, s,e):
    if (s>e):
        return -1

    m=(s+e)//2
    if arr[m]==target:
        return m

    # if first half of the array is sorted
    if arr[s]<arr[m]:
        if arr[s]<=target<=arr[m]:
            return rbs(arr, target,s,m-1)
        else:
            return rbs(arr, target,m+1,e)
    #if second half of the array is sorted
    elif arr[m]<=target<=arr[e]:
        return rbs(arr, target, m+1, e)
    else:
        return rbs(arr, target, s, m-1)




if __name__ == "__main__":
    arr=[5, 6, 7, 8, 9, 1, 2, 3]
    print(rbs(arr,9, 0, len(arr)-1))