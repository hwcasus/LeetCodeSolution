# 565. Array Nesting
# https://leetcode.com/problems/array-nesting/description/

class Solution:
    def arrayNesting_re2(self, nums: List[int]) -> int:
        # revisit  @ 20210726
        ans = 0
        for idx, num in enumerate(nums):
            current_idx = idx
            count = 0

            while(nums[current_idx] != -1):
                nums[current_idx], current_idx = -1, nums[current_idx]
                count += 1
            ans = max(ans, count)

        return ans


    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            current, count = i, 0
            while nums[current] != -1: # next value is -1 means have been visited
                nums[current], current = -1, nums[current]
                count += 1

            ans = count if count > ans else ans
        return ans
