# two pointer

def sortedSquaredArray1(array):
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

def sortedSquaredArray(array):
    sortedSquared = [0 for _ in array]
    smallIndex = 0
    largeIndex = len(array) - 1
    k=len(array) - 1

    while(smallIndex<=largeIndex):
        # print(smallIndex)
        # print(largeIndex)
        if abs(array[smallIndex])> abs(array[largeIndex]):
            sortedSquared[k] = array[smallIndex] * array[smallIndex]
            smallIndex+=1
            k-=1
        else:
            sortedSquared[k] = array[largeIndex] * array[largeIndex]
            largeIndex-=1
            k-=1
    return sortedSquared

    # print(sortedSquared)
# print(sortedSquaredArray([-5,-4,-3,-2,0,2,4,5]))
print(sortedSquaredArray([-7,-5,-4,3,6,8,9]))
# print(sortedSquaredArray1([1, 2, 3, 5, 6, 8, 9]))
# print(sortedSquaredArray([0,2,4,5]))

