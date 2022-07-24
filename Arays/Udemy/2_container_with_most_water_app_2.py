
# https://leetcode.com/problems/container-with-most-water/


def getMaxWaterContainer(heights):
    p1=0
    p2=len(heights)-1
    max_area= float('-inf')
    while(p1<p2):
        length= min(heights[p1], heights[p2])
        width = p2-p1
        area = length*width
        max_area= max(area, max_area)

        if heights[p1]<heights[p2]:
            p1+=1
        else:
            p2-=1
    return max_area




heightsArray = [4,8,1,2,3,9];
print(getMaxWaterContainer(heightsArray))