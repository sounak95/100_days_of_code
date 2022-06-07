

def partition(a,si,ei):
    pivot=a[si]
    c=0
    for i in range(si, ei+1):
        if a[i]<pivot:
            c+=1
    a[si],a[si+c]=a[si+c],a[si]
    pivot_index=si+c
    i=si
    j=ei
    while i < j:
        if a[i] < pivot:
            i = i + 1
        elif a[j] >= pivot:
            j = j - 1
        else:
            a[i], a[j] = a[j], a[i]
            i = i + 1
            j = j - 1
    return pivot_index



def quick_sort(a,si,ei):
    if si>=ei:
        return
    pivot_index=partition(a,si,ei)
    quick_sort(a,si,pivot_index)
    quick_sort(a,pivot_index+1,ei)


# a=[6,10,9,8,7,1,3,5,4,2]
# print(partition(a,0,len(a)-1))
#
#
# a=[6,10,9,8,7,1,3,5,4,2]
# quick_sort(a,0,len(a)-1)
# print(a)

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quick_sort(arr, 0, n-1)
print(*arr)
