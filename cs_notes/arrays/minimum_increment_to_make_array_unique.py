# 945. Minimum Increment to Make Array Unique
# https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/

class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        count = nxt = 0
        for a in sorted(A):
            # print(a, count, nxt)
            count += max(nxt-a, 0) # count 用來計算目前看到的值跟期望值 nxt 差多少
            nxt = max(nxt, a)+1   # nxt 每次都要更新為比目前看到的 a 或是 nxt 還大 (+1)

        return count
