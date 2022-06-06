
def firstIndex(a,x):
    l=len(a)
    if l==0:
        return -1
    if a[0]==x:
        return 0
    smallerList=a[1:]
    smallerListOutput= firstIndex(smallerList,x)
    if smallerListOutput==-1:
        return -1
    else:
        return smallerListOutput+1

def firstIndexB(a,x, si):
    l=len(a)
    if si==l:
        return -1
    if a[si]==x:
        return si
    smallerListOutput= firstIndexB(a,x,si+1)
    return smallerListOutput

a = [1, 2, 4, 5, 6, 7, 8, 9, 7]
print(firstIndex(a, 7))
print(firstIndexB(a, 7, 0))