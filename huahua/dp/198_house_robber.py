# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp2 = nums[0]
        dp1 = nums[1]

        for i in range(2, len(nums)):
            dp2, dp1 = max(dp1, dp2), max(dp2 + nums[i], dp1)

        return max(dp1, dp2)