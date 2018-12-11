# 96. Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees/description/

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        樹的問題的突破口很多都是在解析子樹的狀態
        這題的重點在於選定了某個數值作為 root 之後
        其左右子樹的深度就已經被決定了
        例如 n = 4, 則 root val 必定在 [1, 2, 3, 4] 之間
        假若選定 root.val = 1, 則其左子樹為 None
        而右子樹則的數量則是一個 n=3 子問題, 也就是繼續從 [2, 3, 4] 之間再選一個 root
        所以 n=4 可以拆成
            root.val = 1, left = [] (n = 0),        right = [2, 3, 4] (n = 3)
            root.val = 2, left = [1] (n = 1),       right = [3, 4] (n = 2)
            root.val = 3, left = [1, 2] (n = 2),    right = [4] (n = 1)
            root.val = 4, left = [1, 2, 3] (n = 3), right = [] (n = 0)
        而左右子樹的子問題完全獨立，所以左右子樹的數量相乘之後就是所有可能的左右子樹種類
        所以答案會變成
            dp[4] = dp[0]*dp[3] + dp[1]*dp[2] + dp[2]*dp[1] + dp[3]*dp[0]
        """

        if n < 3: return n
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            for j in range(i):
                # print(i, j, i-j-1)
                dp[i]+=dp[j]*dp[i-j-1]

        return dp[n]
