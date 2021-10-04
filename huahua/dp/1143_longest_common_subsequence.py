# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        ret = 0

        for idx1, char1 in enumerate(text1):
            for idx2, char2 in enumerate(text2):
                if char1 == char2:
                    dp[idx1 + 1][idx2 + 1]  = dp[idx1][idx2] + 1
                else:
                    dp[idx1 + 1][idx2 + 1] = max(
                        dp[idx1 + 1][idx2], dp[idx1][idx2 + 1]
                    )

                ret = max(dp[idx1 + 1][idx2 + 1], ret)

        return ret