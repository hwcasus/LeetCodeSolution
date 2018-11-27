# 240. Search a 2D Matrix II
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if len(matrix)==0: return False
        
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n-1
        
        #row, col = 0, -1
        #while (m-row)>=1 and (n+col)>=0: # slower, less than is faster than subtraction
        
        while m > row and col >= 0:             
            pointer = matrix[row][col]
            if target == pointer: return True
            elif target < pointer: col-= 1
            else: row += 1
        
        return False
    
    def searchMatrixCheat(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if target in row: return True
            
        return False