# 646. Maximum Length of Pair Chain
# https://leetcode.com/problems/maximum-length-of-pair-chain/description/

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        結合 greedy 跟 dp 解
        只要記錄當前最大的tail
        如果遇到更大的head, 就長度+1, 更新最大 tail
        最後回傳長度
        """
        cur, res = float('-inf'), 0
        for p in sorted(pairs, key=lambda x: x[1]):
            if cur < p[0]: cur, res = p[1], res + 1
        return res

    def findLongestChainStack(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        沒想到本題有 Greedy 的解法
        根據尾巴值排序後就從頭開始找就可以
        """
        pairs.sort(key=lambda p: p[1])
        stack = []
        for p in pairs:
            if not stack or (stack and stack[-1][1] < p[0]):
                stack.append(p)
        return len(stack)
    def findLongestChainDP(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        用 DP 解
        dp[i] 表示以當前元素為頭的 chain 之長度
        更新方式是找 i 後面的元素中滿足 pair[i][1] < pair[j][0] 的 j 元素的最大值,
        最後回傳 dp 的最大值
        """
        pairs.sort(key=lambda p: p[0])
        dp = [1]*(len(pairs)+1)
        m = 0
        for i in range(len(pairs)-2, -1, -1):
            dp[i] = max([dp[j] for j in range(i+1, len(pairs)) if pairs[i][1] < pairs[j][0]] + [0])+1
            if dp[i] > m: m = dp[i]

        return m

