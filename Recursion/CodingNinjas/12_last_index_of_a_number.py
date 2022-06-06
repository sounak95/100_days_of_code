
def lastIndex(a,x):
    l=len(a)
    if l==0:
        return -1
    smallerList=a[1:]
    smallerListOutput= lastIndex(smallerList,x)
    if smallerListOutput!=-1:
        return smallerListOutput+1
    else:
        if a[0]==x:
            return 0
        else:
            return -1

def lastIndexB(a,x, si):
    l=len(a)
    if si==-1:
        return -1
    if a[si]==x:
        return si
    smallerListOutput= lastIndexB(a,x,si-1)
    return smallerListOutput

a = [1, 2, 4, 5, 6, 7, 8, 9, 7]
print(lastIndex(a, 7))
print(lastIndexB(a, 7, len(a)-1))