# 712. Minimum ASCII Delete Sum for Two Strings

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        dp = [
            [0 for _ in range(len(s1) + 1)]
            for _ in range(len(s2) + 1)
        ]

        for row, char2 in enumerate(s2):
            for col, char1 in enumerate(s1):
                if char1 == char2:
                    dp[row+1][col+1] = (
                        dp[row][col] + ord(char2)
                    )
                else:
                    dp[row+1][col+1] = max(
                        dp[row][col+1],
                        dp[row+1][col]
                    )

        return sum(map(ord, s1)) + sum(map(ord, s2)) - 2 * dp[-1][-1]