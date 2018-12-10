# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/description/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return intervals
        
        #原本用 end sort, 但不知道為啥用 start 才會過
        intervals.sort(key=lambda i: i.start)
        merged_list=[]
        tmp = None
        for i in range(len(intervals)):
            if not tmp:
                tmp = (intervals[i].start, intervals[i].end)
            elif tmp[1] >= intervals[i].start:
                tmp = (min(tmp[0], intervals[i].start), max(tmp[1], intervals[i].end))
            else:
                merged_list.append(Interval(*tmp))
                tmp = (intervals[i].start, intervals[i].end)
        
        if tmp: merged_list.append(Interval(*tmp))
            
        return merged_list        
        
