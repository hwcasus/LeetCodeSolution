# 212. Word Search II
# https://leetcode.com/problems/word-search-ii/description/

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        特點
        1) 用 nested dict 實現 trie
        2) 很普通的使用 backtracking
           但是檢查當前字元合不合法的時候，使用 trie 就可以很快解決
        """
        trie = {}
        for word in words:
            t = trie
            for char in word:
                if char not in t:
                    t[char]= {}
                t = t[char]
            t["end"] = "end"
        
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.backtracking(board, i, j, trie, "", res)
        
        return list(set(res))
        
        
    def backtracking(self, board, i, j, trie, current, res):
        if "end" in trie:
            res.append(current)
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] not in trie:
            return
        
        tmp = board[i][j]
        board[i][j] = "@"
        self.backtracking(board, i+1, j, trie[tmp], current+tmp, res)
        self.backtracking(board, i, j+1, trie[tmp], current+tmp, res)
        self.backtracking(board, i-1, j, trie[tmp], current+tmp, res)
        self.backtracking(board, i, j-1, trie[tmp], current+tmp, res)
        board[i][j] = tmp
                
