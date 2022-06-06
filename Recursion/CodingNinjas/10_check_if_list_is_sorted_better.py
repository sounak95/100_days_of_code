
def isSorted(a,si):
    l=len(a)
    if si==l-1 or si==l:
        return True
    if a[si]>a[si+1]:
        return False
    isSmallerListSorted=isSorted(a,si+1)
    if isSmallerListSorted:
        return True
    else:
        return False





if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(isSorted(a,0))