

def sortedSquaredArray(array):
    # Write your code here.
    sortedSquared=[0 for _ in array]
    smallIndex =0
    largeIndex=len(array)-1

    for idx in reversed(range(len(array))):
        if abs(array[smallIndex])>abs(array[largeIndex]):
            sortedSquared[idx] = array[smallIndex]*array[smallIndex]
            smallIndex+=1
        else:
            sortedSquared[idx]=array[largeIndex]*array[largeIndex]
            largeIndex-=1
    return sortedSquared

print(sortedSquaredArray([-5,-4,-3,-2,0,2,4,5]))

