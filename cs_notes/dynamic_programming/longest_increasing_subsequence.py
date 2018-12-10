# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/description/

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        dp 對應的是以元素i為起點的最長遞增子數列
        每往回走一步就要檢查之前所有的元素的 dp
        找出所有比當前元素還要大的元素所對應之dp中最大值並+1
        最後回傳整個過程中看過最大的值
        """

        if not nums: return 0
        global_max = 1
        dp = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = dp[i] if dp[i] > dp[j]+1 else dp[j]+1
            global_max = global_max if global_max > dp[i] else dp[i]
        return global_max
