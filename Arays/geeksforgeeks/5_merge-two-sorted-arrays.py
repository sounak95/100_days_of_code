
# two pointer
def mergeArrays(arr1, arr2, n1, n2):

    i=0
    j=0
    k=0
    arr3=[None]*(n1+n2)

    while(i<n1 and j<n2):
        if arr1[i]<arr2[j]:
            arr3[k]=arr1[i]
            i+=1
            k+=1
        elif arr2[j]<arr1[i]:
            arr3[k]=arr2[j]
            j+=1
            k+=1

    while(i<n1):
        arr3[k]=arr1[i]
        k+=1
        i+=1

    while(j<n2):
        arr3[k]=arr2[j]
        j+=1
        k+=1

    for ele in arr3:
        print(ele, end=' ')



# Driver code
arr1 = [1, 3, 5, 7]
n1 = len(arr1)

arr2 = [2, 4, 6, 8]
n2 = len(arr2)
mergeArrays(arr1, arr2, n1, n2)