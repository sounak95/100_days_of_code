
def isSorted(a):
    if len(a)==0 or len(a)==1:
        return True
    if a[0]>a[1]:
        return False
    smallList=a[1:]
    isSmallerListSorted=isSorted(smallList)
    if isSmallerListSorted:
        return True
    else:
        return False





if __name__ == "__main__":
    a = [11,1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(isSorted(a))