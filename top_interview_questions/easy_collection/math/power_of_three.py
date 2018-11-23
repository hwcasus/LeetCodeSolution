# Power of Three
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        from math import log10
        return ((log10(n)/log10(3))%1)==0
    
    def isPowerOfThreeLoop(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        while n%3==0:
            n/=3
            
        return n == 1