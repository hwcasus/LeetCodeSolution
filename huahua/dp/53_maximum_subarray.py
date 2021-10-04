# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray2(self, nums: List[int]) -> int:
        acc_nums = [None] * len(nums)
        current_max = acc_nums[0] = nums[0]

        for i in range(1, len(nums)):
            acc_nums[i] = max(0, acc_nums[i-1]) + nums[i]
            current_max = max(current_max, acc_nums[i])

        return current_max

    def maxSubArray(self, nums: List[int]) -> int:
        overall_max = current_max = nums[0]

        for i in range(1, len(nums)):
            current_max = max(0, current_max) + nums[i]
            overall_max = max(overall_max, current_max)

        return overall_max