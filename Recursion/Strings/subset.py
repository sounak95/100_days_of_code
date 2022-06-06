

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

if __name__ == "__main__":
    subset1("","abc")
    print(subset2([1,2,3]))
