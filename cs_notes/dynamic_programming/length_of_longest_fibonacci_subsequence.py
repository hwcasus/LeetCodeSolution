# 873. Length of Longest Fibonacci Subsequence
# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/

class Solution:
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        本題使用動態規劃，整體算法的流程如下
        1) 建立一個字典方便查閱某個數字是否在 A 之中以及如果該元素在 A 中, 其 index 是多少
        2) 建立 n*n 的 dp array, 定義是從 ith - jth 是多長的費伯納西數列, 預設值為 2
        3) 用雙重迴圈走過所有 j = (0 ~ n-1), k = (j+1 ~ n-1)
           這邊的想法是檢查是否有一元素 i 可以跟 j, k 三個元素構成一費伯納西數列
           同時對 i 元素的限制是 i < j < k, 由於我們已經知道 j 跟 k 的數值
           所以可以推算出 i 的數值是多少，這時候就要做兩個檢查
           a ) A[k]-A[j] in dictionary
           b ) A[k]-A[j] < A[j]
           如果上述兩個條件都有符合，就表示 j, k 是可以和元素 i 構築出費伯納西數列
           當我們更新的時候要注意，必須檢查 i, j 是否可以跟一個更小的元素建構費伯納西數列
           也就是 dp[i][j] 的值，但這個值按照設計，必定會先在之前的迴圈中被更新
           所以我們可以直接更新成 dp[j][k] = dp[i][j]+1, 假若 i, j, k 是第一次被更新的費伯納西數列
           那麼值就會是 2 + 1 也就是長度為 3 的費伯納西數列.
           最後使用一個額外的變數紀錄所看過的最大的數列長度, 最後進行回傳
        """

        # 使用字典是因為要在 O(1) 的時間複雜度來找特定元素
        d = {a:i for i, a in enumerate(A)}

        dp = [[2 for _ in range(len(A))] for _ in range(len(A))]
        ret = 0
        for j in range(len(A)):
            for k in range(j+1, len(A)):
                missing = A[k]-A[j]
                if missing >= A[j]: break
                if missing in d:
                    dp[j][k] = dp[d[missing]][j]+1
                    ret = max(dp[j][k], ret)
        return ret
