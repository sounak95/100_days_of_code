

def selection_sort(arr, r,c,max):
    if r == 0:
        return
    if c < r:
        if arr[c]>arr[max]:
            selection_sort(arr,r,c+1,c)
        else:
            selection_sort(arr,r,c+1,max)
    else:
        arr[r-1],arr[max]= arr[max], arr[r-1]
        selection_sort(arr,r-1,0,0)


if __name__ == "__main__":
    arr=[4,3,2,1]
    selection_sort(arr,len(arr),0, 0)
    print(arr)