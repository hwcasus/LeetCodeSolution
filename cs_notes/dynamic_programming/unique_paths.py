# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/description/

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m or not n: return 0
        dp = [1]*m
        for i in range(1, n):
            for i in range(1, m):
                dp[i] += dp[i-1]

        return dp[-1]

    def uniquePathsOld(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [1] * m

        for i in range(1, n):
            for j in range(m):
                if j == 0:
                    dp[j] = 1
                else:
                    dp[j] = dp[j-1]+ dp[j]

        return dp[-1]
