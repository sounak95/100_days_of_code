

def bubble_sort(l1,n):
    if n==0:
        return
    for i in range(n-1):
        if l1[i]>l1[i+1]:
            l1[i],l1[i+1] = l1[i+1],l1[i]

    bubble_sort(l1,n-1)

l1=[1,3,4,9,4,8]
bubble_sort(l1,len(l1))
print(l1)