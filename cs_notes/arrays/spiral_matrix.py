# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/description/

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        
        ret = []
        while matrix:
            # ret+=(matrix[0])
            # matrix = matrix[1:]
            # matrix = list(reversed((list(zip(*matrix)))))
            ret+=matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return ret
