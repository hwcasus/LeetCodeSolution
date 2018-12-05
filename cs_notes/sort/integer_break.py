# 343. Integer Break
# https://leetcode.com/problems/integer-break/description/

class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2: return 0

        dp = [1] * (n+1)
        for i in range(3, n+1):
            for j in range(1, (i//2)+1):
                dp[i] = max(dp[i], max(j, dp[j])* max(i-j, dp[i-j]))

        return dp[-1]


    def integerBreakOld(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 3: return 1

        dp = [1]*(n+1)

        for i in range(2, len(dp)):
            for j in range(1, (i//2)+1):
                dp[i] = max(dp[i], max(j, dp[j]) * max(i-j, dp[i-j]))
                # print(i, j, i-j, dp[i])

        return dp[-1]
