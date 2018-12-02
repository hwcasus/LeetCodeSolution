# 130. Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/description/

class Solution:
    def solve(self, board):
        """ 先將周圍有連接的都變成 'T', 再將所有 'O' 直接變成 'X' , 'T' 變回 'O'
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """    
        row = len(board)
        if row == 0: return
        col = len(board[0])
        
        def go(i, j, c):
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j]!= 'O':
                return
            else:
                board[i][j] = c
                go(i, j+1, c)
                go(i+1, j, c)
                go(i, j-1, c)
                go(i-1, j, c)
                
        
        for i in [0, row-1]:
            for j in range(col):
                go(i, j, 'T')
        
        for i in range(row):
            for j in [0, col-1]:
                go(i, j, 'T')
                
#         for i in range(1, row-1):
#             for j in range(1, col-1):
#                 go(i, j, 'X')
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                     board[i][j] = 'X'
        

            
                
