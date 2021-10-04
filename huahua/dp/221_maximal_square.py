# https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        num_row = len(matrix)
        num_col = len(matrix[0])

        dp = [[0 for _ in range(num_col+1)] for _ in range(num_row + 1)]

        m = 0
        for row_idx in range(1, num_row + 1):
            for col_idx in range(1, num_col + 1):
                if matrix[row_idx - 1][col_idx - 1] == "1":
                    dp[row_idx][col_idx] = min(
                        dp[row_idx - 1][col_idx - 1],
                        dp[row_idx][col_idx - 1],
                        dp[row_idx - 1][col_idx],
                    ) + int(matrix[row_idx - 1][col_idx - 1])

                    m = max(m, dp[row_idx][col_idx]**2)

        return m
