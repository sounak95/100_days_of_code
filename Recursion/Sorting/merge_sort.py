

def merge_sort(arr):
    if len(arr)==1:
        return arr
    m= len(arr)//2
    left = merge_sort(arr[0:m])
    right= merge_sort(arr[m:len(arr)])
    return merge(left,right)

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
