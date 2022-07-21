
# brute force
def getTrappedRainwater_optimal(heights):
    totalWater=0
    maxLeft=maxRight=0
    left=0
    right = len(heights)-1

    while(left<right):
        if heights[left]<=heights[right]:
            if heights[left]>maxLeft:
                maxLeft = heights[left]
            else:
                totalWater+=maxLeft-heights[left]
            left+=1
        else:
            if heights[right]>=maxRight:
                maxRight = heights[right]
            else:
                totalWater += maxRight-heights[right]
            right-=1
    return totalWater



# brute force
def getTrappedRainwater(heights):
    totalWater=0
    for p, height in enumerate(heights):

        leftP=p
        rightP=p
        maxLeft=0
        maxRight=0

        while(leftP>=0):
            maxLeft=max(maxLeft, heights[leftP])
            leftP-=1

        while(rightP<len(heights)):
            maxRight=max(maxRight, heights[rightP])
            rightP+=1

        currentWater= min(maxLeft, maxRight)-height

        if currentWater>=0:
            totalWater+=currentWater
    return totalWater

elevationArray = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
print(getTrappedRainwater(elevationArray))
print(getTrappedRainwater_optimal(elevationArray))