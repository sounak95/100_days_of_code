

# https://leetcode.com/problems/3sum/


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        for i , num in enumerate(nums):
            if (i>0 and nums[i-1]==num):
                continue

            l,r=i+1, len(nums)-1
            while(l<r):
                cur_sum = num+nums[l] + nums[r]
                if cur_sum>0:
                    r-=1
                elif cur_sum<0:
                    l+=1
                else:
                    res.append([num,nums[l], nums[r]])
                    l+=1
                    r-=1
                    while(l<r and nums[l]==nums[l-1]):
                        l+=1

        return res

s=Solution()
nums = [-1,0,1,2,-1,-4]
print(s.threeSum(nums))