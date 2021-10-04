# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

class Solution:
    def findMin(self, nums: List[int]) -> int:

        def helper(nums, l, r):
            if l + 1 >= r:
                return min(nums[l], nums[r])

            if nums[l] < nums[r]:
                return nums[l]

            mid = l + (r - l) // 2

            return min(
                helper(nums, l, mid-1),
                helper(nums, mid, r),
            )

        return helper(nums, 0, len(nums)-1)
