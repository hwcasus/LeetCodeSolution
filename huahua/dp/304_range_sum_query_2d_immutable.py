# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        num_row = len(matrix)
        num_col = len(matrix[0])
        self.dp = [[0 for _ in range(num_col + 1)] for _ in range(num_row + 1)]


        for row_idx in range(num_row):
            for col_idx in range(num_col):
                self.dp[row_idx + 1][col_idx + 1] = (
                    matrix[row_idx][col_idx]
                    + self.dp[row_idx][col_idx + 1]
                    + self.dp[row_idx + 1][col_idx]
                    - self.dp[row_idx][col_idx]
                )


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.dp[row2 + 1][col2 + 1]
            - self.dp[row2 + 1][col1]
            - self.dp[row1][col2 + 1]
            + self.dp[row1][col1]
        )

    def __init___v2(self, matrix: List[List[int]]):
        self.dps = []

        for row in matrix:
            dp = row
            for i in range(1, len(row)):
                dp[i] += dp[i-1]

            if self.dps:
                dp = [
                    a + b for a, b in zip(dp, self.dps[-1])
                ]

            self.dps.append(dp)

    def sumRegion_v2(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ret = 0
        ret += self.dps[row2][col2]
        if col1 > 0:
            ret -= self.dps[row2][col1-1]
        if row1 > 0:
            ret -= self.dps[row1-1][col2]
        if row1 > 0 and col1 > 0:
            ret += self.dps[row1-1][col1-1]

        return ret

    def __init___v1(self, matrix: List[List[int]]):
        self.dps = []

        for row in matrix:
            dp = row
            for i in range(1, len(row)):
                dp[i] += dp[i-1]

            self.dps.append(dp)

    def sumRegion_v1(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ret = 0
        for r in range(row1, row2 + 1):
            ret += self.dps[r][col2]
            if col1 > 0:
                ret -= self.dps[r][col1-1]

        return ret

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)