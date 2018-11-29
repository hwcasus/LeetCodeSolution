# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/description/

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret = [0] * (num + 1)
        for i in range(1, num+1):
            # DP idea, for example 
            # 9 = 0b1001, 
            # 9 & 1 = 0b1001 & 0x0001    <- check if last bit is '1'
            # 9 >> 1 = 4, 4 = 0b100      <- number of rest bits '1' of 9 as same as 4
            
            
            ret[i] = ret[i>>1] + (i & 1)
        return ret
    
    def countBitsA(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        return [bin(i).count('1') for i in range(num+1)]