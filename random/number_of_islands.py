# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        
        row, col = len(grid), len(grid[0])
            
        def travel(x, y):
            # A DFS travaler go through entire island and destory it 
            if x >= row or y >= col or x < 0 or y < 0:
                return
            if grid[x][y] == '1':
                grid[x][y] = 0
                travel(x, y+1)
                travel(x+1, y)
                travel(x, y-1)
                travel(x-1, y)
                 

        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    travel(i,j)
                    count += 1
        
        return count
            