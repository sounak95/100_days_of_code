

def sortedSquaredArray(array):
    # Write your code here.
    sortedSquared=[0 for _ in array]
    smallIndex =0
    largeIndex=len(array)-1

    for idx in reversed(len(array)):
        if array[smallIndex]>array[largeIndex]:
            sortedSquared[idx] = array[smallIndex]*array[smallIndex]
            smallIndex+=1
        else:
            sortedSquared[idx]=array[largeIndex]*array[largeIndex]
            largeIndex-=1
    return sortedSquared


