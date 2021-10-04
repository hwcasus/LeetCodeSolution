# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1 - obstacleGrid[0][0]
        for i in range(1, n):
            dp[i] = min(dp[i-1], 1 - obstacleGrid[0][i])

        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                dp[0] = 0
            for j in range(1, n):
                left_count = dp[j-1] if obstacleGrid[i][j-1] == 0 else 0
                up_count = dp[j] if obstacleGrid[i-1][j] == 0 else 0
                dp[j] = left_count + up_count if obstacleGrid[i][j] == 0 else 0

        return dp[-1]


    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid: return 0

        dp = [0] * (len(obstacleGrid[0])+1)
        dp[1] = 1

        for i in range(0, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])+1):
                if obstacleGrid[i][j-1] == 1:
                    dp[j] = 0
                else:
                    dp[j] += dp[j-1]

        return dp[-1]