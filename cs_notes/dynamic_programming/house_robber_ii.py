# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/description/

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        # 直接把情況分成 搶第一戶 或 搶最後一戶 , 分頭計算
        return max(self.rob_impl(nums[:-1]), self.rob_impl(nums[::-1][:-1]))

    def rob_impl(self, nums):
        pre1 = pre2 = 0

        for n in nums:
            pre1, pre2 = max(pre1, pre2 + n), pre1

        return pre1


