

def merge_sort(arr):
    if len(arr)==1:
        return arr
    m= len(arr)//2
    left = merge_sort(arr[0:m])
    right= merge_sort(arr[m:len(arr)])
    return merge(left,right)

def merge_sort_in_place(arr,s,e):
    if e-s==1:
        return
    m= (s+e)//2
    merge_sort_in_place(arr,s,m)
    merge_sort_in_place(arr,m,e)
    return merge_in_place(arr,s,m,e)

def merge_in_place(arr,s,m,e):
    mix=[None]*(e-s)

    i=s
    j=m
    k=0

    while (i < m and j < e):
        if arr[i] < arr[j]:
            mix[k] = arr[i]
            i += 1
        else:
            mix[k] = arr[j]
            j += 1
        k += 1

    while (i < m):
        mix[k] = arr[i]
        k += 1
        i += 1

    while (j < e):
        mix[k] = arr[j]
        k += 1
        j += 1

    for k in range(len(mix)):
        arr[s+k]=mix[k]

def merge(left, right):
    mix=[None] * (len(left)+len(right))

    i=0
    j=0
    k=0

    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            mix[k]=left[i]
            i+=1
        else:
            mix[k]=right[j]
            j+=1
        k+=1

    while(i<len(left)):
        mix[k]=left[i]
        k+=1
        i+=1

    while(j<len(right)):
        mix[k]= right[j]
        k+=1
        j+=1

    return mix


if __name__ == "__main__":
    arr=[4,3,2, 9,1]
    print(merge_sort(arr))
    merge_sort_in_place(arr,0,len(arr))
    print(arr)
