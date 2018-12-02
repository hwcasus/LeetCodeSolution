# 417. Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/

ass Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        row = len(matrix)
        if row == 0:return []
        col = len(matrix[0])
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        reach_p = [[False for _ in range(col)] for _ in range(row)]
        reach_a = [[False for _ in range(col)] for _ in range(row)]
        
        def go(i, j, reach):
            if reach[i][j]: return
            reach[i][j] = True
            
            for rd, cd in direction:
                nxt_i, nxt_j = i + rd, j+cd
                # this line means we are looking for water that can flow into current (i, j)
                if (nxt_i < 0 or nxt_j < 0 or nxt_i >= row or nxt_j >= col or matrix[i][j] > matrix[nxt_i][nxt_j]):
                    continue # if current is higher, means there is no water would flow in from this direction.
                go(nxt_i, nxt_j, reach)
        
        for i in range(row):
            go(i, 0, reach_p)
            go(i, col-1, reach_a)
        
        for j in range(col):
            go(0, j, reach_p)
            go(row - 1, j, reach_a)
        
        return [[i, j] for i in range(row) for j in range(col) if reach_p[i][j] and reach_a[i][j]]
        
        
