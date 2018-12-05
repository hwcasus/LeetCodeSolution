# 413. Arithmetic Slices
# https://leetcode.com/problems/arithmetic-slices/description/

class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3: return 0

        dp = [0]*len(A)
        for i in range(2, len(A)):
            if A[i-2]-A[i-1] == A[i-1]-A[i]:
                dp[i] = dp[i-1]+1

        for i in range(1, len(dp)):
            dp[i] += dp[i-1]

        return dp[-1]


    def numberOfArithmeticSlices2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """


        if len(A) < 2: return 0

        dp = [0]*len(A)

        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1


        for i in range(1, len(dp)):
            dp[i] += dp[i-1]

        return dp[-1]
