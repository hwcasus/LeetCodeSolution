# https://leetcode.com/problems/largest-1-bordered-square/

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:

        num_row = len(grid)
        num_col = len(grid[0])

        horizontal = [row[:] for row in grid]
        vertical = [row[:] for row in grid]

        for ridx, cidx in itertools.product(range(num_row), range(num_col)):
            if grid[ridx][cidx] == 1:
                if cidx > 0:
                    horizontal[ridx][cidx] = horizontal[ridx][cidx-1] + 1
                if ridx > 0:
                    vertical[ridx][cidx] = vertical[ridx-1][cidx] + 1


        ans_len = 0
        for ridx, cidx in itertools.product(reversed(range(num_row)), reversed(range(num_col))):
            # 這邊的解法是針對每一個 grid[i][j]
            # 透過 horizontal / vertical 找出兩個方向上最長連續的 1, 取小者 (named x)
            # 然後從 (i, j) 上回頭看 horizontal[i-x][j] 及 vertical[i][j-x]
            # 檢查兩者的值是否有 >= small, 如有則表示有形成一個框, 要更新 ans_len, 並可以跳過後續檢查
            # 若無則縮小 small 再檢查一次, 確認是否有形成, 直到small <= ans_len
            # 就沒必要再確認, 因為就算有形成框也不會產生更大的框
            small = min(horizontal[ridx][cidx], vertical[ridx][cidx])
            while small > ans_len:
                if (
                    vertical[ridx][cidx - (small - 1)] >= small
                    and horizontal[ridx - (small - 1)][cidx] >= small
                ):
                    ans_len = small
                    break
                small-=1

        return ans_len**2
