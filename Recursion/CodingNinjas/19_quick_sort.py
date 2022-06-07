

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
    while(i<j):
        while (a[i]<pivot):
            i+=1
        while(a[j]>pivot):
            j-=1
        if (i<j):
            a[i],a[j]=a[j],a[i]
    return pivot_index


def quick_sort(a,si,ei):
    if si>=ei:
        return
    pivot_index=partition(a,si,ei)
    quick_sort(a,si,pivot_index)
    quick_sort(a,pivot_index+1,ei)


a=[6,10,9,8,7,1,3,5,4,2]
print(partition(a,0,len(a)-1))


a=[6,10,9,8,7,1,3,5,4,2]
quick_sort(a,0,len(a)-1)
print(a)