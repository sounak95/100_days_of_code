


def getMaxWaterContainer(heights):
    max_area= float('-inf')
    for i, ele in enumerate(heights):
        for j in range(i+1,len(heights)):
            height= min(ele, heights[j])
            width= j-i
            area= height*width
            max_area= max(max_area, area)
    return max_area




heightsArray = [4,8,1,2,3,9]
print(getMaxWaterContainer(heightsArray))