# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/description/
# https://leetcode.com/problems/find-the-duplicate-number/discuss/191309/Fast-slow-pointers-w-explanation-of-why-there-must-be-one-cycle

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Revisit 20210727
        slow_idx = nums[0]
        fast_idx = nums[nums[0]]

        # Find the entry point of loop
        while slow_idx != fast_idx:
            slow_idx = nums[slow_idx]
            fast_idx = nums[nums[fast_idx]]

        fast_idx = 0

        while fast_idx != slow_idx:
            slow_idx = nums[slow_idx]
            fast_idx = nums[fast_idx]

        return fast_idx

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return sloww