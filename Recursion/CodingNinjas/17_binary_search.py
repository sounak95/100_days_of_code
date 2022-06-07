
def bs(a,x,si,ei):
    if si>ei:
        return -1
    mid=(si+ei)//2
    if a[mid]==x:
        return mid
    elif x>a[mid]:
        return bs(a,x,mid+1,ei)
    else:
        return bs(a,x,si,mid-1)


print(bs([1,3,5,7,9,11,13,15,16,17],3,0,9))

print(bs([1,3,5,7,9,11,13,15,16,17],2,0,9))