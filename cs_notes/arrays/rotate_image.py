# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/description/

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        # if not in place
        # return [list(reversed(cols)) for cols in zip(*matrix)]
        l = len(matrix)
        for i in range(l):
            for j in range(l-1, -1, -1):
                matrix[i].append(matrix[j][i])
        
        for i in range(l):
            for j in range(l):
                matrix[i].pop(0)
    def rotateBetter(self, matrix):
        n = len(matrix)
        for i in range(n):
            # 對角翻
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # 倒序
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
                
    def rotateEvenBetter(self, matrix):
        # 上下翻
        matrix.reverse() 
        for i in range(len(matrix)):
            # 對角翻
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
