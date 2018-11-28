# 766. Toeplitz Matrix
# https://leetcode.com/problems/toeplitz-matrix/description/

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i-1][j-1]!=matrix[i][j]: return False
        
        return True
    
    def isToeplitzMatrixRough(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
        last_row = None
        for row in matrix:
            if last_row and last_row != row[1:]: return False
            last_row = row[:-1]
        
        return True