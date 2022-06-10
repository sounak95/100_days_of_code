
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