# 79. Word Search
# https://leetcode.com/problems/word-search/description/

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        row = len(board)
        if row == 0: return False
        
        col = len(board[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def go(i, j, word_idx):
            if word_idx == len(word): return True
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != word[word_idx] or visited[i][j]: return False
            visited[i][j]=True
            for i_d, j_d in directions:
                if go(i+i_d, j+j_d, word_idx+1): return True
            visited[i][j]=False
            return False

        for i in range(row):
            for j in range(col):
                if go(i, j, 0): return True
        
        return False
