# 695. Max Area of Island
# https://leetcode.com/problems/max-area-of-island/description/

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        row = len(grid)
        col = len(grid[0])
        
        def go(i, j):
            if i >= row or i < 0 or j < 0 or j >= col or grid[i][j]==0:
                return 0
            else:
                grid[i][j]=0
                ret = (go(i-1, j)+ go(i, j-1)+go(i, j+1)+go(i+1, j))+1
                return ret        
        
        size = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    size = max(size, go(r, c))
                    
        return size
                    
