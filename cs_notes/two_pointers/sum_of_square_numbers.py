# 633. Sum of Square Numbers
# https://leetcode.com/problems/sum-of-square-numbers/description/

class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        
        sx = 0
        lx = int(math.sqrt(c))
        
        while (sx <= lx):
            s = sx*sx + lx*lx
            if s == c:
                return True
            elif s > c:
                lx -= 1
            elif c > s:
                sx += 1
        
        return False
        