# 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/description/

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = ""
        for _ in range(32):
            ret+=str(n&1)
            n = n>>1
        
        return int(ret, 2)
    
    def reverseBitsInteger(self, n):
        result = 0
        for _ in range(32):
            result = result << 1
            result = result | (1 & n)
            n = n >> 1            
        return result
    
    def reverseBitsString(self, n):
        strN = bin(n)[2:]
        if len(strN) < 32:
            strN = '0' * (32 - len(strN)) + strN
        return int(strN[::-1], 2)
