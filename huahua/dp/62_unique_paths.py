# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths2(self, m: int, n: int) -> int:
        count = [[1 for _ in range(n)] for _ in range(m)]
        for n_idx in range(1, n):  # Left:Right
            for m_idx in range(1, m):  # Up:Down
                left_count = count[m_idx][n_idx - 1]
                up_count = count[m_idx - 1][n_idx]
                count[m_idx][n_idx] = left_count + up_count

        return count[-1][-1]

    def uniquePaths(self, m: int, n: int) -> int:
        long, short = (m, n) if m > n else (n, m)
        count = [1 for _ in range(short)]
        for _ in range(1, long):
            for i in range(1, short):
                count[i] += count[i-1]

        return count[-1]