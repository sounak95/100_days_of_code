
# https://leetcode.com/problems/merge-intervals/

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        merged_intervals=[]
        intervals.sort(key= lambda i:i[0])
        current_interval = intervals[0]
        merged_intervals.append(current_interval)

        for next_interval in intervals[1:]:
            _, current_end = current_interval
            next_start, next_end = next_interval
            if current_end >= next_start:
                current_interval[1] = max(current_end, next_end)
            else:
                current_interval = next_interval
                merged_intervals.append(current_interval)
        return merged_intervals
