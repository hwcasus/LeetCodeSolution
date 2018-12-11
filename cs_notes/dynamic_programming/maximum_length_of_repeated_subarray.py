# 718. Maximum Length of Repeated Subarray
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/

class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        更好的 DP 版本
        改善點
        1 ) dp array size 直接多設一層, 省去計算 idx 的時間
        2 ) 從尾巴開始做好像比較簡單一點
        """
        dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
        for i in range(len(A)-1, -1, -1):
            for j in range(len(B)-1, -1, -1):
                if A[i]==B[j]:
                    dp[i][j] += dp[i+1][j+1]+1

        return max(max(row) for row in dp)

    def findLengthMyDP(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0 for _ in B] for _ in A]

        ret = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if i > 0 and j > 0:
                    dp[i][j] += dp[i-1][j-1]
                if A[i] == B[j]:
                    dp[i][j] += 1
                else:
                    dp[i][j] = 0
                ret = max(ret, dp[i][j])

        # for d in dp: print(d)

        return ret
