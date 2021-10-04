# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])


        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(m):
            for j in range(1, n+1):
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j-1]

            # Only the first row should use dp[0]
            dp[0] = float('inf')

        return dp[-1]