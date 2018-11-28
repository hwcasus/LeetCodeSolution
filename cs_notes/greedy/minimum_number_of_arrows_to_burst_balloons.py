# 452. Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/

class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        end, k = None, 0
        points.sort(key=lambda points: points[1])
        for point in points:
            if end is None or point[0]>end:
                k+=1
                end = point[1]
                
        return k
