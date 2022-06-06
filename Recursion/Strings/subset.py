

def subset1(p, up):
    if len(up)==0:
        print(p)
        return

    ch=up[0]

    subset1(p+ch, up[1:])
    subset1(p,up[1:])

def subset2(arr):
    outer=[]
    outer.append([])
    for num in arr:
        n=len(outer)
        for i in range(n):
            internal=outer[i].copy()
            internal.append(num)
            outer.append(internal)
    return outer

def subsetDuplicate(arr):
    arr=sorted(arr)
    outer=[]
    outer.append([])
    start=end=0

    for i in range(len(arr)):
        start=0
        if i>0 and arr[i]==arr[i-1]:
            start=end+1
        end=len(outer)-1
        n=len(outer)
        for j in range(start, n):
            internal=outer[j].copy()
            internal.append(arr[i])
            outer.append(internal)
    return outer

if __name__ == "__main__":
    subset1("","abc")
    print(subset2([1,2,3]))
    print(subsetDuplicate([1, 2, 2]))
