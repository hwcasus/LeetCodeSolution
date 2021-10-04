# https://leetcode.com/problems/maximal-rectangle/

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        num_row = len(matrix)
        num_col = len(matrix[0])

        max_area = 0
        acc_heights = [0] * num_col

        for row_idx in range(num_row):
            acc_heights = [
                (h + 1) if matrix[row_idx][col_idx] == "1" else 0
                for col_idx, h in enumerate(acc_heights)
            ]
            stack = [-1]
            heights = acc_heights + [0]

            for i in range(len(heights)):
                while heights[i] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = (i - stack[-1]) - 1
                    max_area = max(max_area, height * width)

                stack.append(i)

        return max_area


    def maximalRectangleFailed(self, matrix: List[List[str]]) -> int:
        num_row = len(matrix)
        num_col = len(matrix[0])

        dp_row = [[0 for _ in range(num_col+1)] for _ in range(num_row + 1)]
        dp_col = [[0 for _ in range(num_col+1)] for _ in range(num_row + 1)]

        m = 0
        for row_idx in range(1, num_row + 1):
            for col_idx in range(1, num_col + 1):
                if matrix[row_idx - 1][col_idx - 1] == "1":
                    # width
                    if row_idx == 1:
                        dp_row[row_idx][col_idx] = dp_row[row_idx][col_idx - 1] + 1
                    else:
                        dp_row[row_idx][col_idx] = max(
                            min(
                                dp_row[row_idx][col_idx - 1] + 1,
                                dp_row[row_idx - 1][col_idx],
                            ),
                            1
                        )

                    # height
                    if col_idx == 1:
                        dp_col[row_idx][col_idx] = dp_col[row_idx - 1][col_idx] + 1
                    else:
                        dp_col[row_idx][col_idx] = max(
                            min(
                                dp_col[row_idx - 1][col_idx] + 1,
                                dp_col[row_idx][col_idx],
                            ),
                            1
                        )
                    m = max(m, dp_col[row_idx][col_idx] * dp_row[row_idx][col_idx])

        print(dp_row)
        print(dp_col)
        return m