



def bubble_sort(arr,r,c):
    if r==0:
        return
    if c<r:
        arr[c], arr[c+1] = arr[c+1], arr[c]
        bubble_sort(arr,r,c+1)
    else:
        bubble_sort(arr,r-1,0)


if __name__ == "__main__":
    arr=[4,3,2,1]
    bubble_sort(arr,len(arr)-1,0)
    print(arr)