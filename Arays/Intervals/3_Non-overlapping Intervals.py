
# https://leetcode.com/problems/non-overlapping-intervals/

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals.sort(key=lambda x:x[0])
        _, prev_end = intervals[0]
        res=0
        print(intervals)
        for start, end in intervals[1:]:
            if prev_end<=start:
                prev_end = end
            else:
                res+=1
                prev_end= min(end,prev_end)
        return res

s=Solution()
print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))



