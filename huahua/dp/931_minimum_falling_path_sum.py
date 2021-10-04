# https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        dp = [0] * n

        for row_x in range(n):
            # Use list comprehension to prevent dp is updated
            dp = [
                min(dp[max(0, col_x-1): min(col_x+2, n)]) + matrix[row_x][col_x]
                for col_x in range(n)
            ]

        return min(dp)