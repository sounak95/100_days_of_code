

# https://leetcode.com/problems/trapping-rain-water/

class Solution(object):
    def trap(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(heights)
        left =1
        right= n-2
        max_left = heights[0]
        max_right = heights[n-1]
        total_water =0

        while(left<right):
            if heights[left]<heights[right]:
                if heights[left]>max_left:
                    max_left = heights[left]
                else:
                    total_water+=max_left-heights[left]
                left+=1
            else:
                if heights[right]>max_right:
                    max_right = heights[right]
                else:
                    total_water+= max_right-heights[right]
                right-=1

        return total_water

s=Solution()
height = [4,2,0,3,2,5]
print(s.trap(height))
