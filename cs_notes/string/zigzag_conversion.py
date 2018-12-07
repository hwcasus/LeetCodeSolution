# 6. ZigZag Conversion
# https://leetcode.com/problems/zigzag-conversion/description/

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s

        curr = 0
        sign = 1
        parts=[""]*numRows

        for i in range(len(s)):
            parts[curr]+=s[i]
            curr += sign
            if curr == numRows-1 or curr == 0:
                sign = -sign

        return "".join(parts)
