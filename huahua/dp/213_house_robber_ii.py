# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        rob_first = self.actual_rob(nums[0:-1])
        rob_last = self.actual_rob(nums[1:])
        return max(rob_first, rob_last)

    def actual_rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp2 = nums[0]
        dp1 = nums[1]

        for i in range(2, len(nums)):
            dp2, dp1 = max(dp1, dp2), max(dp2 + nums[i], dp1)

        return max(dp1, dp2)