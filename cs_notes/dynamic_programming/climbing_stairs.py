# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if not n: return n

        prv_1, prv_2 = 1, 0
        for i in range(n):
            prv_1, prv_2 = prv_1 + prv_2, prv_1

        return prv_1

    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n

        return self.climbStairs(n-2) + self.climbStairs(n-1)
