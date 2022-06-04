


def bs(arr,target,s,e):
    if (s>e):
        return -1
    m= int((s+e)/2)
    if arr[m]==target:
        return m
    elif target>arr[m]:
        return bs(arr,target,m+1,e)
    else:
        return bs(arr,target,s,m-1)




if __name__ == "__main__":
    l1=[1, 2, 3, 4, 55, 66, 78]
    target = 67
    print(bs(l1,target,0,len(l1)-1))