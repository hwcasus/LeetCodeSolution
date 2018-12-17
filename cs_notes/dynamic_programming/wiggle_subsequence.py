# 376. Wiggle Subsequence
# https://leetcode.com/problems/wiggle-subsequence/description/

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        本題解法很多種, 這邊只記錄 Greedy + DP 的最佳化解法
        """
        if not nums: return 0
        inc = dec = 1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                inc = dec + 1
            elif nums[i] < nums[i+1]:
                dec = inc + 1

        return max(inc, dec)


