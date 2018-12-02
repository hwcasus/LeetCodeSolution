# 172. Factorial Trailing Zeroes
# https://leetcode.com/problems/factorial-trailing-zeroes/description/

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        cnt = 0
        while n > 0:
            cnt += n//5
            n //= 5
        return cnt

    def trailingZeroesSmartRecursive(self, n):
        """
        :type n: int
        :rtype: int
        """    
        return 0 if if n<5 else n/5+self.trailingZeroes(n/5)
