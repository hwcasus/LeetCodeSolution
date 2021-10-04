# https://leetcode.com/problems/delete-operation-for-two-strings/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        for r, char1 in enumerate(word1):
            for c, char2 in enumerate(word2):
                if char1 == char2:
                    dp[r+1][c+1] = dp[r][c] + 1
                else:
                    dp[r+1][c+1] = max(dp[r+1][c], dp[r][c+1])

        return len(word2) + len(word1) - 2 * dp[-1][-1]