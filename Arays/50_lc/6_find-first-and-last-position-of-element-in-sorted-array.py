class Solution(object):

    def get_left_pos(self, nums, target):

        left =0
        right = len(nums)-1

        while(left<=right):
            # mid=left+(right-left)//2
            mid = (left+right)//2

            if nums[mid]==target:
                if (mid-1>=0 and nums[mid-1]!=target or mid==0):
                    return mid
                else:
                    right=mid-1
            elif target>nums[mid]:
                left= mid+1
            elif target<nums[mid]:
                right= mid-1

        return -1

    def get_right_pos(self, nums, target):

        left =0
        right = len(nums)-1

        while(left<=right):
            mid = (left + right) // 2

            if nums[mid]==target:
                if (mid+1<=len(nums)-1 and nums[mid+1]!=target or mid==len(nums)-1):
                    return mid
                else:
                    left=mid+1
            elif target>nums[mid]:
                left= mid+1
            elif target<nums[mid]:
                right= mid-1

        return -1



    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.get_left_pos(nums,target), self.get_right_pos(nums,target)

# nums = [5,7,7,8,8,10]
# target = 8
nums = [2,2]
target = 2
s=Solution()
print(s.searchRange(nums, target))