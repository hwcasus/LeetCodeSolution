# 435. Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/description/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda iv: iv.end)
        current_end, r = None, 0
        
        for iv in intervals:
            if current_end is None or current_end <= iv.start:
                current_end = iv.end
            else:
                r+=1
        
        return r
