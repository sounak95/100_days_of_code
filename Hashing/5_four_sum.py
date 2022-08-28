# https://leetcode.com/problems/4sum-ii/

# use hasing to store sum of two numbers in corresponding arrays

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        m={}
        count=0
        for num1 in nums1:
            for num2 in nums2:
                sum= num1+num2
                if sum not in m:
                    m[sum]=0
                m[sum]+=1
        for num3 in nums3:
            for num4 in nums4:
                target=-(num3+num4)
                if target in m:
                    count+=m[target]
        return count
s=Solution()
nums1 = [0]
nums2 = [0]
nums3 = [0]
nums4 = [0]
print(s.fourSumCount(nums1, nums2, nums3, nums4))

