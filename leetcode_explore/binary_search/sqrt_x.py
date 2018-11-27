# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/description/

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1: return x
        
        low, high = 1, x
        
        while low < high:   
            mid = low + (high - low)//2
            est = mid*mid
            if est > x:
                high = mid
            else:
                low = mid + 1
                
        return high -1
