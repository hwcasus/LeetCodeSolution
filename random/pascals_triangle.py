# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        ret = []
        
        while numRows > 0:
            numRows-=1
            if not ret:
                ret.append([1])
            elif len(ret)==1:
                ret.append([1, 1])
            else:
                ret.append([1]+[ret[-1][i]+ret[-1][i+1] for i in range(len(ret)-1)]+[1])
 
        return ret
