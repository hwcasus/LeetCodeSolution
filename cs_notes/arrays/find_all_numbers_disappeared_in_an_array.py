# 448. Find All Numbers Disappeared in an Array
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # revisit 20210726
        return list(set(range(1, len(nums) + 1)) - set(nums))
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for n in nums:
            idx = abs(n)-1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        return [i+1 for i in range(len(nums)) if nums[i] > 0]