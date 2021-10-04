# https://leetcode.com/problems/n-th-tribonacci-number/
class Solution:
    def tribonacci_me(self, n: int) -> int:
        # 超時了
        dp = [0] * n
        dp[0:3] = [0, 1, 1]
        if n < 3:
            return dp[n]

        for i in range(3, n):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[-1] + dp[-2] + dp[-3]

    def tribonacci(self, n: int) -> int:
        dp0, dp1, dp2 = 0, 1, 1
        if n < 3:
            return (n+1)//2

        for i in range(3, n):
            dp0, dp1, dp2 = dp1, dp2, (dp0 + dp1 + dp2)

        return dp0 + dp1 + dp2