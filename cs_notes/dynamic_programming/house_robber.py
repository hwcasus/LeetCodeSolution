# 198. House Robber
# https://leetcode.com/problems/house-robber/description/

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        pre1 = pre2 = 0
        for n in nums:
            pre1, pre2 = max(pre1, pre2 + n), pre1

        return pre1
