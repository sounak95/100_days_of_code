# https://leetcode.com/problems/top-k-frequent-elements/

# use hashing to store frequency of elements, then apply bucket sort

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq =[[] for i in range(len(nums)+1)]
        count={}

        for num in nums:
            count[num] = count.get(num,0)+1

        for key,v in count.items():
            freq[v].append(key)

        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res



s=Solution()
nums = [1,1,1,2,2,3]
k = 2
print(s.topKFrequent(nums, k))

