

# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-arrays/problem/three-sum-closest

class Solution:
    def threeSumClosest (self, arr, target):
    # Your Code Here
        arr.sort()
        closest_sum = float('inf')
        for i, num in enumerate(arr):
            left =i+1
            right = len(arr)-1
            while(left<right):
                curr_sum = num+ arr[left]+ arr[right]
                if abs(target - curr_sum) < abs(target - closest_sum):
                    closest_sum = curr_sum
                if abs(target - curr_sum) == abs(target - closest_sum):
                    closest_sum = max(curr_sum, closest_sum)
                if curr_sum==target:
                    break
                if curr_sum> target:
                    right-=1
                else:
                    left+=1


        return closest_sum
s=Solution()
print(s.threeSumClosest([-7,9,8,3,1,1], 2))