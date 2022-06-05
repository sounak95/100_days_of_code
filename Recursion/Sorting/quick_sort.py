
def quick_sort(arr, low, high):
    if low>=high:
        return
    s=low
    e=high
    m=s+(e-s)//2
    pivot= arr[m]
    while(s<=e):
        while arr[s]<pivot:
            s+=1
        while arr[e]>pivot:
            e-=1
        if s<=e:
            arr[s], arr[e]= arr[e], arr[s]
            s+=1
            e-=1
    quick_sort(arr, low, e)
    quick_sort(arr, s, high)

if __name__ == "__main__":
    arr=[4,3,2,1]
    quick_sort(arr,0,len(arr)-1)
    print(arr)