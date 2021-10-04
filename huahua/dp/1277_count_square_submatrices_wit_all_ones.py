# 1277. Count Square Submatrices with All Ones

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        num_row = len(matrix)
        num_col = len(matrix[0])

        dp = [[0] * (num_col + 1) for _ in range(num_row + 1)]

        out = 0
        for r in range(num_row):
            for c in range(num_col):
                if matrix[r][c]:
                    s = dp[r+1][c+1] = min(
                        dp[r][c],
                        dp[r+1][c],
                        dp[r][c+1]
                    ) + matrix[r][c]
                    out += s

        return out
