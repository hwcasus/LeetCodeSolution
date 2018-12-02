# 367. Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/description/

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low, high = 0, num
        
        while low <= high:
            mid = low + (high-low)//2
            est = mid**2
            if est == num:
                return True
            elif est > num:
                high = mid - 1
            else:
                low = mid + 1
                
        return False
