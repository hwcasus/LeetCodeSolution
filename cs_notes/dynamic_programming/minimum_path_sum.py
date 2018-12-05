# 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        w = len(grid)
        if not w: return 0
        h = len(grid[0])

        dp = [0] * h
        for i in range(w):
            for j in range(h):
                if i == 0:
                    dp[j] = sum(grid[i][:j+1]) #要注意index,  j 會從 0 開始
                else:
                    if j == 0:
                        dp[j] += grid[i][j]
                    else:
                        dp[j] = grid[i][j] + min(dp[j-1], dp[j])

        return dp[-1]



    def minPathSumOld(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        w = len(grid)
        if w == 0:
            return 0

        h = len(grid[0])
        if h == 0:
            return 0

        dp_top = [0] * h

        for i in range(w):
            for j in range(h):
                if i == 0:
                    dp_top[j] = dp_top[j-1]
                else:
                    dp_top[j] = min(dp_top[j-1], dp_top[j]) if j != 0 else dp_top[j]

                dp_top[j] += grid[i][j]

        return dp_top[-1]
