# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/description/

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n > 0:
            if (n&1) == 1: cnt+=1
            n = n >> 1
        
        return cnt
    
    def hammingWeightSmart(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n:
            n &= (n-1)
            cnt += 1
        return cnt
