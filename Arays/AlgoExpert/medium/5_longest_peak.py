

def longestPeak(array):
    # Write your code here.
    maxPeakLength=0
    i=1
    while(i<len(array)-1):
        # print(i)
        isPeak= array[i]>array[i-1] and array[i]>array[i+1]
        if not isPeak:
            i+=1
            continue

        leftIdx=i-2
        while(leftIdx>=0 and array[leftIdx]<array[leftIdx+1]):
            leftIdx-=1

        rightIdx=i+2
        while(rightIdx<len(array) and array[rightIdx]<array[rightIdx-1]):
            rightIdx+=1

        currentPeakLength=rightIdx-leftIdx-2+1
        maxPeakLength=max(currentPeakLength,maxPeakLength)
        i=rightIdx
    return maxPeakLength


# print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
print(longestPeak([1, 3,2]))

