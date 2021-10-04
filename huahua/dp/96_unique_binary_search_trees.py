# 96. Unique Binary Search Trees

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        if n < 2:
            return dp[n]

        for i in range(2, n+1):
            dp[i] = sum([dp[j] * dp[i - (j + 1)] for j in range(i)])

        return dp[-1]